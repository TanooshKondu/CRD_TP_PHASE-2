#<!---Sir's code--!>
#deletion of linked lists

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
#deletion code
def deleteTailNode(head):
    curr = head
    if curr == None or curr.next == None:
        return None
    while curr.next.next != None:
        curr = curr.next
        
    curr.next = None
    return head

###

#delete head node
def deleteHeadNodeInLinkedList(head):
    if head == None:
        return None
    secondNode = head.next
    head.next = None
    return secondNode
###
head = None
nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
for ele in nums:
    head = insertAtBeginning(head, ele)

printLinkedList(head)
head = insertAtSpecificPosition(head, 5, 1899)
printLinkedList(head)
head = deleteTailNode(head)
printLinkedList(head)
head = deleteHeadNodeInLinkedList(head)
printLinkedList(head)
# n = int(input())
# for i in range(n):
#     ele = int(input())
#     head = insertAtTailNode(head, ele)