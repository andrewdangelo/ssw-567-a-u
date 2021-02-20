# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
"""

import unittest

from Triangle import classifyTriangle


# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

    # Right triangle tests
    def testRightTriangleA(self):
        self.assertEqual(classifyTriangle(3, 4, 5), 'Right', '3,4,5 is a Right triangle')

    def testRightTriangleB(self):
        self.assertEqual(classifyTriangle(6, 8, 10), 'Right', '5,3,4 is a Right triangle')

    def testRightTriangleC(self):
        self.assertEqual(classifyTriangle(5, 12, 13), 'Right', '5,12,13 is a Right triangle')

    # Equilaterial
    def testEquilateralTriangleA(self):
        self.assertEqual(classifyTriangle(1, 1, 1), 'Equilateral', '1,1,1 should be equilateral')

    def testEquilateralTriangleB(self):
        self.assertEqual(classifyTriangle(10, 10, 10), 'Equilateral', '10,10,10 should be equilateral')

    def testEquilateralTriangleC(self):
        self.assertEqual(classifyTriangle(20, 20, 20), 'Equilateral', '20,20,20 should be equilateral')

    # Isoscles
    def testIsoscelesTriangleA(self):
        self.assertEqual(classifyTriangle(2, 2, 1), 'Isosceles', '2,2,1 should be Isosceles')

    def testIsoscelesTriangleB(self):
        self.assertEqual(classifyTriangle(1, 2, 2), 'Isosceles', '1,2,2 should be Isosceles')

    def testIsoscelesTriangleC(self):
        self.assertEqual(classifyTriangle(2, 1, 2), 'Isosceles', '2,1,2 should be Isosceles')

    # Scalene
    def testScaleneTriangleA(self):
        self.assertEqual(classifyTriangle(2, 4, 3), 'Scalene', '2, 4, 3 should be Scalene')

    def testScaleneTriangleB(self):
        self.assertEqual(classifyTriangle(6, 5, 3), 'Scalene', '6, 5, 3 should be Scalene')

    def testScaleneTriangleC(self):
        self.assertEqual(classifyTriangle(25, 22, 14), 'Scalene', '25, 22, 14 should be Scalene')

    # Invalid
    def testNotATriangleA(self):
        self.assertEqual(classifyTriangle(12, 32, 3), 'NotATriangle', '12,32,3 is not a triangle')

    def testNotATriangleB(self):
        self.assertEqual(classifyTriangle(35, 2, 14), 'NotATriangle', '35,2,14 is not a triangle')

    def testNotATriangleC(self):
        self.assertEqual(classifyTriangle(3, 28, 11), 'NotATriangle', '3,28,11 is not a triangle')


if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()
