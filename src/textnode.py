from enum import Enum

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
    LIST_ITEM = "list_item"
    ORDERED_LIST_ITEM = "ordered_list_item"
    UNORDERED_LIST_ITEM = "unordered_list_item"

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