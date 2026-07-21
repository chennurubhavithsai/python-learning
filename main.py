import random

secret = random.randint(1, 10)

guess = int(input("Guess a number (1-10): "))

if guess == secret:
    print("🎉 Congratulations! You guessed correctly.")
else:
    print("❌ Wrong guess.")
    print("The correct number was:", secret)