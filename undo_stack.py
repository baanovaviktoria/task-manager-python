class UndoStack: # принцип LIFO
    def __init__(self): # инициализация работы стека
        self.stack = []

    def push(self, action): # добавление задачи
        self.stack.append(action)

    def pop(self): # удаление и возвращение задачи

        if len(self.stack) == 0:
            return None

        return self.stack.pop()

    def is_empty(self): # проверка на наличие задач в стеке
        return len(self.stack) == 0