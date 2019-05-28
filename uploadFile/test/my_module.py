class MyObject(object):
  def test(self):
    print('MyObject.test')
    MyObject1().test()
    MyObject2().test()
class MyObject1(object):
  def test(self):
    print('MyObject1.test')
class MyObject2(object):
  def test(self):
    print('MyObject2.test')