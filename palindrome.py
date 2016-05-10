a = raw_input("enter your string")
def is_palindrome(a):
    if a == a[::-1]:
        print a ,"is palindrome"
    else:
        print a , "is not palindrome"
is_palindrome(a)
