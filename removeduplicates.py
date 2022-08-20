def cleanupfile(file):
  r = open(file,"r").readlines()
  with open(file,"w") as f:
    x = list(set(r))
    for i in range(len(x)):
      omg = x[i]
      if "\n" not in omg:
        omg = omg+"\n"
      f.write(omg)
