class Node:
  def __init__(self, data):
    self.data = data
    self.next = None


class Stack:
  def __init__(self):
    self.head = None

  def push(self, data) -> None:
    # Write your code here
        node = Node(x)
        if node is None:
            print('Heap Overflow')
            return
        node.data = x
        node.next = self.top
        self.top = node
        self.nodesCount += 1
    def isEmpty(self):
        return self.top is None
    def peek(self):
        if not self.isEmpty():
            return self.top.data
        else:
            print('The stack is empty')
            exit(-1)

  def pop(self) -> None:
    # Write your code here
    if self.top is None:
            print('Stack Underflow')
            exit(-1)
    top = self.top.data
    self.top = self.top.next
     self.nodesCount -= 1
 
        return top
  def status(self):
    """
    It prints all the elements of stack.
    """
    # Write your code here  


# Do not change the following code
stack = Stack()
operations = []
for specific_operation in input().split(','):
    operations.append(specific_operation.strip())
input_data = input()
data = input_data.split(',')
for i in range(len(operations)):
  if operations[i] == "push":
    stack.push(int(data[i]))
  elif operations[i] == "pop":
    stack.pop()
stack.status()
