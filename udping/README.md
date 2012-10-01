UDP Pinger
==========

This was written for a CS class, specifically CSC 251 aka Net-Centric Computing
at ECSU. The spec is behind a login form, but essentially the message format is
a space-separated ascii string in the form of:

    ping sequence_number time

Where ``sequence_number`` is an integer that starts at 1 and ``time`` is the
time that the message was sent, in no particular format. For this assignment, I
send a UNIX timestamp that has been converted to milliseconds and cast to an
integer.

The response from the 'pong' message by the server is identifical, with the
obvious exception that in place of 'ping' the server replaces it with 'pong'.


Dependencies
------------

You need Python 2.6-ish and the standard library.

Example
-------

    $ python server.py 7777
    $ python client.py localhost 7777 # run this in another terminal
    pong! seq=1, rtt=1 ms from ('127.0.0.1', 7777)
    pong! seq=2, rtt=0 ms from ('127.0.0.1', 7777)
    pong! seq=3, rtt=1 ms from ('127.0.0.1', 7777)
    pong! seq=4, rtt=1 ms from ('127.0.0.1', 7777)
    Request timed out
    pong! seq=6, rtt=1 ms from ('127.0.0.1', 7777)
    Request timed out
    pong! seq=8, rtt=1 ms from ('127.0.0.1', 7777)
    Request timed out
    Request timed out
    summary: 6/10 (40.0% loss) packets received, mean rtt = 0.83 ms

The server will also print some debugging information.

