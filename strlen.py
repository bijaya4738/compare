s = raw_input("enter string")
def strlen(a):
    length = 0
    for i in a:
        if i == "":
            break
        else:
            length+=1
    print length
    
strlen(s) 
