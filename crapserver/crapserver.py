#!/usr/bin/env python

import os
import sys
import socket

# TODO: Don't do this shit
DOCROOT = '/home/chooper/projects/csc251/crapserver/docroot'

def main(serverport):
    serverSocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    serverSocket.bind(('',serverport))
    serverSocket.listen(1)
    print 'I am listening'
    while 1:
        connectionSocket, addr = serverSocket.accept()
        data = connectionSocket.recv(1024)
        print data
        request_headers = [l.strip() for l in data.split("\n")]

        # Parse request
        method, uri, protocol = request_headers[0].split(' ')
        # TODO: url decode
        assert method in ['GET']    # TODO: 405s for unimplemented methods
        assert protocol in ['HTTP/1.0', 'HTTP/1.1']
        assert uri.find('..') == -1 # Attempt at blocking directory traversal

        # normalize urls
        if not uri.startswith('/'):
            uri = '/' + uri

        if uri == '/': 
            uri = '/index.html'

        local_path = os.path.join(DOCROOT, uri[1:])

        # TODO: MIME type detection

        headers = [
            "HTTP/1.1 200 OK",
            "Connection: close",
            "Content-Type: text/html", ]

        try:
            with open(local_path,'r') as requested_file:
                # send headers
                connectionSocket.send("\r\n".join(headers))
                # mark end of headers
                connectionSocket.send("\r\n\r\n")
                # send content
                connectionSocket.send(requested_file.read())
                requested_file.close()
        except IOError: # file not found
            connectionSocket.send("HTTP/1.1 404 Not Found\r\n\r\n")
            connectionSocket.send("These aren't the droids you're looking for.")
        finally:
            connectionSocket.close()


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
