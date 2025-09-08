from src.regex import extract_markdown_images, extract_markdown_links
import unittest

class TestMarkdownExtraction(unittest.TestCase):

    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_extract_multiple_images(self):
        matches = extract_markdown_images(
            "Here is ![img1](url1.png) and ![img2](url2.jpg)"
        )
        self.assertListEqual([
            ("img1", "url1.png"),
            ("img2", "url2.jpg")
        ], matches)

    def test_extract_complex_image(self):
        matches = extract_markdown_images(
            "Text ![alt text with spaces](https://site.com/img.png?query=1&other=2) end"
        )
        self.assertListEqual([
            ("alt text with spaces", "https://site.com/img.png?query=1&other=2")
        ], matches)

    def test_extract_markdown_links(self):
        matches = extract_markdown_links(
            "This is text with a [link](https://example.com)"
        )
        self.assertListEqual([("link", "https://example.com")], matches)

    def test_extract_multiple_links(self):
        matches = extract_markdown_links(
            "[Google](https://google.com) and [Bing](https://bing.com)"
        )
        self.assertListEqual([
            ("Google", "https://google.com"),
            ("Bing", "https://bing.com")
        ], matches)

    def test_extract_complex_link(self):
        matches = extract_markdown_links(
            "Check [this link with (parentheses)](https://site.com/path_(1)) and [another](https://site.com?q=1&x=2)"
        )
        self.assertListEqual([
            ("this link with (parentheses)", "https://site.com/path_(1)"),
            ("another", "https://site.com?q=1&x=2")
        ], matches)