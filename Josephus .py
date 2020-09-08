#  File: Josephus.py

#  Description: This program is about ritual suicide, which is kinda depressing tbh.

#  Student Name: Eric Ji

#  Student UT EID: ej6638

#  Partner Name: Brock Brennan

#  Partner UT EID: btb989

#  Course Name: CS 313E

#  Unique Number: 50210

#  Date Created: 10/3/19

#  Date Last Modified:11/4/2019
class Link(object):
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class CircularList(object):
    # Constructor
    def __init__ ( self ):
        self.first = None

    # Insert an element (value) in the list
    def insert ( self, data):
        if self.first is None:
            current = Link(data)
            self.first = current
            self.first.next = self.first
        else:
            current = Link(data)
            current.next = self.first.next
            self.first.next = current
            self.first = current

    # Find the link with the given data (value)
    def find ( self, data ):
        current = self.first
        if current is None:
            return
        else:
            while True:
                if current.data == data:
                    return current.data
                else:
                    current = current.next
    # Delete a link with a given data (value)
    def delete ( self, data ):
        if self.first.data == data:
            current = self.first
            while current.next != self.first:
                current = current.next
            current.next = self.first.next
            self.first = self.first.next
        else:
            current = self.first
            previous = None
            while current.next != self.first:
                previous = current
                current = current.next
                if current.data == data:
                    previous.next = current.next
                    current = current.next

    # Delete the nth link starting from the Link start
    # Return the next link from the deleted Link
    def delete_after(self, start, n):
        temp = self.find(start)
        current = self.first
        while current.data != temp:
            current = current.next
        for i in range(1, n):
            current = current.next

        print(str(current.data), end='\n')

        self.delete(current.data)
        return current.next.data


    # Return a string representation of a Circular List
    def __str__ ( self ):
        list = ""
        current = self.first.next
        while current:
            list += str(current.data) + '\n'
            current = current.next
            if current == self.first.next:
                break
        return list

def main():
    file = open("josephus.txt", "r")
    numofsoldiers = file.readline()
    numofsoldiers = int(numofsoldiers.strip())

    startsoldier = file.readline()
    startsoldier = int(startsoldier.strip())

    elimnum = file.readline()
    elimnum = int(elimnum.strip())

    file.close()

    circle = CircularList()
    for x in range(1, numofsoldiers + 1):
        circle.insert(x)

    for i in range(1, numofsoldiers + 1):
        startsoldier = circle.delete_after(startsoldier, elimnum)
main()
