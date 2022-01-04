import numpy as np

a = 2 ** 52 <= 2**56 //10
print(a)

season = "What is coming"
length = len(season)
print(length)
print(type(length))
last = season[length-3]
print(last)
middle = season[length-8]
print(middle)

for char in season:
    print(char)


ch = 0
while (ch < length):
    print(season[ch])
    ch = ch+1

print(season[6:])
print(season[:4])
#without space
string = "Good Morning. This is 366.";
count = 0;
for i in range(0, len(string)):
    if(string[i]!= ' '):
        count = count + 1;

print("Total number of characters in a string: " + str(count));
#with space
string = "Good Morning. This is 366.";
count = 0;
for i in range(0, len(string)):

        count = count + 1;

print("Total number of characters in a string: " + str(count));

new = season.upper()
print(new)

cricket = "banglasesh lost the game"
print(cricket.strip)

a = [12,10,34,90,30]
print(a)

mixed = ['sakib', 'sheme', 10.79, 20]

a = 33
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")


a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")

loc = "bank"
if loc =="auto shop":
    print("welcome to the auto shop")

elif loc == "bank":
    print("welcome to the bank")
else:
    print("where are u?")
