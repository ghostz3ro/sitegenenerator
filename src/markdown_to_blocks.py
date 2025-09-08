

def markdown_to_blocks(markdown_text):
    blocks = markdown_text.split("\n\n")
    markdown_blocks = []
    for block in blocks:
        stripped = block.strip()
        if len(stripped) > 0:
            markdown_blocks.append(stripped)
    return markdown_blocks