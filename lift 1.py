# Oscar Stanley
#15-9-2014
#fridge and lift
print("These are in cm")
fridge_depth = int(input("what is the depth of the fridge?: "))
fridge_width = int(input("What is the width of the fridge?: "))
fridge_height = int(input("What is the hight of the fridge?: "))

lift_depth = int(input("What is the depth of the lift?: "))
lift_width = int(input("What is the width of the lift?: "))
lift_height = int(input("What is the height of the lift?: "))

answer =(lift_depth * lift_width * lift_height) - (fridge_depth * fridge_width * fridge_height)
print("your awswer is {0} cm³".format(answer))
