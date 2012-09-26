#!/usr/bin/env python

import cStringIO

class HTTPResponse(object):

    """Handles the actual response to a given HTTPRequest.

    Performs the requested resource and performs all I/O with the
    client.
    """

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
        """Returns the "status" header for the responses current HTTP
        status code and version.
        """
        assert self.code and int(self.code)

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
        """Prepares the response for returning a given HTTP error."""
        self.code = code
        self.headers['Content-Type'] = 'text/plain'
        self._rep_stream = cStringIO.StringIO(msg + "\n")

    def _prepare(self, code=None):
        """Populate headers and prepare to respond to the request."""
        try:
            self.code = 200
            self._rep_stream = open(self.request.uri_path, 'r')
            self.headers['Content-Type'] = 'text/html'
        except IOError:
            # TODO: Check real error (e.g., not found vs permissions)
            self.http_error(404, "File not found")

    def prepare(self, code=None):
        """Wrapper to ``self._prepare``. It's job is simply to catch any
        errors during a response and return a HTTP error 500 should it
        not be able to recover."""
        try:
            return self._prepare(code)
        except:
            self.http_error(500, 'Internal error')

    def finish(self):
        """Send the response and close all sockets."""
        self.socket.sendall(self.status + "\r\n")
        for header, value in self.headers.iteritems():
            self.socket.sendall( "{0}: {1}\r\n".format(header, value) )
        self.socket.sendall("\r\n")  # end of headers
        self.socket.sendall( self._rep_stream.read() )
        self._rep_stream.close()
        self.socket.close()


