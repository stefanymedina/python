# for num in range(9):
#     print("\U0001f600" * num)

num = 1
num_aux = 11
while num < 11:
    if(num == 1):
        print((" " * num_aux)+"\U0001f600" * num)
    else:
        print((" " * num_aux)+"\U0001f600 " * num) 
    num += 1
    num_aux -= 1


# #ugly solution
# for num in range(9):
#    x = 0
#    char = ""  
#    while x <= num: 
#     char += "\U0001f600"
#     x += 1
#    print(char+'\n')

