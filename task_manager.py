class TaskManager:
    def __init__(self): # инициализация работы менеджера задач
        self.tasks = []

    def add_task(self, task): # добавление задачи
        self.tasks.append(task)

    def show_tasks(self): # показ задач
        if not self.tasks:
            print('В списке задач пока пусто!')
            return

        print('\n| Список задач |\n')

        for task in self.tasks:
            print(task)

    def find_task(self, task_id): # поиск задачи по ID
        for task in self.tasks:

            if task.task_id == task_id:
                return task

        return None
    
    def delete_task(self, task_id): # удаление задачи

        for task in self.tasks:

            if task.task_id == task_id:
                self.tasks.remove(task)
                return task

        return None

    def edit_task(self, task_id, new_title, new_priority, new_execution_time, new_deadline): # редактирование задачи

        task = self.find_task(task_id)

        if task:

            task.title = new_title
            task.priority = new_priority
            task.execution_time = new_execution_time
            task.deadline = new_deadline

            return True

        return False
    
    def undo(self, undo_stack):

        action = undo_stack.pop()

        if action is None:
            print("Нет действий для отмены.")
            return

        action_type = action["type"]

        if action_type == "ADD":

            self.delete_task(action["task"].task_id)

            print("Добавление отменено.")

        elif action_type == "DELETE":

            self.add_task(action["task"])

            print("Удаление отменено.")

        elif action_type == "EDIT":

            old_task = action["old_task"]

            task = self.find_task(old_task.task_id)

            if task:
                task.title = old_task.title
                task.priority = old_task.priority
                task.execution_time = old_task.execution_time
                task.deadline = old_task.deadline

            print("Изменение отменено.")