from task import Task
from task_manager import TaskManager
from undo_stack import UndoStack
from execution_queue import ExecutionQueue
from bst import DeadlineBST


manager = TaskManager() # Менеджер для хранения задач и операций над ними
undo_stack = UndoStack() # Стек для поддержки отмены действий
execution_queue = ExecutionQueue() # Очередь для выполнения задач

next_id = 1

def show_menu():
    """
    Отображает главное меню пользователя.
    """
    print("\n~ Менеджер управления задачами ~")

    print("1. Добавить задачу")
    print("2. Показать задачи")
    print("3. Удалить задачу")
    print("4. Изменить задачу")

    print("5. Отменить действие")

    print("6. Добавить задачу в очередь")
    print("7. Выполнить следующую задачу")
    print("8. Показать очередь")

    print("9. Показать задачи по дедлайну")
    print('10. Показать задачи по приоритету')
    print("11. Самый ранний дедлайн")
    print("12. Самый поздний дедлайн")

    print("0. Выход")

while True:

    show_menu()
    
    choice = input("\nВыберите пункт: ")

    # Создание и добавление новой задачи
    if choice == "1":

        title = input("Название: ")
        priority = int(input("Приоритет: "))
        execution_time = int(input("Время выполнения (мин): "))
        deadline = input("Дедлайн (YYYY-MM-DD): ")

        task = Task(
            next_id,
            title,
            priority,
            execution_time,
            deadline
        )

        manager.add_task(task)

        # Сохраняем действие в стек, чтобы было возможно отменить добавление
        undo_stack.push({
            "type": "ADD",
            "task": task
        })

        next_id += 1

        print("Задача добавлена.")

    # Просмотр всех задач
    elif choice == "2":
        manager.show_tasks()

    # Удаление задачи по ID
    elif choice == "3":

        task_id = int(input("Введите ID задачи: "))

        deleted_task = manager.delete_task(task_id)

        if deleted_task:

            # В случае отмены удаления восстанавливаем задачу
            undo_stack.push({
                "type": "DELETE",
                "task": deleted_task
            })

            print("Задача удалена.")

        else:
            print("Задача не найдена.")

    # Редактирование задач
    elif choice == "4":

        task_id = int(input("Введите ID задачи: "))

        task = manager.find_task(task_id)

        if task:

            # Копируем старую версию на случай, если необходимо будет вернуться к оригиналу
            old_copy = task.copy()

            title = input("Новое название: ")
            priority = int(input("Новый приоритет: "))
            execution_time = int(input("Новое время: "))
            deadline = input("Новый дедлайн: ")

            manager.edit_task(
                task_id,
                title,
                priority,
                execution_time,
                deadline
            )

            undo_stack.push({
                "type": "EDIT",
                "old_task": old_copy
            })

            print("Задача изменена.")

        else:
            print("Задача не найдена.")

    # Отмена последнего действия
    elif choice == "5":

        manager.undo(undo_stack)

    # Добавление существующей задачи в очередь выполнения
    elif choice == "6":

        task_id = int(input("Введите ID задачи: "))

        task = manager.find_task(task_id)

        if task:

            # Добавляем в конец очереди
            execution_queue.enqueue(task)

            print("Задача добавлена в очередь.")

        else:

            print("Задача не найдена.")

    # Выполнение задачи из начала очереди
    elif choice == "7":

        completed_task = execution_queue.dequeue()

        if completed_task:

            print("\nВыполнена задача:")
            print(completed_task)

        else:

            print("Очередь пуста.")

    # Просмотр содержимого очереди
    elif choice == "8":

        execution_queue.show_queue()

    # Сортировка задач по дедлайну 
    elif choice == "9":

        tree = DeadlineBST()
        # Создаём бинарное дерево поиска (ключ - дата дедлайна)
        for task in manager.tasks:
            tree.insert(task)

        print("\nЗадачи по возрастанию дедлайна:\n")

        tree.inorder()

    # Сортировка от высшего к низшему
    elif choice == "10":
        sorted_tasks = sorted(manager.tasks, key=lambda task: task.priority, reverse=True)

        print("\nЗадачи по возрастанию приоритета:\n")
        print(sorted_tasks)

    # Поиск задачи с самым ранним (минимальным) дедлайном
    elif choice == "11":

        tree = DeadlineBST()

        for task in manager.tasks:
            tree.insert(task)

        earliest = tree.find_earliest() # Самый левый узел

        if earliest:

            print("\nСамая ранняя задача:\n")
            print(earliest)

        else:

            print("Список задач пуст.")

    # Поиск задачи с самым поздним (максимальным) дедлайном
    elif choice == "12":

        tree = DeadlineBST()

        for task in manager.tasks:
            tree.insert(task)

        latest = tree.find_latest() # Самый правый узел

        if latest:

            print("\nСамая поздняя задача:\n")
            print(latest)

        else:

            print("Список задач пуст.")

    # Выход из программы
    elif choice == "0":

        print("До свидания!")

        break

    # Если команда неизвестна
    else:

        print("Неверный пункт меню.")
