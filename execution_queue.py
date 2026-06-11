from collections import deque

class ExecutionQueue: # принцип FIFO
    def __init__(self): # инициализация очереди
        self.queue = deque()

    def enqueue(self, task): # добавление задачи в очередь
        self.queue.append(task)

    def dequeue(self): # удаление задачи из очереди
        if len(self.queue) == 0:
            return None
        
        return self.queue.popleft()

    def show_queue(self): # показ очереди
        if len(self.queue) == 0:
            print("Очередь пуста.")
            return

        print('\n| Очередь выполнения |\n')

        for task in self.queue:
            print(task)

    def is_empty(self): # проверка на наличие задач в очереди
        return len(self.queue) == 0