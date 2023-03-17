import os
os.system('cls')

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.pages = []
        self.num_pages = 0
        self.items_per_page = 5

    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
        else:
            current = self.head

            while current.next is not None:
                current = current.next

            current.next = new_node

        if len(self.pages) == 0 or len(self.pages[self.num_pages-1]) == self.items_per_page:
            self.pages.append([])
            self.num_pages += 1

        self.pages[self.num_pages-1].append(data)

    def display(self, page):
        if page > self.num_pages:
            print("Page not found.")
            return

        print("Pomodoro timer - Page", page)
        print("----------------------------")

        for item in self.pages[page-1]:
            print(item)
        
        if page % self.num_pages == page: 
            print("----------------------------")
            input("Enter to see next")
        print("----------------------------")
        print("")
        print("-- Keep up the good work! --")
        print("")

    def display_all(self):
        for i in range(1, self.num_pages+1):
            self.display(i)

linked_list = LinkedList()

# Pomo usage input
linked_list.append("Pomo 25 Minutes")
linked_list.append("Pomo 25 Minutes")
linked_list.append("Pomo 25 minutes")
linked_list.append("5 Minutes break")
linked_list.append("Pomo 25 minutes")
linked_list.append("Pomo 25 minutes")
linked_list.append("15 Minutes break")
linked_list.append("Pomo 25 minutes")
linked_list.append("Pomo 25 minutes")
linked_list.append("Pomo 25 minutes")
linked_list.append("5 Minutes break")
linked_list.append("Pomo 25 minutes")
linked_list.append("15 Minutes break")
linked_list.append("Pomo 25 minutes")
linked_list.append("Pomo 25 minutes")
linked_list.append("Pomo 25 minutes")
linked_list.append("Pomo 25 minutes")
linked_list.append("15 Minutes break")

# Display all pages
linked_list.display_all()