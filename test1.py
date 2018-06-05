class MonIter():
   current = 0
   def __init__(self, stop):
       self.stop = stop
   def next(self):
       self.current += 1
       if self.current > self.stop:
           raise StopIteration
       if self.current == 5:
           print("Quoi déjà 5eme tour?")
       return self.current

for i in MonIter(10):
  print(i)