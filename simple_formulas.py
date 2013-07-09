#!/usr/bin/env python

from __future__ import division


class Rectangle(object):
  """Compute the area of a rectangle.
  
  A = bh
  
  Attributes:
    base: the base lenght of the rectangle
    height: the height of the rectangle.
  """
  def __init__(self, base, height):
    self.base = base
    self.height = height
  
  def area(self):
    """Compute the area of a rectangle.
    
    Returns:
      number: the area of the rectangle
    """
    return self.base * self.height
  
  def convert(self, unit=None):
    """Convert the area in meters to a differant unit.
    """
    unit_mapping = {'inches': 1550,
                    'feet': 144}
    return unit_mapping.get(unit) * self.area()


class Triangle(object):
  """Compute the area of a triangle.
  
  A = bh/2
  
  Args:
    base: the base lenght of the triangle in meters.
    height: the height of the triangle in meters.
  """
  def __init__(self, base, height):
    self.base = base
    self.height = height
  
  def area(self):
    """Compute the area of a triangle.
    
    Returns:
      number: the area of the triangle
    """
    return self.base * self.height / 2
  
  def convert(self, unit=None):
    """Convert the area in meters to a differant unit.
    """
    unit_mapping = {'inches': 1550,
                    'feet': 144}
    return unit_mapping.get(unit) * self.area()


class DistanceTraveled(object):
  """Compute the distance traveled.
  
  d = st
  
  Args:
    speed: the speed meters per second.
    time: the time in seconds.
  """
  def __init__(self, speed, time):
    self.speed = speed
    self.time = time
  
  def distance_traveled(self):
    """Compute the area of a triangle.
    
    Returns:
      number: the area of the triangle
    """
    return self.speed * self.time