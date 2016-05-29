import string
a=str()
def check_panagram(a):
    b=a.upper()
    b=b.replace(" ","")
    c=set(b)
    d=string.uppercase[:26]
    e=set(d)
    for element in c:
        for element in e:
            if c == e:
               return True
            else:
                return False        
print check_panagram(a)
