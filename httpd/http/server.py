#!/usr/bin/env python

import socket, threading
from .request import HTTPRequest
from .response import HTTPResponse

# TODO: Request logging
# TODO: Implement better control of threading
# TODO: Strip these globals out of here and pass them in from the app

LISTEN_IP = '0.0.0.0'
LISTEN_BACKLOG = -1

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


