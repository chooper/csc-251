#!/usr/bin/env python

import os, os.path
import sys, socket, threading
import cStringIO

LISTEN_IP = '0.0.0.0'
LISTEN_BACKLOG = 1
RECV_BUFFER = 1024
DOCROOT = os.path.join(os.path.dirname(__file__), 'docroot')

class HTTPRequest(object):

    socket = None
    peer = None
    headers = {}
    method = None
    protocol = None
    uri = None
    uri_path = None

    def __init__(self, conn_socket, conn_addr):
        self.socket = conn_socket
        self.peer = conn_addr

    def handle(self):
        """Handle request. Returns errors encountered or None if the request is
        valid."""
        data = self.socket.recv(RECV_BUFFER)
        print data

        # Parse request
        # TODO: Detect end of headers (req'd for POST and PUT support)
        # TODO: urldecode the URL
        # TODO: request variables
        request_headers = [l.strip() for l in data.split("\n")]
        self.method, self.uri, self.protocol = request_headers[0].split(' ')
        for header in request_headers[1:]:
            if header == '':
                continue
            header_parts = header.split(':')
            header_key = header_parts[0].strip()
            header_value = header_parts[1].strip()
            self.headers[header_key] = header_value

        if self.protocol not in ['HTTP/1.0', 'HTTP/1.1']:
            return (505, 'HTTP Version Not Supported')

        if self.method not in ['GET']:
            return (405, 'Not Implemented')

        # Lame attempt at blocking directory traversal
        if self.uri.find('..') > -1:
            return (403, 'Forbidden')

        # normalize urls
        if not self.uri.startswith('/'):
            self.uri = '/' + self.uri

        if self.uri == '/': 
            self.uri = '/index.html'

        self.uri_path = os.path.join(DOCROOT, self.uri[1:])

        # TODO: MIME type detection
        return None


class HTTPResponse(object):

    request = None
    code = None
    version = '1.1' # This probably isn't true
    headers = {
        'Connection': 'close',
    }
    _rep_stream = None

    def __init__(self, request):
        self.request = request
        self.socket = request.socket # for convenience

    @property
    def status(self):
        assert self.code
        reasons = { # TODO: This doesn't belong here
            200: 'OK',
            403: 'Forbidden',
            404: 'Not Found',
            405: 'Not Implemented',
            500: 'Internal Server Error',
            505: 'HTTP Version Not Supported',
        }
        reason = reasons[int(self.code)]
        return "HTTP/{0} {1} {2}".format(self.version, self.code, reason)

    def http_error(self, code, msg):
        self.code = code
        self.headers['Content-Type'] = 'text/plain'
        self._rep_stream = cStringIO.StringIO(msg + "\n")

    def _prepare(self, code=None):
        """Populate headers and prepare to responde to the request"""
        try:
            self.code = 200
            self._rep_stream = open(self.request.uri_path, 'r')
            self.headers['Content-Type'] = 'text/html'
        except IOError:
            # TODO: Check real error
            self.http_error(404, "File not found")

    def prepare(self, code=None):
        try:
            return self._prepare(code)
        except:
            self.http_error(500, 'Internal error')

    def finish(self):
        self.socket.sendall(self.status + "\r\n")
        for header, value in self.headers.iteritems():
            self.socket.sendall( "{0}: {1}\r\n".format(header, value) )
        self.socket.sendall("\r\n")  # end of headers
        self.socket.sendall( self._rep_stream.read() )
        self._rep_stream.close()
        self.socket.close()


class HTTPServer(object):
    def __init__(self, port, listen_ip=LISTEN_IP, listen_backlog=LISTEN_BACKLOG):
        self.port = port
        self.listen_ip = listen_ip
        self.listen_backlog = listen_backlog

    def setup(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.bind( (self.listen_ip, self.port) )
        self.socket.listen(self.listen_backlog)

    def handle_connection(self, conn_socket, addr):
        error = None
        error_code = None
        error_msg = None

        req = HTTPRequest(conn_socket, addr)
        error = req.handle()

        rep = HTTPResponse(req)
        if error:
            error_code, error_msg = error
            rep.prepare(error_code)
            rep.http_error(error_code, error_msg)
        else:
            rep.prepare()
        rep.finish()

    def run(self):
        while 1:
            conn_socket, addr = self.socket.accept()
            self.handle_connection(conn_socket, addr)


def main(port):
    server = HTTPServer(port)
    server.setup()
    server.run()


if __name__ == '__main__':
    def usage():
        print
        print 'Usage: {0} <port>'.format(sys.argv[0])
        print

    if len(sys.argv) < 2:
        usage()
        sys.exit(1)

    port = int(sys.argv[1])
    try:
        main(port)
    except KeyboardInterrupt:
        sys.exit(1)
