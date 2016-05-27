a=str("Rise to vote sir")
def new_palindrome(a):
    a=a.lower()
    b = a.replace(" ","")
    pal = ""
    for i in b:
        pal = i+pal
        if pal == b:
            return"is palindrome"
        elif pal != b and len(b) == len(pal):
            return"is not palindrome"
print new_palindrome(a)

