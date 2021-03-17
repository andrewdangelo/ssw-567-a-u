import unittest
import requests
from unittest.mock import patch, Mock
from main import getUserRepos
from nose.tools import assert_is_not_none


class TestMain(unittest.TestCase):
    @patch('main.requests.get')
    def mock_testGetApi(self):
        self.return_value.status_code = 200
        response = getUserRepos('andrewdangelo')
        assert_is_not_none(response)

    def testGetApi(self):
        response = requests.get('https://api.github.com/users/andrewdangelo/repos')
        self.assertEqual(response.status_code, 200)

    def testGetReposFunction(self):
        self.assertEqual(len(getUserRepos('andrewdangelo')), 4)


if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()
