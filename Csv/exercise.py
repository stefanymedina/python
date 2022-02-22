from csv import  writer
from csv import DictReader
def add_user(first, last):
    with open("users.csv", "a") as f:
        csv_write = writer(f)
        csv_write.writerow([first, last])

#add_user("Carlos", "perez")

def print_user():
    with open("users.csv") as file:
        csv_reader = DictReader(file)
        for row in csv_reader:
            print("{} {}".format(row['First Name'],row['Last Name']))

print_user()


def find_user(first, last):
    with open("users.csv") as file:
        csv_reader = DictReader(file)
        cont = 0
        for row in csv_reader:
            cont +=1
            if row['First Name'] == first and row['Last Name'] == last :
                return cont 
        return 'Not Here not found.'

print(find_user('Carlos', 'perez'))