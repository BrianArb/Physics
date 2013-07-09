#!/usr/bin/env python

import unittest

from simple_formulas import (Rectangle,
                             Triangle,
                             DistanceTraveled)

class TestSimpleFormulas(unittest.TestCase):
  
  def test_area_of_a_rectangle(self):
    check = Rectangle(2, 2).area()
    expect = 4
    self.assertEquals(check, expect)
  
  def test_area_of_a_rectangle_in_inches(self):
    check = Rectangle(1, 1).convert('inches')
    expect = 1550
    self.assertEquals(check, expect)
  
  def test_area_of_a_rectangle_in_feet(self):
    """A = 144(bh)"""
    base = 1
    height = 1
    check = 144 * base * height
    expect = 144
    self.assertEquals(check, expect)
    
    check = Rectangle(1, 1).convert('feet')
    expect = 144
    self.assertEquals(check, expect)
    
  def test_area_of_a_rectangle_in_inches(self):
    """A = 1550(bh)"""
    base = 1
    height = 1
    check = 1550 * base * height
    expect = 1550
    self.assertEquals(check, expect)
    
    check = Rectangle(1, 1).convert('inches')
    self.assertEquals(check, expect)
    
  def test_area_of_a_triangle(self):
    check = Triangle(2, 2).area()
    expect = 2
    self.assertEquals(check, expect)

  def test_area_of_a_triangle_in_feet(self):
    """A = 144(bh)/2"""
    base = 1
    height = 1
    check = 144 * base * height / 2
    expect = 72
    self.assertEquals(check, expect)
    
    check = Triangle(1, 1).convert('feet')
    self.assertEquals(check, expect)
  
  def test_area_of_a_triangle_in_inches(self):
    """A = 1550(bh/2)"""
    base = 1
    height = 1
    check = 1550 * base * height / 2
    expect = 775
    self.assertEquals(check, expect)
    
    check = Triangle(1, 1).convert('inches')
    self.assertEquals(check, expect)
  
  def test_distance_traveled(self):
    check = DistanceTraveled(60, 1).distance_traveled()
    expect = 60
    self.assertEquals(check, expect)

if __name__ == '__main__':
  unittest.main()
  