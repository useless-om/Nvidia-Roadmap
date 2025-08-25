# i= 0
# while(i<=10):
#     print(i*'*')
#     i = i+1

# n = [1,3,5,23,63]
# for no in n:
#     print(no)

# i =0
# while(i<len(n)):
#     print(n[i])
#     i = i+1
# number  = range(3,14,2)
# for num in number:
#     print(num)




# functions
# def greet(a,b):
#     print(f" hi {a} {b}")
#     print("nice to meet yoo")


# greet("om","pawar")

# def greet(name):
#     return (f"hi {name}")

# message = greet("Zoro")
# print(message)



#types of fun
def add(a,b=2):
    return a+b
print(add(6))

def mul(*n):  # stores like [1,23,4] for mul(1,23,4)
    total = 1
    for num in n:
        total = total*num
    return total
print(mul(1,2,3,4))



def save_user(**user): # saves as dictionary
    print(user)
save_user(roll = 1, name="om",age= 19)




# fuction to check prime no.
def is_prime(n):
    if(n<=1):
        return " not prime"
    for i in range (2,int(n/2)):
        if n%i==0 :
            return " not prime"
    else :
        return "yes prime"
    
print(is_prime(13))
