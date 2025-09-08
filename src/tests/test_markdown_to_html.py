from src.markdown_to_html import markdown_to_html_node
import unittest

class TestMarkdownToHtml(unittest.TestCase):

    def test_paragraph(self):
        md = "This is a simple paragraph with **bold** and _italic_."
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
        html,
        "<div><p>This is a simple paragraph with <b>bold</b> and <i>italic</i>.</p></div>",
    )

    def test_unordered_list(self):
        md = "- Item 1\n- **Item 2**\n- Item with _italic_"
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ul><li>Item 1</li><li><b>Item 2</b></li><li>Item with <i>italic</i></li></ul></div>",
        )

    def test_ordered_list(self):
        md = "1. First item\n2. Second item with **bold**\n3. Third item"
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ol><li>First item</li><li>Second item with <b>bold</b></li><li>Third item</li></ol></div>",
        )

    def test_quote(self):
        md = "> This is a quote with _italic_ and **bold**."
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><blockquote>This is a quote with <i>italic</i> and <b>bold</b>.</blockquote></div>",
        )
    # testing quote without space after >
    def test_quote_no_space(self):
        md = ">This is a quote with _italic_ and **bold**."
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><blockquote>This is a quote with <i>italic</i> and <b>bold</b>.</blockquote></div>",
        )

    def test_paragraphs(self):
        md = """
    This is **bolded** paragraph
    text in a p
    tag here

    This is another paragraph with _italic_ text and `code` here

    """

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )

    def test_codeblock(self):
        md = """
    ```
    This is text that _should_ remain
    the **same** even with inline stuff
    ```
    """

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
        )

    # Only test code block output here
