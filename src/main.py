import os
import shutil
from utils import generate_page

def main():
    folderPath = "/home/anas/workspace/github.com/mohdanas96/static-site-generator/public"
    content_path = "/home/anas/workspace/github.com/mohdanas96/static-site-generator/content/index.md"
    template_path = "/home/anas/workspace/github.com/mohdanas96/static-site-generator/template.html"
    dest_path = "/home/anas/workspace/github.com/mohdanas96/static-site-generator/public/index.html"
    cwd = os.getcwd()
    folderExists = os.path.exists(folderPath)
    if folderExists:
        shutil.rmtree(folderPath)
    shutil.copytree(cwd + "/src/static/", folderPath)
    generate_page(content_path, template_path, dest_path)
    
main()