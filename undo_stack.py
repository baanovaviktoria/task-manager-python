class UndoStack: 
    """
    Стек, поддерживающий отмену действий. 
    Работает по принципу LIFO (последний пришёл - первым ушёл).
    """
    # Инициализация работы стека
    def __init__(self): 
        self.stack = []

    # Добавление задачи
    def push(self, action): 
        self.stack.append(action)

    # Удаление и возвращение задачи
    def pop(self): 
        if len(self.stack) == 0:
            return None

        return self.stack.pop()

    # Проверка на наличие задач в стеке
    def is_empty(self): 
        return len(self.stack) == 0
