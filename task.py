from copy import deepcopy

class Task:
    '''
    Данный класс содержит:
    - task_id — уникальный номер задачи
    - title — название
    - priority — приоритет
    - execution_time — время выполнения
    - deadline — дедлайн
    '''
    def __init__(self, task_id, title, priority, execution_time, deadline):
        self.task_id = task_id
        self.title = title
        self.priority = priority
        self.execution_time = execution_time
        self.deadline = deadline

    def copy(self):
        return deepcopy(self)
    
    def __str__(self):
        return (
                f'ID: {self.task_id}\n'
                f'Название: {self.title}\n'
                f'Приоритет: {self.priority}\n'
                f'Время выполнения: {self.execution_time} минут(ы)\n'
                f'Дата дедлайна: {self.deadline}\n'
                )
    
    