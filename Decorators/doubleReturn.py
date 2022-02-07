from functools import wraps

def double_return(fn):
    @wraps(fn)
    def inner(*args, **kwargs):
        result = fn(*args, **kwargs)
        return [result, result]
    return inner

@double_return
def add(x,y):
    return x + y

print(add(1,2))


def ensure_fewer_than_three_args(fn):
    @wraps(fn)
    def inner(*args, **kwargs):
        result = fn(*args, **kwargs)
        if len(args) >= 3:
            return "Too many arguments!"
        else:
            return result    
    return inner

def sum(args):
    total = 0
    for i in args:
        total += i
    return total

@ensure_fewer_than_three_args
def add_all(*nums):
    return sum(nums)

print(add_all(1,2))




def only_ints(fn):
    @wraps(fn)
    def internal(*args, **kwargs):
        if any([val for val in args if type(val) == int]):
            return fn(*args, **kwargs)
        return "Please only invoke with integers."
    return internal

@only_ints
def add(x,y):
    return x + y


print(add(2,12))