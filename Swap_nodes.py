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

    def swap(self,x,y):
        temp_x = self.head
        temp_y = self.head
        while(temp_x is not None):
            if(temp_x.data == x):
                print('temp_x.data ' + str(temp_x.data))
                break
            prev_x = temp_x
            temp_x = temp_x.next


        while (temp_y is not None):
            if (temp_y.data == y):
                print('temp_y.data ' + str(temp_y.data))
                break

            prev_y = temp_y
            temp_y = temp_y.next


        prev_x.next = temp_y
        prev_y.next = temp_x
        temp = temp_y.next

        temp_y.next = temp_x.next
        temp_x.next = temp





if __name__ == '__main__':
    obj = Linked_list()
    obj.push(3)
    obj.push(2)
    obj.push(1)
    obj.push(0)

    print("---------- Befor any Change ----------")
    obj.print_linked_list()

    print("---------- After Change ----------")
    obj.swap(1,2)

    obj.print_linked_list()
