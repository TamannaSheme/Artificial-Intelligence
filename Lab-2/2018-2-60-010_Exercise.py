#####################################################START#####################################


#1. Write a program in Python to find the root of a quadraticeequation.

import cmath

a = 1
b = 5
c = 6

# calculate the discriminant
d = (b**2) - (4*a*c)

# find two solutions
sol1 = (-b-cmath.sqrt(d))/(2*a)
sol2 = (-b+cmath.sqrt(d))/(2*a)

print('The solution are {0} and {1}'.format(sol1,sol2))


#2. Write code to perform grade computation

marks = float(input("Enter your marks in Computer Science: "))

if marks > 90:
    print("Grade: A+")
elif marks >= 80 and marks <= 90:
    print("Grade: A+")
elif marks >= 70 and marks < 80:
    print("Grade: A")
elif marks >= 60 and marks < 70:
    print("Grade: B+")
elif marks >= 50 and marks < 60:
    print("Grade: B")
elif marks >= 40 and marks < 50:
    print("Grade: C")
else:
    print("Grade: F")

"""3. Given two numeric lists or tuples x_vals and y_vals of equal
length, compute their inner product uzing zip(). Additionally count
the number of even number in 0 to 99. Furthermore given pairs =
((4, 5), (6,7), (8,9)) count the number of pairs (x,y) such that a and b
are odd."""


# Part 1
x_vals , y_vals = (1,2,3),(4,5,6)
sum = 0
for x,y in zip(x_vals,y_vals):
      sum = sum + x*y
print("The inner product is:", sum)

# Part 2
print(len([n for n in range(0,99) if n%2==0]))

# Part 3
pairs = ((4,5),(6,7),(8,9))
count = 0
for i in pairs:
      if i[0]%2 == 0 and i[1]%2 == 0:
            count = count + 1
print(count)


#####################################################FINISH####################################
