#!/usr/bin/python

import os
import sys
import unittest

sys.path.insert(0, os.path.abspath('..'))

from rubik_box import rubik_box as rubik

class TestInstallation(unittest.TestCase):
    def test(self):
        self.assertEqual(rubik.isInstalled(), 'yes')

face_numbers = dict(front = 0, top = 1, right = 2, back = 3, bottom = 4, left = 5)
face_names = {number:name for name, number in face_numbers.iteritems()}
face_acrosses = dict(front='back', back='front', left='right', right='left', top='bottom', bottom='top')

class TestCube(unittest.TestCase):
    def test_across_faces_names(self):
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

    
if __name__ == '__main__':
    unittest.main()
