class Node:

    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkList:

    def __init__(self):
        self.head = Node()

    def append(self, data):
        new_node = Node(data)
        cur = self.head

        while cur.next is not None:
            cur = cur.next

        cur.next = new_node

    @property
    def length(self):
        cur = self.head
        total = 0
        while cur.next is not None:
            cur = cur.next
            total += 1
        return total

    def index(self, data):
        cur = self.head
        index = 0

        while cur.next is not None:
            cur = cur.next
            if data == cur.data:
                return index
            index += 1

    def __get_element(self, index=None):
        cur = self.head
        cur_index = 0

        if index >= self.length:
            raise IndexError('Index out of range.')

        while cur.next is not None:
            cur = cur.next
            if index == cur_index:
                return cur

            cur_index += 1

    def pop(self, index):
        return self.__get_element(index).data

    @property
    def show_items(self):
        elements = []
        cur = self.head

        while cur.next is not None:
            cur = cur.next
            elements.append(cur.data)
        return elements

    def update(self, data, index):
        old = self.__get_element(index)
        old.data = data
        return old.data

    def delete(self, index):
        cur = self.head
        cur_index = 0

        if index >= self.length:
            raise IndexError('Index out of range.')

        while cur.next is not None:
            last = cur
            cur = cur.next
            if cur_index == index:
                last.next = cur.next
                return None

            cur_index += 1


my_list = LinkList()
my_list.append(1)
my_list.append(2)
my_list.append(3)
my_list.append(4)

print('=' * 25, 'Length', '=' * 25)
print(my_list.length)

print('=' * 25, 'Pop', '=' * 25)
print(my_list.pop(1))

print('=' * 25, 'Show Items', '=' * 25)
print(my_list.show_items)

print('=' * 25, 'Update', '=' * 25)
print(my_list.update(10, 1))


print('=' * 25, 'Index', '=' * 25)
print(my_list.index(1))

print('=' * 25, 'Show Items', '=' * 25)
print(my_list.show_items)

print('=' * 25, 'Delete', '=' * 25)
my_list.delete(1)

print('=' * 25, 'Show Items', '=' * 25)
print(my_list.show_items)
