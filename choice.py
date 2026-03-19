
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


