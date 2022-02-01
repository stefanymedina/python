from time import time
from functools import wraps

def wrapper_fun(fn):
    @wraps(fn)
    def inner_fun(*args, **kwargs):
        start_time = time()
        result = fn(*args, **kwargs)
        finish_time = time()
        print(f"the name of the fn is : {fn.__name__}")

        print(f"the finish time was:{finish_time - start_time}")
        return result
    return inner_fun
def sum(x):
    total = 0
    for num in x:
        total += num
    return total

@wrapper_fun
def sum_list():
    return sum([x for x in range(5000000)])
    
@wrapper_fun
def sum_gener():
    return sum(x for x in range(5000000))

print(sum_list())
print(sum_gener())