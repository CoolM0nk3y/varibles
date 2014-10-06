# program to print the list of characters and their ASCII values
for value in range(0, 255):
   print "ASCII Value:", value, "\t", "Character:", chr(value), "\n"

# Convertion from text to ASCII codes

message = raw_input("Enter message to encode: ")

print "Decoded string (in ASCII):"
for ch in message:
   print ord(ch),
print "\n\n"

# Convertion from ASCII codes to text

message = raw_input("Enter ASCII codes: ")

decodedMessage = ""

for item in message.split():
   decodedMessage += chr(int(item))   

print "Decoded message:", decodedMessage
