#find Left View
class Box:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        
def findLeftView(root):
    if root == None:
        return []
    result = []
    Q = [root]
    while len(Q) > 0:
        n = len(Q)
        for i in range(n):
            curr = Q.pop(0)
            if i == 0:
                result.append(curr.data)
            if curr.left != None:
                Q.append(curr.left)
            if curr.right != None:
                Q.append(curr.right)
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


findLeftView(obj1)
#output
#[10, 20, 50, 100, -40]

#=== Code Execution Successful ===