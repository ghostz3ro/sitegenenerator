import unittest
from src.block_to_block_type import block_to_block_type

class TestBlockToBlockType(unittest.TestCase):
    def test_paragraph(self):
        block = "This is a paragraph."
        self.assertEqual(block_to_block_type(block), "paragraph")

    def test_heading(self):
        block = "# This is a heading"
        self.assertEqual(block_to_block_type(block), "heading")
        block = "### Subheading"
        self.assertEqual(block_to_block_type(block), "heading")

    def test_paragraph(self):
        block = """
        This is a paragraph.
        that spans multiple lines.
        It should still be classified as a paragraph.
        """
        from src.block_to_block_type import BlockType
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)

    def test_heading(self):
        block = "# This is a heading"
        from src.block_to_block_type import BlockType
        self.assertEqual(block_to_block_type(block), BlockType.HEADING)
        block = "### Subheading"
        self.assertEqual(block_to_block_type(block), BlockType.HEADING)

    def test_list(self):
        block = "- item 1\n- item 2"
        from src.block_to_block_type import BlockType
        self.assertEqual(block_to_block_type(block), BlockType.ULIST)
        block = "1. First\n2. Second"
        self.assertEqual(block_to_block_type(block), BlockType.OLIST)

    def test_quote(self):
        block = "> This is a quote\n> that spans multiple lines.\n> It should still be classified as a quote."
        from src.block_to_block_type import BlockType
        self.assertEqual(block_to_block_type(block), BlockType.QUOTE)

    def test_quote_paragraph(self):
        block = "> This is a quote\n> that spans multiple lines.\nbut it now changes to a paragraph.\nand should be classified as a paragraph."

        from src.block_to_block_type import BlockType
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)

    def test_code(self):
        block = "```\ncode here\n```"
        from src.block_to_block_type import BlockType
        self.assertEqual(block_to_block_type(block), BlockType.CODE)

    def test_code(self):
        block = "``` ```"
        from src.block_to_block_type import BlockType
        self.assertEqual(block_to_block_type(block), BlockType.CODE)

    def test_code(self):
        block = "``````"
        from src.block_to_block_type import BlockType
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)