class Node:
    def __init__(self, data=None):
        self.data = data 
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, data):
        if self.head is None:
            self.add_at_first(data)
        else:
            self.add_at_last(data)
            
    
    def add_at_first(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node
    
    def add_at_last(self, new_data):
        new_node = Node(new_data)
        val = self.head

        while val.next is not None:               
            val = val.next
            
        val.next = new_node
    
    def add_after(self, value, new_data):
        new_node = Node(new_data)
        val = self.head

        while val.data != value:
            val = val.next
        
        temp = val.next
        val.next = new_node
        new_node.next = temp

    def delete(self, value):
        val = self.head

        if val.data == value:
            self.head = val.next
            return

        prev = val
        while val.data != value:
            prev = val
            val = val.next

        prev.next = val.next
        
                
    def list_print(self):
        val = self.head
        ll_str = "["
        while val is not None:
            ll_str += " " + val.data 
            val = val.next
        ll_str += " ]\n"

        print(ll_str)
    


ll = LinkedList()


ll.add("23")
ll.add("12")
ll.add("13")
ll.add("14")
ll.add("61")

print("Original Linked List")
ll.list_print()

ll.add_at_first("100")
print("After adding 100 at firs:")
ll.list_print()

ll.add_at_last("200")
print("After addind 200 at last:")
ll.list_print()

ll.add_after("14", "71")
print("After adding 71 followed by 14")
ll.list_print()

ll.delete("13")
print("After deleting a middle element 13")
ll.list_print()

ll.delete("100")
print("After deleting the first element")
ll.list_print()

ll.delete("200")
print("After deleting the last element")
ll.list_print()

