#Max + Abs
def max_magnitude(nums):
    return max(list(abs(i) for i in nums))

print(max_magnitude([300, 20, -900]))


#Sum even values

def sum_even_values(*args):
    return sum(i for i in args if i%2 == 0)

print(sum_even_values(1))

#Sum floats
def sum_floats(*args):
    return sum(i for i in args if type(i) == float)

print(sum_floats(1.5, 2.4, 'awesome', [],1))