#!/usr/bin/python

from __future__ import print_function
import os
import sys
import unittest
import copy

sys.path.insert(0, os.path.abspath('..'))

from rubik_box import rubik_box as rubik

class TestInstallation(unittest.TestCase):
    def test(self):
        self.assertEqual(rubik.isInstalled(), 'yes')

face_numbers = dict(front = 0, top = 1, right = 2, back = 3, bottom = 4, left = 5)
face_names = {number:name for name, number in face_numbers.iteritems()}
face_acrosses = dict(front='back', back='front', left='right', right='left', top='bottom', bottom='top')


def out(c,cont,  a = []):
    if len(a) %2 == 0:
        print(cont)
        for i in range(6):
            print(c.face_name[i])
            print(c.side(i))
            print('')
        print('')
    else:
        with open('a.txt', 'a') as f:
            print(cont, file = f)
            for i in range(6):
                print(c.face_name[i], file = f)
                print(c.side(i), file = f)
                print('', file = f)
            print('', file = f)
    a.append(0)

class TestCube(unittest.TestCase):
    def test_across_faces_names(self):
        a = 0
        c = rubik.Cube(1)
        for face, expected_across in face_acrosses.iteritems():
            got_across_number = c.face_across[face_numbers[face]]
            got_name_across = c.face_name[got_across_number]
            self.assertEqual(expected_across, got_name_across)


    def test_face_number_to_name(self):
        c = rubik.Cube(1)
        for i in range(6):
            self.assertEqual(face_names[i], c.face_name[i])


    def test_face_name_to_number(self):
        c = rubik.Cube(1)
        for i in range(6):
            expected_name = face_names[i];
            self.assertEqual(c.face_name[i], expected_name)


    def test_rotation_from_top_0_clockwise(self):
        c = rubik.Cube(4)
        c.side("front").set_all([x for x in range(0, 16)]);
        c.side("top").set_all([x for x in range(16, 32)]);
        c.side("bottom").set_all([x for x in range(32, 48)])
        c.side("left").set_all([x for x in range(48, 64)])
        c.side("right").set_all([x for x in range(64, 80)])
        c.side("back").set_all([x for x in range(80, 96)])

        context = "top 0 cw"
        out(c, context)
        expected = copy.deepcopy(c)
        c.rotate_nth_from_top(0, 1)
        out(c, context)

    def test_rotation_from_top_1_clockwise(self):
        c = rubik.Cube(4)
        c.side("front").set_all([x for x in range(0, 16)]);
        c.side("top").set_all([x for x in range(16, 32)]);
        c.side("bottom").set_all([x for x in range(32, 48)])
        c.side("left").set_all([x for x in range(48, 64)])
        c.side("right").set_all([x for x in range(64, 80)])
        c.side("back").set_all([x for x in range(80, 96)])
        
        context = "top 1 clockwise"
        out(c, context)
        expected = copy.deepcopy(c)
        c.rotate_nth_from_top(1, 1)
        out(c, context)
    
    def test_rotation_from_bot_0_clockwise(self):
        c = rubik.Cube(4)
        c.side("front").set_all([x for x in range(0, 16)]);
        c.side("top").set_all([x for x in range(16, 32)]);
        c.side("bottom").set_all([x for x in range(32, 48)])
        c.side("left").set_all([x for x in range(48, 64)])
        c.side("right").set_all([x for x in range(64, 80)])
        c.side("back").set_all([x for x in range(80, 96)])
        
        context = "bot 0 clockwise"
        out(c, context)
        expected = copy.deepcopy(c)
        c.rotate_nth_from_bottom(0, 1)
        out(c, context)
    

    def test_rotation_from_bot_1_clockwise(self):
        c = rubik.Cube(4)
        c.side("front").set_all([x for x in range(0, 16)]);
        c.side("top").set_all([x for x in range(16, 32)]);
        c.side("bottom").set_all([x for x in range(32, 48)])
        c.side("left").set_all([x for x in range(48, 64)])
        c.side("right").set_all([x for x in range(64, 80)])
        c.side("back").set_all([x for x in range(80, 96)])
        
        context = "bot 1 clockwise"
        out(c, context)
        expected = copy.deepcopy(c)
        c.rotate_nth_from_bottom(1, 1)
        out(c, context)
        pass
    
    def test_rotation_from_lef_0_clockwise(self):
        c = rubik.Cube(4)
        c.side("front").set_all([x for x in range(0, 16)]);
        c.side("top").set_all([x for x in range(16, 32)]);
        c.side("bottom").set_all([x for x in range(32, 48)])
        c.side("left").set_all([x for x in range(48, 64)])
        c.side("right").set_all([x for x in range(64, 80)])
        c.side("back").set_all([x for x in range(80, 96)])

        context = "left 0 clockwise"
        out(c, context)
        expected = copy.deepcopy(c)
        c.rotate_nth_from_left(0, 1)
        out(c, context)
        pass
    

    def test_rotation_from_lef_1_clockwise(self):
        c = rubik.Cube(4)
        c.side("front").set_all([x for x in range(0, 16)]);
        c.side("top").set_all([x for x in range(16, 32)]);
        c.side("bottom").set_all([x for x in range(32, 48)])
        c.side("left").set_all([x for x in range(48, 64)])
        c.side("right").set_all([x for x in range(64, 80)])
        c.side("back").set_all([x for x in range(80, 96)])
        
        context= "left 1 clockwise"
        out(c, context)
        expected = copy.deepcopy(c)
        c.rotate_nth_from_left(1, 1)
        out(c, context)
        pass
    
    def test_rotation_from_rig_0_clockwise(self):
        c = rubik.Cube(4)
        c.side("front").set_all([x for x in range(0, 16)]);
        c.side("top").set_all([x for x in range(16, 32)]);
        c.side("bottom").set_all([x for x in range(32, 48)])
        c.side("left").set_all([x for x in range(48, 64)])
        c.side("right").set_all([x for x in range(64, 80)])
        c.side("back").set_all([x for x in range(80, 96)])

        context= "rig 0 clockwise"
        out(c, context)
        expected = copy.deepcopy(c)
        c.rotate_nth_from_right(0, 1)
        out(c, context)
        pass
    
    def test_rotation_from_rig_1_clockwise(self):
        c = rubik.Cube(4)
        c.side("front").set_all([x for x in range(0, 16)]);
        c.side("top").set_all([x for x in range(16, 32)]);
        c.side("bottom").set_all([x for x in range(32, 48)])
        c.side("left").set_all([x for x in range(48, 64)])
        c.side("right").set_all([x for x in range(64, 80)])
        c.side("back").set_all([x for x in range(80, 96)])

        context= "rig 1 clockwise"
        out(c, context)
        expected = copy.deepcopy(c)
        c.rotate_nth_from_right(1, 1)
        out(c, context)

    def test_rotation_from_bac_0_clockwise(self):
        c = rubik.Cube(4)
        c.side("front").set_all([x for x in range(0, 16)]);
        c.side("top").set_all([x for x in range(16, 32)]);
        c.side("bottom").set_all([x for x in range(32, 48)])
        c.side("left").set_all([x for x in range(48, 64)])
        c.side("right").set_all([x for x in range(64, 80)])
        c.side("back").set_all([x for x in range(80, 96)])

        context= "back 0 clockwise"
        out(c, context)
        expected = copy.deepcopy(c)
        c.rotate_nth_from_back(0, 1)
        out(c, context)
    
    def test_rotation_from_bac_1_clockwise(self):
        c = rubik.Cube(4)
        c.side("front").set_all([x for x in range(0, 16)]);
        c.side("top").set_all([x for x in range(16, 32)]);
        c.side("bottom").set_all([x for x in range(32, 48)])
        c.side("left").set_all([x for x in range(48, 64)])
        c.side("right").set_all([x for x in range(64, 80)])
        c.side("back").set_all([x for x in range(80, 96)])

        context= "bac 1 clockwise"
        out(c, context)
        expected = copy.deepcopy(c)
        c.rotate_nth_from_back(1, 1)
        out(c, context)
        c = rubik.Cube(4)
        c.side("front").set_all([x for x in range(0, 16)]);
        c.side("top").set_all([x for x in range(16, 32)]);
        c.side("bottom").set_all([x for x in range(32, 48)])
        c.side("left").set_all([x for x in range(48, 64)])
        c.side("right").set_all([x for x in range(64, 80)])
        c.side("back").set_all([x for x in range(80, 96)])

        context = "back 1 clockwise"
        out(c, context)
        expected = copy.deepcopy(c)
        c.rotate_nth_from_front(0, 1)
        out(c, context)

    def test_rotation_from_fro_1_clockwise(self):
        c = rubik.Cube(4)
        c.side("front").set_all([x for x in range(0, 16)]);
        c.side("top").set_all([x for x in range(16, 32)]);
        c.side("bottom").set_all([x for x in range(32, 48)])
        c.side("left").set_all([x for x in range(48, 64)])
        c.side("right").set_all([x for x in range(64, 80)])
        c.side("back").set_all([x for x in range(80, 96)])

        context= "from 1 clockwise"
        out(c, context)
        expected = copy.deepcopy(c)
        c.rotate_nth_from_front(1, 1)
        out(c, context)




    def test_rotation_from_top_0_counter_clockwise(self):
        c = rubik.Cube(4)
        c.side("front").set_all([x for x in range(0, 16)]);
        c.side("top").set_all([x for x in range(16, 32)]);
        c.side("bottom").set_all([x for x in range(32, 48)])
        c.side("left").set_all([x for x in range(48, 64)])
        c.side("right").set_all([x for x in range(64, 80)])
        c.side("back").set_all([x for x in range(80, 96)])

        context = "top 0 ccw"
        out(c, context)
        expected = copy.deepcopy(c)
        c.rotate_nth_from_top(0, 0)
        out(c, context)

    def test_rotation_from_top_1_counter_clockwise(self):
        c = rubik.Cube(4)
        c.side("front").set_all([x for x in range(0, 16)]);
        c.side("top").set_all([x for x in range(16, 32)]);
        c.side("bottom").set_all([x for x in range(32, 48)])
        c.side("left").set_all([x for x in range(48, 64)])
        c.side("right").set_all([x for x in range(64, 80)])
        c.side("back").set_all([x for x in range(80, 96)])

        context = "top 1 ccw"
        out(c, context)
        expected = copy.deepcopy(c)
        c.rotate_nth_from_top(1, 0)
        out(c, context)
    
    def test_rotation_from_bot_0_counter_clockwise(self):
        c = rubik.Cube(4)
        c.side("front").set_all([x for x in range(0, 16)]);
        c.side("top").set_all([x for x in range(16, 32)]);
        c.side("bottom").set_all([x for x in range(32, 48)])
        c.side("left").set_all([x for x in range(48, 64)])
        c.side("right").set_all([x for x in range(64, 80)])
        c.side("back").set_all([x for x in range(80, 96)])

        context = "bot 0 ccw"
        out(c, context)
        expected = copy.deepcopy(c)
        c.rotate_nth_from_bottom(0, 0)
        out(c, context)
    

    def test_rotation_from_bot_1_counter_clockwise(self):
        c = rubik.Cube(4)
        c.side("front").set_all([x for x in range(0, 16)]);
        c.side("top").set_all([x for x in range(16, 32)]);
        c.side("bottom").set_all([x for x in range(32, 48)])
        c.side("left").set_all([x for x in range(48, 64)])
        c.side("right").set_all([x for x in range(64, 80)])
        c.side("back").set_all([x for x in range(80, 96)])

        context= "bot 1 ccw"
        out(c, context)
        expected = copy.deepcopy(c)
        c.rotate_nth_from_bottom(1, 0)
        out(c, context)
        pass
    
    def test_rotation_from_lef_0_counter_clockwise(self):
        c = rubik.Cube(4)
        c.side("front").set_all([x for x in range(0, 16)]);
        c.side("top").set_all([x for x in range(16, 32)]);
        c.side("bottom").set_all([x for x in range(32, 48)])
        c.side("left").set_all([x for x in range(48, 64)])
        c.side("right").set_all([x for x in range(64, 80)])
        c.side("back").set_all([x for x in range(80, 96)])

        context= "lef 0 ccw"
        out(c, context)
        expected = copy.deepcopy(c)
        c.rotate_nth_from_left(0, 0)
        out(c, context)
        pass
    

    def test_rotation_from_lef_1_counter_clockwise(self):
        c = rubik.Cube(4)
        c.side("front").set_all([x for x in range(0, 16)]);
        c.side("top").set_all([x for x in range(16, 32)]);
        c.side("bottom").set_all([x for x in range(32, 48)])
        c.side("left").set_all([x for x in range(48, 64)])
        c.side("right").set_all([x for x in range(64, 80)])
        c.side("back").set_all([x for x in range(80, 96)])

        context = "lef 1 ccw"
        out(c, context)
        expected = copy.deepcopy(c)
        c.rotate_nth_from_left(1, 0)
        out(c, context)
        pass
    
    def test_rotation_from_rig_0_counter_clockwise(self):
        c = rubik.Cube(4)
        c.side("front").set_all([x for x in range(0, 16)]);
        c.side("top").set_all([x for x in range(16, 32)]);
        c.side("bottom").set_all([x for x in range(32, 48)])
        c.side("left").set_all([x for x in range(48, 64)])
        c.side("right").set_all([x for x in range(64, 80)])
        c.side("back").set_all([x for x in range(80, 96)])

        context = "rig 0 ccw"
        out(c, context)
        expected = copy.deepcopy(c)
        c.rotate_nth_from_right(0, 0)
        out(c, context)
        pass
    
    def test_rotation_from_rig_1_counter_clockwise(self):
        c = rubik.Cube(4)
        c.side("front").set_all([x for x in range(0, 16)]);
        c.side("top").set_all([x for x in range(16, 32)]);
        c.side("bottom").set_all([x for x in range(32, 48)])
        c.side("left").set_all([x for x in range(48, 64)])
        c.side("right").set_all([x for x in range(64, 80)])
        c.side("back").set_all([x for x in range(80, 96)])

        context= "rig 1 ccw"
        out(c, context)
        expected = copy.deepcopy(c)
        c.rotate_nth_from_right(1, 0)
        out(c, context)

    def test_rotation_from_bac_0_counter_clockwise(self):
        c = rubik.Cube(4)
        c.side("front").set_all([x for x in range(0, 16)]);
        c.side("top").set_all([x for x in range(16, 32)]);
        c.side("bottom").set_all([x for x in range(32, 48)])
        c.side("left").set_all([x for x in range(48, 64)])
        c.side("right").set_all([x for x in range(64, 80)])
        c.side("back").set_all([x for x in range(80, 96)])

        context= "bac 0 ccw"
        out(c, context)
        expected = copy.deepcopy(c)
        c.rotate_nth_from_back(0, 0)
        out(c, context)
    
    def test_rotation_from_bac_1_counter_clockwise(self):
        c = rubik.Cube(4)
        c.side("front").set_all([x for x in range(0, 16)]);
        c.side("top").set_all([x for x in range(16, 32)]);
        c.side("bottom").set_all([x for x in range(32, 48)])
        c.side("left").set_all([x for x in range(48, 64)])
        c.side("right").set_all([x for x in range(64, 80)])
        c.side("back").set_all([x for x in range(80, 96)])

        context = "bac 1 ccw"
        out(c, context)
        expected = copy.deepcopy(c)
        c.rotate_nth_from_back(1, 0)
        out(c, context)

    def test_rotation_from_fro_0_counter_clockwise(self):
        c = rubik.Cube(4)
        c.side("front").set_all([x for x in range(0, 16)]);
        c.side("top").set_all([x for x in range(16, 32)]);
        c.side("bottom").set_all([x for x in range(32, 48)])
        c.side("left").set_all([x for x in range(48, 64)])
        c.side("right").set_all([x for x in range(64, 80)])
        c.side("back").set_all([x for x in range(80, 96)])

        context = "fro 0 ccw"
        out(c, context)
        expected = copy.deepcopy(c)
        c.rotate_nth_from_front(1, 0)
        out(c, context)

    def test_rotation_from_fro_1_counter_clockwise(self):
        c = rubik.Cube(4)
        c.side("front").set_all([x for x in range(0, 16)]);
        c.side("top").set_all([x for x in range(16, 32)]);
        c.side("bottom").set_all([x for x in range(32, 48)])
        c.side("left").set_all([x for x in range(48, 64)])
        c.side("right").set_all([x for x in range(64, 80)])
        c.side("back").set_all([x for x in range(80, 96)])

        context = "fro 1 ccw"
        out(c, context)
        expected = copy.deepcopy(c)
        c.rotate_nth_from_front(1, 0)
        out(c, context)


if __name__ == '__main__':
    unittest.main()
