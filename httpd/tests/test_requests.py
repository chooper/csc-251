
import unittest
from cStringIO import StringIO
from http.request import HTTPRequest

class TestHTTPRequestForIndex(unittest.TestCase):

    test_addr = ('127.0.0.1', 1025)
    request = (
        "GET /index.html HTTP/1.1\r\n"
        "User-Agent: unit test"
        "Host: localhost:7777"
        "Accept: */*"
    )

    def testForIndex(self):
        buf = StringIO(self.request)
        req = HTTPRequest(buf, self.test_addr)
        result = req.handle()
        self.assertIsNone(result)  # make sure no errors are returned


class TestHTTPRequestForRoot(unittest.TestCase):

    test_addr = ('127.0.0.1', 1025)
    request = (
        "GET / HTTP/1.1\r\n"
        "User-Agent: unit test"
        "Host: localhost:7777"
        "Accept: */*"
    )

    def testForRoot(self):
        buf = StringIO(self.request)
        req = HTTPRequest(buf, self.test_addr)
        result = req.handle()
        self.assertIsNone(result)  # make sure no errors are returned


