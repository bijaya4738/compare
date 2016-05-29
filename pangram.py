import string
a=str(" the quick brown fox jumps over lazy dog")
def check_panagram(a):
    b=a.upper()
    b=b.replace(" ","")
    c=set(b)
    print c
    d=string.uppercase[:26]
    e=set(d)
    for element in c:
        for element in e:
            if c == e:
               return True
            else:
                return False        
print check_panagram(a)
