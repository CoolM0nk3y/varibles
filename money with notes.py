#oscar stanley
#01/10/14
#Revision Exercises
money = int(input("enter the amout of money you have:£ "))

m50 = money // 50
remainder = money % 100

m20 = remainder // 20
remainder = remainder % 50

m10 = remainder // 10
remainder = remainder % 10

m5 = remainder // 5
remainder = remainder % 5

m2 = remainder // 2
remainder = remainder % 2

m1 = remainder 


print ("the amount of £50 notes you need are {0}".format(m50))
print ("the amount of £20 notes you need are {0}".format(m20))
print ("the amount of £10 notes  you need are {0}".format(m10))
print ("the amount of £5 notes you need are {0}".format(m5))
print ("the amount of £2 coins you need are {0}".format(m2))
print ("the amount of £1 coins you need are {0}".format(m1))
