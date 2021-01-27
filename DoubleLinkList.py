#Test
#Double Link List
import pdb

#pdb.set_trace()

class Node:
    def __init__(self,Data):
        self.Data = Data
        self.next = None
        self.prev = None

class doubleLinkList:

    def __init__(self):
        self.head = None

    def push(self,newValue):
        #pdb.set_trace()
        newNode = Node(newValue)
        #pdb.set_trace()
        newNode.next = self.head
        if self.head is not None:
            self.head.prev = newNode
        self.head = newNode

    # Print the Doubly Linked list
    def listprint(self, Node):
        while (Node is not None):
            print(Node.Data),
            last = Node
            Node = Node.next

dll = doubleLinkList()
dll.push(2)
dll.push(4)
dll.push(6)
dll.push(8)
dll.listprint(dll.head)




