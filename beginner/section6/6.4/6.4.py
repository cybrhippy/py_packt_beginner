#!/opt/local/bin/python

def reverse(s):
    new_str = ""
    for i in range(len(s)):
        new_str += s[len(s)- i - 1]
    return new_str

def is_palindrome(p):
    pass


print(reverse("123"))
