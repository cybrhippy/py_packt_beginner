#!/opt/local/bin/python

n = 11
f = 1.2345678
s = "computer"

print("my number is {:d}".format(n)) # Decimal
print("my number is {:b}".format(n)) # Binary

print("{:f}".format(f))

print("{:.3f}".format(f))

print("{:11.3f}".format(f))

print("{:011.3f}".format(f))


print("{0} {1} {2}".format(n,f,s))


print("{name} own(s) {amount} of {object}".format(
    name = "William",
    amount = 5,
    object = "mangos"
))
