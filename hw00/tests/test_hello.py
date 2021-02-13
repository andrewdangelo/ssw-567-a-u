import pytest
from lib.hello import hello

class Test_Hello:

    def test_hello(self):
        greet = hello('World')
        assert greet == 'Hello World'