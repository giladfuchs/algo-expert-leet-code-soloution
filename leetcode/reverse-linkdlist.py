class Node:

    # Constructor to initialize the node object
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:

    # Function to initialize head
    def __init__(self):
        self.head = None

    def reverseUtil(self, curr:Node, prev:Node):

        if curr.next is None:
            self.head = curr
            curr.next=prev
            return  self.head
        next = curr.next
        curr.next =prev
        return self.reverseUtil(next, curr)


    def reverse(self):
        if self.head is None:
            return
        return self.reverseUtil(self.head, None)

    # Function to insert a new node at the beginning

    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    # Utility function to print the linked LinkedList
    def printList(self):
        temp = self.head
        while (temp):
            print(temp.data)
            temp = temp.next


# Driver code
llist = LinkedList()
llist.push(8)
llist.push(7)
llist.push(6)
llist.push(5)
llist.push(4)
llist.push(3)
llist.push(2)
llist.push(1)

llist.printList()

head =  llist.reverse()


llist.printList()
print(head)