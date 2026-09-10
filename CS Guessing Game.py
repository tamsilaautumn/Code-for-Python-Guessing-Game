print("GUESSING GAME")

print("1. Easy Level - 15 attempts")
print("2. Medium Level - 10 attempts")
print("3. Hard Level - 5 attempts")

level = eval(input("Enter your level: "))

if level == 1:
    tries = 15
elif level == 2:
    tries = 10
elif level == 3:
    tries = 5
else:
    print("Invalid level")
    exit()

number = eval(input("Enter any number between 1 and 100 to generate a secret number: "))

if number < 1 or number > 100:
    print("Invalid number")
    exit()

secret = (number * 7 + 13) % 100 + 1

print("Guess the secret number between 1 and 100")

count = 0
correct = False
hint = False

while count < tries:

    guess = eval(input("Enter your guess: "))
    count = count + 1

    if guess < 1 or guess > 100:
        print("Enter a number between 1 and 100")
        continue

    if guess == secret:
        print("Correct!")
        correct = True
        break
    else:
        if guess > secret:
            print("Too High")
        else:
            print("Too Low")

    if count >= 3 and hint == False:
        if secret % 2 == 0:
            print("Hint: The secret number is even.")
        else:
            print("Hint: The secret number is odd.")
        hint = True

for i in range(2):
    for j in range(2):
        pass

if correct:
    print("You won!")
else:
    print("Game Over")
    print("The secret number was", secret)