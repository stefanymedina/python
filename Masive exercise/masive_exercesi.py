'''
Reverse string
'''

# add whatever parameters you deem necessary - good luck!



from itertools import count


def reverse_string(arg):
    return arg[::-1]
#print(reverse_string('awesome')) # 'emosewa'
#------------------------------------------------------------------------------

'''
List Check
'''

def list_check(args):
    for i in args:
        if type(i) != list:
            return False
    return True

#print(list_check([[],[1],[2,3], (1,2)])) # False

#------------------------------------------------------------------------------
'''
Remove every other
'''

def remove_every_other(arg):
    return arg[::2]

#print(remove_every_other([1,2,3,4,5])) # [1,3,5] 


#-----------------------------------------------------------------------------
'''
sum_pairs([4,2,10,5,1], 6) # [4,2]
sum_pairs([11,20,4,2,1,5], 100) # []
'''

def sum_pairs(list1,num):
    cont = 0
    for i in list1:
        if (i + list1[cont + 1]) == num :
            return [i , list1[cont + 1]]
    return []
#print(sum_pairs([11,20,4,2,1,5], 100))
#-----------------------------------------------------------------------------


'''
vowel_count('awesome') # {'a': 1, 'e': 2, 'o': 1}
vowel_count('Elie') # {'e': 2, 'i': 1}
vowel_count('Colt') # {'o': 1}
'''

def vowel_count(word):
    return {item : word.lower().count(item) for item in word if item in "aeiou" }

#print(vowel_count('Elie')) # {'a': 1, 'e': 2, 'o': 1}


#-----------------------------------------------------------------------------
'''
titleize('this is awesome') # "This Is Awesome"
titleize('oNLy cAPITALIZe fIRSt') # "ONLy CAPITALIZe FIRSt"
'''

def titleize(words):
    return ' '.join(word[0].upper()+word[1:] for word in words.split())

#print(titleize('this is awesome'))

#-----------------------------------------------------------------------------
'''
Find factor
find_factors(10) # [1,2,5,10 ]
find_factors(11) # [1,11]
'''

def find_factors(arg):
    cont = 1
    result = []
    while cont <= arg:
        if arg % cont == 0:
            result.append(cont)
        cont +=1
    return result

#print(find_factors(10))
#-----------------------------------------------------------------------------
'''
includes([1, 2, 3], 1) # True 
includes([1, 2, 3], 1, 2) # False 

'''
def includes(coll,num,start=0):
    if type(coll) == list or type(coll) == str :
        return num in coll[start:]
    return num in coll.values()

        
#print(includes([1, 2, 3], 1))
#-----------------------------------------------------------------------------
'''
repeat('*', 3) # '***' 
repeat('abc', 2) # 'abcabc' 
repeat('abc', 0) # ''
'''

def repeat(arg, repeat):
    if repeat > 0 :
        return arg * repeat

#print(repeat('abc',0))
#-----------------------------------------------------------------------------

'''
truncate("Super cool", 2) # "Truncation must be at least 3 characters."
truncate("Super cool", 1) # "Truncation must be at least 3 characters."
truncate("Super cool", 0) # "Truncation must be at least 3 characters."
truncate("Hello World", 6) # "Hel..."
truncate("Problem solving is the best!", 10) # "Problem..."
truncate("Another test", 12) # "Another t..."
truncate("Woah", 4) # "W..."
truncate("Woah", 3) # "..."
truncate("Yo",100) # "Yo"
truncate("Holy guacamole!", 152) # "Holy guacamole!"
'''

def truncate(word,num):
    if (num > len(word)):
        return word
    elif num >= 3:
        return word[:num-3]+"..."
    return "Truncation must be at least 3 characters."

#print(truncate("Yo",100))
#-----------------------------------------------------------------------------

'''
two_list_dictionary(['a', 'b', 'c', 'd'], [1, 2, 3]) # {'a': 1, 'b': 2, 'c': 3, 'd': None}
two_list_dictionary(['a', 'b', 'c']  , [1, 2, 3, 4]) # {'a': 1, 'b': 2, 'c': 3}
two_list_dictionary(['x', 'y', 'z']  , [1,2]) # {'x': 1, 'y': 2, 'z': None}
'''

def two_list_dictionary(list1,list2):
    dict = {}
    for idx, val in enumerate(list1):
        if idx < len(list2):
            dict[val] = list2[idx]
        else:
            dict[val] = None
    return dict

#print(two_list_dictionary(['a','b','c'],[1,2]))
#-----------------------------------------------------------------------------

'''
range_in_list([1,2,3,4],0,2) #  6
range_in_list([1,2,3,4],0,3) # 10
range_in_list([1,2,3,4],1) #  9
range_in_list([1,2,3,4]) # 10
range_in_list([1,2,3,4],0,100) # 10
range_in_list([],0,1) # 0
'''

def range_in_list(list,start=0,last=None):
    last = last or len(list)
    return sum(list[start:last+1])

#print(range_in_list([1,2,3,4],0,2))
#-----------------------------------------------------------------------------


'''
same_frequency(551122,221515) # True
same_frequency(321142,3212215) # False
same_frequency(1212, 2211) # True
'''

def same_frequency(num,num1):
    for n in str(num):
        if str(num).count(n) != str(num1).count(n):
            return False
    return True

            
#print(same_frequency(551122,551122))
#-----------------------------------------------------------------------------
'''
find_the_duplicate([1,2,1,4,3,12]) # 1
find_the_duplicate([6,1,9,5,3,4,9]) # 9
find_the_duplicate([2,1,3,4]) # None
'''

def find_the_duplicate(list):
    for i in list:
        if list.count(i) > 1 :
            return i
    return None

print(find_the_duplicate([1,2,1,4,3,12]))