class Node:
    def __init__(self,data):
        self.val=data
        self.next=None
def createLinkedList(arr): # 1 2 3 4
    head=None
    for data in arr:
        if(head==None):
            head=Node(data)
            temp=head
        else:
            temp.next=Node(data)
            temp=temp.next 
    printLinkedList(head) #creating linkdlist
def printLinkedList(head):
    temp=head
    while(temp):
        print(temp.val,end=" ")
        temp=temp.next  

arr=list(map(int,input().split()))
createLinkedList(arr)             
          
