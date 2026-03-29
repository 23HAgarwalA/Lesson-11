even = 0
odd = 0
num = int(input("Please enter a number"))
temp = num
while temp>0:
    digit = temp%10
    if digit % 2 == 0:
        even = even+1
    else:
        odd = odd+1
    temp//= 10
print ("There are ", even, "even numbers in the number given")
print ("There are ", odd, "odd numbers in the number given")