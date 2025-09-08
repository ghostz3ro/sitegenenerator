from src.htmlnode import LeafNode
import unittest


class TestLeafNode(unittest.TestCase):
    def test_initialization(self):
        node = LeafNode('p', 'Hello, World!', props={"class": "text"})
        assert node.tag == 'p'
        assert node.content == 'Hello, World!'
        assert node.props == {"class": "text"}

    def test_leaf_to_html_p(self):
        node1 = LeafNode("p", "Hello, world!")
        node2 = LeafNode(content="Hello, world!")
        self.assertEqual(node1.to_html(), "<p>Hello, world!</p>")
        self.assertEqual(node2.to_html(), "Hello, world!")

    def test_repr(self):
        node = LeafNode('span', 'Sample Text', props={"style": "color: blue;"})
        expected_repr = "LeafNode(tag=span, content=Sample Text, props={'style': 'color: blue;'})"
        assert repr(node) == expected_repr
