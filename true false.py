length = input("enter length of list")
list_a=[]
for i in range(length):
    a = raw_input()
    if(a.isdigit()):
        list_a.insert(i,float(a))
    else:
        list_a.insert(i,a)
n = len(list_a)
x = raw_input("input your value")
if x.isdigit():
    y = int(x)
else:
    y = x
def is_member():
    i = -1
    for index in list_a:
        i += 1
        if y == list_a[i]:
            print"true"
            break
        elif y!= list_a[i]:
            print"false"
            break
is_member()
 
