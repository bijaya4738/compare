a = input("input no")
b = raw_input("input char")
def generate(x,y):
    return ''.join(y for n in range(x))
print generate(a,b)
