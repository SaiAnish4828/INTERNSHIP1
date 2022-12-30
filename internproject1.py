import time  
import threading

# providing the months
print("===SURVEY IN THE WAIT PERIOD===")
print("\n")

AppliData = ["sai" , 20 , "pluginlive" , "3 months"]
name , age , company , waitperiod= AppliData
print("name = ",name ,"\nage = " , age , "\ncompany = ", company , "\nwait period = " , waitperiod )
print("\t")

join1 = 0
join2 = 0

print("Q1 WAS THE INTERVIEW PROCESS TOO LONG\t")
print("OPTIONS\t")
print("1> YES \n2=> NO")
x = int(input("Choice = "))
if x == 1:
    join1 += 0
else:
    join1 += 1

print("Q2 ARE YOU SATISFIED WITH THE PACKAGE")
print("OPTIONS\t")
print("1> YES \n2=> NO")
y = int(input("Choice = "))
if y == 1:
    join1+=1
else:
    join1+=0

print("Q3 IS THE COMPANY'S LOCATION SUITABLE FOR YOU")
print("OPTIONS\t")
print("1> YES \n2=> NO")
z = int(input("Choice = "))
if z == 1:
    join1+=1
else:
    join1+=0
print("done")


time.sleep(10)
current_time = time.time()
print(current_time)




print("Q1 WOULD YOU RECOMMEND THIS COMPANY TO OTHERS\t")
print("OPTIONS\t")
print("1> YES \n2=> NO")
a = int(input("Choice = "))
if a == 1:
    join2+=1
else:
    join2+=0
    
print("Q2 IF A COMPANY WITH BETTER PACKAGES APPROACH YOU , WOULD YOU ACCEPT")
print("OPTIONS\t")
print("1> YES \n2=> NO")
b = int(input("Choice = "))
if b == 1:
    join2+=1
else:
    join2+=0

print("Q3 ARE YOU SATISFIED WITH THE ROLE GIVEN TO YOU IN THE COMPANY")
print("OPTIONS\t")
print("1> YES \n2=> NO")
c = int(input("Choice = "))
if c == 1:
    join2+=1
else:
    join2+=0
print("done")





join = join1 + join2       

match join:
  case 6:
    print("more likely to join")
  case 5:
    print("more lkely to join")
  case 4:
    print("likely to join")
  case 3:
    print("likely to join")
  case 2:
    print("less likely to join")
  case 1:
    print("less likely to join")
  case 0 :
    print("would not join")
    
print("process is done")
