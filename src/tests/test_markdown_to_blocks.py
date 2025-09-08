import unittest
from src.markdown_to_blocks import markdown_to_blocks


class TestMarkdownToBlocks(unittest.TestCase):
    def test_text_with_extra_whitespace(self):
        md = "\n\n   This is a block with leading whitespace.\n\n\nAnother block after extra newlines.   \n\n"
        blocks = markdown_to_blocks(md)
        self.assertEqual(blocks, [
            "This is a block with leading whitespace.",
            "Another block after extra newlines."
        ])
    def test_empty_input(self):
        md = ""
        blocks = markdown_to_blocks(md)
        self.assertEqual(blocks, [])

    def test_whitespace_and_newlines(self):
        md = "\n\n   \n\n"
        blocks = markdown_to_blocks(md)
        self.assertEqual(blocks, [])


    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        print(blocks)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )