class Node:
    def __init__(self, data=None, next_node=None) -> None:
        self.data = data
        self.next_node = next_node



class LinkedList:
    def __init__(self) -> None:
        self.head_node = None
        self.last_node = None

    def to_list(self):
        nlist = []
        if self.head_node is None:
            return nlist

        node = self.head_node
        while node:
            nlist.append(node.data)
            node = node.next_node
        return nlist 

    def insert_begining(self, data):
        if self.head_node is None:
            self.head_node = Node(data)
            self.last_node = self.head_node
            return
        
        new_node = Node(data, self.head_node)
        self.head_node = new_node

    def insert_end(self, data):
        if self.head_node is None:
            self.insert_begining(data)
            return
        
        self.last_node.next_node = Node(data, None)
        self.last_node = self.last_node.next_node


    def print_nodes(self):
        nodes = ""

        node = self.head_node

        if node is None:
            print(None)
        while node:
            nodes += f"{node.data} ->"
            node = node.next_node

        nodes += "None"
        print(nodes)

