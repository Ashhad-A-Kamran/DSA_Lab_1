class Node: 
    def __init__(self, value=0, next=None): 
        self.value = value 
        self.next = next 
            
class LinkedList():
    def __init__(self):  # Fixed typo here
        self.head = None
        
    def push(self, new_data):
        new_node = Node(new_data, self.head)
        self.head = new_node
    
    def reverse_linked_list(self, head: Node) -> Node: 
        stack = []
        
        # Push the elements of list to stack  
        ptr = self.head
        while ptr is not None:
            stack.append(ptr)
            ptr = ptr.next

        if len(stack) == 0:
            return None
            
        self.head = stack.pop()  # setting the head to the last element of the stack
        ptr = self.head
        
        while len(stack) != 0:
            ptr.next = stack.pop()  # setting the next node to the popped one
            ptr = ptr.next
            
        ptr.next = None  # setting the end node to None

    def print_list(self):
        current = self.head
        while current:
            print(current.value)  # Fixed attribute name here
            current = current.next
        print("\n") 

ll = LinkedList()

ll.push(5)
ll.push(4)
ll.push(3)
ll.push(2)
ll.push(1)

print("Original List:")
ll.print_list()

ll.reverse_linked_list(ll.head)

print("Reversed List:")
ll.print_list()
