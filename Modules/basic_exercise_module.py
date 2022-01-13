from math import sqrt
from keyword import iskeyword

answer = sqrt(15129)
print(answer)

# return true if any of the arguments are considered python keywords
def contains_keyword(*args):
    result = [iskeyword(x) for x in args]
    if True in result: return True
    return False

print(contains_keyword('hi','no'))