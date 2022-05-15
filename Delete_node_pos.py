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

    def delete_node(self, pos):
        temp = self.head
        index = 0
        if (index == pos):
            self.head = temp.next
            temp = None

        while(temp is not None):

            if(index == pos):
                break

            prev = temp
            temp = temp.next
            index +=1

        if(temp == None):
            return

        prev.next = temp.next
        temp = None
        # while (temp is not None):
        #     if (temp.data == key):
        #         break
        #     prev = temp
        #     temp = temp.next
        #
        # if (temp == None):
        #     return
        #
        # prev.next = temp.next
        # temp = None


if __name__ == '__main__':
    print("----------------")
    obj = Linked_list()
    obj.push(3)
    obj.push(2)
    obj.push(1)
    print("---------- Befor Delete----------")
    obj.print_linked_list()

    # obj.delete_node(1)
    # print("---------- After Delete At First position ----------")
    # obj.print_linked_list()

    obj.delete_node(1)
    print("---------- After Delete At any other position ----------")
    obj.print_linked_list()