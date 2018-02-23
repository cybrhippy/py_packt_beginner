#!/opt/local/bin/python

import sys # sys.exit() quits the program

line = input()
#line = "45 * 2"
split = line.split()

if len(split) != 3:
    print("Wrong format")
    sys.exit(5)
    
left = int(split[0])
op = split[1]
right = int(split[2])

val = 0

if op == '+':
    val = left + right
elif op == '-':
    val = left - right
elif op == '*':
    val = left * right
elif op == '/':
    if right == 0:
        print("Divinsion by zero. Halting.")
        sys.exit(10)
    val = left / right
else:
    print("Unknow operator: {operator}".format(operator=op))
    sys.exit(20)

print("{line_expr} = {value:.2f}".format(line_expr=line, value=val))
