class Node:
    def __init__(self,items = None):
        if items is None:
            self.items = []
        else:
            self.items = items
hashtable_SIZE  = 10**5+3
def code(items):
    return (items[0]+items[1]+items[2]+items[3]+items[4]+items[5])%hashtable_SIZE
def identical_right(items1,items2,start):
    for i in range(6):
        if items1[i] != items2[(i+start)%6]:
            return False
    return True

def identical_left(items1,items2,start):
    for i in range(6):
        index = start - i
        if index < 0:
            index+=6
        if items1[i] != items2[index]:
            return False
    return True

def are_identical(items1,items2):
    for start in range(6):
        if identical_right(items1,items2,start):
            return True
        if identical_left(items1,items2,start):
            return True
    return False
def find(snowflakes):
    hashtable = [None]*hashtable_SIZE
    res = None
    for i,item in enumerate(snowflakes):
        hashcode = code(item)
        curr = hashtable[hashcode]
        found = False
        if curr is not None:
            while curr is not None:
                if are_identical(item,curr.items):
                    found = True
                    break
                curr = curr.next
        if found:
            return i,"found"
        new = Node(item)
        new.next = hashtable[hashcode]
        hashtable[hashcode] = new
    return -1,"unique"
if __name__ == "__main__":
    snowflake_list = [
        [1, 2, 3, 4, 5, 6],
        [4, 5, 6, 7, 8, 9],
        [3, 4, 5, 6, 1, 2],
        [10, 11, 12, 13, 14, 15]
    ]
    print(find(snowflake_list))
    # res = find(snowflake_list)
    # print(res)

