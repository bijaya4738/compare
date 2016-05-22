y=[]
def word_len(y):
    z=[]
    for i in range(len(y)):
        a=len(y[i])
        z.insert(i,a)
        if len(z)==len(y):
            return z
            break

