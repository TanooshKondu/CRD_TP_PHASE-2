#https://pastebin.com/mXprcNB0

class Box:
    def __init__(self, data):
        self.data = data 
        self.left = None 
        self.right = None 

def levelOrderTraversal(root):
    if root == None:
        return []
    result = []
    Q = [root]
    level = 0
    while len(Q) > 0:
        n = len(Q)
        subResult = []
        for i in range(n):
            # step - 1
            currNode = Q.pop(0)
            # step - 2
            subResult.append(currNode.data)
            # step - 3
            if currNode.left != None:
                Q.append(currNode.left)
            # step - 4
            if currNode.right != None:
                Q.append(currNode.right)
        if level % 2 == 1:
            subResult = subResult[::-1]
        level += 1
        result.append(subResult)
    print(result)

# 20 100 -40 50 90 10 30    
# objects creation is happening here    
obj1 = Box(10)
obj2 = Box(20)
obj3 = Box(30)
obj4 = Box(40)
obj5 = Box(50)
obj6 = Box(60)
obj7 = Box(70)
obj8 = Box(90)
obj9 = Box(100)
obj10 = Box(-40)

# establishing links among those nodes
obj1.left = obj2
obj1.right = obj3 
obj2.right = obj4
obj2.right = obj5 
obj4.right = obj6 
obj6.left = obj7 
obj5.right = obj8 
obj5.left = obj9 
obj9.right = obj10 

#printInOrderTraversal(obj1)
levelOrderTraversal(obj1)
