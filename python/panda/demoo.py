import pandas as pd

df = pd.read_csv(r"C:\Users\OM\Desktop\nvidia-roadmap\python\panda\marks.csv")
df.columns = df.columns.str.strip() # removes leading/trailing spaces from column names to avoid KeyError

print(df)

print(df.head()) # see first 5 rows

print(df.tail()) # see last 5 rows

print(df.info()) #get basic info about data

print(df.describe()) # get summary (mean,min,max,etc for numbers)

print(df["Math"])   # prints all values in Maths column

print(df[["Name", "Science"]])

# iloc ->  INTEGER LOCATION (ROW NUMBER)

print(df.iloc[0])    # prints first row (row index 0)
print(df.iloc[2])    # prints third row





print(df["Math"].mean())     # average of Maths column
print(df["Science"].max())    # highest Science mark
print(df["English"].min())    # lowest English mark

# ADDING NEW COLUMN
df["total"] = df["Math"] + df["Science"] + df["English"]
print(df)


df.to_csv("marks_updated.csv", index=False) #index=False means don’t save the row numbers (extra column).