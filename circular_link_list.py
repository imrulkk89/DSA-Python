class Node:
    def __init__(self, key, data) -> None:
        self.key = key
        self.data = data
        self.next = None
        
head = None
current = None

def is_head_empty():
    return head is None

""" 
### Circular Linked List provided in Tutorials point
def insert_first(key, data):
    global head
    new_node = Node(key, data)
    if is_empty():
        head = new_node
        head.next = head 
    else:
        new_node.next = head 
        head = new_node            

def print_list():
    global head
    ptr = head

    while True:
        print(ptr.data)
        ptr = ptr.next
        if ptr.next is ptr:
            break


insert_first(1, 10)
insert_first(2, 20)
insert_first(3, 30)

print_list() """

### corrected Linked List code. 

def insert_first(key, data):
    global head
    global current
    new_node = Node(key, data)
    if is_head_empty():
        head = new_node
        new_node.next = head
        current = new_node
    else:
        current.next = new_node
        new_node.next = head
        current = new_node
            
def print_list():
    global head
    ptr = head

    while True:
        print(ptr.data)
        ptr = ptr.next
        if ptr is head:
            break





insert_first(1, 10)
insert_first(2, 20)
insert_first(3, 30)

print_list()
