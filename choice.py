
#1
import sys
def addition(num1, num2): #called function
    print("Addition=", num1+num2)
def substraction(num1, num2):#called function
    print("Substraction=", num1 - num2)
def multiplication(num1, num2):#called function
    print("Multiplication=", num1 * num2)
def division():# called function
    pass
while True:
    print("1. Addition")
    print("2. Substraction")
    print("3. Multiplication")
    print("4. division ")
    print("5. Exit")
    choice = int(input("Enter your choice from above options :"))
    if choice == 5:
        sys.exit()
    val1   = int(input("Enter First Value :"))
    val2   = int(input("Enter Second Value :"))
    if choice == 1:
        addition(val1, val2)
    elif choice == 2:
        substraction(val1, val2)
    elif choice == 3:
        multiplication(val1, val2)
    elif choice == 4:
        pass
    else:
        print("You have entered wrong choice :")


#2
Nested function
 def outer_function():
     print("This is the outer function")
     def inner_function():
         print("This is the inner function")
     inner_function()  #Calling the inner function
outer_function()  #Calling the outer function


#3
# input= prashant is good programmer
#WAP to count the word
#output = 4
name ="prashant is good programmer"
count =1
for i in name:#i=0
    if i == " ":
        count += 1
    else:
        continue
print("Total word count =",count)


#4
init_tuple_a = 'a', 'b'
init_tuple_b = ('a', 'b')
print (init_tuple_a == init_tuple_b)


#5
init_tuple_a = '1', '2'
init_tuple_b = ('3', '4')
print (init_tuple_a + init_tuple_b)


#6
l = [1, 2, 3]
init_tuple = ('Python',) * (l.__len__() - l[::-1][0])
print(init_tuple)


#7
init_tuple = ('Python') * 3
print(type(init_tuple))


#8
init_tuple = (1,) * 3
init_tuple[0] = 2
print(init_tuple)


#9
init_tuple = ((1, 2),) * 7
print(len(init_tuple[3:8]))


#10
# Block 1: Empty string replacement
s = ""
s1 = s.replace("difficult", "easy")
print(s1) 
# Output: (An empty string is printed)

# Block 2: All occurrences replacement
s = "abababababab"
s1 = s.replace("a", "b")
print(s1)
# Output: bbbbbbbbbbbb


#11
# Removing spaces from the string:
# 1. rstrip() ===> To remove spaces at right hand side
# 2. lstrip() ===> To remove spaces at left hand side
# 3. strip() ===> To remove spaces both sides

city = input("Enter your city Name:")
scity = city.strip()

if scity == 'Hyderabad':
    print("Hello Hyderbadi..Adab")
elif scity == 'Chennai':
    print("Hello Madrasi...Vanakkam")
elif scity == 'Bangalore':
    print("Hello Kannadiga...Shubhodaya")
else:
    print("your entered city is invalid")


#12 list comprehension 
s = [i for i in range(1, 11)]
print(s)

val = [2**i for i in range(1, 6)] # i = 1, 2, 3, 4, 5
print(val)

#s = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
#val=[2**i for i in range(1,6)]# i= 1,2,3,4,5
#print(val)

val2=[i for i in s if i%2==0]#i=1
print(val2)


#13 Dictionary Comprehension:

squares={x:x*x for x in range(1,6)}#x=6
print(squares)


