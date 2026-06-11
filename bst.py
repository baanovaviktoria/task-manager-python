class TreeNode:
    def __init__(self, task): # инициализация создания узла
        self.task = task
        self.left = None
        self.right = None

class DeadlineBST:
    def __init__(self): # инициализация создания бинарного дерева поиска
        self.root = None

    def insert(self, task): # вставка корневого узла
        self.root = self._insert(self.root, task)

    def _insert(self, node, task): # вставка дочерних узлов
        if node is None:
            return TreeNode(task)

        if task.deadline < node.task.deadline:
            node.left = self._insert(node.left, task)
        else:
            node.right = self._insert(node.right, task)

        return node
    
    def inorder(self): # симметричный обход от корня
        self._inorder(self.root)
    
    def _inorder(self, node): # механизм симметричного обхода
        if node is None:
            return

        self._inorder(node.left)

        print(node.task)

        self._inorder(node.right)

    def find_earliest(self): # поиск самой ранней задачи
        if self.root is None:
            return None

        current = self.root

        while current.left:
            current = current.left

        return current.task
    
    def find_latest(self): # поиск самой поздней задачи
        if self.root is None:
            return None

        current = self.root

        while current.right:
            current = current.right

        return current.task