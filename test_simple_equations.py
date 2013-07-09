#!/usr/bin/env python

import unittest

class TestSimpleEquations(unittest.TestCase):
  
  def test_equals(self):
    self.assertEquals(3, 3)
    
    check = 3 + 5
    expect = 4 + 4
    self.assertEquals(check, expect)
    
    check = 10**6
    expect = 1000000
    self.assertEquals(check, expect)
    
    check = -(-20)
    expect = 20
    self.assertEquals(check, expect)
  
  def test_more_than_one_equals(self):
    check = 3 + 5 == 4 + 4 == 10 -2
    self.assertTrue(check)
    
    check = 1000000 == 1000 * 1000 == 10**3 * 10**3 == 10**6
    self.assertTrue(check)
    
    check = -(-20) == -1 * -20 == 20
    self.assertTrue(check)
    

if __name__ == '__main__':
  unittest.main()