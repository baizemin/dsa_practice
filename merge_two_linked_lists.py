class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def merge(l1, l2):
    dummy = Node(0)
    curr = dummy

    # PART 1: Loop while both lists have nodes to compare
    while l1 and l2:
        if l1.data < l2.data:
            curr.next = l1
            l1 = l1.next
        else:
            curr.next = l2
            l2 = l2.next
        curr = curr.next

    # PART 2: The loop is finished. Now, attach the single remaining list.
    # One of these will be a list of nodes, and the other will be None.
    if l1:
        curr.next = l1
    else:
        curr.next = l2

    return dummy.next


# Helper function to print
def print_list(head):
    while head:
        print(head.data, end=" -> ")
        head = head.next
    print("None")


# --- Example ---
l1 = Node(1)
l1.next = Node(5)

l2 = Node(2)
l2.next = Node(4)

merged_head = merge(l1, l2)
print_list(merged_head)
# Correct Output: 1 -> 2 -> 4 -> 5 -> None