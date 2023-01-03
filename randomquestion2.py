import psycopg2
import random

connection = psycopg2.connect(database="Student Details",
                              user='postgres', password='root', host='127.0.0.1', port='5432')
cursor = connection.cursor()
print("Connected to PSQL\n\n")

# data is stored as lists
data = list(range(1, 7))
random.shuffle(data)

# the given list is traversed
for i in data:
    i = str(i)
    query = "select q_text from question where q_id= " + i
    cursor.execute(query)
    records = cursor.fetchall()
    print(records, "\n")
