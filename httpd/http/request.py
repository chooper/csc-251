#!/usr/bin/env python

import __main__
import os.path

RECV_BUFFER = 1024
DOCROOT = os.path.join(os.path.dirname(__main__.__file__), 'docroot')

class HTTPRequest(object):

    """Performs the initial handling of HTTP request. Generally an
    instance of this object will be passed to an ``HTTPResponse`` object.

    WARNING: This should not send anything over the client socket
            (``self.socket``).
    """

    socket = None
    peer = None
    headers = {}
    method = None
    protocol = None
    uri = None
    uri_path = None

    def __init__(self, conn_socket, conn_addr, docroot=DOCROOT):
        self.socket = conn_socket
        self.peer = conn_addr

    def handle(self):
        """Validates and handles the receiving part of a HTTP request.

        Returns errors encountered or None if the request is valid. Errors
        are a tuple in the form of (http_error, message).
        """
        data = self.socket.recv(RECV_BUFFER)
        print data

        # Parse the request
        #
        # TODO: Detect end of headers (req'd for POST and PUT support)
        # TODO: urldecode the URL
        # TODO: request variables
        #
        request_headers = [l.strip() for l in data.split("\n")]
        self.method, self.uri, self.protocol = request_headers[0].split(' ')

        # Parse headers
        for header in request_headers[1:]:
            if header == '':
                continue
            header_parts = header.split(':')
            header_key = header_parts[0].strip()
            header_value = header_parts[1].strip()
            self.headers[header_key] = header_value
        #
        ####

        # Validate the request
        #
        if self.protocol not in ['HTTP/1.0', 'HTTP/1.1']:
            return (505, 'HTTP Version Not Supported')

        if self.method not in ['GET']:
            return (405, 'Not Implemented')

        # Lame attempt at blocking directory traversal
        if self.uri.find('..') > -1:
            return (403, 'Forbidden')

        #
        ####

        # Normalize provided URL (might not belong here)
        if not self.uri.startswith('/'):
            self.uri = '/' + self.uri
        if self.uri == '/': 
            self.uri = '/index.html'

        # Determine requested resource's local path
        self.uri_path = os.path.join(DOCROOT, self.uri[1:])

        return None

