#!/opt/local/bin/python

my_list     = [1,2,3,4,5]
my_tuple    = (2,7,8,9,10)
my_string   = "Hello World!"

print('__iter__' in dir(my_list))
print('__iter__' in dir(my_tuple))
print('__iter__' in dir(my_string))

# for elem in my_list:
#   print(elem)

list_iterator = iter(my_list)

while True:
    try:
        next_elem = next(list_iterator)
        print(next_elem)
    except StopIteration:
        break
