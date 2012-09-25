#!/usr/bin/env python

"""
UDP client that sends simple ping-like requests.
"""

from __future__ import division
import time, socket

RECV_BUFFER     = 1024 # bytes
RECV_TIMEOUT    = 1    # seconds
NUM_REQUESTS    = 10

def main(dst_ip, port):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    client_socket.settimeout(RECV_TIMEOUT)

    for i in xrange(NUM_REQUESTS):
        start = int(time.time() * 1000) # send time in ms
        # message format: <cmd> <seq #> <time>
        msg = 'ping {0} {1}'.format(i, start)
        client_socket.sendto(msg, (dst_ip, int(port)))

        try:
            data, addr = client_socket.recvfrom(RECV_BUFFER)
        except socket.timeout:
            print 'Request timed out'
            continue
        else:
            end = int(time.time() * 1000)
            # parse the received message
            response = data.split(' ')
            assert len(response) == 3

            cmd, seq_num, timestamp = response
            assert cmd == 'pong'

            time_in_ms = end - int(timestamp)

            print 'pong! seq={0}, rtt={1} ms from {2}' \
                .format(seq_num, time_in_ms, addr)

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

