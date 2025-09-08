from src.textnode import TextNode, TextType, textnode_to_htmlnode
import unittest

class TestTextNodeToHtmlNode(unittest.TestCase):

    def test_textnode_to_htmlnode(self):
        # Test conversion of a link TextNode to an HtmlNode
        text_node = TextNode("Click here", "link", "https://example.com")
        html_node = textnode_to_htmlnode(text_node)
        assert html_node.tag == "a"
        assert html_node.props_to_html() == 'href="https://example.com"'
        # print(html_node.content, html_node.tag, html_node.props)

        # Test conversion of a paragraph TextNode to an HtmlNode
        text_node = TextNode("This is a paragraph.", "paragraph")
        html_node = textnode_to_htmlnode(text_node)
        assert html_node.tag == "p"
        assert html_node.props == {}

        # Test conversion of a heading TextNode to an HtmlNode
        text_node = TextNode("This is a heading", "heading")
        html_node = textnode_to_htmlnode(text_node)
        assert html_node.tag == "h1"
        assert html_node.props == {}


        # Test conversion of an italic TextNode to an HtmlNode
        text_node = TextNode("Italic text", "italic")
        html_node = textnode_to_htmlnode(text_node)
        assert html_node.tag == "i"
        assert html_node.props == {}


        # Test conversion of an underline TextNode to an HtmlNode
        text_node = TextNode("Underline text", "underline")
        html_node = textnode_to_htmlnode(text_node)
        assert html_node.tag == "u"
        assert html_node.props == {}


    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = textnode_to_htmlnode(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.content, "This is a text node")