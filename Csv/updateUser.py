from csv import  writer
from csv import reader

def update_users(firstOld, lastOld, firstNew, lastNew):
    with open("users.csv") as file:
        csv_reader = reader(file)
        rows = list(csv_reader)
    cont = 0
    with open("users.csv", "w") as file:
        csv_writer = writer(file)
        for row in rows:
            if row[0] == firstOld and row[1] == lastOld :
                cont += 1
                csv_writer.writerow([firstNew, lastNew])

            else:
                csv_writer.writerow(row)
    return "User updated:{}".format(cont)





def delete_users(firstOld, lastOld):
    with open("users.csv") as file:
        csv_reader = reader(file)
        rows = list(csv_reader)
    cont = 0
    with open("users.csv", "w") as file:
        csv_writer = writer(file)
        for row in rows:
            if row[0] == firstOld and row[1] == lastOld :
                cont += 1
            else:
                csv_writer.writerow(row)
    return "Users deleted: {}".format(cont)



print(delete_users("Colt", "Steele"))