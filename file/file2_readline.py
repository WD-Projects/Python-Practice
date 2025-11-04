# f = open("file/file2.txt")
# line1 = f.readlines()
# print(line1)


# f = open("file/file2.txt")
# line1 = f.readline()
# print(line1)
# line2 = f.readline()
# print(line2)
# line3 = f.readline()
# print(line3)
# line4 = f.readline()
# print(line4 == "")


f = open("file/file2.txt")
line  = f.readline()
while(line != ""):
    print(line)
    line = f.readline()

f.close()