import os

class ValidatePassword:
    
    def __init__(self, position1, position2, character):
        self.position1 = position1
        self.position2 = position2
        self.character = character

    def validate(self, password):
        count = password.count(self.character)
        if count >= self.position1 and count <= self.position2:
            return True
        else:
            return False

    @staticmethod
    def process_rule_part1(path="file.dat"):

        counter = 0

        file_path=(os.path.dirname(__file__)) + "/" + path

        with open(file_path,"r") as f:
            for row in f.readlines():
                isValid = ValidatePassword._validate_pw(row)
                if isValid:
                    counter += 1
        
        return counter

    @staticmethod
    def _validate_pw(row):
        number1, number2, char, password=ValidatePassword._parse_line(row)
        return ValidatePassword(number1, number2, char).validate(password)

    @staticmethod
    def _parse_line(line):
        #process min and max
        numbers = line.partition(' ')[0]
        first_number = int(numbers.partition('-')[0])
        second_number = int(numbers.partition('-')[2])
        
        #process letters part
        letters=line.partition(' ')[2]
        character=letters.partition(': ')[0]
        password=letters.partition(': ')[2]
        
        return (first_number, second_number, character, password)
