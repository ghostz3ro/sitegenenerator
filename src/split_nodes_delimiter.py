from src.textnode import TextNode, TextType

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    """
    Splits text nodes in old_nodes by the given delimiter and assigns text_type to the delimited text.
    Returns a new list of nodes.
    """
    new_nodes = []
    for node in old_nodes:
        # Only split TextType.TEXT nodes
        if not isinstance(node, TextNode) or node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        text = node.text
        parts = text.split(delimiter)
        # If no delimiter found, keep node as is
        if len(parts) == 1:
            new_nodes.append(node)
            continue
        # Odd number of parts means delimiters are matched
        if len(parts) % 2 == 0:
            raise Exception(f"Invalid Markdown syntax: unmatched delimiter '{delimiter}' in '{text}'")
        for i, part in enumerate(parts):
            if part == "":
                continue
            if i % 2 == 0:
                new_nodes.append(TextNode(part, TextType.TEXT))
            else:
                new_nodes.append(TextNode(part, text_type))
    return new_nodes

def split_nodes_image(old_nodes):
    """
    Splits text nodes in old_nodes by markdown image syntax ![alt](url) and assigns TextType.IMAGE to the image text.
    Returns a new list of nodes.
    """
    new_nodes = []
    for node in old_nodes:
        # Only split TextType.TEXT nodes
        if not isinstance(node, TextNode) or node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        text = node.text
        parts = text.split("![")
        if len(parts) == 1:
            new_nodes.append(node)
            continue
        for i, part in enumerate(parts):
            if part == "":
                continue
            if i == 0:
                new_nodes.append(TextNode(part, TextType.TEXT))
            else:
                if "](" in part:
                    alt_text, rest = part.split("](", 1)
                    if ")" in rest:
                        url, remaining = rest.split(")", 1)
                        new_nodes.append(TextNode(alt_text, TextType.IMAGE))
                        new_nodes.append(TextNode(url, TextType.IMAGE))
                        if remaining:
                            new_nodes.append(TextNode(remaining, TextType.TEXT))
                    else:
                        raise Exception(f"Invalid Markdown syntax: unmatched ')' in '{text}'")
                else:
                    raise Exception(f"Invalid Markdown syntax: unmatched '](' in '{text}'")
    return new_nodes

def split_nodes_link(old_nodes):
    """
    Splits text nodes in old_nodes by markdown link syntax [text](url) and assigns TextType.LINK to the link text.
    Returns a new list of nodes.
    """
    new_nodes = []
    for node in old_nodes:
        # Only split TextType.TEXT nodes
        if not isinstance(node, TextNode) or node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        text = node.text
        parts = text.split("[")
        if len(parts) == 1:
            new_nodes.append(node)
            continue
        for i, part in enumerate(parts):
            if part == "":
                continue
            if i == 0:
                new_nodes.append(TextNode(part, TextType.TEXT))
            else:
                if "](" in part:
                    link_text, rest = part.split("](", 1)
                    if ")" in rest:
                        url, remaining = rest.split(")", 1)
                        new_nodes.append(TextNode(link_text, TextType.LINK))
                        new_nodes.append(TextNode(url, TextType.LINK))
                        if remaining:
                            new_nodes.append(TextNode(remaining, TextType.TEXT))
                    else:
                        raise Exception(f"Invalid Markdown syntax: unmatched ')' in '{text}'")
                else:
                    raise Exception(f"Invalid Markdown syntax: unmatched '](' in '{text}'")
    return new_nodes