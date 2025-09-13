import os
import shutil
from generate_html_page import generate_pages_recursive

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


copy_to_directory('static', 'public')
generate_pages_recursive('content', 'template.html', 'public')
