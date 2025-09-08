from src.textnode import TextNode, TextType
from src.regex import extract_markdown_images, extract_markdown_links
from src.split_nodes_delimiter import split_nodes_delimiter

def text_to_textnodes(text):
    # 1. Extract images and links first
    image_nodes = [TextNode(alt, TextType.IMAGE, url) for alt, url in extract_markdown_images(text)]
    link_nodes = [TextNode(label, TextType.LINK, url) for label, url in extract_markdown_links(text)]

    # 2. Remove image and link markdown from text
    import re
    text_no_img = re.sub(r'!\[[^\]]*\]\([^)]*\)', '', text)
    text_no_link = re.sub(r'\[[^\]]*\]\([^)]*\)', '', text_no_img)
    text_clean = text_no_link.strip()

    # 3. Split remaining text with delimiter functions
    nodes = [TextNode(text_clean, TextType.TEXT)] if text_clean else []
    nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)
    nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)
    nodes = split_nodes_delimiter(nodes, "_", TextType.ITALIC)
    nodes = split_nodes_delimiter(nodes, "~", TextType.STRIKETHROUGH)
    nodes = split_nodes_delimiter(nodes, "__", TextType.UNDERLINE)
    nodes = split_nodes_delimiter(nodes, ">", TextType.QUOTE)
    nodes = split_nodes_delimiter(nodes, "\n", TextType.PARAGRAPH)

    # 4. Combine all nodes
    # Only add non-empty text nodes
    non_empty_nodes = [n for n in nodes if n.text.strip()]
    final_nodes = image_nodes + link_nodes + non_empty_nodes
    return final_nodes
