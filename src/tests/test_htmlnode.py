from src.htmlnode import HtmlNode
import unittest

class TestHtmlNode(unittest.TestCase):
    def test_initialization(self):
        node = HtmlNode('div', {'class': 'container'}, props={"href": "https://www.google.com","target": "_blank",})
        self.assertEqual(node.tag, 'div')
        self.assertEqual(node.content, {'class': 'container'})
        self.assertEqual(node.props, {"href": "https://www.google.com","target": "_blank",})
        self.assertEqual(node.children, [])

    def test_repr(self):
        node = HtmlNode('span', {'id': 'text'}, props={"style": "color: red;"})
        expected_repr = "HtmlNode(tag=span, content={'id': 'text'}, children=[], props={'style': 'color: red;'})"
        self.assertEqual(repr(node), expected_repr)

    def test_props_to_html(self):
        node = HtmlNode('a', props={"href": "https://www.google.com","target": "_blank",})
        expected_html = 'href="https://www.google.com" target="_blank"'
        self.assertEqual(node.props_to_html(), expected_html)