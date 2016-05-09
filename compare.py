x = input("enter a number x")
y = input ("enter a number y")
def compare(a,b):
    if a > b:
        print "a is greater than b","& a is",a
    elif b >a:
        print "b is greater than a","& b is ",b
    else:
        print "your entry is not valid"
compare(x,y)
