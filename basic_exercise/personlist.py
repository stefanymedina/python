person = [["name", "Jared"], ["job", "Musician"], ["city", "Bern"]]

answer = { i[0] : i[1] for i in person}


# concate aeiou
answer = dict.fromkeys("aeiou", 0) 


# create a dictonary that maps ASCII keys to their corresponding letter

answer = {i:chr(i) for i in range(65,91)}
print(answer)

