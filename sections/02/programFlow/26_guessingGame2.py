import random

highest = 11
answer = random.randint(1, highest)
print(answer)

print("Please guess number between 1 and {}: ".format(highest))
guess = int(input())

if guess == 0:
    print("You are not fun at all")
elif guess == answer and guess != 0:
    print("Well done, you guessed it on the first try")

while guess != answer and guess != 0:
    guess = int(input("Make another guess: "))
    if guess == 0:
        print("You are 2nd time not fun at all today")
        break
    elif guess == answer:
        print("Well done, this time you guessed it correct")
        break
    else:
        if guess < answer:
            print("Please guess higher")
        else:
            print("Please guess lower")
