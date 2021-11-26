from random import random

#Define your make_noise function below
def make_noise():
    print("THE CROWD GOES WILD")

#Then, call make_noise once:
make_noise()


# Write a function called speak_pig that returns 'oink'
def speak_pig():
    return 'oink'
    
print(speak_pig())

#Define a function called generate_evens
#It should return a list of even numbers between 1 and 50(not including 50)
def generate_evens():
    return [n for n in range(1,50) if n%2 == 0]

print(generate_evens())


#Yell function
def yell(test ):
    return test.upper() + "!" 
print(yell("What's up"))