class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def print_list(self):
        curr = self.head
        while curr:
            print(curr.data, end=" -> ")
            curr = curr.next
        print("None")

    def reverse(self):
        prev = None
        curr = self.head
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        self.head = prev

    def merge_sort(self):
        if self.head is None or self.head.next is None:
            return self.head

        middle = self.get_middle(self.head)
        next_to_middle = middle.next
        middle.next = None

        left = self.merge_sort_helper(self.head)
        right = self.merge_sort_helper(next_to_middle)

        sorted_list = self.sorted_merge(left, right)
        self.head = sorted_list

    def get_middle(self, head):
        if head is None:
            return head

        slow = head
        fast = head

        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        return slow

    def sorted_merge(self, a, b):
        result = None
        if a is None:
            return b
        if b is None:
            return a

        if a.data <= b.data:
            result = a
            result.next = self.sorted_merge(a.next, b)
        else:
            result = b
            result.next = self.sorted_merge(a, b.next)
        return result

    def merge_sort_helper(self, head):
        if head is None or head.next is None:
            return head

        middle = self.get_middle(head)
        next_to_middle = middle.next
        middle.next = None

        left = self.merge_sort_helper(head)
        right = self.merge_sort_helper(next_to_middle)

        sorted_list = self.sorted_merge(left, right)
        return sorted_list

def merge_sorted_lists(list1, list2):
    dummy = Node(0)
    tail = dummy

    while list1 and list2:
        if list1.data <= list2.data:
            tail.next = list1
            list1 = list1.next
        else:
            tail.next = list2
            list2 = list2.next
        tail = tail.next

    if list1:
        tail.next = list1
    elif list2:
        tail.next = list2

    return dummy.next

# Перевірка

# Створення списків та виконання операцій
llist1 = LinkedList()
llist1.append(3)
llist1.append(1)
llist1.append(4)
llist1.append(2)

print("Початковий список:")
llist1.print_list()

llist1.reverse()
print("Зворотній список:")
llist1.print_list()

llist1.merge_sort()
print("Відсортований список:")
llist1.print_list()

llist2 = LinkedList()
llist2.append(5)
llist2.append(6)
llist2.append(7)

merged_list = LinkedList()
merged_list.head = merge_sorted_lists(llist1.head, llist2.head)
print("З'єднані відсортовані списки:")
merged_list.print_list()
