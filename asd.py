y=[]
def max_in(y):
    maxno = y[0]
    for num in y:
        if maxno < num:
            maxno = num
    return maxno

    
