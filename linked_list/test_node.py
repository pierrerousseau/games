import unittest

from .node import List, Node, add_to_nodes, create_nodes, nodes_to_str, \
    remove_from_nodes


class TestNode(unittest.TestCase):

    def setUp(self):
        pass

    def test_node_to_string_1(self):
        """ str(node): the str representation of the data of the node
        """ 
        self.assertEquals(str(Node("first")), "first")

    def test_node_to_string_2(self):
        """ str(node): not any str representation 
        """ 
        self.assertNotEquals(str(Node("real first")), "last")

    def test_nodes_to_str(self):
        """ nodes_to_str: convert a linked list to a string
        """
        nodes = Node("h", Node("e", Node("l", Node("l", Node("o")))))

        self.assertEquals(nodes_to_str(nodes), "hello")

    def test_create_nodes(self):
        """ create_nodes: create a linked list from a python list
        """
        self.assertEquals((nodes_to_str(create_nodes(list("hello")))), "hello")
        self.assertEquals((str(List(list("hello")))), "hello")


    def test_add_to_nodes_1(self):
        """ add_to_nodes: add a node at the end of a list of nodes
        """
        nodes = Node("h", Node("e", Node("l", Node("l", Node("o")))))
        node  = Node("!")

        linked_list = List(list("hello"))
        linked_list.add(node)

        self.assertEquals(nodes_to_str(add_to_nodes(nodes, node)), "hello!")
        self.assertEquals(str(linked_list), "hello!")


    def test_add_to_nodes_2(self):
        """ add_to_nodes: add a node at the begining of a list of nodes
        """
        nodes = Node("h", Node("e", Node("l", Node("l", Node("o")))))
        node  = Node("!")

        linked_list = List(list("hello"))
        linked_list.add(node, True)

        self.assertEquals(nodes_to_str(add_to_nodes(nodes, node, True)), 
                          "!hello")
        self.assertEquals(str(linked_list), "!hello")

    def test_remove_from_nodes_1(self):
        """ remove_from_nodes: remove last node from a list of nodes
        """
        nodes = Node("h", Node("e", Node("l", Node("l", Node("o")))))
        data  = "o"

        linked_list = List(list("hello"))
        linked_list.remove(data)

        self.assertEquals(nodes_to_str(remove_from_nodes(nodes, data)), 
                          "hell")
        self.assertEquals(str(linked_list), "hell")


    def test_remove_from_nodes_2(self):
        """ remove_from_nodes: remove first node from a list of nodes
        """
        nodes = Node("h", Node("e", Node("l", Node("l", Node("o")))))
        data  = "h"

        linked_list = List(list("hello"))
        linked_list.remove(data)

        self.assertEquals(nodes_to_str(remove_from_nodes(nodes, data)), 
                          "ello")
        self.assertEquals(str(linked_list), "ello")


    def test_remove_from_nodes_3(self):
        """ remove_from_nodes: remove multiple nodes from a list of nodes
        """
        nodes = Node("h", Node("e", Node("l", Node("l", Node("o")))))
        data  = "l"

        linked_list = List(list("hello"))
        linked_list.remove(data, False)

        self.assertEquals(nodes_to_str(remove_from_nodes(nodes, data, False)), 
                          "heo")
        self.assertEquals(str(linked_list), "heo")

    def test_remove_from_nodes_4(self):
        """ remove_from_nodes: remove a node from a list of nodes
        """
        nodes = Node("h", Node("e", Node("l", Node("l", Node("o")))))
        data  = "e"

        linked_list = List(list("hello"))
        linked_list.remove(data)

        self.assertEquals(nodes_to_str(remove_from_nodes(nodes, data)), 
                          "hllo")
        self.assertEquals(str(linked_list), "hllo")

    def test_remove_from_nodes_5(self):
        """ remove_from_nodes: remove a node from an empty list
        """
        nodes = None
        data  = "e"

        linked_list = List(list([]))
        linked_list.remove(data)

        self.assertEquals(nodes_to_str(remove_from_nodes(nodes, data)), "")
        self.assertEquals(str(linked_list), "")

    def test_remove_from_nodes_6(self):
        """ remove_from_nodes: remove the only element of a list
        """
        nodes = Node("e")
        data  = "e"

        linked_list = List(list(["e"]))
        linked_list.remove(data)

        self.assertEquals(nodes_to_str(remove_from_nodes(nodes, data)), "")
        self.assertEquals(str(linked_list), "")



if __name__ == '__main__':
    unittest.main()
