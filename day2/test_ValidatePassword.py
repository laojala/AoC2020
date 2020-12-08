
import unittest
from ValidatePassword import ValidatePassword

class TestValidatePassword(unittest.TestCase):
    
    def test_parse_line(self):
        self.assertEqual(ValidatePassword._parse_line('1-3 a: abcde'),(1,3,'a','abcde'))
        self.assertEqual(ValidatePassword._parse_line('10-13 r: rrrnrkfrrcrtnrlh'),(10,13,'r','rrrnrkfrrcrtnrlh'))

    def test_validate_pw(self):
        self.assertEqual(ValidatePassword(1,3,'a').validate('abcde'), True)
        self.assertEqual(ValidatePassword(1,3,'b').validate('cdefg'), False)

    def test_process_rule_part1(self):
        self.assertEqual(ValidatePassword.process_rule_part1(), 569)
