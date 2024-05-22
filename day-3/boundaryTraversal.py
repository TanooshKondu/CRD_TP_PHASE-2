#Boundary Traversal of Binary Tree
#https://pastebin.com/b3Xw97sX

class Box:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        
def isLeafNode(root):
    if root.left == None and root.right == None:
        return True 
    return False

def collectLeftView(root, result):
    if root == None:
        return 
    while root != None and isLeafNode(root)== False:
        result.append(root.data)
        if root.left != None:
            root = root.left 
        else:
            root = root.right

def collectLeafNodes(root, result):
    if root == None:
        return 
    elif isLeafNode(root):
        result.append(root.data)
        return  
    collectLeafNodes(root.left, result)
    collectLeafNodes(root.right, result)
    
    
def collectRightViewInReverseFashion(root, result):
    if root == None:
        return 
    temp = []
    while root != None and isLeafNode(root)== False:
        temp.append(root.data)
        if root.right != None:
            root = root.right 
        else:
            root = root.left
    temp = temp[::-1]
    for ele in temp:
        result.append(temp)

def findBoundaryTraversal(root):
    if root == None:
        return []
    result = []
    result.append(root.data)

    collectLeftView(root.left, result)
    collectLeafNodes(root, result)
    collectRightViewInReverseFashion(root.right, result)
    return result


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


print(findBoundaryTraversal(obj1))

#output
#[10, 20, 50, 100, -40, 90, 30]