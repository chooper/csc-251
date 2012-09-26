
import unittest
from cStringIO import StringIO
from http.request import HTTPRequest

class TestHTTPRequestForRoot(unittest.TestCase):

    test_addr = ('127.0.0.1', 1025)
    request = (
        "GET / HTTP/1.1\r\n"
        "User-Agent: unit test"
        "Host: localhost:7777"
        "Accept: */*"
    )

    def run(self):
        buf = String().write(self.request)
        req = HTTPRequest(buf, self.test_addr)

        self.assertIsNone(req)  # make sure no errors are returned

