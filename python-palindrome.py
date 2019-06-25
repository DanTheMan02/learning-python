with open("text.txt", "r") as file: #this opens the text file and reads it, then assigns data as a string containing the contents of the file
    data = file.read()

print("Original Word In File: " + data)

str = ""
for a in data:      #this loop cycles as many times as the length of data which is equal to a, as it cycles, a is reduces by one, so it begins assigning the first letter of str with the
    str = a + str   #last letter of data, and cycles through the length of the word, which leaves str being a reversed data

print("Reversed: " + str)

if str == data:     #if the reverse of data (str) is the same as data, then data must be a palindrome, if not than it isnt a palindrome
    print("The file contains a palindrome!")
else:
    print("The file does not contain a palindrome!")
