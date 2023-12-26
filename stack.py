class Stack:
    def __init__(self):
        self.container =[]

    def push(self,*data):
        return self.container.extend(data)

    def length(self):
        return  len(self.container)

    def pop(self):

        if self.length() == 0:
            print("Stack is empty")
            return

        return self.container.pop()

    def peek(self):
        if self.length() == 0:
            print("Stack is empty")
            return
        return self.container[-1]


stack=Stack()

stack.push(1)
print("Peek val",stack.peek())
stack.push(2)

print("Peek val",stack.peek())

stack.push(3)
print("Peek val",stack.peek())

stack.push(4,5,6)
print("Peek val",stack.peek())

print(stack.container)



