#1
frulist1 = ['apple', 'berry', 'cherry', 'papaya']
frulist2 = frulist1 
frulist3 = frulist1[:]
frulist2[0] = 'guava'
frulist3[1] = 'kiwi'

sum = 0 
for ls in (frulist1, frulist2, frulist3):
    if ls[0] == 'guava':
        sum += 1
    if ls[1] == 'kiwi':
        sum += 20
print(sum)


#2
def f(i, values = []):
    values.append(i)
    print (values)
f(1)
f(2)
f(3)  


#3
def func(value, values):
    var = 1
    values[0] = 44
t = 3
v = [1,2,3]
func(t,v)
print(t, v[0])     


#4
dict = {'c': 97, 'a': 96, 'b': 98}
for _ in sorted(dict):
    print(dict[_]) 


#5
fruit = {}
def addone(index):
    if index in fruit:
        fruit[index] += 1
    else: 
        fruit[index] = 1
addone('Apple')
addone('Banana')
addone('apple')
print(len(fruit))


#6 Prod of array except self: 
"""Given an array, return an array where each element is the prod of all the elements in the array except itself."""


#7 Time Conversion - Hackerrank 


#8 Two Sum - LeetCode

def Twosum(num, target):
    for i in range(len(num)):
        for j in range(i+1, len(num)):
            pair_sum = num[i] + num[j]
            if pair_sum == target:
                return [i, j]

num = [2,7,11,15]
target = 9

print(Twosum(num, target))


