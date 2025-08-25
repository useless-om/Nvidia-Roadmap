import pandas as pd


numbers = [10, 20, 30, 40]
s = pd.Series(numbers)
print(s)

s = pd.Series([10,23,45], index=["a","b","c"])
print(s)


# FROM DICTINARY

marks = {"math": 90, "science": 85, "english": 92}
s = pd.Series(marks)
print(s)

# accescing data 

print(s["math"])
print(s.iloc[0])

# basic operations 

s = pd.Series([1, 2, 3, 4])

print(s.max())      # 4
print(s.min())      # 1
print(s.sum())      # 10
print(s.mean())     # 2.5
print(s.describe()) # summary
print()
print()


# DAY 4

data = {
    "Name": ["Aman", "Riya", "Karan", "Aman", "Riya"],
    "Subject": ["Math", "Math", "Math", "Physics", "Physics"],
    "Marks": [88, 92, 79, 85, 95]
} # creating dataframe
df = pd.DataFrame(data)
print(df)

#filtering single coloum
print(df["Marks"])
print(df[["Name","Marks"]]) # Multiple columns

# Filtering Rows

print(df[df["Marks"]>90]) # Students who scored > 90

# Students who studied "Math"
print(df[df["Subject"] == "Math"])



# Simple Stats
print(df["Marks"].mean())   # Average of all marks
print(df["Marks"].sum())    # Total marks
print(df["Marks"].count())  # No. of entries
print(df["Marks"].max())    # Highest mark
print(df["Marks"].min())    # Lowest mark
