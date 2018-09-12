f = open("helloworld.txt","r")

content = f.read()
print(content)

list = content.split("\n")
print(list)