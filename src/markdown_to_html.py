from src.markdown_to_blocks import markdown_to_blocks
from src.block_to_block_type import block_to_block_type
from src.htmlnode import LeafNode, ParentNode
from src.text_to_textnodes import text_to_textnodes
from src.textnode import textnode_to_htmlnode

def markdown_to_html_node(markdown: str) -> str:
    # Implementation of markdown to HTML conversion
    markdown_blocks = markdown_to_blocks(markdown)
    nodes = []
    for block in markdown_blocks:
        block_type = block_to_block_type(block)
        if block_type.value == "heading":
            nodes.append(heading_to_html(block))
        elif block_type.value == "paragraph":
            nodes.append(paragraph_to_html(block))
        elif block_type.value == "unordered_list":
            nodes.append(unordered_list_to_html(block))
        elif block_type.value == "ordered_list":
            nodes.append(ordered_list_to_html(block))
        elif block_type.value == "quote":
            nodes.append(quote_to_html(block))
        elif block_type.value == "code":
            nodes.append(code_to_html(block))
        else:
            raise Exception(f"Unknown block type: {block_type}")
    return ParentNode("div", nodes)

def text_to_children(text):
    text_nodes = text_to_textnodes(text)
    html_nodes = [textnode_to_htmlnode(node) for node in text_nodes]
    return html_nodes

def heading_to_html(block: str) -> str:
    heading_level = len(block.split(" ")[0])
    tag = f"h{heading_level}"
    content = block[heading_level+1:].strip()
    children = text_to_children(content)
    return ParentNode(tag, children)

def paragraph_to_html(block: str) -> str:
    # Join lines and strip whitespace for paragraphs
    content = " ".join([line.strip() for line in block.splitlines() if line.strip()])
    children = text_to_children(content)
    return ParentNode("p", children)

def unordered_list_to_html(block: str) -> str:
    lines = [line.lstrip("- ") for line in block.split("\n") if line.strip()]
    children = [ParentNode("li", text_to_children(line)) for line in lines]
    return ParentNode("ul", children)

def ordered_list_to_html(block: str) -> str:
    lines = [line.split(". ", 1)[1] if ". " in line else line for line in block.split("\n") if line.strip()]
    children = [ParentNode("li", text_to_children(line)) for line in lines]
    return ParentNode("ol", children)

def quote_to_html(block: str) -> str:
    # Remove leading '>' and any whitespace
    content = block.lstrip('> ').strip()
    children = text_to_children(content)
    return ParentNode("blockquote", children)

def code_to_html(block: str) -> str:
    # Remove triple backticks and leading/trailing whitespace
    import textwrap
    code_content = block.strip()
    if code_content.startswith("```") and code_content.endswith("```"):
        code_content = code_content[3:-3]
    # Remove leading/trailing newlines and dedent
    code_content = code_content.strip("\n")
    code_content = textwrap.dedent(code_content)
    if not code_content.endswith("\n"):
        code_content += "\n"
    return ParentNode("pre", [ParentNode("code", [LeafNode(None, code_content)])])