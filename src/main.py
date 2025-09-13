import os
from generate_html_page import generate_pages_recursive, copy_to_directory
import sys


basepath = sys.argv[1] if len(sys.argv) > 1 else '/'
print(f'Base path set to: {basepath}')

print('static')
copy_to_directory('static', 'docs')
generate_pages_recursive(basepath, 'content', 'template.html', 'docs')

# copy_to_directory('static', 'public')
# generate_pages_recursive('content', 'template.html', 'public')