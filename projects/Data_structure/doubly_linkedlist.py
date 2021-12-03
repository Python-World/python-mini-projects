"""
A queue system based on a "Doubly Linked-list" principle
"""
import warnings


class LinkedError(Exception):
    pass


class NegativeNumber(LinkedError):
    pass


class EmptyLinked(LinkedError):
    pass


class EmptyLinkedWarnings(RuntimeWarning):
    pass


class DoublyLinkedNode:
    """Queue with previous"""


    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.previous = None


class DoublyLinkedList:
    """Doubly Linked-list"""

    def __init__(self):
        self.head = None
        self.length = -1


    def __len__(self):
        return self.length + 1


    def is_empty(self):
        """
        Check that the list is empty
        """
        return True if self.head is None else False


    def push(self, data):
        """
        Push item inside the queue
        """
        new_node = DoublyLinkedNode(data)
        if self.is_empty():
            self.head = new_node
            self.length += 1
            return new_node
        current_node = self.head

        while current_node.next is not None:
            current_node = current_node.next
        new_node.previous = current_node
        current_node.next = new_node
        self.length += 1
        return current_node


    def valid_number(self, number):
        """
        Check that number is valid or not.
        """
        try:
            if number < 0 and number.is_integar():
                raise ValueError("Previous is None.!")
        except (TypeError, ValueError):
            raise NegativeNumber(
                (
                    """That linked-list is an
                    empty and not support negative number."""
                )
            )
        if number > self.length:
            raise EmptyLinked("That number greater than linked length")
        return number


    def pop(self):
        """
        Remove the following item from the queue
        """
        try:

            self.length = self.valid_number(self.length)
            temp = self.head.data
            self.head = self.head.next
            self.length -= 1

        except EmptyLinked:
            warnings.warn(
                "That Linked is Empty please add items first",
                EmptyLinkedWarnings,
                stacklevel=3,
            )
        return temp


    def get_item(self, index):
        """
        Get the following item from the queue
        Note get is just get
        """
        current = 0
        data = self.head
        try:
            if index < 0:
                raise ValueError('sdfsdf')
            index = self.valid_number(index)
        except (NegativeNumber, ValueError):
            warnings.warn("""The element before the 
            first element cannot be displayed
            """,
                          EmptyLinkedWarnings,
                          stacklevel=3
                          )
            index = 0
        while index > current:
            data = data.next
            current += 1
        return data.data


    def get_list(self):
        """
        Get all items from the queue
        """
        elements = []
        current_node = self.head
        while current_node is not None:
            elements.append(current_node.data)
            current_node = current_node.next
        return elements


    def get_previous(self, index=None):
        """
        Get the item that accepted the current element of the queue
        """
        if index is None:
            return self.head.previous
        index -= 1
        return self.get_item(index)


    def delete(self, index):
        current_node = self.head
        current_index = 0
        while current_index < index:
            current_node = current_node.next
            current_index += 1
        current_node.previous.next = current_node.next
        del current_node


    def update(self, new_value, index: int):
        current_index = 0
        current_node = self.head
        while current_index < index:
            current_node = current_node.next
            current_index += 1
        current_node.data = new_value
        return current_node.data


# Remove commit for Testing
# # -------------------------
# my_list = DoublyLinkedList()
# my_list.push(1)
# my_list.push(2)
# my_list.push(3)
# my_list.push(4)

# print(my_list.get_previous(0))
# print('=' * 25, 'Length', '=' * 25)
# length = len(my_list)
# assert length == 4, "Error Test Length Interrelated List"
# print(length)
#
# print('=' * 25, 'Pop', '=' * 25)
# item = my_list.pop()
# assert item == 1, """
# Test error Take the next item out of the queue doubly linked-list
# """
# print(item)
#
# print('=' * 25, 'Show Items', '=' * 25)
# elements_list = my_list.get_list()
# assert len(elements_list) == 3, "Test error Create a list of items"
# print(elements_list)
#
# print('=' * 25, 'Update Value', '=' * 25)
# new = my_list.update(10, 1)
# print(new)
#
# print('=' * 25, 'Get updated value', '=' * 25)
# new = my_list.get_item(1)
# assert new == 10, "Error Test Update Specific Node Value"
# print(new)
#
# print('=' * 25, 'Show Items', '=' * 25)
# print(my_list.get_list())
#
# print('=' * 25, 'Delete', '=' * 25)
# my_list.delete(1)
#
# print('=' * 25, 'Show Items', '=' * 25)
# length = len(my_list.get_list())
# assert length == 2, "Error Test Delete Specific Node"
# print(my_list.get_list())
