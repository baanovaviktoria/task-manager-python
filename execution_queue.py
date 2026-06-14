from collections import deque

class ExecutionQueue: 
    """
    Очередь задач с дисциплиной FIFO (первым пришёл - первым ушёл).
    """
    # Инициализация пустой очереди
    def __init__(self): 
        self.queue = deque()

    # Добавление задачи в конец очереди
    def enqueue(self, task): 
        self.queue.append(task)

    # Удаление задачи из очереди
    def dequeue(self): 
        if len(self.queue) == 0:
            return None
        
        return self.queue.popleft()

    # Показ очереди
    def show_queue(self): 
        if len(self.queue) == 0:
            print("Очередь пуста.")
            return

        print('\n| Очередь выполнения |\n')

        for task in self.queue:
            print(task)

    # Проверка на наличие задач в очереди
    def is_empty(self): 
        return len(self.queue) == 0
