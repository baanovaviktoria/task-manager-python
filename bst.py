class TreeNode:
    """
    Создержит задачу и указатели на потомков.
    """
    def __init__(self, task): 
        self.task = task
        self.left = None
        self.right = None

class DeadlineBST:
    """
    Бинарное дерево поиска, упорядоченное по дате дедлайна задачи (от ранних к поздним).
    """
    def __init__(self): 
        self.root = None

    # Вставка корневого узла
    def insert(self, task): 
        self.root = self._insert(self.root, task)

    # Вставка дочерних узлов
    def _insert(self, node, task): 
        if node is None:
            return TreeNode(task)

        # Сравниваем строки вида "YYYY-MM-DD" для верного хронологического порядка
        if task.deadline < node.task.deadline:
            node.left = self._insert(node.left, task)
        else:
            node.right = self._insert(node.right, task)

        return node
    
    def inorder(self):
        """
        Печатает все задачи, используя лево-корень-право обход.
        """
        self._inorder(self.root)
    
    def _inorder(self, node): 
        """
        Обходит левое поддерево, печатает текущий узел, обходит правое поддерево.
        """
        if node is None:
            return

        self._inorder(node.left)

        print(node.task)

        self._inorder(node.right)

    # Поиск самой ранней задачи (минимального дедлайна)
    def find_earliest(self): 
        if self.root is None:
            return None

        current = self.root

        while current.left:
            current = current.left

        return current.task
    
    # Поиск самой поздней задачи (максимального дедлайна)
    def find_latest(self): 
        if self.root is None:
            return None

        current = self.root

        while current.right:
            current = current.right

        return current.task
