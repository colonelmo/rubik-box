#!/usr/bin/python
import copy

def isInstalled():
    return 'yes'
    
class Face():
    def __init__(self, side_length):
        self.size = side_length
        self.squares = [[0 for __ in range(self.size)] for __ in range(self.size)]
    
    def __str__(self):
        return '\n'.join([' '.join(map(str, x)) for x in self.squares])
    
class Cube():
    face_name = {0: "front", 1: "top", 2:"right", 3:"back", 4:"bottom", 5:"left"}
    face_number = {name:number for number, name in face_name.iteritems()}
    face_across = {x:(x + 3)%6 for x in range(6)}
    _face_down = {'bottom':'back', 'top':'front'} 
    _face_up = {}
    _face_left = {}
    _face_right = {}

    
    def __init__(self, side_length):
        self.size = side_length
        self.sides = [Face(self.size) for __ in range(6)]
    
    def side(self, side):
        return self.sides[self.face_number.get(side, side)]
        
def out(*args):
    for cube in args:
        print cube.side(0)
        print ''

def main():
    c = Cube(1)

if __name__ == '__main__':
    main()        
