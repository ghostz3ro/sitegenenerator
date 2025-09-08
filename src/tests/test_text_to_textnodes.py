import unittest
from src.text_to_textnodes import text_to_textnodes
from src.textnode import TextType

class TestTextToTextNodes(unittest.TestCase):
	def test_plain_text(self):
		nodes = text_to_textnodes("Just some text.")
		self.assertEqual(len(nodes), 1)
		self.assertEqual(nodes[0].text, "Just some text.")
		self.assertEqual(nodes[0].text_type, TextType.TEXT)

	def test_code_and_bold(self):
		nodes = text_to_textnodes("This is `code` and **bold** text.")
		texts = [n.text for n in nodes]
		types = [n.text_type for n in nodes]
		self.assertIn("code", texts)
		self.assertIn("bold", texts)
		self.assertIn(TextType.CODE, types)
		self.assertIn(TextType.BOLD, types)

	def test_image_and_link(self):
		nodes = text_to_textnodes("Here is ![img](url.png) and [Google](https://google.com)")
		self.assertTrue(any(n.text == "img" and n.text_type == TextType.IMAGE and n.url == "url.png" for n in nodes))
		self.assertTrue(any(n.text == "Google" and n.text_type == TextType.LINK and n.url == "https://google.com" for n in nodes))

	def test_nested_formatting(self):
		nodes = text_to_textnodes("**bold and _italic_** text")
		texts = [n.text for n in nodes]
		types = [n.text_type for n in nodes]
		# Current behavior: only outermost formatting is split
		self.assertIn("bold and _italic_", texts)
		self.assertIn(" text", texts)
		self.assertIn(TextType.BOLD, types)

	def test_multiple_images_and_links(self):
		nodes = text_to_textnodes("![img1](url1.png) [Link1](url1.com) ![img2](url2.jpg) [Link2](url2.com)")
		self.assertTrue(any(n.text == "img1" and n.url == "url1.png" for n in nodes))
		self.assertTrue(any(n.text == "img2" and n.url == "url2.jpg" for n in nodes))
		self.assertTrue(any(n.text == "Link1" and n.url == "url1.com" for n in nodes))
		self.assertTrue(any(n.text == "Link2" and n.url == "url2.com" for n in nodes))

	def test_edge_case_empty(self):
		nodes = text_to_textnodes("")
		self.assertEqual(nodes, [])

	def test_edge_case_only_image(self):
		nodes = text_to_textnodes("![alt](img.png)")
		image_nodes = [n for n in nodes if n.text_type == TextType.IMAGE]
		self.assertEqual(len(image_nodes), 1)
		self.assertEqual(image_nodes[0].text, "alt")
		self.assertEqual(image_nodes[0].url, "img.png")
		self.assertEqual(image_nodes[0].text_type, TextType.IMAGE)

	def test_edge_case_only_link(self):
		nodes = text_to_textnodes("[label](url.com)")
		self.assertEqual(len(nodes), 1)
		self.assertEqual(nodes[0].text, "label")
		self.assertEqual(nodes[0].url, "url.com")
		self.assertEqual(nodes[0].text_type, TextType.LINK)

if __name__ == "__main__":
	unittest.main()
