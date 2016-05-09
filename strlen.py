s = raw_input("enter string")
def stringlen(a):
    length = 0
    for i in a:
        if i == "":
            break
        else:
            length+=1
    print length
    
stringlen(s) 
