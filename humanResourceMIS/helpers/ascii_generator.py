#Author=> Adriko Debo joel. Copyright 2017.
import random
import string
class ascii_52(object):
  '''Represents the generation of 52 ascii letter strings'''
  def __init__(self):
    self.mes=''
    for char_ in random.sample(string.ascii_letters,52):
      self.mes+=char_
class ascii_104(object):
  '''Represents the generation of 104 ascii letter strings'''
  def __init__(self):
    self.ascii_1=ascii_52()
    self.ascii_2=ascii_52()
    self.mes=self.ascii_1.mes+self.ascii_2.mes
class ascii_156(object):
  '''Represents the generation of 156 ascii letter strings'''
  def __init__(self):
    self.ascii_1=ascii_52()
    self.ascii_2=ascii_104()
    self.mes=self.ascii_1.mes+self.ascii_2.mes
class ascii_208(object):
  '''Represents the generation of 208 ascii letter strings'''
  def __init__(self):
    self.ascii_1=ascii_104()
    self.ascii_2=ascii_104()
    self.mes=self.ascii_1.mes+self.ascii_2.mes
class ascii_260(object):
  '''Represents the generation of 260 ascii letter strings'''
  def __init__(self):
    self.ascii_1=ascii_208()
    self.ascii_2=ascii_52()
    self.mes=self.ascii_1.mes+self.ascii_2.mes
class ascii_312(object):
  '''Represents the generation of 312 ascii letter strings'''
  def __init__(self):
    self.ascii_1=ascii_208()
    self.ascii_2=ascii_104()
    self.mes=self.ascii_1.mes+self.ascii_2.mes
class ascii_624(object):
  '''Represents the generation of 624 ascii letter strings'''
  def __init__(self):
    self.ascii_1=ascii_312()
    self.ascii_2=ascii_312()
    self.mes=self.ascii_1.mes+self.ascii_2.mes
