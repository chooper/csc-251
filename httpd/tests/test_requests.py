
import unittest
from cStringIO import StringIO
from http.request import HTTPRequest

TEST_ADDR = ('127.0.0.1', 1025)
TEST_REQUEST = (
    "{method} {uri} {protocol}\r\n"
    "User-Agent: Unit Test"
    "Host: localhost:7777"
    "Accept: */*"
)


class TestHTTPRequestForUnsupportedMethod(unittest.TestCase):

    req_params = {
        'method': 'FAIL',
        'uri': '/',
        'protocol': 'HTTP/1.1',
    }

    def testBadProtocol(self):
        buf = StringIO(TEST_REQUEST.format(**self.req_params))
        req = HTTPRequest(buf, TEST_ADDR)
        result = req.handle()
        self.assertNotEqual(result, None)  # make sure no errors are returned
        self.assertEqual(result[0], 405)


class TestHTTPRequestForBadProtocol(unittest.TestCase):

    req_params = {
        'method': 'GET',
        'uri': '/',
        'protocol': 'FAILFAILFAIL/1.1',
    }

    def testBadProtocol(self):
        buf = StringIO(TEST_REQUEST.format(**self.req_params))
        req = HTTPRequest(buf, TEST_ADDR)
        result = req.handle()
        self.assertNotEqual(result, None)  # make sure no errors are returned
        self.assertEqual(result[0], 505)


class TestHTTPRequestForDirTraversal(unittest.TestCase):

    req_params = {
        'method': 'GET',
        'uri': '/../',
        'protocol': 'HTTP/1.1',
    }

    def testDirTraversal(self):
        buf = StringIO(TEST_REQUEST.format(**self.req_params))
        req = HTTPRequest(buf, TEST_ADDR)
        result = req.handle()
        self.assertNotEqual(result, None)  # make sure no errors are returned
        self.assertEqual(result[0], 403)


class TestHTTPRequestForIndex(unittest.TestCase):

    req_params = {
        'method': 'GET',
        'uri': '/index.html',
        'protocol': 'HTTP/1.1',
    }

    def testForIndex(self):
        buf = StringIO(TEST_REQUEST.format(**self.req_params))
        req = HTTPRequest(buf, TEST_ADDR)
        result = req.handle()
        self.assertEqual(result, None)  # make sure no errors are returned


class TestHTTPRequestForRoot(unittest.TestCase):

    req_params = {
        'method': 'GET',
        'uri': '/',
        'protocol': 'HTTP/1.1',
    }

    def testForRoot(self):
        buf = StringIO(TEST_REQUEST.format(**self.req_params))
        req = HTTPRequest(buf, TEST_ADDR)
        result = req.handle()
        self.assertEqual(result, None)  # make sure no errors are returned


