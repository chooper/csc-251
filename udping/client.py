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
        start = time.time()
        # message format: <cmd> <seq #> <time>
        msg = 'ping {0} {1}'.format(i, start)
        client_socket.sendto(msg, (dst_ip, int(port)))

        try:
            data, addr = client_socket.recvfrom(RECV_BUFFER)
        except socket.timeout:
            print 'Request timed out'
            continue
        else:
            end = time.time()
            time_in_ms = int((end - start) * 1000)

            print 'Received:', data, 'from', addr, 'rtt={0} ms)' \
                .format(time_in_ms)

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

