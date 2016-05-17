length = input("enter length of list")
list_a=[]
list_b=[]
for i in range(length):
    a = raw_input("l1")
    if(a.isdigit()):
        list_a.insert(i,float(a))
    else:
        list_a.insert(i,a)
for i in range(length):
    b = raw_input("l2")
    if(b.isdigit()):
        list_b.insert(i,float(b))
    else:
        list_b.insert(i,b)

print list_a
print list_b
def is_member(x,y):
    for i in x:
       for j in y:
           if type(i)==type(j):
               if i==j:
                   return True
    return False
        
print is_member(list_a,list_b)
    

            
