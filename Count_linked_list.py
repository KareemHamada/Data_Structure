class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Linked_list:
    def __init__(self):
        self.head = None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def print_linked_list(self):
        node = self.head
        while (node):
            print(node.data)
            node = node.next


    def count_linked_list(self):
        counter = 0
        temp = self.head
        while (temp is not None):
            counter +=1
            temp = temp.next

        print(counter)


if __name__ == '__main__':
    print("----------------")
    obj = Linked_list()
    obj.push(3)
    obj.push(2)
    obj.push(1)

    print("---------- Befor any Change  ----------")
    obj.print_linked_list()

    print("---------- Count of linked list items ----------")
    obj.count_linked_list()

