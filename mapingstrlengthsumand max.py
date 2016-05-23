y=["bijay","asdfasdf","ram"]
def word_len(y):
    z=[]
    for i in range(len(y)):
        a=int(len(y[i]))
        z.insert(i,a)
        if len(z)==len(y):
            return z
su=0
for x in word_len(y):
    su=su+x
su
maxno=0
for num in word_len(y):
    if maxno<num:
        maxno=num
maxno
