class ListNode:
    def __init__(self, val=0, next = None):
        self.val = val
        self.next = next

head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)

# print recursivly

def reverse(node):
    if not node:
        return None
    
    newHead = node
    if node.next:
        newHead = reverse(node.next)
        node.next.next = node
    node.next = None
    return newHead

reverse(head)

def print_node(node:ListNode):
    if not node:
        return
    else:
        print(node.val)
        print_node(node.next)

print_node(head)


