y=[]
z=[]
def word_len(y):
    for i in range(len(y)):
        a=len(y[i])
        z.insert(i,a)
        if len(z)==len(y):
            print z
            break
word_len(y)


      
