# Node class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Queue class using Linked List
class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    # ENQUEUE operation
    def enqueue(self, value):
        new_node = Node(value)
        if self.rear is None:  # Queue is empty
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node
        print(f"{value} enqueued to queue.")

    # DEQUEUE operation
    def dequeue(self):
        if self.front is None:
            print("Queue is EMPTY! Cannot dequeue.")
        else:
            removed = self.front.data
            self.front = self.front.next
            if self.front is None:  # If queue becomes empty
                self.rear = None
            print(f"{removed} dequeued from queue.")

    # DISPLAY operation
    def display(self):
        if self.front is None:
            print("Queue is EMPTY!")
        else:
            print("Queue elements are:")
            temp = self.front
            while temp is not None:
                print(f"{temp.data} --> ", end="")
                temp = temp.next
            print("NULL")

# Menu-driven interface
queue = Queue()

while True:
    print("\n--- Linked List Queue Menu ---")
    print("1. Enqueue")
    print("2. Dequeue")
    print("3. Display")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        value = input("Enter value to enqueue: ")
        queue.enqueue(value)
    elif choice == '2':
        queue.dequeue()
    elif choice == '3':
        queue.display()
    elif choice == '4':
        print("Exiting program. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
