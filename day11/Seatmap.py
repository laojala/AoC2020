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
        previous = Seatmap(Seatmap._readInitialFile())
        new = Seatmap([])

        while True:
            newLayout = Seatmap.countNewSeats(previous.layout)
            new.setLayout(newLayout)
            if previous.layout == new.layout:
                break
            else:
                previous.setLayout(new.layout)

        Seatmap.print_part_1_result(new)
        
    @staticmethod
    def print_part_1_result(seatmap):
        occupied = 0
        #count seats in new layout
        for row in seatmap.layout:
            occupied = occupied + row.count("#")
        assert(occupied == 2406)
        print('Occupied, part 1:', occupied)

    @staticmethod
    def countNewSeats(seats_map):
        
        new_seat_map = []
        
        for index_row,row in enumerate(seats_map):

            new_row = ''
            seats_around_spot=''

            for index_spot,spot in enumerate(row):

                #set floor to floor (no need to calculate statuses around the seat)
                if spot == '.':
                    new_row = new_row + '.'
                    continue
                #list seats statuses around the spot:
                seats_around_spot = Seatmap._getSeatsAround(seats_map, index_row, index_spot)

                if spot == '.':
                    new_row = new_row + '.'

                #occupy seat if it has only free seats around it
                if spot == 'L' and seats_around_spot.count('#') == 0:
                    new_row = new_row + '#'
                
                if spot == 'L' and seats_around_spot.count('#') >= 1:
                    new_row = new_row + 'L'

                #release seat if it has four or more occupied seats around it
                if spot == '#' and seats_around_spot.count('#') >= 4:
                    new_row = new_row + 'L'

                if spot == '#' and seats_around_spot.count('#') < 4:
                    new_row = new_row + '#'
            
                if index_spot != len(new_row) - 1:
                    raise Exception('nothing added to the row in this rounnd - why?')

            new_seat_map.append(new_row)
            new_row = ''
            seats_around_spot.clear()

        return new_seat_map


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

