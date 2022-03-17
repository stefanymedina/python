import re
def parse_date(arg):
    valid_date = re.compile(r'^(?P<d>\d\d)[.,/](?P<m>\d\d)[.,/](?P<y>\d{4})$')
    match = valid_date.search(arg)
    if match:
        return {'d' : match.group("d"), 'm' : match.group('m'), 'y': match.group('y')}
    return None 
print(parse_date("12,03/2003")) 