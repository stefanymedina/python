# Decremente list

def decrement_list(args):
    return list(map(lambda x : x-1, args))

print(decrement_list([1,2,3]))

# Filter - remove negative

def remove_negative(collect):
    return list(filter(lambda i: i >= 0, collect))


print(remove_negative([-1,2,4,-99]))