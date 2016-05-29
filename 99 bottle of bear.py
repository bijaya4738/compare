import re
a="99 bottles of beer on the wall"
def bottle(a):
    a = re.findall("[-+]?\d+[\.]?\d*",a)
    print a
bottle(a)
