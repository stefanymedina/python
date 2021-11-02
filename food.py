from random import choice
food = choice(['apple','grape', 'bacon', 'steak', 'worm', 'dirt'])
# NO TOUCHING =============================================


# YOUR CODE GOES HERE vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv
print("the food is " + food)
if food == "apple" or food == "grape":
    print("fruit")
elif food == "bacon" or food == "steak":
    print("meat")
else:
    print("yuck")