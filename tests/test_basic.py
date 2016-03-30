#!/usr/bin/python

import os
import sys
import unittest

sys.path.insert(0, os.path.abspath('..'))

from rubik_box import rubik_box as rubik

class TestInstallation(unittest.TestCase):
    def test(self):
        self.assertEqual(rubik.isInstalled(), "yes")

if __name__ == '__main__':
    unittest.main()
