class student:
    __name = None
    __rollnumber = None

    def setname(self, name):
        self.__name = name

    def getname(self):
        return self.__name
    def setrollnumber(self, rollnumber):
        self.__rollnumber = rollnumber

    def getrollnumber(self):
        return self.__rollnumber

read1 = student()
read1.setname("shreeram")
print("name:",read1.getname())
read1.setrollnumber(5421)
print("Roll Number:", read1.getrollnumber())

            


 