# WORKS WELL IN PYCHARM --- TRIED AND TESTED

import random

# count is used for logging in the number of tries.
count = 0

# score is -1. -1 is added so that the score is recorded properly.
score = -1

# chance is 1. 1 is the default value so that the loop runs forever till chances becomes 0.
chance = 1

while chance:
    print("   ","*" * 20)
    print("\tNumber Guessing Game")
    print("   ","*" * 20)

    print("\n\t1. Play the game.")
    print("\t2. Exit.\n")
    print("\tSelect your option [1-2] and press Enter: ", end='')

    option = int(input())

    if option == 1:

        # This function is for generating random numbers from 0 to 10. It is stored in x.
        # 0 => minimum value
        # 10 => maximum value

        x = random.randint(0, 10)

        print("Guess the number [min = 0 and max = 10] within 3 tries.")

        while count < 3:
            count = count + 1
            guess = int(input("Guess a number: "))

            if x == guess:
                print("Your guess was correct. Congratulations.\n")
                if count == 1:
                    score = 100

                elif count == 2:
                    score = 50

                elif count == 3:
                    score = 25

                print("Your score is", score, "\n")
                break

            elif x > guess:
                print("Your guess was small. Try again.\n")

            elif x < guess:
                print("Your guess was large. Try again.\n")

            if count == 3:
                print("All the chances are over. The correct number is %d.\n" % x)
                count = 0
                break
                # reset the counter otherwise, the loop will not break.

    elif option == 2:
        chance = 0
        exit()

    else:
        print("Invalid option selected. Try again.\n")
