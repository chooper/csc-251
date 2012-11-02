Simple SMTP Client
==================

Dead simple SMTP client written in Python.

Usage & Testing
---------------

Once configured, you can test it like so:

    $ ./smtpclient.py 
    => HELO Joshua
    <= 220 mxbackup1.plumata.net ESMTP Postfix (Ubuntu)
    => MAIL FROM: cchooper@dynamic-alliance.com
    <= 250 mxbackup1.plumata.net
    => RCPT TO: chooper@plumata.com
    <= 250 2.1.0 Ok
    => DATA
    <= 250 2.1.5 Ok
    => <message>
    => .
    <= 354 End data with <CR><LF>.<CR><LF>
    => QUIT
    <= 250 2.0.0 Ok: queued as 9FA6886B2

You'll note that output isn't in the exact order as the SMTP spec.
That's OK! It's actually sending in correct order, but we're not
printing the responses in order.

