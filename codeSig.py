class ListNode(object):
  def __init__(self, x):
    self.value = x
    self.next = None
x = ListNode(1)
x.next = ListNode(2)
x.next.next =ListNode(3)
x.next.next.next = ListNode(4)
x.next.next.next.next =ListNode(5)


# while curr is not None:
#     print(curr.value)
#     curr = curr.next

curr = x
bumper = curr
count = 0    
while curr is  not None:
    for i in range(5):
        try:
            bumper = bumper.next
        except AttributeError:
            
            bumper = None
    if bumper is None:
        print(f'on to something')
        if curr.value == x.value:
            print(' but item is to long its to wideee')
            break
        else:
            print(f' a haa this may be what you want {curr.value}')
            break
    count += 1 
    curr = curr.next