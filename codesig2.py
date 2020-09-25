class Tree(object):
  def __init__(self, x):
    self.value = x
    self.left = None
    self.right = None

x = Tree(22)
x.left= Tree(1)

stack = []
stack.append(x)
val =0
while len(stack) > 0:
    popped = stack.pop(0)
    val += popped.value
    print('i did the first')
    lft = popped.left
    rgt = popped.right
    print(rgt)
    if lft is not None:
        stack.append(lft)
    elif rgt is not None:
        stack.append(rgt)
print(val)
    