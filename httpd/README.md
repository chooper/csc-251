httpd
=====
For this class, I had to write a web server in Python that implemented
only a very small subset of the HTTP protocol and only serves static
files. This directory is my solution to that assignment.

It is by no means a complete web server, nor is it guaranteed to be
secure or stable enough for production traffic.


Usage
-----
The server may be invoked like:

    python httpd.py <listen port>


Discussion
----------
At first, we were given a very basic, single file boilerplate with a
typical wait/`accept()` loop and minimal parsing of the headers. I chose
to split the code up into 3 main parts (excluding the program entry
point):

### HTTPRequest
This is the object representing the user's request. Given a buffer
(actually a `StringIO` object) it parses the request and performs some
basic error checking. It also attempts to locate the resource (file) on disk.

### HTTPResponse
This is the object representing the *response*. This is in charge of
reading the given resource and sending the response to the client. This
is unlike the `HTTPRequest`, which does not interact with the socket at
all.

### HTTPServer
This is the glue that binds the `HTTPRequest` to the `HTTPResponse`. It
represents one single server and its state and contains the
wait/accept loop. When a connection is accepted, it writes the request
into a buffer and does all of the basic handling (through `HTTPRequest`
and `HTTPResponse`) in a new thread.


