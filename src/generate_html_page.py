import os
from markdown_to_html import markdown_to_html_node
import shutil

def copy_to_directory(src, dest):
    
    if not os.path.exists(src):
        raise Exception(f"Source directory '{src}' does not exist.")
    if len(os.listdir(src)) == 0:
        raise Exception(f"Source directory '{src}' is empty.")

    if os.path.exists(dest):
        shutil.rmtree(dest)
    os.makedirs(dest)
    for item in os.listdir(src):
        s = os.path.join(src, item)
        d = os.path.join(dest, item)
        if os.path.isdir(s):
            copy_to_directory(s, d)
        else:
            shutil.copy2(s, d)



def extract_title(markdown):
    for line in markdown.split("\n"):
        if line.startswith("# "):
            return line[2:].strip()
    raise Exception("No title found in markdown")

def generate_page(basepath, from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using template {template_path}")
    with open(from_path, "r", encoding="utf-8") as f:
        markdown = f.read()
    with open(template_path, "r", encoding="utf-8") as f:
        template = f.read()
    html_markdown = markdown_to_html_node(markdown).to_html()
    title = extract_title(markdown)
    html_content_temp = template.replace("{{ Title }}", title).replace("{{ Content }}", html_markdown)
    html_content = html_content_temp.replace('href="/', f'href="{basepath}').replace('src="/', f'src="{basepath}')
    # print(html_content)
    os.makedirs(os.path.dirname(dest_path), exist_ok=True)
    print(f"Writing to {dest_path}")
    with open(dest_path, "w", encoding="utf-8") as f:
        f.write(html_content)
        f.close()
    return

def generate_pages_recursive(basepath,from_path, template_path, dest_path):
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
                generate_page(basepath, os.path.join(from_path, entry), template_path, os.path.join(dest_path, dest_file))
            else:
                print('is dir true')
                generate_pages_recursive(basepath, os.path.join(from_path, entry), template_path, os.path.join(dest_path, entry))
    else:
        raise Exception(f"Folder {from_path} does not exist")
    print(f"Finished generating pages from {from_path} to {dest_path}")