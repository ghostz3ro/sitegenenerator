from src.generate_html_page import extract_title
import unittest

class TestGenerateHtmlPage(unittest.TestCase):
    def test_extract_title(self):
        md = """# My Title
This is some content.
"""
        self.assertEqual(extract_title(md), "My Title")

    def test_extract_title_no_title(self):
        md = """This is some content.
"""
        with self.assertRaises(Exception) as context:
            extract_title(md)
        self.assertEqual(str(context.exception), "No title found in markdown")


    def test_extract_title_multiple_titles(self):
        md = """# First Title
## Second Title
This is some content.
"""
        self.assertEqual(extract_title(md), "First Title")