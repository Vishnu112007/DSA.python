 
# Node class for queue
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Initialize front and rear
front = None
rear = None

# Enqueue function (Add car)
def enqueue():
    global front, rear
    car = input("Enter car number to park: ")
    newNode = Node(car)
    if rear is None: # Queue is empty
        front = rear = newNode
    else:
        rear.next = newNode
        rear = newNode
    print("Car parked.")

# Dequeue function (Remove car)
def dequeue():
    global front, rear
    if front is None:
        print("Queue is Empty!")
    else:
        print("Car removed:", front.data)
        temp = front
        front = front.next
        del temp
        if front is None:
            rear = None

# Display function
def display():
    if front is None:
        print("Queue is Empty!")
    else:
        print("Cars in parking:")
        temp = front
        while temp is not None:
            print(temp.data, end=" --> ")
            temp = temp.next
        print("NULL")

# Main menu
while True:
    print("\nQueue Menu:")
    print("1. Park a Car")
    print("2. Remove a ")
    print("3. Show All Cars")
    print("4. Exit")
    choice = input("Enter choice (1-4): ")

    if choice == '1':
        enqueue()
    elif choice == '2':
        dequeue()
    elif choice == '3':
        display()
    elif choice == '4':
        print("Exiting Program.")
        break
    else:
        print("Invalid choice! Try again.")
