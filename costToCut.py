#https://leetcode.com/problems/minimum-cost-to-cut-a-stick/ 
# Given a wooden stick of length n units. The stick is labelled from 0 to n. For example, a stick of length 6 is labelled as follows:
# Given an integer array cuts where cuts[i] denotes a position you should perform a cut at.
# You should perform the cuts in order, you can change the order of the cuts as you wish.
# The cost of one cut is the length of the stick to be cut, the total cost is the sum of costs of all cuts. When you cut a stick, it will be split into two smaller sticks (i.e. the sum of their lengths is the length of the stick before the cut). Please refer to the first example for a better explanation.

# Return the minimum total cost of the cuts.

 
x =9
y = [5,6,1,4,2]

def minCost(lengthToCut, cutList):
    cutList.sort()
    copyCut = list(cutList)
    copyCut.reverse()
    fakeList = [i for i in range(lengthToCut + 1)]
    cutsMade=[]
    toDo = []
    toDo.append(0)
    cost = 0
    initial = lengthToCut
    while len(copyCut) > 0:
        last = toDo.pop()
        cut = copyCut.pop()
        cutsMade.append(fakeList[last:cut+1])
        value = len(fakeList[last:cut])
        initial -= value
        cost += initial
        if len(copyCut) == 0:
            cutsMade.append(fakeList[cut:])
            enVal = len(cutsMade[-1])  
            
            print(f'this is the end val {enVal}\nthis is the init{initial}')
        
        toDo.append(cut)
    print(cutsMade)
    print(cost)
minCost(x,y)
