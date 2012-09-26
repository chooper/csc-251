#!/usr/bin/env python

import os, os.path
import sys

from http.server import HTTPServer

LISTEN_IP = '0.0.0.0'
LISTEN_BACKLOG = -1
RECV_BUFFER = 1024
DOCROOT = os.path.join(os.path.dirname(__file__), 'docroot')

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
