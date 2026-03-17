#1
username = ""
password = ""
while (username !="admin" and password !="hello"):
    username = input("Enter Username: ")
    password = input("Enter Password: ")


#2
name = "Mississippi"
newname = " "
for i in name:
    if i not in newname:
        newname += i
print(name)
print(newname) 

rev = newname[::-1]
print(rev)


#3
mycart = [10, 20, 200, 300, 800, 60, 700]
for i in mycart:
    if i>400:
        print("This is my purchased cart item")
        continue 
    print(i)    


#4
n = int(input("Enter no of rows: "))
for i in range(1,n+1):
    for j in range(1,n+1):
        print(n+1-i, end = " ")
    print()    


#5
str1 = input("Enter first string: ")
str2 = input("Enter second string: ")

if sorted(str1) == sorted(str2):
    print("The strings are anagrams")
else:
    print("The strings are not anagrams")


#6
for i,j in zip(range(1,6), range(5,0,-1)):
    if i==3 and j==3:
        continue
    print(i, " ", j)    