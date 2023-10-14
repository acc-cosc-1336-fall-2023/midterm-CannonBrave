#write function tests here, don't add input('') statements here!
import unittest

#follow this example to add questions b, c, and d for testing including their functions
from src.question_a.question_a import get_fahrenheit, test_config

from src.question_c.question_c import get_assessment_value, get_tax_assessed

from src.question_d.question_d import get_person_category

from src.question_b import question_b

class Test_Config(unittest.TestCase):

    def test_question_a_config(self):
        self.assertEqual(True, test_config())

    def test_get_fahrenheit(self):
        self.assertEqual(32, get_fahrenheit(0))
        self.assertEqual(41, get_fahrenheit(5))
        self.assertEqual(50, get_fahrenheit(10))

    def test_use_global(self):
        old_value = question_b.global_variable
        question_b.use_global()
        new_value = question_b.global_variable
        self.assertEqual(old_value + 1, new_value)

    def test_get_assessment_value(self):
        self.assertEqual(6000, get_assessment_value(10000))
        self.assertEqual(12000, get_assessment_value(20000))

    def test_get_tax_assessed(self):
        self.assertEqual(43.20, get_tax_assessed(6000))

    def test_get_person_category(self):
        self.assertEqual('infant', get_person_category(1))
        self.assertEqual('child', get_person_category(2))
        self.assertEqual('teenager', get_person_category(14))
        self.assertEqual('adult', get_person_category(20))

    

    


    

    





    

    







