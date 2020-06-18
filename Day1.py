'#hello world'
print('Hello World!')

input('Please enter your name: ')


#example functions
def userName():
    name = input("Please input your name: ")
    return name

print(userName())


#while loop
i = 0
while i <= 10:    #don't forget the :
    print(i)
    i += 1


#for loop
print("For Loops")
print('\n')
admins = ["Rab", "Bobby", "Pinky"]
for i in admins:
    print (i)
#this should create an dictionary of data in Admins and then print each one.
print('\n')
for i in range (0,10):
    print(i)
#a simpliler way of doing the while loop but this doesn't include the number 10

print ('\n')
#you can also add a increment to see how much it should go up by
for i in range (0,10, 8): #this should incremement by 8 everyime up to the number 10
    print(i)

print ('\n')
#same as before but it shows a bigger subset
for i in range (0,100,8):
    print(i)



print('\n')
file = open("README.md", "r")
print(file.read())
#this opens the README.md file on the Repo in the termial and displays all the text.


print('\n')
file = open("README.md", "r")
print(file.readline())
print(file.readline())
print(file.readline())
print(file.readline())
print(file.readline())
print(file.readline())
print(file.readline())
#this code exectues each line, line by line to the terminal - this is different to the above that displays it all

#using a loop with readline - makes it more efficient to code
print('\n')
file = open("README.md", "r")
for line in file:
    print(line, end='')
#This will be called line each time it prints line and will end with ''

#writing to a file - using the open (..,"w") command
# print('\n')
# file = open("test.txt", "w")
# file.write("This is how we write to files!")

#putting this as comments so it doesn't write over the text.text
