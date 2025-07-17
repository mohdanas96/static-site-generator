import os
import shutil
import sys
from utils import generate_pages_recursive

def main():
    basepath = sys.argv[1] if sys.argv[1] else "/"
    
    folderPath = "/home/anas/workspace/github.com/mohdanas96/static-site-generator/docs"
    content_path = "/home/anas/workspace/github.com/mohdanas96/static-site-generator/content/"
    template_path = "/home/anas/workspace/github.com/mohdanas96/static-site-generator/template.html"
    dest_path = "/home/anas/workspace/github.com/mohdanas96/static-site-generator/docs/"
    cwd = os.getcwd()
    folderExists = os.path.exists(folderPath)
    if folderExists:
        shutil.rmtree(folderPath)
    shutil.copytree(cwd + "/src/static/", folderPath)
    generate_pages_recursive(content_path, template_path, dest_path, basepath)
    
main()