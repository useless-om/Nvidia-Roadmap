# # create list
# fruits = ["apple","kele","cherry"]

# #acces items
# print(fruits[0])
# print(fruits[-1])

# #change items
# fruits[1]="mango"

# #add items
# fruits.append("orange") #add ay end
# fruits.insert(1,"kiwi") #add at index 1

# #remmpov items
# fruits.remove("apple")
# last = fruits.pop() #remove last and returns it

# #loop through
# for fruit in fruits:
#  print(fruit)

# #lenght
# print(len(fruits))





# #create a tuple
# colors =("red","green","blue")

# #acces
# print(colors[0])

# #loop
# for color in colors:
#  print(color)
 
# # lengeth
# print(len(colors))




# creat a dictionanry  {key:value}
marks = {
    "om":69,
    "zoro":88,
    "sanji":67
}
#acces value
print(marks["om"])
print(marks.get("sanji")) #or

#change value
marks["zoro"]= 99

# add new key values
marks["robin"]=6969

# remove key value
del marks["om"]

# loop
for name, grade in marks.items():
    print(name,grade)
for naav in marks.keys(): #same for value
    print(naav)

# length
print(len(marks))
