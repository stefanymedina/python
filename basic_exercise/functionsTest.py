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


# you need to have a perfect indentation in python, if not this maybe will give you
# some problems for example :

def count_dollar_signs(word):
    count = 0
    for char in word:
        if char == '$':
            count += 1
        return count  # --> this identation is not in the correct way because in this way
        # only count the first time that symbol $ appear beacuse is into the for and when the 
        # symbol apeear for the first time this return and not keep going throught the for 
        # to do the this work tou need put the return in the same level of the for like this:

def count_dollar_signs(word):
    count = 0
    for char in word:
        if char == '$':
            count += 1
    return count 

count_dollar_signs("$uper $size")


# talking Animals
def speak(animal = "dog"):
    if animal == "pig":
        return "oink"
    elif animal == "duck":
        return "quack"
    elif animal == "cat":
        return "meow"
    elif animal == "dog"
        return "woof"
    else:
        return "?"

print(speak())       
        






