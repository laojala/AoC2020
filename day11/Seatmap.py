from collections import Counter
from itertools import chain
import os

class Seatmap:
    
    def __init__(self, list_of_seats):
        self.layout = list_of_seats

    def setLayout(self, new_layout):
        self.layout = new_layout


    @staticmethod
    def process_file():
        initial = Seatmap(Seatmap._readInitialFile())
        
        previous_part1 = Seatmap(initial.layout[:])
        new_part1 = Seatmap([])

        Seatmap._loopSeats(previous_part1, new_part1)

        occupied_part1 = Seatmap.count_occupied(new_part1)
        print('Occupied, part1:', occupied_part1)
        assert(occupied_part1 == 2406)

        previous_part2 = Seatmap(initial.layout[:])
        new_part2 = Seatmap([])

        Seatmap._loopSeats(previous_part2, new_part2, False, 5)

        occupied_part2 = Seatmap.count_occupied(new_part2)
        print('Occupied, part2:', occupied_part2)
        assert(occupied_part2 == 2149)

    @staticmethod   
    def _loopSeats(previous, new, part1=True, treshold=4):

        while True:
            newLayout = Seatmap.countNewSeats(previous.layout, part1, treshold)
            new.setLayout(newLayout)
            if previous.layout == new.layout:
                break
            else:
                previous.setLayout(new.layout)

    @staticmethod
    def count_occupied(seatmap):
        occupied = 0
        #count seats in new layout
        for row in seatmap.layout:
            occupied = occupied + row.count("#")
        return occupied

    @staticmethod
    def countNewSeats(seats_map, part1=True, treshold=4):
        
        new_seat_map = []
        
        for index_row,row in enumerate(seats_map):

            new_row = ''
            seats_around_spot = ''

            for index_spot,spot in enumerate(row):

                #set floor to floor (no need to calculate statuses around the seat)
                if spot == '.':
                    new_row = new_row + '.'
                    continue

                #list seats statuses around the spot:
                if part1:
                    seats_around_spot = Seatmap._getSeatsAround(seats_map, index_row, index_spot)
                else:
                    seats_around_spot = Seatmap._getDiagonalSeats(seats_map, index_row, index_spot)

                if spot == '.':
                    new_row = new_row + '.'

                #occupy seat if it has only free seats around it
                if spot == 'L' and seats_around_spot.count('#') == 0:
                    new_row = new_row + '#'
                
                if spot == 'L' and seats_around_spot.count('#') >= 1:
                    new_row = new_row + 'L'

                #release seat if it has four or more occupied seats around it
                if spot == '#' and seats_around_spot.count('#') >= treshold:
                    new_row = new_row + 'L'

                if spot == '#' and seats_around_spot.count('#') < treshold:
                    new_row = new_row + '#'
            
                if index_spot != len(new_row) - 1:
                    raise Exception('nothing added to the row in this rounnd - why?')

            new_seat_map.append(new_row)
            new_row = ''
            seats_around_spot.clear()

        return new_seat_map    

    @staticmethod
    def _getDiagonalSeats(seat_map, row, char):
        seats_around = []

        seats_around = []
        map_length = len(seat_map)
        row_length = len(seat_map[0])

        #up:
        up = row
        while up != 0:
            up = up - 1            
            if seat_map[up][char] != '.':
                seats_around.append(seat_map[up][char])
                break
                
        #up-left:
        up = row
        left = char
        while up != 0 and left != 0:
            up = up - 1
            left = left -1
            if seat_map[up][left] != '.':
                seats_around.append(seat_map[up][left])
                break
        
        #up-right:
        up = row
        right = char
        while up != 0 and right != row_length - 1:
            up = up - 1
            right = right + 1
            if seat_map[up][right] != '.':
                seats_around.append(seat_map[up][right])
                break

        #left:
        left = char
        while left != 0:
            left = left - 1
            if seat_map[row][left] != '.':
                seats_around.append(seat_map[row][left])
                break

        #right:
        right = char
        while  right != row_length - 1:
            right = right + 1
            if seat_map[row][right] != '.':
                seats_around.append(seat_map[row][right])
                break
        
        #down:
        down = row
        while down != map_length - 1:
            down = down + 1
            if seat_map[down][char] != '.':
                seats_around.append(seat_map[down][char])
                break

        #down-left
        down = row
        left = char
        while down != map_length - 1 and left != 0:
            down = down + 1
            left = left - 1
            if seat_map[down][left] != '.':
                seats_around.append(seat_map[down][left])
                break
        
        #down-right
        down = row
        right = char
        while down != map_length - 1 and right != row_length - 1:
            down = down + 1
            right = right + 1
            if seat_map[down][right] != '.':
                seats_around.append(seat_map[down][right])
                break
        
        return seats_around

    @staticmethod
    def _getSeatsAround(seat_map, row, char):
        
        seats_around= []
        map_length = len(seat_map)
        row_length = len(seat_map[0])

        #left pixels
        if char != 0: #unless in left boundary
            seats_around.append(seat_map[row][char-1]) #same row
            if row != 0: # unless in top row
                seats_around.append(seat_map[row-1][char-1]) #top row
            if row != map_length-1: #unless bottom row
                seats_around.append(seat_map[row+1][char-1]) #bottom row
        
        #same row pixels
        if row != 0: # unless in top row
            seats_around.append(seat_map[row-1][char]) #left pixel
        if row != map_length-1: #unless bottom row
            seats_around.append(seat_map[row+1][char]) #right pixel
        
        #right pixels
        if char != row_length-1:
            seats_around.append(seat_map[row][char+1]) #same row
            if row != 0: # unless in top row
                seats_around.append(seat_map[row-1][char+1]) #top row
            if row != map_length-1: #unless bottom row
                seats_around.append(seat_map[row+1][char+1]) # bottom row
        return seats_around


    @staticmethod
    def _readInitialFile(path="11_input.dat"):
        data = []
        file_path=(os.path.dirname(__file__)) + "/" + path
        with open(file_path,'r') as f:
            data = f.read().splitlines() 
        return data
