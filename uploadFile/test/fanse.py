from operator import methodcaller


def test(arg):
    a = 1
    b = 2
    data_dict = {}
    print(locals())
    print(globals())
b = 1
def test2():
    a = 1
    locals()["a"] = 2  # 修改局部变量
    print("a=", a)
    globals()["b"] = 6 # 修改全局变量
    print("b=", b)

#2
class Student(object):
    def __init__(self, name):
        self.name = name
    def getName(self):
        return self.name

class Student2(object):
    def __init__(self, name,x):
        self.name = name
        self.x = x
    def getName(self):
        return self.name,self.x

#3
def createInstance(module_name, class_name, *args, **kwargs):
  module_meta = __import__(module_name, globals(), locals(), [class_name])
  class_meta = getattr(module_meta, class_name)
  obj = class_meta(*args, **kwargs)
  return obj



if __name__ == '__main__':
    test(3)
    test2()
    #2
    stu = Student("Jim")
    func = methodcaller('getName')
    print( func(stu))
    #3
    obj = createInstance("my_module","MyObject")
    obj.test()

    obj1=createInstance("fanse","Student2","chenn","yishu")
    print(obj1.getName())
