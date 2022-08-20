open("numberamount.txt","w")

def test(number):
  x = int(number)
  amount = 0
  while x != 1:
    if x % 2 != 0:
      x = x*3+1
    else:
      x /= 2
    amount +=1
    print(f"Testing {number}, I am currently at {amount} tries and at number {x}")
  with open("numberamount.txt",'a') as f:
    if len(open("numberamount.txt","r").readlines()) != 0:
      f.write("\n")
    f.write(str(number)+"="+str(amount))
  if x == 1:
    return(True)
  else:
    exit(str(number)+"!")

index = 1000000000000 #1 trillion
x = True
while x == True:
  x = test(index)
  index+=1
