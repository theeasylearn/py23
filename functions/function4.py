# return multile value as tuple
def getoperation(text):
    u = text.upper()
    l = text.lower()
    rev = text[::-1]
    
    return u,l,rev

print(getoperation("hello"))
