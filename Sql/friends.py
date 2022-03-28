import sqlite3
conn = sqlite3.connect("my_firends.db")

#create cursor object
c = conn.cursor()
# Execute some sql
# c.execute("CREATE TABLE friends (first_name TEXT, last_name TEXT, close_name TEXT);"
# insert_query = '''INSERT INTO friends 
#                     VALUES ('Luis', 'Lopez', 7);'''
# data = "dana"
# query = f"INSERT INTO friends (first_name) VALUES (?)"
# c.execute(query, (data,))   
data = ('stef', 'carol', 2)
query = f"INSERT INTO friends VALUES (?,?,?)"
c.execute(query, (data))  

# commit change
conn.commit()
conn.close


