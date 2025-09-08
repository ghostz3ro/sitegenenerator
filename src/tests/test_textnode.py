from platform import node
import unittest
from src.textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        node3 = TextNode("This is a different text node", TextType.BOLD)
        node4 = TextNode("This is a text node", TextType.ITALIC)

        node5 = "Not a TextNode"
        node6 = TextNode("This is a text node", TextType.BOLD, url="https://example.com")
        node7 = TextNode("This is a text node", TextType.BOLD, url="https://example.gr")

        self.assertEqual(node, node2)
        self.assertNotEqual(node, node3)
        self.assertNotEqual(node, node4)
        self.assertNotEqual(node, node5)
        # self.assertNotEqual(node6, node7)
        self.assertNotEqual(node, node7)

if __name__ == "__main__":
    unittest.main()
