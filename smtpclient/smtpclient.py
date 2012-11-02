#!/usr/bin/env python
#-------------------------------------------------------------------------------
# Name:        SMTP Client
# Purpose:
#
# Author:      Started by rosienej
#              Completed by hooperc
#
# Created:     28/09/2012
# Updated:     12/10/2012
# Copyright:   (c) rosienej 2012, hooperc 2012
#-------------------------------------------------------------------------------

from socket import *

def sendCommand(SMTPClientSocket, cmd):
    """Sends a command to the server, returns False on error"""

    print '=> {0}'.format(cmd.strip())
    error = None
    try:
        SMTPClientSocket.send(cmd)
        recv1 = SMTPClientSocket.recv(1024)
    except timeout:
        status = False
        print "== timed out"
        error = 'timed out'
    else:
        print "<= {0}".format(recv1.strip())
        status = (recv1[:3].startswith('2') or recv1[:3].startswith('3'))
        error = recv1
    return (status, recv1, error)


def main():
    # Choose your message settings
    socket_timeout = 10 # in seconds
    from_address = 'user@example.com'
    to_address = 'user@example.com'
    msg = "\r\n Hello, real world!"
    endmsg = "\r\n.\r\n"

    # Choose a mail server (e.g. Google mail server) and call it mailserver
    # CCH: You can't use gmail unless you use SSL/TLS
    # CCH: Can't use outlook.com (school email) unless you use authentication
    mailServer = 'smtp.example.com'
    mailPort = 25

    # Set socket options
    setdefaulttimeout(socket_timeout)

    # Create socket and establish a TCP connection with mailserver
    SMTPClientSocket = socket(AF_INET,SOCK_STREAM)
    SMTPClientSocket.connect((mailServer,mailPort))

    # Send HELO command and print server response.
    heloCommand = 'HELO Joshua\r\n'
    status, recv, error = sendCommand(SMTPClientSocket, heloCommand)
    if not status:
        print '== Error: {0}'.format(error)

    # Send MAIL FROM command and print server response.
    mailFromCommand = 'MAIL FROM: {0}\r\n'.format(from_address)
    status, recv, error = sendCommand(SMTPClientSocket, mailFromCommand)
    if not status:
        print '== Error: {0}'.format(error)

    # Send RCPT TO command and print server response.
    rcptToCommand = 'RCPT TO: {0}\r\n'.format(to_address)
    status, recv, error = sendCommand(SMTPClientSocket, rcptToCommand)
    if not status:
        print '== Error: {0}'.format(error)

    # Send DATA command and print server response.
    startDataCommand = 'DATA\r\n'
    status, recv, error = sendCommand(SMTPClientSocket, startDataCommand)
    if not status:
        print '== Error: {0}'.format(error)

    # Send message data.
    SMTPClientSocket.send(msg)
    print "=> <message>"

    # Message ends with a single period.
    endDataCommand = endmsg
    status, recv, error = sendCommand(SMTPClientSocket, endDataCommand)
    if not status:
        print '== Error: {0}'.format(error)

    # Send QUIT command and get server response.
    quitCommand = 'QUIT\r\n'
    status, recv, error = sendCommand(SMTPClientSocket, quitCommand)
    if not status:
        print '== Error: {0}'.format(error)

    SMTPClientSocket.close()
    pass


if __name__ == '__main__':
    main()

