import random

top_of_range = input("Type a number: ")


if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <= 1:
        print("Please type a number more than 1")
        quit()

    elif top_of_range >= 100:
        print("Please type a number not more than 100")
        quit()
else:
    print("Please type a number")
    quit()

random_number = random.randint(0, top_of_range)
tries = 0

while True:
    tries += 1
    user_guess = input("Make a guess: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("Please type a number next time.")
        continue #continue to get into the top of the `while` func again

    if user_guess == random_number:
        print("You got it!")
        break
    elif user_guess > random_number:
        print("You were above the number! \n")
    else:
        print("You were below the number! \n")

print("You got it in", tries, "tries !")


