#oscar stanley
#29/09/14
#task
weight = int(input("enter the weight: "))

g100 = weight // 100
remainder = weight % 100

g50 = remainder // 50
remainder = remainder % 50

g10 = remainder // 10
remainder = remainder % 10

g5 = remainder // 5
remainder = remainder % 5

g2 = remainder // 2
remainder = remainder % 2

g1 = remainder 


print ("the amount of 100g you need are {0}".format(g100))
print ("the amount of 50g you need are {0}".format(g50))
print ("the amount of 10g you need are {0}".format(g10))
print ("the amount of 5g you need are {0}".format(g5))
print ("the amount of 2g you need are {0}".format(g2))
print ("the amount of 1g you need are {0}".format(g1))
