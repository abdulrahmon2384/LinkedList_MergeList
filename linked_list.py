class Node:
    name = None
    next = None
    def __init__(self, name, age, telephone, address):
        self.name = name
        self._age = age
        self._telephone = telephone
        self._address = address
        self.next = None


    def __repr__(self):
        return self.name


class Linked:

    def __init__(self):
        self.head = None


    def length(self):
        if self.head == None:
            return 0
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count


    def add(self, nm, age, tel, adrs):
        details = Node(nm, age, tel, adrs)
        details.next = self.head
        self.head = details


    def remove(self, data):
        if self.head == None:
            return print("List is empty")
        if self.head.name.lower() == data.lower():
            self.head = self.head.next
            return print(data, "Remove successfully")

        found = False
        temp = None
        current = self.head
        for element in range(self.length()):
            if current.name.lower() == data.lower():
                found = True
                temp.next = current.next
                Node.size -= 1
                print(data.upper(), "Removed successfully")
                break
            else:
                temp = current
                current = current.next
        if not found:
            print(data.upper(), "Not found")

    def insert(self, index, nm, age, tel, adrs):
        if self.head == None:
            return print("list is empty")
        if index == 0:
            self.add(nm, age, tel, adrs)
            return print(nm.upper(), "details inserted")

        new = Node(nm, age, tel, adrs)
        position = 1
        found = False
        current = self.head
        for elenemt in range(self.length()):
            if position == index:
                next = current.next
                current.next = new
                new.next = next

                return print(nm.upper(), "Inserted successfully")

            current = current.next
            position += 1

        if not found:
            return print(f"Opp's index {index} Out of range")

    def print_l(self):
        if self.head == None:
            return print('List is empty')
        else:
            print(f"You have {self.length()} list details")
            count = 1
            current = self.head
            while current != None:
                print(count, str(current).upper())
                current = current.next
                count += 1
            print()

    def find(self, data):
        if self.head != None:
            current = self.head
            while current.name.lower() != data.lower():
                current = current.next
                if current == None:
                    return print(data.upper(), "Not found")
            print("\tFound")
            print('Name :', current.name.upper())
            print('Age :', current._age)
            print('Tel :', current._telephone)
            print('Address :', current._address.upper())
            print()

    def index(self, val):
        if val != 0:
            current = self.head
            position = 0
            while position < val:
                current = current.next
                position += 1
            return current
        return self.head

