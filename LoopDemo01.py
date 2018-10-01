#remember to remove hashes in front of certain lines to run program

print("********BASICS********")


for i in range (4,11,2):
	print(i)

print("*********DONE*********")

#count check change
print(" ")
print(" ")

print("***************BACKWARDS***************")

for i in range(10, -1, -1):
	print (i)
print("******************DONE******************")

print(" ")
print(" ")

print("******Printing String Characters******")
str = "Monkey"

#python automatically recognized each letter as a number in order, and will print it
#ALWAYS InDICATE THE LENGTH OF A WORD USING THE FUNCTION LEN

for i in range(0,len(str),1):
	print (str[i])

print ("******PRINT STRING IN REVERSE******")

str = "Monkey, yeknoM"
for i in range(len(str)-1,-1,-1):
	print (str[i])

print("******PRINT EVERY SECOND LETTER STR STARTING AT INDEX 0******")

str = "Monkey!!!!!"
for i in range(0, len(str),1):
	print (str[i])