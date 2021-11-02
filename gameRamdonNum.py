import random
random_number = random.randint(1,10)
number_user = None

while number_user != random_number:
    number_user = int(input("Guess a number between 1 and 10:"))
    if number_user > random_number:
        print ("Too high, try again!")
    elif number_user < random_number :
        print("Too low, try again!")
    else:
        print("You guessed it! you won!")
        flag_user = input("Dou you want to keep playain? (y/n)")
        if flag_user == "y" :
            number_user = None
            random_number = random.randint(1,10)
        else:
            print("Thanks for paying. Bye!")
