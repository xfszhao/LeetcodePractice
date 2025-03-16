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

    def preorder_print(self, node):
        if not node:
            return
        print(node.val, end=' ')
        self.preorder_print(node.left_child)
        self.preorder_print(node.right_child)

    def preorder_build(self, level_order_serialized_data, curr_index):
        if curr_index >= len(level_order_serialized_data) or level_order_serialized_data[curr_index] is None:
            return None
        left_child_index = curr_index * 2 + 1
        right_child_index = curr_index * 2 + 2
        node = TreeNode(level_order_serialized_data[curr_index])
        node.left_child = self.preorder_build(level_order_serialized_data, left_child_index)
        node.right_child = self.preorder_build(level_order_serialized_data, right_child_index)
        return node

    def print_tree_pre_order(self):
        print("Tree in preorder", end=' ')
        self.preorder_print(self.root)
        print()

    def print_tree_level_order_double_loop(self):
        print("Tree in level order", end=' ')
        q = queue.Queue()
        q.put(self.root)
        while not q.empty():
            qsize = q.qsize()
            print()
            for i in range(qsize):
                node = q.get()
                if not node:
                    print('None', end=' ')
                    continue
                print(node.val, end=' ')
                q.put(node.left_child)
                q.put(node.right_child)
        print()

    def print_tree_level_order_double_queue(self):
        print("Tree in level order", end=' ')
        curr_q = queue.Queue()
        curr_q.put(self.root)
        next_q = queue.Queue()
        while not curr_q.empty():
            node = curr_q.get()
            if node is not None:
                next_q.put(node.left_child)
                next_q.put(node.right_child)
                print(node.val, end=' ')
            else:
                print('None', end=' ')

            if curr_q.empty():
                print()
                curr_q = next_q
                next_q = queue.Queue()
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

    @staticmethod
    def deserialize_level_order_tree_using_preorder_traversal(level_order_serialized_tree):
        binary_tree = BinaryTree()
        if not level_order_serialized_tree:
            return binary_tree

        binary_tree.root = binary_tree.preorder_build(level_order_serialized_tree, curr_index=0)
        return binary_tree

    @staticmethod
    def deserialize_level_order_tree_using_preorder_iteration(level_order_serialized_tree):
        binary_tree = BinaryTree()
        if not level_order_serialized_tree:
            return binary_tree

        curr_index = 0
        binary_tree.root = TreeNode(level_order_serialized_tree[curr_index])
        stack = [(binary_tree.root, curr_index)]
        while stack:
            node, curr_index = stack.pop()
            left_child_index = curr_index * 2 + 1
            right_child_index = curr_index * 2 + 2
            if right_child_index < len(level_order_serialized_tree) \
                    and level_order_serialized_tree[right_child_index] is not None:
                node.right_child = TreeNode(level_order_serialized_tree[right_child_index])
                stack.append((node.right_child, right_child_index))
            if left_child_index < len(level_order_serialized_tree) \
                    and level_order_serialized_tree[left_child_index] is not None:
                node.left_child = TreeNode(level_order_serialized_tree[left_child_index])
                stack.append((node.left_child, left_child_index))

        return binary_tree


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    level_order_serialized_tree = [0, 1, 2, 3, None, 5, None, 7]
    binary_tree = BinaryTreeDeserializer.deserialize_level_order_tree(level_order_serialized_tree)
    binary_tree.print_tree_pre_order()
    binary_tree.print_tree_level_order_double_loop()
    # level_order_serialized_tree = [0, 1, 2, 3]
    binary_tree_built_by_preorder_traversal = \
        BinaryTreeDeserializer.deserialize_level_order_tree_using_preorder_traversal(level_order_serialized_tree)
    binary_tree_built_by_preorder_traversal.print_tree_level_order_double_loop()

    binary_tree_built_by_preorder_iteration = \
        BinaryTreeDeserializer.deserialize_level_order_tree_using_preorder_iteration(level_order_serialized_tree)
    binary_tree_built_by_preorder_iteration.print_tree_level_order_double_queue()


