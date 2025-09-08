import unittest
from src.textnode import TextNode, TextType
from src.split_nodes_delimiter import split_nodes_delimiter

class TestSplitNodesDelimiter(unittest.TestCase):
    def test_extract_multiple_images(self):
        from src.regex import extract_markdown_images
        matches = extract_markdown_images("Here is ![img1](url1.png) and ![img2](url2.jpg)")
        self.assertListEqual(matches, [("img1", "url1.png"), ("img2", "url2.jpg")])

    def test_extract_complex_image(self):
        from src.regex import extract_markdown_images
        matches = extract_markdown_images("Text ![alt text with spaces](https://site.com/img.png?query=1&other=2) end")
        self.assertListEqual(matches, [("alt text with spaces", "https://site.com/img.png?query=1&other=2")])

    def test_extract_multiple_links(self):
        from src.regex import extract_markdown_links
        matches = extract_markdown_links("[Google](https://google.com) and [Bing](https://bing.com)")
        self.assertListEqual(matches, [("Google", "https://google.com"), ("Bing", "https://bing.com")])

    def test_extract_complex_link(self):
        from src.regex import extract_markdown_links
        matches = extract_markdown_links("Check [this link with (parentheses)](https://site.com/path_(1)) and [another](https://site.com?q=1&x=2)")
        self.assertListEqual(matches, [
            ("this link with (parentheses)", "https://site.com/path_(1)"),
            ("another", "https://site.com?q=1&x=2")
        ])
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

    def test_extract_markdown_images(self):
        from src.regex import extract_markdown_images
        matches = extract_markdown_images("This is an ![alt](image.png) in text")
        self.assertListEqual(matches, [("alt", "image.png")])

    def test_extract_markdown_links(self):
        from src.regex import extract_markdown_links
        matches = extract_markdown_links("This is a [link](https://example.com) in text")
        self.assertListEqual(matches, [("link", "https://example.com")])

if __name__ == "__main__":
    unittest.main()
