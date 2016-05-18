def max_in():
    y=[]
    a = input("enter range")
    for i in range(a):
        b = input("enter number")
        y.insert(i,b)
    maxno = y[0]
    for num in y:
        if maxno < num:
            maxno = num
    return maxno
print max_in()

    
    
    
    
