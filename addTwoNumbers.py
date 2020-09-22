# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
            
pList1 = ListNode(3,ListNode(1,ListNode(2)))
pList2 = ListNode(6,ListNode(3,ListNode(4)))
class Solution:
    def getValues(self,nlist):
        current = nlist
        val = ''
        while current is not None:
            val = str(current.val) + val
            current = current.next
        return int(val)
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        num1 = self.getValues(l1)
        num2 = self.getValues(l2)
        theSum = [i for i in str(num1 + num2)]
        rev= []
        while len(theSum) >0:
            rev.append(theSum.pop())
        mem = []
        count = 0 
        nList = '' 
        while count < len(rev):
            if count is 0:
                nList = ListNode(int(rev[count]))
                mem.append(nList)
            elif count > 0:
                newNode = ListNode(int(rev[count]))
                y = mem.pop()
                y.next = newNode
                mem.append(newNode)
            count +=1
        return self.getValues(nList)
            

th = Solution()

print(th.addTwoNumbers(pList1,pList2))