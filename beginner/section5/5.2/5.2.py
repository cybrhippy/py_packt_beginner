#!/opt/local/bin/python

index = 0
names = ["Josh", "Harry", "Leah", "Mich"]

while index < len(names):
    name = names[index]
    print(name)
    index = index + 1

total = 0
v = 1
while v <= 10:
    total = total + v
    v = v + 1
print(total)

print("Please make sure a + b = 20")
while True:

    a, b = int(input("a: ")), int(input("b: "))
    if a + b ==20:
        print("Stopping loop")
        break
    else:
        print("Please make sure a + b = 20")
