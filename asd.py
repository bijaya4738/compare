def max_in(howmany,element):
    y=[]
    a=howmany
    for i in range(a):
        b=element
        y.insert(i,b)
    maxno = y[0]
    for num in y:
        if maxno < num:
            maxno = num
    return maxno

    
