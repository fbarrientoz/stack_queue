class Stack():
    def __init__(self):
        self.items = []
    

    def is_empty(self):
        return self.items == []
    
    def push(self, item):
        self.items.append(item)

    def pop(self):
        data = self.items[-1]
        self.items.remove(data)
        return data
    
    def peek(self):
        return self.items[-1]

    def size(self):
        return len(self.items)
    

class Queue():
    def __init__(self):
        self.items = []
    
    def is_empty(self): 
        return self.items == []

    def enqueue(self, item):
        self.items.append(item)
    
    def dequeue(self):
        return self.items.pop(0)

    def size(self):
        return len(self.items)



if __name__ == "__main__":

    new_Stack = Stack()
    new_Stack.push("Number 1")
    new_Stack.push("Number 2")
    new_Stack.push("Number 3")
    new_Stack.push("Number 4")
    new_Queue = Queue()

    new_Queue.enqueue("Number 1")
    new_Queue.enqueue("Number 2")
    new_Queue.enqueue("Number 3")
    new_Queue.enqueue("Number 4")

    print("")
    print("Test Stack Methods: ")
    print("Stack empty: " + str(new_Stack.is_empty()))   
    print("Peek " + str(new_Stack.peek()))
    print("Size " + str(new_Stack.size()))
    
    print("")
    print("Test Queue Methods: ")
    print("Queue empty: " + str(new_Queue.is_empty()))
    print("Size " + str(new_Queue.size()))
