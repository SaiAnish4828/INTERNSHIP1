import psycopg2
import random


connection = psycopg2.connect(database="Student Details", user='postgres', password='root', host='127.0.0.1', port= '5432')
cursor = connection.cursor()
print("Connected to PSQL")

#getting a random number

randnum = random.randrange(1,7)
print(randnum)
strnum = str(randnum)
print(strnum)

# returning the query

query = "select q_text from question where q_id= " + strnum
cursor.execute(query)        
records = cursor.fetchall()
print(records)

