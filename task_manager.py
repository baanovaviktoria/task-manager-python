class TaskManager:
    """
    Управляет списком задач: 
    - добавление; 
    - удаление;
    - редактирование; 
    - отмена действий
    """
    def __init__(self): 
        """
        Инициализация работы менеджера задач
        """
        self.tasks = []

    # Добавление задачи в конец списка
    def add_task(self, task): 
        self.tasks.append(task)

    # Выводит все задачи 
    def show_tasks(self): 
        if not self.tasks:
            print('В списке задач пока пусто!')
            return

        print('\n| Список задач |\n')

        for task in self.tasks:
            print(task)

    # Ищет задачу по ID
    def find_task(self, task_id): 
        for task in self.tasks:

            if task.task_id == task_id:
                return task

        return None
    
    # Удаляет задачу с указанным ID
    def delete_task(self, task_id): 

        for task in self.tasks:

            if task.task_id == task_id:
                self.tasks.remove(task)
                return task

        return None

    # Редактирует задачу
    def edit_task(self, task_id, new_title, new_priority, new_execution_time, new_deadline): 

        task = self.find_task(task_id)

        if task:

            task.title = new_title
            task.priority = new_priority
            task.execution_time = new_execution_time
            task.deadline = new_deadline

            return True

        return False
    
    # Отменяет последнее действие
    def undo(self, undo_stack):

        action = undo_stack.pop()

        if action is None:
            print("Нет действий для отмены.")
            return

        action_type = action["type"]

        if action_type == "ADD":
            # Отменяем добавление (удаляем добавленную задачу)
            self.delete_task(action["task"].task_id)

            print("Добавление отменено.")

        elif action_type == "DELETE":
            # Отменяем удалению (возвращаем удалённую задачу)
            self.add_task(action["task"])

            print("Удаление отменено.")

        elif action_type == "EDIT":
            # Отменяем редактирование (восстанавливаем старую версию задачи)
            old_task = action["old_task"]

            task = self.find_task(old_task.task_id)

            if task:
                task.title = old_task.title
                task.priority = old_task.priority
                task.execution_time = old_task.execution_time
                task.deadline = old_task.deadline

            print("Изменение отменено.")
