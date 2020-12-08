
import unittest
from ValidatePassword import ValidatePassword

class TestValidatePassword(unittest.TestCase):
    
    def test_parse_line(self):
        self.assertEqual(ValidatePassword._parse_line('1-3 a: abcde'),(1,3,'a','abcde'))
        self.assertEqual(ValidatePassword._parse_line('10-13 r: rrrnrkfrrcrtnrlh'),(10,13,'r','rrrnrkfrrcrtnrlh'))

    def test_validate_policy1(self):
        self.assertEqual(ValidatePassword(1,3,'a').validate_policy1('abcde'), True)
        self.assertEqual(ValidatePassword(1,3,'b').validate_policy1('cdefg'), False)

    def test_validate_policy2(self):
        self.assertEqual(ValidatePassword(1,3,'a').validate_policy2('abcde'), True)
        self.assertEqual(ValidatePassword(1,3,'b').validate_policy2('cdefg'), False)
        self.assertEqual(ValidatePassword(2,9,'c').validate_policy2('ccccccccc'), False)

    def test_process_rule_policy1(self):
        counters = ValidatePassword.process_file()
        self.assertEqual(counters["policy1"], 569)

    def test_process_rule_policy2(self):
        counters = ValidatePassword.process_file()
        self.assertEqual(counters["policy2"], 346)