import random
correct_no = int(input("Think of a number between 1 and 100 and enter it (for testing): "))
computer_guess = random.randint(1, 100)
print(f"Computer guesses: {computer_guess}")
count = 0
while True:
    count += 1
    feedback = input("Your feedback (H/L/C): ").strip().upper()
    if feedback == "H":
        computer_guess = random.randint(1, computer_guess - 1)
        print(f"Computer guesses: {computer_guess}")
    elif feedback == "L":
        computer_guess = random.randint(computer_guess + 1, 100)
        print(f"Computer guesses: {computer_guess}")
    elif feedback == "C":
        print("Computer guesses the correct number.")
        break
    else:
        print("Please enter valid feedback!!!")
print(f"Computer guessed your number in {count} tries!")