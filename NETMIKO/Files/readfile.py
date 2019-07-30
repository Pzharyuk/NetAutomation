import csv

f = open("/home/pzharyuk/writetofile.csv", "r")

if f.mode == 'r':
    contents = f.read()
    print(contents)