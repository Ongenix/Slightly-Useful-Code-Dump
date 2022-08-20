def deleteline(file,line):
    r = open(file,"r").readlines()
    r[line] = ""
    with open(file,"w") as f:
      f.writelines(r)
