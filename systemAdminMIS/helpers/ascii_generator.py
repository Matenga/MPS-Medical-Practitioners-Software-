#Author=> Adriko Debo joel. Copyright 2017.
import random
import string
import base64
class LightEncryption(object):
    """docstring for LightEncryption."""
    def encode(self,key, clear):
      enc = []
      for i in range(len(clear)):
        key_c = key[i % len(key)]
        enc_c = chr((ord(clear[i]) + ord(key_c)) % 256)
        enc.append(enc_c)
      return base64.urlsafe_b64encode("".join(enc).encode()).decode()

    def decode(self,key, enc):
      dec = []
      enc = base64.urlsafe_b64decode(enc).decode()
      for i in range(len(enc)):
        key_c = key[i % len(key)]
        dec_c = chr((256 + ord(enc[i]) - ord(key_c)) % 256)
        dec.append(dec_c)
      return "".join(dec)
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
