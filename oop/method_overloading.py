class calc:
    def __init__(self,n):
        self.__n = n
        
    def add(self,a,b):
        print(a+b)
        
    def add(self,a,b,c):
        print(a+b+c)
        print(self.__n)
        
c1 = calc(2)
c1.add(1,2,3)

print(c1._calc__n)