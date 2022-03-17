import re

def is_valid_time(arg):
    validate_time = re.compile(r'^\d\d?:\d\d$')
    match = validate_time.search(arg)
    if match:
        return True
    return False

print(is_valid_time("12:15"))
print(is_valid_time("1:15"))