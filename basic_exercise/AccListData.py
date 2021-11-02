people = ["Hanna","Louisa","Claudia", "Angela","Geoffrey", "aparna"]
cont = 0
for item in people:
    if(item == 'Hanna'):
        people[cont] = 'Hannah'
    elif(item == 'Geoffrey'):
        people[cont] = 'jeoffrey'
    elif(item == 'aparna'):
        people[cont] = 'Aparna'
    cont +=1

print(people)