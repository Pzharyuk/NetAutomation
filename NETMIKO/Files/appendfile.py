f = open("writetofile.csv", "a+")

for i in range(2):
    f.write("Append Line %d\r\n" % (i+1))

f.close()
