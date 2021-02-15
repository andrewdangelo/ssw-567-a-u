import pytest

from lib.main import classify_triangle


class TestMain:

    def test_equilateral(self):
        assert classify_triangle(3, 3, 3) == 'Equilateral'
        assert classify_triangle(4, 4, 4) == 'Equilateral'
        assert classify_triangle(5, 5, 4) != 'Equilateral'

    def test_isosceles(self):
        assert classify_triangle(3, 3, 2) == 'Isosceles'
        assert classify_triangle(4, 4, 3) == 'Isosceles'
        assert classify_triangle(5, 5, 4) == 'Isosceles'

    def test_scalene(self):
         assert classify_triangle(3, 1, 2) == 'Scalene'
         assert classify_triangle(4, 6, 3) == 'Scalene'
         assert classify_triangle(5, 1, 4) == 'Scalene'

    def test_right(self):
         assert classify_triangle(3, 4, 5) == 'Right'
         assert classify_triangle(5, 12, 13) == 'Right'
         assert classify_triangle(6, 8, 10) == 'Right'
