import math
import queue

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left_child = self.right_child = None

    def is_null(self):
        return not self.val

class BinaryTree:
    def __init__(self):
        self.root = None

    def preorder(self, node):
        if not node:
            return
        print(node.val, end=' ')
        self.preorder(node.left_child)
        self.preorder(node.right_child)

    def print_tree_pre_order(self):
        print("Tree in preorder", end=' ')
        self.preorder(self.root)
        print()

    def print_tree_level_order(self):
        print("Tree in level order", end=' ')
        q = queue.Queue()
        q.put(self.root)
        while not q.empty():
            qsize = q.qsize()
            for i in range(qsize):
                node = q.get()
                if not node:
                    print('None', end=' ')
                    continue
                print(node.val, end=' ')
                q.put(node.left_child)
                q.put(node.right_child)
        print()

class BinaryTreeDeserializer:

    @staticmethod
    def is_full_binary_tree(serialized_tree):
        def is_integer(x):
            return x == int(x)
        num_nodes = len(serialized_tree)
        return is_integer(math.log2(num_nodes + 1))

    @staticmethod
    def get_binary_tree_height(serialized_tree):
        num_nodes = len(serialized_tree)
        return math.log2(num_nodes + 1)

    @staticmethod
    def deserialize_pre_order_tree(serialized_tree):
        # ... your deserialization logic for preorder ...
        root_of_tree = TreeNode()
        return root_of_tree

    @staticmethod
    def deserialize_level_order_tree(serialized_tree):
        binary_tree = BinaryTree()
        if not serialized_tree:
            return binary_tree

        assert BinaryTreeDeserializer.is_full_binary_tree(serialized_tree), "Error: input serialized_tree is not full!"

        index = 0
        binary_tree.root = TreeNode(serialized_tree[index])
        q = queue.Queue()
        q.put(binary_tree.root)
        num_nodes = len(serialized_tree)
        while not q.empty():
            qsize = q.qsize()
            for i in range(qsize):
                node = q.get()
                left_child_index = index * 2 + 1
                right_child_index = index * 2 + 2
                left_child = TreeNode(serialized_tree[left_child_index]) \
                    if left_child_index < num_nodes and serialized_tree[left_child_index] else None
                right_child = TreeNode(serialized_tree[right_child_index]) \
                    if right_child_index < num_nodes and serialized_tree[right_child_index] else None
                if left_child:
                    node.left_child = left_child
                    q.put(left_child)
                if right_child:
                    q.put(right_child)
                    node.right_child = right_child
                index += 1

        return binary_tree


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    serialized_tree_1 = [0, 1, 2, 3, None, 5, None]
    binary_tree = BinaryTreeDeserializer.deserialize_level_order_tree(serialized_tree_1)
    binary_tree.print_tree_pre_order()
    binary_tree.print_tree_level_order()


