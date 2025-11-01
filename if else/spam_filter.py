p1 = "this is now"
p2 = "click now"
p3 = "It is not good"

message = input("Enter your text: ")

if((p1 in message) or (p2 in message) or (p3 in message)):
    print("This is spam message")
else:
    print("This is not spam")