import unittest
from src.textnode import TextNode, TextType
from src.split_nodes_delimiter import split_nodes_delimiter

class TestSplitNodesDelimiter(unittest.TestCase):
    def test_bold_delimiter(self):
        node = TextNode("This is **bold** text", TextType.TEXT)
        result = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(
            [n.text for n in result],
            ["This is ", "bold", " text"]
        )
        self.assertEqual(
            [n.text_type for n in result],
            [TextType.TEXT, TextType.BOLD, TextType.TEXT]
        )


    def test_italic_delimiter(self):
        node = TextNode("This is _italic_ text", TextType.TEXT)
        result = split_nodes_delimiter([node], "_", TextType.ITALIC)
        self.assertEqual(
            [n.text for n in result],
            ["This is ", "italic", " text"]
        )
        self.assertEqual(
            [n.text_type for n in result],
            [TextType.TEXT, TextType.ITALIC, TextType.TEXT]
        )

    def test_quote_delimiter(self):
        node = TextNode(">This is a quote\nThis is normal text", TextType.TEXT)
        lines = node.text.split("\n")
        result = []
        for line in lines:
            if line.startswith(">"):
                quote_text = line[1:].lstrip()
                result.append(TextNode(quote_text, TextType.QUOTE))
            else:
                result.append(TextNode(line, TextType.TEXT))
        self.assertEqual([n.text_type for n in result], [TextType.QUOTE, TextType.TEXT])
        self.assertEqual([n.text_type for n in result], [TextType.QUOTE, TextType.TEXT])

    def test_no_delimiter(self):
        node = TextNode("No delimiter here", TextType.TEXT)
        result = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(result, [node])

    def test_non_text_node(self):
        node = TextNode("Not text", TextType.CODE)
        result = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(result, [node])

    def test_unmatched_delimiter(self):
        node = TextNode("Unmatched `delimiter", TextType.TEXT)
        with self.assertRaises(Exception):
            split_nodes_delimiter([node], "`", TextType.CODE)

if __name__ == "__main__":
    unittest.main()
