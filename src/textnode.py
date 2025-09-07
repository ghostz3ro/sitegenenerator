from enum import Enum

class TextType(Enum):
    ANCHOR = "anchor"
    LINK = "link"
    PARAGRAPH = "paragraph"
    HEADING = "heading"

class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = TextType(text_type)
        self.url = url


    def __eq__(self, obj1, obj2):
        if isinstance(obj1, TextNode) and isinstance(obj2, TextNode):
            return obj1.text == obj2.text and obj1.text_type == obj2.text_type and obj1.url == obj2.url
        return False
    
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"

    def __str__(self):
        return self.text