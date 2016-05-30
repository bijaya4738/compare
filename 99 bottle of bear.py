import string
import re
a=str("99 bottles of beer on the wall Take one down pass it around ")
def bottle(a):
    d = re.findall(r'\w+',a)
    f = int(d[0])
    g = (d[1:7])
    g = string.join(g,' ')
    i = (d[1:5])
    i = string.join(i,' ')
    j = (d[6:13])
    j = string.join(j,' ')
    for counter in range(f,0,-1):
        print counter,g
        print counter,i,j
bottle(a)
  
