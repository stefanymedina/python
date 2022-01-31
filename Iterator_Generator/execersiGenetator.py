#week exercis
def week():
    days = ['Monday','tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
    for day in days:
        yield day

w1 = week()

# yes_or_no
def yes_or_no():
    word = 'yes'
    while True:
        yield word
        word = 'no' if word == 'yes' else 'yes'

#"{} bottles of {} on the wall.".format(cont, beverage)
#Make song
def make_song(num = 99, beverage="Soda"):
    while num > 0:
        if num == 1:
            yield "Only 1 bottle of {} on the wall.".format(beverage)
        else:
            yield "{} bottles of {} on the wall.".format(num, beverage)
        num -=1
    yield "No more {}!".format(beverage)
    


#get_multiples
def get_multiples(num=1, count=10):
    for cont in range(1,count+1):
        yield num * cont


#get_unlimetd_multipeles
def get_unlimited_multiples(num=1):
    cont = 1
    while True:
        yield num * cont
        cont += 1
