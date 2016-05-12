a = ["ass",1,"ram",100,"hari"]
x = raw_input("input your value")
if x.isdigit():
        y = int(x)
else:
        y = x
def is_member():
    if y == a[0] or y == a[1] or y == a[2] or y == a[3] or y == a[4]:
        print "true"
    else:
        print "false"
is_member()
