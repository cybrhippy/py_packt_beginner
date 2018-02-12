#!/opt/local/bin/python

# Use range to generate a list of numbers
a = list(range(0, 10))
print(a)

print(a[0:5])
print(a[2:len(a)])
print(a[:])
print(a[:6:2])
print(a[:6:3])

print(a[-1])
print(a[-2])

print(a[2:-2])
# Reverses the array
print(a[::-1])
print(a[::-2])
