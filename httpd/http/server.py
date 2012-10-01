#!/usr/bin/env python

import __main__
import os.path, socket, cStringIO, threading
from .request import HTTPRequest
from .response import HTTPResponse

# TODO: Request logging
# TODO: Implement better control of threading
# TODO: Strip these globals out of here and pass them in from the app

RECV_BUFFER = 1024
LISTEN_IP = '0.0.0.0'
LISTEN_BACKLOG = -1
DOCROOT = os.path.join(os.path.dirname(__main__.__file__), 'docroot')

class HTTPServer(object):

    """Maintains the state of the server. This is essentially the "glue" between
    a client's requests and our responses to them."""

    def __init__(self, port, listen_ip=LISTEN_IP, listen_backlog=LISTEN_BACKLOG):
        self.port = port
        self.listen_ip = listen_ip
        self.listen_backlog = listen_backlog

    def setup(self):
        """Sets up socket and starts listening for requests."""
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.bind( (self.listen_ip, self.port) )
        self.socket.listen(self.listen_backlog)

    def handle_connection(self, conn_socket, addr):
        """Handles a new client connection. Should be called immediately
        after the socket accepts a connection.
        """

        error = None
        error_code = None
        error_msg = None

        # Write the request into a buffer
        buf = cStringIO.StringIO()
        buf.write(conn_socket.recv(RECV_BUFFER))

        # Process the response
        req = HTTPRequest(buf, addr, docroot=DOCROOT)
        error = req.handle()

        # Build the response
        rep = HTTPResponse(conn_socket, req)
        if error:
            error_code, error_msg = error
            rep.prepare(error_code)
            rep.http_error(error_code, error_msg)
        else:
            rep.prepare()

        # Send the response
        rep.finish()

    def run(self):
        """Blocking loop to accept new connections.

        Current implementation is to give client connections their own thread.
        """

        while 1:
            conn_socket, addr = self.socket.accept()  # blocks

            # Spin up new thread to handle the client connection
            handler_thread = threading.Thread(
                target=self.handle_connection,
                args=(conn_socket, addr)
            ).start()


