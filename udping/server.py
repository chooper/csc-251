#!/usr/bin/env python

"""
UDP Server that responds to simple ping-like requests and simulates packet
loss.

Please see the README for more information, including the specification.
"""

import socket, random

LISTEN_ON       = '127.0.0.1'
RECV_BUFFER     = 1024  # bytes
RECV_TIMEOUT    = 1     # seconds
PACKET_LOSS     = 0.3   # per-1

def main(port):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.settimeout(RECV_TIMEOUT)
    server_socket.bind( (LISTEN_ON, int(port)) )

    print 'Listening on {0}:{1}'.format(LISTEN_ON, port)

    while True:
        try:
            data, addr = server_socket.recvfrom(RECV_BUFFER)
        except socket.timeout:
            continue

        print 'Received', data, 'from', addr

        # Simulate packet loss
        if random.random() <= PACKET_LOSS:
            print 'Simulating packet loss, nothing to see here'
            continue

        # Parse the message
        msg = data.split(' ')
        assert len(msg) == 3

        cmd, sequence_number, timestamp = msg
        if cmd == 'ping':
            # Build and send the response
            response_msg = 'pong {0} {1}' \
                .format(sequence_number, timestamp)
            server_socket.sendto(response_msg, addr)
        else:
            print 'Received unknown request'


if __name__ == '__main__':
    import sys
    def usage():
        print
        print 'Usage: {0} <listen port>'.format(sys.argv[0])
        print

    if len(sys.argv) < 2:
        usage()
        sys.exit(1)

    main(sys.argv[1])

