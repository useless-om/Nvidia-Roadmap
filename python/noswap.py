# a = int(input("enter a number : "))
# b = int(input("enter b number : "))

# b = a + b 
# a = b - a 
# b = (b - a)

# print(f" the value of a is {a} and value of b is {b}")

n = input("enter a string:")
l = len(n)
temp = n[0]
n[l-1] = n[0]
n[0] = temp
# c = n.replace(n[-1],a)
print(f"the out put is {n}")  