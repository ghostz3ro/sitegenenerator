from enum import Enum
from htmlnode import HtmlNode, LeafNode

class TextType(Enum):
    ANCHOR = "anchor"
    LINK = "link"
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    BOLD = "bold"
    ITALIC = "italic"
    UNDERLINE = "underline"
    STRIKETHROUGH = "strikethrough"
    CODE = "code"
    QUOTE = "quote"
    ORDERED_LIST_ITEM = "ordered_list_item"
    UNORDERED_LIST_ITEM = "unordered_list_item"
    TEXT = "text"
    IMAGE = "image"

class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = TextType(text_type)
        self.url = url


    def __eq__(self, obj2):
        if isinstance(self, TextNode) and isinstance(obj2, TextNode):
            return self.text == obj2.text and self.text_type == obj2.text_type and self.url == obj2.url
        return False
    
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"

    def __str__(self):
        return self.text
    

def textnode_to_htmlnode(text_node):
    if text_node.text_type == TextType.ANCHOR:
        return text_node.text
    elif text_node.text_type == TextType.LINK:
        return LeafNode("a", text_node.text, props={"href": text_node.url})
    elif text_node.text_type == TextType.BOLD:
        return LeafNode("b", text_node.text)
    elif text_node.text_type == TextType.ITALIC:
        return LeafNode("i", text_node.text)
    elif text_node.text_type == TextType.UNDERLINE:
        return LeafNode("u", text_node.text)
    elif text_node.text_type == TextType.STRIKETHROUGH:
        return LeafNode("s", text_node.text)
    elif text_node.text_type == TextType.CODE:
        return LeafNode("code", text_node.text)
    elif text_node.text_type == TextType.QUOTE:
        return LeafNode("blockquote", text_node.text)
    elif text_node.text_type == TextType.PARAGRAPH:
        return LeafNode("p", text_node.text)
    elif text_node.text_type == TextType.HEADING:
        return LeafNode("h1", text_node.text)
    elif text_node.text_type == TextType.ORDERED_LIST_ITEM:
        return LeafNode("li", text_node.text)
    elif text_node.text_type == TextType.UNORDERED_LIST_ITEM:
        return LeafNode("li", text_node.text)
    elif text_node.text_type == TextType.TEXT:
        return LeafNode(content=text_node.text)
    elif text_node.text_type == TextType.IMAGE:
        return LeafNode("img", "", props={"src": text_node.url, "alt": text_node.text})
    else:
        raise ValueError(f"Unknown node type: {text_node.text_type}")