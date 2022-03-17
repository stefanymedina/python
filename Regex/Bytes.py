import re

def parse_bytes(arg):
    valid_bytes = re.compile(r'\b[10]{8}\b')
    match = valid_bytes.findall(arg)
    return match

print(parse_bytes("11010101 101 323"))