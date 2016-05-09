x = input("enter a number x")
y = input("enter a number y")
z = input("enter a number z")
def compare(a,b,c):
    if (a > b and a > c):
        print "x is the max no","and max is:",a
    elif (b > c and b > a):
        print "y is the max","and max is:",b
    elif (c > a and c > b):
        print "z is the max","and max is:",c
    else:
        print "your entry is invalid"
compare (x,y,z)
