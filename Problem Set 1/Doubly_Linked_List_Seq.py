class Doubly_Linked_List_Node:
    def __init__(self, x):
        self.item = x
        self.prev = None
        self.next = None

    def later_node(self, i):
        if i == 0: return self
        assert self.next
        return self.next.later_node(i - 1)

class Doubly_Linked_List_Seq:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node.item
            node = node.next

    def __str__(self):
        return '-'.join([('(%s)' % x) for x in self])

    def build(self, X):
        for a in X:
            self.insert_last(a)

    def get_at(self, i):
        node = self.head.later_node(i)
        return node.item

    def set_at(self, i, x):
        node = self.head.later_node(i)
        node.item = x

    def insert_first(self, x):
        node = Doubly_Linked_List_Node(x)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            node.next = self.head
            self.head.prev = node
            self.head = node
        pass

    def insert_last(self, x):
        node = Doubly_Linked_List_Node(x)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            node.prev = self.tail
            self.tail.next = node
            self.tail = node
        pass

    def delete_first(self):
        x = None
        if self.head is not None:
            x = self.head
            self.head = self.head.next
        if self.head is None:
            self.tail = None
        else:
            self.head.prev = None
        return x

    def delete_last(self):
        x = None
        if self.tail is not None:
            x = self.tail
            self.tail = self.tail.prev
        if self.tail is None:
            self.head = None 
        else:
            self.tail.next = None
        return x

    def remove(self, x1, x2):
        L2 = Doubly_Linked_List_Seq()
        ###########################
        # Part (b): Implement me! # 
        ###########################
        return L2

    def splice(self, x, L2):
        ###########################
        # Part (c): Implement me! # 
        ###########################
        pass
