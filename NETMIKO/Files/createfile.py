f = open("writetofile.csv", "w+")

for i in range(10):
    f.write("write this Line %d\r\n" % (i+1))

f.close()
