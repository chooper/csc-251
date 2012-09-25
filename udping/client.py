#!/usr/bin/env python

"""
UDP client that sends simple ping-like requests.

Please see the README for more information, including the specification.
"""

import time, socket

RECV_BUFFER     = 1024 # bytes
RECV_TIMEOUT    = 1    # seconds
NUM_REQUESTS    = 10

def timestamp():
    """Returns current timestamp in milliseconds"""
    return int(time.time() * 1000)


def handle_message(data, addr):
    """Parse an incoming 'pong' message and return a tuple of
    (``sender_address``, ``sequence_number``, ``round_trip_time``). Returns
    None on error.

    ``sender_address`` is a tuple of ``ip`` (string) and ``port`` (int).
    ``sequence_number`` is an integer in the range [0, inf).
    ``round_trip_time`` is an integer, unit ms, in the range [0, ``recv_timeout``).
    """

    receive_time = timestamp()

    # Parse the received message
    response = data.split(' ')

    if len(response) != 3:
        return

    cmd, seq_num, send_time = response[0], int(response[1]), int(response[2])

    if cmd != 'pong':
        return

    rtt = receive_time - send_time

    return addr, seq_num, rtt


def main(dst_ip, port):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    client_socket.settimeout(RECV_TIMEOUT)

    for i in xrange(NUM_REQUESTS):
        send_time = timestamp()

        # Build the message and send it
        # - Format: "<cmd> <seq #> <time>"
        msg = 'ping {0} {1}'.format(i, send_time)
        client_socket.sendto(msg, (dst_ip, int(port)))

        # Our receiving is currently coupled to our sending :<
        try:
            data, addr = client_socket.recvfrom(RECV_BUFFER)
        except socket.timeout:
            print 'Request timed out'
            continue
        else:
            response = handle_message(data, addr)

            if response:
                print 'pong! seq={1}, rtt={2} ms from {0}' \
                    .format(*response)

        time.sleep(0.5)


if __name__ == '__main__':
    import sys
    def usage():
        print
        print 'Usage: {0} <dst ip> <dst port>'.format(sys.argv[0])
        print

    if len(sys.argv) < 3:
        usage()
        sys.exit(1)

    main(sys.argv[1], sys.argv[2])

