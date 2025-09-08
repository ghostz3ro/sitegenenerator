from src.parentnode import ParentNode
from src.leafnode import LeafNode
import unittest

class TestParentNode(unittest.TestCase):
    def test_initialization(self):
        child1 = LeafNode('p', 'Child 1')
        child2 = LeafNode('p', 'Child 2')
        node = ParentNode('div', [child1, child2], props={"class": "container"})
        self.assertEqual(node.tag, 'div')
        self.assertEqual(node.children, [child1, child2])
        self.assertEqual(node.props, {"class": "container"})

    def test_to_html(self):
        child1 = LeafNode('p', 'Child 1')
        child2 = LeafNode('p', 'Child 2')
        node = ParentNode('div', [child1, child2])
        expected_html = "<div><p>Child 1</p><p>Child 2</p></div>"
        self.assertEqual(node.to_html(), expected_html)

    def test_to_html_no_tag(self):
        child = LeafNode('p', 'Child')
        node = ParentNode(None, [child])
        with self.assertRaises(ValueError) as context:
            node.to_html()
        self.assertEqual(str(context.exception), "tag must be defined for ParentNode")

    def test_to_html_no_children(self):
        node = ParentNode('div', [])
        with self.assertRaises(ValueError) as context:
            node.to_html()
        self.assertEqual(str(context.exception), "children must be defined for ParentNode")

    def test_repr(self):
        child = LeafNode('p', 'Child')
        node = ParentNode('div', [child], props={"class": "container"})
        expected_repr = "ParentNode(tag=div, children=[LeafNode(tag=p, content=Child, props={})], props={'class': 'container'})"
        self.assertEqual(repr(node), expected_repr)

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span><b>grandchild</b></span></div>")

    def test_repr(self):
        child_node = LeafNode("span", "child")
        child_node2 = LeafNode("span", "child2")
        parent_node = ParentNode("div", [child_node, child_node2], props={"class": "container"})
        expected_repr = "ParentNode(tag=div, children=[LeafNode(tag=span, content=child, props={}), LeafNode(tag=span, content=child2, props={})], props={'class': 'container'})"
        self.assertEqual(repr(parent_node), expected_repr)