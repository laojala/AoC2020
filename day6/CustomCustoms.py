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
                entry = entry + line.strip('\n')
            if line == '\n' or index == len(all_lines)-1:
                data.append(entry)
                entry = ''
        
        return data

    @staticmethod 
    def _printSumOfUnique(all_answers):

        sum = 0

        for answer in all_answers:

            counted = []

            for char in answer:
                if char in string.ascii_lowercase and char not in counted:
                    sum = sum + 1
                    counted.append(char)
        
        assert(sum == 6310)
        print('part 1', sum)

        


data = CustomCustoms(CustomCustoms._readGroup())
CustomCustoms._printSumOfUnique(data.groups)
