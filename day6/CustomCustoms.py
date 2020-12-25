import string

class CustomCustoms:

    def __init__(self, groups):
        self.groups = groups

    @staticmethod
    def _readGroup(filename='day6.dat'):

        all_lines = []

        with open(filename,'r') as f:
            all_lines = f.readlines()

        entry = ''
        data = [] 

        for index,line in enumerate(all_lines):
            if line != '\n':
                entry = entry + line
            if line == '\n' or index == len(all_lines)-1:
                data.append(entry)
                entry = ''
        
        return data

    @staticmethod 
    def _printSumOPart1(all_answers):
        sum = 0
        for answer in all_answers:
            counted = []
            for char in answer:
                if char in string.ascii_lowercase and char not in counted:
                    sum = sum + 1
                    counted.append(char)
        assert(sum == 6310)
        print('part 1', sum)

    @staticmethod 
    def _printSumOPart2(all_answers):
        sum = 0
        for answer in all_answers:
            answers_for_group = answer.split('\n')
            if '' in answers_for_group:
                answers_for_group.remove('')
            counted = []
            for item in answers_for_group:
                for char in item:
                    if all([char in i for i in answers_for_group]) and char in string.ascii_lowercase and char not in counted:
                        sum = sum + 1
                        counted.append(char)
        assert(sum == 3193)
        print('part 2', sum)

data = CustomCustoms(CustomCustoms._readGroup())
CustomCustoms._printSumOPart1(data.groups)
CustomCustoms._printSumOPart2(data.groups)
