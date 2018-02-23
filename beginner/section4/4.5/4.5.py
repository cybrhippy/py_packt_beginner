#!/opt/local/bin/python

# ---------------------------------------------------------
# Write a program that given two numbers a, b print "divisible"
# if one of the two numbers divides the other

# a = input("First number ")
# b = input("Second number ")
a, b = int(input("a = "), int("b = "))
if a % b == 0 or b % A == 0:
    print("divisible")

# ---------------------------------------------------------
# Given input a, b print a/b if b is not equal to zero

a, b = int(input("a = "), int("b = "))
if b != 0: print(a/b)
if b is not 0: print(a/b)
if not (b == 0): print(a/b)


# ---------------------------------------------------------
# Write a program that given three names prints "equal"
# if all three names are equal to each other when lowercase

name1 = input("Name 1: ")
name2 = input("Name 2: ")
name3 = input("Name 3: ")
if name1.lower() == name2.lower() == name3.lower(): print("Equal")
