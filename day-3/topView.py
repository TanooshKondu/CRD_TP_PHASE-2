#https://pastebin.com/uyLBEuvU
class Box:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def topViewHelper(root, store, hd, level):
    if root == None:
        return []
    if hd not in store or store[hd][0] > level:
        store[hd] = [level, root.data]
    topViewHelper(root.left, store, hd - 1, level + 1)
    topViewHelper(root.right, store, hd + 1, level + 1)

def findTopView(root):
    result = []
    if root == None:
        return result
    store = {}
    topViewHelper(root, store, 0, 0)
    sortedKeys = sorted(store.keys())
    for key in sortedKeys:
        result.append(store[key][1])
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


print(findTopView(obj1))
#output
#[20, 10, 30]
#
#=== Code Execution Successful ===