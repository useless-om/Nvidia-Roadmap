# x =3
# try :
#     print(x/0)
# except NameError:
#     print('nameError means theres something undifined')
# except ZeroDivisionError:
#     print('please do notdivide my zero')
# else :
#     print('NO ERROR!')
# finally:
#     print(" i'm going to print regardless of error")






# a =  input("enter a no. : ")
# print(f"the multiplication table of {a} is: ")

# try:
#     for i in range(1,11):
#         print(f"{int(a)} X {i} = {int(a)*i}")
# except Exception as e:
#     print(e)

# print(" some lines of code")
# print(" end of code")





# try:
#     num= int(input("enter a number: "))
#     a = [2,6]
#     print(a[num])
# except ValueError:
#     print("number not integer")
# except IndexError:
#     print(" index error")




# try:
#     with open("practice2.txt","r") as f:
#         data = f.read()
#         print(data)
# except FileNotFoundError:
#     print(" File not found. please check the filename")
# finally:
#     print("closing the file if it was oened")



# a = int(input("enter a number: "))
# b = int(input("enter a number: "))
# try :
#     print(f" a/b = {a/b}")
# except ZeroDivisionError:
#     print(" ur dividing by zero")



# RAISING EXCEPTIONS -> Sometimes you want to trigger an error manually—maybe when a condition isn’t met.
a = int(input(" emter a number between 5 and 10 "))

if(a<5 or  a>10):
    raise ValueError("value should be between 5 and 10")

