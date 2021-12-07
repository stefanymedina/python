# define product below:
# function that return the product of the two parameters
def product(num1,num2):
    return num1 * num2

print(product(2,3))

#return day of the week

def return_day(day):
    days = {1 : "Sunday" , 2 : "Monday", 3:"Tuesday", 4:"Wednesday", 5 : "Thursday", 6:"Friday", 7:"Saturday"}
    if days.get(day):
        return days.get(day)
    return None
print(return_day(8))

# return last element

def last_element(info):
    if info:
        return info[-1]
    return None

print(last_element([]))

# compare 2 numbers
def number_compare(num1,num2):
    if num1 == num2:
        return "Numbers are equal"
    elif num1 > num2:
        return "First is greater"
    return "Second is grater"
        
print(number_compare(1,1))


# count letter

def single_letter_count(word1,letter):
    return word1.lower().count(letter.lower())

print(single_letter_count("Hello World", "z"))


# count multiple letter

def multiple_letter_count(word1):
    return { letter : word1.count(letter) for letter in word1}


print(multiple_letter_count("casa"))

#list manipulation 

def list_manipulation(numbers, action, loc, num = 0):
    if action == 'remove':
        if loc == 'end':
            resul = numbers.pop()
        else :
            resul = numbers.pop(0)
    elif action == 'add':
        if loc == 'end':
            numbers.append(num)
            resul = numbers
        else :
            numbers.insert(0,num)
            resul = numbers
    return resul

print(list_manipulation([1,2,3], "add", "end", 30))

#plindrome

def is_palindrome(word):
    word_res = ''.join(char for char in word if char is not " ")
    return word_res == word_res[::-1]
print(is_palindrome("amanaplanacanalpanama"))

# frequency

def frequency(list, item):
    return list.count(item)

print(frequency([True, False, True, True], False))


#myltiply even numbers
def multiply_even_numbers(numbers):
    cont = 1
    for num in numbers:
        if num%2 == 0:
            cont = cont * num
    return cont
print(multiply_even_numbers([2,3,4,5,6]))

def capitalize(test):
    test[0].upper()+test[1:]

print(capitalize("tim"))



#'''compact([0,1,2,"",[], False, {}, None, "All done"]) # [1,2, "All done"]'''
def compact(collection):
    return [item for item in collection if item]

print(compact([0,1,2,"",[], False, {}, None, "All done"]))    



# flesh out intersection 
def intersection(collec1, collec2):
    return [item for item in collec1 if item in collec2]


print(intersection([1,2,3,1],[3,2,4,1]))
#this solution is ok but if a number is duplicate this appears all the times that this appears

# flesh out intersection 
def bestintersection(collec1, collec2):
    return [item for item in set(collec1) & set(collec2)]

print(bestintersection([1,2,3,1],[3,2,4,1]))



#'''def isEven(num):
#return num % 2 == 0
#partition([1,2,3,4], isEven) # [[2,4],[1,3]]



def partition(colle, func):
    return [[item for item in colle if isEven(item)],[i for i in colle if not isEven(i)]]

def isEven(num):
    if num % 2 == 0:
        return True
    else:
        return False

print(partition([1,2,3,4], isEven))