y=["bijay","wrufesh"]
def word_len(y):
    z=[]
    for i in range(len(y)):
        a=int(len(y[i]))
        z.insert(i,a)
        if len(z)==len(y):
            return z
sum=0
for x in word_len(y):
    sum=sum+x
print sum
