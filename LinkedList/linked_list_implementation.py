class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class linked_list:
    def __int__(self):
        self.head = None

    def insertAtBegining(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def insertAtPostion(self,data,index):
        new_node = Node(data)
        curr_node = self.head
        pos =0

        if pos == index:
            insertAtBegining(new_node)
        else:
            while (curr_node is not None and pos+1 != index):
                pos =pos+1
                curr_node = curr_node.next
            #After loop ends
            if curr_node is not None:
                new_node.next = curr_node.next
                curr_node.next = new_node
            else:
                print('index error')

    def insertAtEnd(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head =  new_node
        curr_node = self.head
        while(curr_node.next):
            curr_node = curr_node.next

        if curr_node is not None:
            curr_node.next = new_node


    def updateNode(self,val,index):
        pos = 0
        curr_node = self.head
        if pos == index :
            self.head.data = val
        else:
            while(curr_node is not None and pos != index):
                pos =pos+1
                curr_node = curr_node.next

            if curr_node is not None:
                curr_node.data = val

    def delNodeATBegining(self):
        if self.head is None:
            return
        else:
            self.head  = self.head.next

    def delNodeAtIndex(self,index):
        curr_node = self.head
        pos = 0
        if pos == index:
            delNodeATBegining()
        else :

            while(curr_node!=None and pos+1 != index):
                pos = pos +1
                curr_node =  curr_node.next

            if curr_node != None:
                curr_node.next = curr_node.next.next

    def delNodeAtLast(self):
        if self.head is None:
            return
        else :

            curr_node = self.head
            while(curr_node.next):
                curr_node = curr_node.next
            curr_node.next = None

    def delNodeBasedOnData(self,data):
        curr_node = self.head
        if curr_node.data == data:
            delNodeATBegining()
        else:

            while (curr_node != None and curr_node.next.data!= data):

                curr_node = curr_node.next

            if curr_node != None:
                curr_node.next = curr_node.next.next

    def printNodeData(self):
        curr_node =  self.head
        while(curr_node):
            print(curr_node.data)
            curr_node =  curr_node.next

    def lengthOfLinkedList(self):
        curr_node =self.head
        if self.head is None:
            return 0
        else:
            size = 0
            while(curr_node):
                size = size+1
                curr_node = curr_node.next
            return size






