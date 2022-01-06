# some example about min a max

nums = [1,2,88,9,65]
print(max(nums)) #returns the maximun numbers
print(min(nums))

# Another example a litter more difficult

users = [
    {"name" :"Car", "age" : 5, "tweets": 5},
    {"name" :"Peteer P", "age" : 20, "tweets": 4},
    {"name" :"Simon", "age" : 15, "tweets": 1}
    ]

# in this we need to know who is the most large name in the collection, the last
# parameter is only to return only the name and not all the array
print(max(users, key=lambda n:len(n['name']))['name'])

# in this we need to know who has more tweets in the collection, the last
# parameter is only to return only the tweets and not all the array
print(max(users, key=lambda n:n['tweets'])['tweets'])


#Extrems
#  some give you a list a need that you return in a tupple the min a max value of 
# the collection:

def extremes(collec):
    return (min(collec), max(collec))

print(extremes((99,25,30,-7))