print("you can convert 1. number to charicter 2.caricter to number")

awncer = int(input(" what do you want to do: "))


if awncer == 1:
   number = int(input(" what value do you want to convert: "))
   result = chr(number)
   print("the answer is{0}.".format(result))

elif awncer == 2:
    character = input("What character would you like to convert?")
    result1 = ord(character)
    print("The answer is {0}.".format(result1))
