# Intervaling String

def interleave(str1, str2):
    str_r = ''
    for i in (zip(str1, str2)):
        for a in i:
            str_r = str_r + a
    return str_r

# a shorter solution

def interleave(str1,str2):
    return ''.join(''.join(x) for x in (zip(str1,str2)))

print(interleave('aaa','zzz'))


def triple_and_filter(coll):
    return list((num*3) for num in coll if num % 4 == 0)

print(triple_and_filter([1,2,3,4]))


#Extract Full name
def extract_full_name(l):
    return list(map(lambda val: "{} {}".format(val['first'], val['last']), l))


names = [{'first': 'Elie', 'last': 'Schoppik'}, {'first': 'Colt', 'last': 'Steele'}]
print(extract_full_name(names))