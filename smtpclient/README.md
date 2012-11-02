Simple SMTP Client
==================

Dead simple SMTP client written in Python.

Usage & Testing
---------------

Once configured, you can test it like so:

    $ ./smtpclient.py 
    <= 220 smtp.example.com ESMTP Postfix (Ubuntu)
    => HELO Joshua
    <= 250 smtp.example.com
    => MAIL FROM: user@example.com
    <= 250 2.1.0 Ok
    => RCPT TO: user@example.com
    <= 250 2.1.5 Ok
    => DATA
    <= 354 End data with <CR><LF>.<CR><LF>
    => <message>
    => .
    <= 250 2.0.0 Ok: queued as 9289E816E
    => QUIT
    <= 221 2.0.0 Bye

