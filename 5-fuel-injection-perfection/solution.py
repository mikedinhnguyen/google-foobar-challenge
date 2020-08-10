def solution(n):
  count = 0
  fuel = int(n)
  while (fuel > 1): 
    if (fuel % 2 == 0):
      fuel = fuel / 2
    elif ((fuel == 3) or (fuel % 4 == 1)):
      fuel -= 1
    else:
      fuel += 1
    count += 1
  return count
