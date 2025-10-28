class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def clear(self):
        data = self.data
        self.data = None
        return data

class LinkedList:
    def __init__(self):
        self.head: Node = None
        self.tail: Node = None

    def init_node(self, new_node: Node) -> None:
        self.head = new_node
        self.tail = new_node

    def empty(self):
        self.head = None
        self.tail = None
    
    def insert_at_beginning(self, data) -> None:
        new_node = Node(data)
        if self.head:
            new_node.next = self.head
            self.head = new_node
        else:
            self.init_node(new_node)

    def insert_at_end(self, data) -> None:
        new_node = Node(data)
        if self.head:
            self.tail.next = new_node
            self.tail = new_node
        else:
            self.init_node(new_node)

    def search(self, data) -> bool:
        current_node = self.head
        while current_node:
            if current_node.data == data:
                return True
            else:
                current_node = current_node.next
        return False

    def remove_beginning(self):
        rm_data = None

        if self.head:
            rm_data = self.head.clear()
            if self.head == self.tail:
                self.empty()
            else:
                self.head = self.head.next
            
        return rm_data

    def remove_at_end(self):
        rm_data = None
        if self.head == None:
            return rm_data
        if self.head == self.tail:
            rm_data = self.head.clear()
            self.empty()

        current_node = self.head
        while current_node:
            next_node = current_node.next
            if next_node == self.tail:
                rm_data = self.tail.clear()
                current_node.next = None
                self.tail = current_node
            current_node = next_node
        return rm_data

    def remove_at(self, data):
        rm_data = None
        if self.head == None:
            return rm_data
        if self.head.data == data:
            return self.remove_beginning()

        current_node = self.head
        while current_node:
            next_node = current_node.next
            if next_node == None:
                return rm_data
            if next_node.data == data:
                rm_data = next_node.clear()
                current_node.next = next_node.next
                break
            current_node = next_node
        return rm_data

    # CONVERTS TO LIST FOR UNIT TESTS
    def __iter__(self):
        out = []
        current_node = self.head
        while current_node:
            out.append(current_node.data)
            current_node = current_node.next
        return iter(out)

