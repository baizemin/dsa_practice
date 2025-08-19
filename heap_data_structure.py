class Heap:
    def __init__(self):
        self.heap = []

    def _parent_index(self, index):
        return (index - 1) // 2

    def _left_child_index(self, index):
        return 2 * index + 1

    def _right_child_index(self, index):
        return 2 * index + 2

    def _swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def insert(self, value):
        self.heap.append(value)
        print(f"{value} is inserted")
        self._shift_up(len(self.heap) - 1)

    # Corrected for a min-heap
    def _shift_up(self, i):
        parent = self._parent_index(i)
        while i > 0 and self.heap[parent] > self.heap[i]:
            self._swap(parent, i)
            i = parent
            parent = self._parent_index(i)

    # Corrected for a min-heap with a recursive call fix
    #it it used to maintain the heap when the a root is removed
    def _shift_down(self, index):
        min_idx = index
        right = self._right_child_index(index)
        left = self._left_child_index(index)

        if right < len(self.heap) and self.heap[min_idx] > self.heap[right]:
            min_idx = right

        if left < len(self.heap) and self.heap[min_idx] > self.heap[left]:
            min_idx = left

        if index != min_idx:
            self._swap(min_idx, index)
            self._shift_down(min_idx)  # The recursive call must use the new index

    def is_empty(self):
        return self.heap == []

    def extract_min(self):
        if self.is_empty():
            return None
        if len(self.heap) == 1:
            return self.heap.pop()
        min_value = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._shift_down(0)
        return min_value

    def peek_min(self):
        if self.is_empty():
            return None
        return self.heap[0]


min_heap = Heap()
min_heap.insert(2)
min_heap.insert(29)
min_heap.insert(34)
min_heap.insert(45)
min_heap.insert(1)
min_heap.insert(9)
# now storing the elements in an separate array
arr = []
print(min_heap.heap)
while not min_heap.is_empty():
    arr.append(min_heap.extract_min())

print('this is an sorted ', arr)