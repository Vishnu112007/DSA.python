class Stack:
    def __init__(self, max_size):
        self.stack = [None] * max_size  # fixed size stack
        self.top = -1                   # top pointer initialized to -1 (empty stack)
        self.max_size = max_size

    # Push operation
    def push(self, data):
        # Step 1: Check if the stack is full
        if self.top == self.max_size - 1:
            # Step 2: Produce error and exit
            print("Error: Stack Overflow. Cannot push", data)
            return False
        else:
            # Step 3: Increment top pointer to next empty space
            self.top += 1
            # Step 4: Add data element at the top location
            self.stack[self.top] = data
            # Step 5: Return success
            print(f"Pushed {data} onto the stack.")
            return True

    # Pop operation
    def pop(self):
        # Step 1: Check if the stack is empty
        if self.top == -1:
            # Step 2: Produce error and exit
            print("Error: Stack Underflow. Cannot pop.")
            return None
        else:
            # Step 3: Access the data element at the top pointer
            data = self.stack[self.top]
            self.stack[self.top] = None  # Optional: clear the slot
            self.top -= 1  # decrement top
            # Step 5: Return success and popped data
            print(f"Popped {data} from the stack.")
            return data

    # Peek operation
    def peek(self):
        # Step 1: Check if the stack is empty
        if self.top == -1:
            # Step 2: Produce error and exit
            print("Error: Stack is empty. Nothing to peek.")
            return None
        else:
            # Step 3: Print the value at the top pointer
            data = self.stack[self.top]
            print(f"Top element is {data}.")
            return data

    # Helper method to display stack contents (for debugging/demo)
    def display(self):
        if self.top == -1:
            print("Stack is empty.")
        else:
            print("Stack elements:", self.stack[:self.top + 1])

# Demo:
stack = Stack(3)

# Try pushing elements
stack.push(10)
stack.push(20)
stack.push(30)
stack.push(40)  # This should give overflow error

stack.display()

# Peek top element
stack.peek()

# Pop elements
stack.pop()
stack.pop()
stack.pop()
stack.pop()  # This should give underflow error

stack.display()
