import random

class algorithms:
  def __init__(self, arr):
    self.arr = arr
    self.letters = ""  

  def _shuffle(self,string):
    tempList = list(string)
    random.shuffle(tempList)
    return ''.join(tempList)

  def randoms(self):
    
    for i in range(int(self.arr[0])):
      temp = chr(random.randint(65,90))
      self.letters = self.letters + temp

    for i in range(int(self.arr[1])):
      temp = chr(random.randint(97,122))
      self.letters += temp

    for i in range(int(self.arr[2])):
      temp = chr(random.randint(48,57))
      self.letters += temp
      
    for i in range(int(self.arr[3])):
      temp = chr(random.randint(33,47))
      self.letters += temp

    return self._shuffle(self.letters)

