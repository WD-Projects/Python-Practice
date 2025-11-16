# f = open("file/first.txt", "a")
# f.write(" This is file 3")
# print(f)

with open("file\\first.txt", "a") as f:
    f.write("I am Mahir")
    print(f)