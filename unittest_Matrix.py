import unittest
from LAB1_EX_MATRICE import matrix

class test_matrix(unittest.TestCase):
    def setUp(self):
        self.matTest = matrix([[1,1,1],[1,1,1],[1,1,1]])
        self.m2=matrix([[1,2,3],[1,2,3],[1,2,3]])
    
    def test_on_int_prod_operation_method_correct_result(self):
        result=matrix([[3,6,9],[3,6,9],[3,6,9]])
        self.assertEqual(result.mat, (self.matTest.prod(self.m2)).mat)
    
    def test_on_int_add_matrix_to_matrix_operation_method_correct_result(self):
        result=matrix([[2,3,4],[2,3,4],[2,3,4]])
        self.assertEqual(result.mat, (self.matTest + self.m2).mat)
        
    def test_on_int_add_scalar_to_matrix_operation_method_correct_result(self):
        result=matrix([[6,6,6],[6,6,6],[6,6,6]])
        self.assertEqual(result.mat, (self.matTest + 5).mat)
        
    def test_on_int_add_matrix_to_scalar_operation_method_correct_result(self):
        result=matrix([[6,6,6],[6,6,6],[6,6,6]])
        self.assertEqual(result.mat, (5 + self.matTest).mat)
        
    def test_on_int_sub_matrix_to_matrix_operation_method_correct_result(self):
        result=matrix([[0,-1,-2],[0,-1,-2],[0,-1,-2]]) 
        self.assertEqual(result.mat, (self.matTest-self.m2).mat)
        
    def test_on_int_sub_matrix_to_scalar_operation_method_correct_result(self):
        result=matrix([[4,4,4],[4,4,4],[4,4,4]])  
        self.assertEqual(result.mat, (5-self.matTest).mat)
        
    def test_on_int_sub_scalar_to_matrix_operation_method_correct_result(self):
        result=matrix([[-4,-4,-4],[-4,-4,-4],[-4,-4,-4]]) 
        self.assertEqual(result.mat, (self.matTest-5).mat)
        
    def test_on_prod_with_different_size(self):
        m2=matrix([[1,2,3],[1,2,3]])
        result=None
        self.assertEqual(result, (self.matTest.prod(m2)))
    
    def test_on_float_add_scalar_to_matrix_operation_method_correct_result(self):
        result=matrix([[6.5,6.5,6.5],[6.5,6.5,6.5],[6.5,6.5,6.5]])
        self.assertEqual(result.mat, (self.matTest + 5.5).mat)
    
    def test_on_float_sub_matrix_to_matrix_operation_method_correct_result(self):
        m2=matrix([[1.5,2.5,3.5],[1.5,2.5,3.5],[1.5,2.5,3.5]])
        result=matrix([[-0.5,-1.5,-2.5],[-0.5,-1.5,-2.5],[-0.5,-1.5,-2.5]]) 
        self.assertEqual(result.mat, (self.matTest-m2).mat)
    
    def test_on_add_with_unsupported_type(self):
        m2 = "[[1.5,2.5,3.5],[1.5,2.5,3.5],[1.5,2.5,3.5]]"
        result = None
        self.assertEqual(result, (self.matTest+m2))
    
    def test_on_sub_with_unsupported_type(self):
        m2 = "[[1.5,2.5,3.5],[1.5,2.5,3.5],[1.5,2.5,3.5]]"
        result = None
        self.assertEqual(result, (self.matTest-m2))
    
    def test_on_prod_with_unsupported_type(self):
        m2 = "[[1.5,2.5,3.5],[1.5,2.5,3.5],[1.5,2.5,3.5]]"
        result = None
        self.assertEqual(result, (self.matTest.prod(m2)))
    
    
    def test_on_costructor(self):
        m2 = matrix([[1,1,1],[1,1,1],[1,1,1]])
        self.assertEqual(self.matTest.mat,m2.mat)

