path = "C:\\Users\\kimtg\\OneDrive\\Desktop\\"

with open("%s%s" %(path, "output.txt"), "w") as fo:
    fo.write("hello world")