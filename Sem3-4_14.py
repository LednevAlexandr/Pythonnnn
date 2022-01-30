a = 2.88

def fog(a):
    result=0
    for i in str(a):
        if i != '.': 
            result = result + int(i)
    return result

print(fog(a))