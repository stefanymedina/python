#Arg exercise

def contains_purple(*args):
    if "purple" in args : return True
    return False
  
print(contains_purple(25,"purple"))

# **Kwargs Exercise

def combine_words(word,**kwargs):
    if 'prefix' in kwargs:
        return kwargs['prefix'] + word
    elif 'suffix' in kwargs:
        return word + kwargs['suffix']
    return word


print(combine_words("child", suffix="man"))