f = open("practice.txt","a+")
f.write("asghn")

f.close()

f = open("practice.txt","r")
data = f.read()
print(data)