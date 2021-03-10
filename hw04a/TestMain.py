import unittest
from main import getUserRepos


class TestMain(unittest.TestCase):
    def testGetReposFunction(self):
        self.assertEqual(len(getUserRepos("andrewdangelo")), 4)


if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()
