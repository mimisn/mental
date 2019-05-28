class ClassTest(object):
    __num = 0

    @classmethod
    def addNum(self):
       ClassTest.__num +=1

    @classmethod
    def getNum(self):
        print(ClassTest.__num)



class Student(ClassTest):
    def __init__(self):
        self.name = ''


ClassTest.getNum()
ClassTest.getNum()
ClassTest.getNum()