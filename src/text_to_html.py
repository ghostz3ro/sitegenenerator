from src.textnode import TextType
from src.htmlnode import HtmlNode
from src.leafnode import LeafNode

def textnode_to_htmlnode(text_node):
    if text_node.text_type == TextType.ANCHOR:
        return text_node.text
    elif text_node.text_type == TextType.LINK:
        return HtmlNode("a", text_node.text, props={"href": text_node.url})
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
        return HtmlNode("img", "", {"src": text_node.url, "alt": text_node.text})
    else:
        raise ValueError(f"Unknown node type: {text_node.text_type}")