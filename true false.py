length = input("enter length of list")
list_a=[]
for i in range(length):
    a = raw_input()
    if(a.isdigit()):
        list_a.insert(i,float(a))
    else:
        list_a.insert(i,a)
x = raw_input("input your value")
if x.isdigit():
    y = int(x)
else:
    y = x
def is_member(value,c_list):
        for item in c_list:
           if type(value) == type(item):
                if value == item:
                    return True
                
        return False
print is_member(y,list_a)
 
