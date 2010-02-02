import unittest

def pass_func():
    assert True

def fail_func():
    assert False

def error_func():
    raise Exception

PASS = unittest.FunctionTestCase(pass_func)
FAIL = unittest.FunctionTestCase(fail_func)
ERROR = unittest.FunctionTestCase(error_func)

