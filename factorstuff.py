x = int(input("x?\n"));y=int(input("y?\n"))
def checkfactors(checknum):
  factors = []
  for i in range(1, checknum+1):
    (factors.append(i) if checknum % i == 0 else 1)
  if (bool(len(factors)>1)) and checknum in factors:
    return True
  else:
    return False
while bool(checkfactors((x*y)+1)) != True:
  x *= y;
print(x*y)
