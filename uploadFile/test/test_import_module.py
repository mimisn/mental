class ClassA:
  def test(self):
    print('test')
  int_value = 1
# 全局方法，加载时会被调用
print(__file__, 'global function.')
if __name__ == '__main__':
  print(__file__, __name__)