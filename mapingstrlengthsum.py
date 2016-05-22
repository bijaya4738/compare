y=[]
def word_len(y):
    z=[]
    for i in range(len(y)):
        a=int(len(y[i]))
        z.insert(i,a)
        if len(z)==len(y):
            sum =0
            for i in z:
                sum=sum+i
            return sum
            break
