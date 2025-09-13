from textnode import TextNode, TextType
from regex import extract_markdown_images, extract_markdown_links
from split_nodes_delimiter import split_nodes_delimiter
import re

def text_to_textnodes(text):
    # Start with a single text node
    nodes = [TextNode(text, TextType.TEXT)]

    # Process images first (since they have ! prefix)
    nodes = split_nodes_image(nodes)

    # Process links
    nodes = split_nodes_link(nodes)

    # Process other formatting
    nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)
    nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)
    nodes = split_nodes_delimiter(nodes, "_", TextType.ITALIC)
    nodes = split_nodes_delimiter(nodes, "~", TextType.STRIKETHROUGH)
    nodes = split_nodes_delimiter(nodes, "__", TextType.UNDERLINE)

    return nodes

def split_nodes_image(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue

        images = extract_markdown_images(node.text)
        if not images:
            new_nodes.append(node)
            continue

        current_text = node.text
        for alt_text, url in images:
            image_markdown = f"![{alt_text}]({url})"
            parts = current_text.split(image_markdown, 1)

            if len(parts) == 2:
                # Add text before image if it exists
                if parts[0]:
                    new_nodes.append(TextNode(parts[0], TextType.TEXT))

                # Add image node
                new_nodes.append(TextNode(alt_text, TextType.IMAGE, url))

                # Continue with remaining text
                current_text = parts[1]

        # Add any remaining text
        if current_text:
            new_nodes.append(TextNode(current_text, TextType.TEXT))

    return new_nodes

def split_nodes_link(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue

        links = extract_markdown_links(node.text)
        if not links:
            new_nodes.append(node)
            continue

        current_text = node.text
        for link_text, url in links:
            link_markdown = f"[{link_text}]({url})"
            parts = current_text.split(link_markdown, 1)

            if len(parts) == 2:
                # Add text before link if it exists
                if parts[0]:
                    new_nodes.append(TextNode(parts[0], TextType.TEXT))

                # Add link node
                new_nodes.append(TextNode(link_text, TextType.LINK, url))

                # Continue with remaining text
                current_text = parts[1]

        # Add any remaining text
        if current_text:
            new_nodes.append(TextNode(current_text, TextType.TEXT))

    return new_nodes
