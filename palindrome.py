a = raw_input("enter your string")
def is_palindrome(a):
   pal = ""
   for i in a:
       pal = i+pal
       if pal == a:
           print"is palindrome"
       else:
           print"is not palindrome"
is_palindrome(a)
