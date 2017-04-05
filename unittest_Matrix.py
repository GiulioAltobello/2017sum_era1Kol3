import unittest
from LAB1_EX_MATRICE import matrix

class test_matrix(unittest.TestCase):
    def setUp(self):
        self.mat = matrix([[[1,1,1],[1,1,1],[1,1,1]]])
    
    def test_on_int_prod_operation_method_correct_result(self):
        m2=matrix([[1,2,3],[1,2,3],[1,2,3]])
        result=matrix([[3,6,9],[3,6,9],[3,6,9]])
        self.assertEqual(result.mat, (self.mat.prod(m2)).mat)
    
    def test_on_float_prod_operation_method_correct_result(self):
        m2=matrix([[1.5,2.5,3.5],[1.5,2.5,3.5],[1.5,2.5,3.5]])
        result=matrix([[4.5,7.5,10.5 ],[4.5,7.5,10.5],[4.5,7.5,10.5]])
        self.assertEqual(result.mat, (self.mat.prod(m2)).mat)
    
    
    def test_on_int_add_operation_method_correct_result(self):
        m2=matrix([[1,2,3],[1,2,3],[1,2,3]])
        result=matrix([[3,6,9],[3,6,9],[3,6,9]])
        self.assertEqual(result.mat, (self.mat+m2).mat)
        
if __name__=='__main__':
    unittest.main()
