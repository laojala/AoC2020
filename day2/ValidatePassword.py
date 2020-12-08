import os

class ValidatePassword:
    
    def __init__(self, position1, position2, character):
        self.position1 = position1
        self.position2 = position2
        self.character = character

    def validate_policy1(self, password):
        count = password.count(self.character)
        if count >= self.position1 and count <= self.position2:
            return True
        else:
            return False
    
    def validate_policy2(self, password):
        pos1 = password[self.position1 - 1]
        pos2 = password[self.position2 - 1]

        if (pos1 != self.character) and (pos2 != self.character):
            return False

        if (pos1 == self.character) and (pos2 == self.character):
            return False
        
        return True

    @staticmethod
    def process_file(path="file.dat"):

        counter = {
            "policy1": 0,
            "policy2": 0
        }

        file_path=(os.path.dirname(__file__)) + "/" + path

        with open(file_path,"r") as f:
            for row in f.readlines():
                number1, number2, char, password=ValidatePassword._parse_line(row)
                policy1Valid = ValidatePassword(number1, number2, char).validate_policy1(password)
                policy2Valid = ValidatePassword(number1, number2, char).validate_policy2(password)
                if policy1Valid:
                    counter["policy1"] += 1
                if policy2Valid:
                    counter["policy2"] += 1
        
        return counter

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
