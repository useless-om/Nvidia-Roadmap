# print("enter the number of divisibility you want to check")

# print("----------------------------------")

# a = int(input("enter the numbert :"))

# if a % 5 == 0 and a % 11 == 0 :
#     print(f"yes the number {a} is divisible either by 5 or  11")

# else :
#      print(f"no the number {a} is not divisible either by 5 or  11")






# ch = input("enter the key :")

# if ch.isdigit() :
#     print("you entered a number")

# elif ch.isalpha() :
#     print("you enter a alphabet")

# else :
#     print("you entered other key")





# import math

# print(" a is coeff of x^2 b is coeff of x and c is constant")

# a = int(input("enter a :"))
# b = int(input("enter b :"))
# c = int(input("enter c :"))

# d = math.sqrt(b*b - 4*a*c)

# x1 = (-b + d)/2
# x2 = (-b - d)/2

# print(f"the roots are {x1} , {x2}")





# str = input("enter a sentence:")

# print(str)

# str = str.replace("o","l")
# print(str)






# print("so lets start the game")

# print("--------------------------------------------------------")

# name = input(" enter the name of charactor :")
# age = input("enter the age:")
# verb = input("input the verb:")

# print(f"there was a chodarmad boy named {name}.who used to {verb} 💦 at the age of {age}")




# n = int(input("Enter the number of rows :"))

# for i in range(1,n+1):
  
#     for j in range(i,n):
#       print(" ",end="")

#     for j in range(1,2*i):
#        print("*",end="")
#     print()




# n = int(input(" enter the number of row:"))

# for i in range(0,n):
#   for j in range(0,i):
#     print("",end="")
#   for j in range(0,2*n-(2*i-1)):
#     print("*",end="")
#   print()

# 

# str = []
# for i in range(5):
#   a = input("enter a charactor name:")
#   str.append(a)

# for i in range(5):
#   print(str[i])

# print(str[1:4])





# a = input("input a string:")
# b = a[::-1]
# if a == b:
#     print("yes palindrode")

# else :
#     print("not palindeome")




# a = input("enter a string:")
# print(a[-1])
# temp = a[0]
# a = a.replace(a[0],a[-1])
# a = a.replace(a[-1],temp)
# print(f" the new string is {a}")




# num = [1,2,6,9,43,3,69,21,33]

# print(max(num))
# print(min(num))
# print(help(num))



# try :
#     result = 10 / 0
# except ZeroDivisionError:
#     print("u cant divide")

# try :
#     num = int(input("enter a number :"))
#     result = 10 / num
# except (ValueError , ZeroDivisionError) as e:
#     print(f"error occured :{e}")
# else:
#     print(f"the result is {result}")
# finally :
#     print("this wil always be exceted")




# def copyfile(source , destination):
#     try:
#         with open(source,'r') as f:
#             copy = f.read()
#         with open(destination,'w') as f1:
#             f1.write(copy)
#         print("copy succesful")
#     except FileNotFoundError:
#         print("no file exist to copy")
#     except Exception as e:
#         print(f"error occured")
    

# copyfile('practice2.txt','practice.txt')



def count_word(infile,outfile):
    try :
        with open(infile,'r') as f1:
            word = f1.read()
            count = len(word.split())
        with open(outfile,'w') as f2:
            f2.write(f"number of words from file 1 are {count}")
            print("print succece")
    except FileNotFoundError:
        print("the input file does not exist")
    except Exception as e:
        print(f" an error occured {e}")

count_word('practice2.txt','practice.txt')