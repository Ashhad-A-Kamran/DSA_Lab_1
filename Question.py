class Node: 
    def __init__(self, data, next=None): 
        self.data = data 
        self.next = next
  
class LinkedList: 
    def __init__(self): 
        self.head = None
          
    # Function to push a new Node in  
    # the linked list  
    def push(self, new_data):  
        new_node = Node(new_data, self.head)  
        self.head = new_node 
      
    # Function to reverse linked list using a stack  
    def reverseList(self):  
        # Stack to store elements of list  
        stk = [] 
      
        # Push the elements of list to stack  
        ptr = self.head  
        while ptr is not None:  
            stk.append(ptr)  
            ptr = ptr.next
      
        # Pop from stack and replace the current nodes' next pointer  
        if len(stk) == 0:
            return  # If the list is empty, no reversal is needed
        
        self.head = stk.pop()  # Set the head to the last element of the stack
        ptr = self.head
        
        while len(stk) != 0:  
            ptr.next = stk.pop()  # Set the next node to the popped node
            ptr = ptr.next
        
        ptr.next = None  # The last node's next should be None to indicate the end of the list
      
    # Function to print the Linked list  
    def printList(self): 
        curr = self.head 
        while curr:  
            print(curr.data, end=" ")  
            curr = curr.next
        print()  # To move to the next line after printing list
  
# Driver Code  
if __name__ == "__main__": 
    # Start with the empty list 
    linkedList = LinkedList()  
    
    # Use push() to construct the list 1->2->3->4->5 
    linkedList.push(5)  
    linkedList.push(4)  
    linkedList.push(3)  
    linkedList.push(2)  
    linkedList.push(1)  
    
    print("Original Linked List:")
    linkedList.printList()
  
    # Reverse the list
    linkedList.reverseList()  
  
    print("Reversed Linked List:")
    linkedList.printList()
