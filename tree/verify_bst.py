""" How to verify whether a binary tree is a binary search tree?
    
    from : http://codercareer.blogspot.fr/2012/01/no-31-binary-search-tree-verification.html
"""
from bst import Node, create_nodes, in_traversal, nodes_to_str


def verify(tree, minimum=0):
    """ :returns: True if <tree> is a bst

        :param Node tree: a tree
    """
    is_bst = True

    if tree is not None:
        is_bst, minimum = verify(tree.left, minimum)
        if is_bst:
            is_bst = tree.data > minimum
            if is_bst:
                minimum         = tree.data
                is_bst, minimum = verify(tree.right, minimum)

    return is_bst, minimum


def answer(tree):
    """ :returns: a readable answer

        :param Node tree: a tree
    """
    str_tree = nodes_to_str(tree)
    check, _ = verify(tree)
    is_bst   = "is" if check else "is not"

    list_tree   = in_traversal(tree)
    is_real_bst = (list_tree == sorted(list_tree)) == check

    is_true     = "and it's true" if is_real_bst else "you just found a bug!"

    return "This {} a bst ({})\n{}".format(is_bst, is_true, str_tree)


if __name__ == '__main__':
    print(answer(create_nodes([])))
    print(answer(Node(1, Node(10))))
    print(answer(create_nodes([4, 2, 6, 3, 1, 5, 7])))
