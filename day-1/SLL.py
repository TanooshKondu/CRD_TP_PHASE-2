# #10, 15, 20, 5, 18
# https://pastebin.com/S1DqVuSn

# class Box:
#     def __init__(self, data):
#         self.data = data
#         self.next = None
# obj1 = Box(10)
# obj2 = Box(20)
# obj3 = Box(30)
# obj4 = Box(40)

# # print(obj1.data)
# # print(obj2.data)
# # print(obj3.data)
# # print(obj4.data)

# # print(obj1.next)
# # print(obj2.next)
# # print(obj3.next)
# # print(obj4.next)

# obj1.next = obj2
# obj2.next = obj3
# obj3.next = obj4
# obj4.next = None


class Box:
    def __init__(self, data):
        #print("printing address from constructor",obj1)
        self.data = data
        self.next = None
        
def printLinkedList(curr):
    while curr != None:
        print(curr.data)
        curr = curr.next
        
def insertAtTailNode(head, ele):
    temp = Box(ele)
    if head == None:
        return temp
    tail = head
    while tail.next != None:
        tail = tail.next
    tail.next = temp
    return head
head = None
nums = [40, 50, 60, 30, 20, 10, 70, 80, 90, 100]
for ele in nums:
    head = insertAtTailNode(head, ele)
#n = int(input())
#for i in range(n):
#   if ele in n:
#       head = insertAtTailNode(head, ele)
        
        
# #block creation is happening in below 4 lines
# obj1 = Box(10)
# #print("printing address from main function", obj1)
# obj2 = Box(20)
# obj3 = Box(30)
# obj4 = Box(40)

# #establishing links in below 4 lines
# obj1.next = obj2
# obj2.next = obj3
# obj3.next = obj4
# obj4.next = None
printLinkedList(head)




###<!-------Sir Code--------!>

class Box:
    def __init__(self, data):
        self.data = data 
        self.next = None
        
def printLinkedList(curr):
    while curr != None:
        print(curr.data, end = " --> ")
        curr = curr.next 
    print()
    
def insertAtTailNode(head, ele):
    temp = Box(ele) 
    if head == None:
        return temp
    tail = head 

    while tail.next != None:
        tail = tail.next 
    tail.next = temp
    return head 

def insertAtBeginning(head, ele):
    temp = Box(ele)
    if head == None:
        return temp 
    temp.next = head 
    return temp

def insertAtSpecificPosition(head, position, ele):
    if position == 0:
        return insertAtBeginning(head, ele)

    temp = Box(ele)
    currentIndex = 0 
    currentNode = head 
    while currentIndex != position - 1:
        currentIndex += 1 
        currentNode = currentNode.next 

    temp.next = currentNode.next 
    currentNode.next = temp 
    return head

head = None
nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
for ele in nums:
    head = insertAtBeginning(head, ele)

printLinkedList(head)
head = insertAtSpecificPosition(head, 5, 1899)
printLinkedList(head)

# n = int(input())
# for i in range(n):
#     ele = int(input())
#     head = insertAtTailNode(head, ele)