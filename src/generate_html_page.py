
import os
from markdown_to_html import markdown_to_html_node

def extract_title(markdown):
    for line in markdown.split("\n"):
        if line.startswith("# "):
            return line[2:].strip()
    raise Exception("No title found in markdown")

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using template {template_path}")
    with open(from_path, "r", encoding="utf-8") as f:
        markdown = f.read()
    with open(template_path, "r", encoding="utf-8") as f:
        template = f.read()
    html_markdown = markdown_to_html_node(markdown).to_html()
    title = extract_title(markdown)
    html_content = template.replace("{{ Title }}", title).replace("{{ Content }}", html_markdown)
    # print(html_content)
    os.makedirs(os.path.dirname(dest_path), exist_ok=True)
    print(f"Writing to {dest_path}")
    with open(dest_path, "w", encoding="utf-8") as f:
        f.write(html_content)
        f.close()
    return

def generate_pages_recursive(from_path, template_path, dest_path):
    print(f"Generating pages recursively from {from_path} to {dest_path} using template {template_path}")
    print(f'checking path {from_path}')
    if os.path.exists(from_path):
        print("path exists")
        print(f'path contents: {os.listdir(from_path)}')
        
        for entry in os.listdir(from_path):
            print(f'checking entry {entry}')
            if entry.endswith(".md"): # and os.path.isfile(entry):
                print('is file true')
                print(f"Processing file {entry}")
                dest_file = entry[:-3] + ".html"
                generate_page(os.path.join(from_path, entry), template_path, os.path.join(dest_path, dest_file))
            else:
                print('is dir true')
                generate_pages_recursive(os.path.join(from_path, entry), template_path, os.path.join(dest_path, entry))
    else:
        raise Exception(f"Folder {from_path} does not exist")
    print(f"Finished generating pages from {from_path} to {dest_path}")