class Box:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
        
def printInOrderTraversal(root):
    if root == None:
        return
    printInOrderTraversal(root.left)
    print(root.data, end=" ")
    printInOrderTraversal(root.right)
        
def printPreOrderTraversal(root):
    if root == None:
        return
    print(root.data)
    printPreOrderTraversal(root.left)
    printPreOrderTraversal(root.right)
    
########
obj1 = Box(10)
obj2 = Box(20)
obj3 = Box(30)
obj4 = Box(40)
obj5 = Box(50)
obj6 = Box(60)
obj7 = Box(70)
obj8 = Box(80)
obj9 = Box(90)
obj10 = Box(100)
###
obj1.left = obj2
obj1.right = obj3
obj3.right = obj4
obj4.right = obj5
obj5.right = obj6
obj6.right = obj7
obj7.right = obj8
obj8.right = obj9
obj9.right = obj10
print(printPreOrderTraversal(obj6))
print(printInOrderTraversal(obj3))