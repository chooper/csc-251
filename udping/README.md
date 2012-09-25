UDP Pinger
==========

This was written for a CS class, specifically CSC 251 aka Net-Centric Computing
at ECSU. The spec is behind a login form, but essentially:

Message format is a space-separated ascii string in the form of:

    "ping sequence_number time"

Where ``sequence_number`` is an integer that starts at 1 and ``time`` is the
time that the message was sent, in no particular format. For this assignment, I
send a UNIX timestamp that has been converted to milliseconds and cast to an
integer.

The response from the 'pong' message by the server is identifical, with the
obvious exception that in place of 'ping' the server replaces it with 'pong'.

