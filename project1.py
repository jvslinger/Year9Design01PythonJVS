f=open("project1.txt","w+")

inp=input("Write now:   ")

for i in range(1):
	f.write(inp)

f.close()

fh = open ("project1.txt","r")
print(fh.read())