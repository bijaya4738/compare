def generate():
    a = input("input no")
    b = raw_input("input char")
    return ''.join(b for n in range(a))
print generate()
