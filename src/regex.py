import re

def extract_markdown_images(text):
    """
    Extracts markdown image syntax ![alt text](image_url) from the given text.
    Returns a list of tuples (alt_text, image_url).
    """
    pattern = r'!\[([^\]]*)\]\(([^)]+)\)'
    matches = re.findall(pattern, text)
    return matches

def extract_markdown_links(text):
    """
    Extracts markdown link syntax [link text](url) from the given text.
    Returns a list of tuples (link_text, url).
    """
    pattern = r'\[([^\]]*)\]\(([^\)]*)\)'
    matches = re.findall(pattern, text)
    return matches


