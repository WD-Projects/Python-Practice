import os

if os.path.exists("file\\first.txt"):
    print(os .path.abspath("file\\first.txt")) #getting the full path
else:
    print("File not found")

