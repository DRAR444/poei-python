def bubule():
  list = [4, 8, 415, 1, 25, 75, 6]
  last = True
  limit = len(list)
  while last:
     for i in range(0, limit-1):
        last = False
        if (list[i] > list[i+1]):
           list[i+1], list[i] = list[i], list[i+1]
           last = True
     limit = limit - 1
  print(list)