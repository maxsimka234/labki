import math
import random

#1
print("task one \n")
print("input a :")
a = int(input())
print(math.cos(a)+math.sin(a)+math.cos(3*a)+math.sin(3*a))
print("\n\n")

#2
print("task two \n")
fib1 = 1
fib2 = 1

n = input("input fibonacci number: ")
n = int(n)

i = 0
while i < n - 2:
    fib_sum = fib1 + fib2
    fib1 = fib2
    fib2 = fib_sum
    i = i + 1

print(fib2)
print("\n\n")

#3
print("task three \n")
matrix=[[0 for i in range (4)] for i in range (5)]
for i in range(5):
    for j in range(4):
        matrix[i][j]=random.randint(1,10)

for i in matrix:
        print(str(i)+" ")
        
tmp=matrix[2][:]
matrix[2][:]=matrix[0][:]
matrix[0][:]=tmp

print("\n")
for i in matrix:
        print(str(i)+" ")
