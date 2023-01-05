import time
import random
import psycopg2

# connection to the database

connection = psycopg2.connect(database="Student Details",
                              user='postgres',
                              password='root',
                              host='127.0.0.1',
                              port='5432')
cursor = connection.cursor()
print("Connected to PSQL\n\n")

# providing static user details

print("===SURVEY IN THE WAIT PERIOD===\n")

e_name = input("enter your name= ")
e_id = int(input("enter your id= "))

# AppliData = ["sai", 1, 20, "pluginlive", "3 months"]
# name, e_id, age, company, waitperiod = AppliData
# print("name = ", name, "\nID = ", e_id, "\nage = ", age, "\ncompany = ",
#      company, "\nwait period = ", waitperiod)
# print("\n")

# week1 question set
print("===WEEK 1===\n")


def QS1():
    global join1
    join1 = 0
    data1 = list(range(1, 4))
    random.shuffle(data1)
    for i in data1:
        i = str(i)

        query = "select q_text from question where q_id= " + i
        cursor.execute(query)
        records = cursor.fetchall()
        print(records, "\n")
        for j in i:
            j = str(j)
            ans = int(input("enter your answer (yes(1) or no(0))\n"))
            if ans == 1:
                join1 += 1
            else:
                join1 += 0


QS1()

time.sleep(5)

print("\n===WEEK2===\n")


def QS2():
    global join2
    join2 = 0
    data2 = list(range(4, 7))
    random.shuffle(data2)
    for k in data2:
        k = str(k)
        query = "select q_text from question where q_id= " + k
        cursor.execute(query)
        records = cursor.fetchall()
        print(records, "\n")
        for m in k:
            m = str(m)
            ans = int(input("enter your answer (yes(1) or no(2))\n"))
            if ans == 1:
                join2 += 1
            else:
                join2 += 0


QS2()


join = join1 + join2

match join:
    case 6:
        predict = "more likely to join"
    case 5:
        predict = "more likely to join"
    case 4:
        predict = "likely to join"
    case 3:
        predict = "likely to join"
    case 2:
        predict = "less likely to join"
    case 1:
        predict = "less likely to join"
    case 0:
        predict = "would not join"

print("\nprocess is done")

# print(predict)

sql = "INSERT INTO prediction (emp_id , emp_name , predict_val) VALUES (%s, %s , %s)"
val = (e_id, e_name, predict)

cursor.execute(sql, val)
connection.commit()

print(cursor.rowcount, "record inserted.")
