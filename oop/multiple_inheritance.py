class student:
    def read(self):
        print("read method")

    def write(self):
        print("write method")

class teacher:
    def teach(self):
        print("teach method")

    def homework(self):
        print("hmework method")
    

class person(student,teacher):
    def details(self):
        print("detail method")
        
o1 = person()
o1.read()
o1.write()
o1.homework()
o1.teach()
o1.details()
