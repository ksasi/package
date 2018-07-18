#Any changes to this library need to be reinstalled with 
#pip install --upgrade

#For running unit tests use
#/usr/bin/python -m unittest test

import unittest

from matrix_ops import matrix2by2

class Testmatrix2by2Class(unittest.TestCase):
    def setUp(self):
        self.matrix = matrix2by2([[1,2],[4,5]])
       
    def test_det(self):
        self.assertEqual(matrix2by2.det(self.matrix),-3,'incorrect determinent')
        
    def test_add(self):
        A1 = matrix2by2([[3,4],[6,7]])
        B1 = matrix2by2([[1,1],[1,1]])
        SU = A1+B1
        self.assertEqual(SU.data_elements[0][0],4,'Incorrect matrix addition')
        self.assertEqual(SU.data_elements[0][1],5,'Incorrect matrix addition')
        self.assertEqual(SU.data_elements[1][0],7,'Incorrect matrix addition')
        self.assertEqual(SU.data_elements[1][1],8,'Incorrect matrix addition')
                         
    def test_sub(self):
        A2 = matrix2by2([[3,4],[6,7]])
        B2 = matrix2by2([[1,1],[1,1]])
        SB = A2-B2
        self.assertEqual(SB.data_elements[0][0],2,'Incorrect matrix subtraction')
        self.assertEqual(SB.data_elements[0][1],3,'Incorrect matrix subtraction')
        self.assertEqual(SB.data_elements[1][0],5,'Incorrect matrix subtraction')
        self.assertEqual(SB.data_elements[1][1],6,'Incorrect matrix subtraction')
                         
if __name__ == '__main__':
       unittest.main()
                         
                         
    
