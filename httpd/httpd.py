#!/usr/bin/env python

import os, os.path
import sys
import socket
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
        """Handle request"""
        data = self.socket.recv(RECV_BUFFER)
        print data

        # TODO: Detect end of headers
        # Parse request
        request_headers = [l.strip() for l in data.split("\n")]
        method, uri, protocol = request_headers[0].split(' ')
        for header in request_headers[1:]:
            if header == '':
                continue
            header_parts = header.split(':')
            header_key = header_parts[0].strip()
            header_value = header_parts[1].strip()
            self.headers[header_key] = header_value

        # TODO: url decode
        assert method in ['GET']    # TODO: 405s for unimplemented methods
        assert protocol in ['HTTP/1.0', 'HTTP/1.1']
        assert uri.find('..') == -1 # Attempt at blocking directory traversal

        self.method = method
        self.protocol = protocol
        self.uri = uri

        # normalize urls
        if not uri.startswith('/'):
            uri = '/' + uri

        if uri == '/': 
            uri = '/index.html'

        self.uri_path = os.path.join(DOCROOT, uri[1:])

        # TODO: MIME type detection


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
            404: 'Not found',
        }
        reason = reasons[int(self.code)]
        return "HTTP/{0} {1} {2}".format(self.version, self.code, reason)

    def prepare(self):
        """Populate headers and prepare to responde to the request"""
        try:
            self.code = 200
            self._rep_stream = open(self.request.uri_path, 'r')
            self.headers['Content-Type'] = 'text/html'
        except IOError:
            # TODO: Check real error
            self.code = 404
            self.headers['Content-Type'] = 'text/plain'
            self._rep_stream = cStringIO.StringIO("File not found\n")

    def finish(self):
        self.socket.sendall(self.status + "\r\n")
        for header, value in self.headers.iteritems():
            self.socket.sendall( "{0}: {1}\r\n".format(header, value) )
        self.socket.sendall("\r\n")  # end of headers
        self.socket.sendall( self._rep_stream.read() )
        self._rep_stream.close()
        self.socket.close()


def main(port):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind( (LISTEN_IP, port) )
    server_socket.listen(LISTEN_BACKLOG)

    print 'I am listening'

    while 1:
        conn_socket, addr = server_socket.accept()

        req = HTTPRequest(conn_socket, addr)
        req.handle()

        rep = HTTPResponse(req)
        rep.prepare()
        rep.finish()


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
