import os
import shutil
from helperfunctions import extract_title, markdown_to_html_node


def main():
    destination = "./public/"
    if os.path.exists(destination):
        shutil.rmtree(destination)
    copy_static_to_public_recursive()
    generate_pages_recursive()

def copy_static_to_public_recursive(source = "./static/", destination = "./public/"):
    os.mkdir(destination)
    for target in os.listdir(source):
        if os.path.isdir(source + target):
            copy_static_to_public_recursive(source + target + '/', destination + target + '/')
        elif os.path.isfile(source + target):
            shutil.copy(source + target, destination + target)

def generate_page(from_path: str, template_path: str, dest_path: str):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    page = ""
    with open(from_path, 'r') as fp:
        with open(template_path, 'r') as tp:
            md = fp.read()
            template = tp.read()
            node = markdown_to_html_node(md)
            html = node.to_html()
            title = extract_title(md)
            page = template.replace("{{ Title }}", title).replace("{{ Content }}", html)
    dir_path = os.path.dirname(dest_path)
    os.makedirs(dir_path, exist_ok=True)
    with open(dest_path, 'w') as f:
        f.write(page)

def generate_pages_recursive(dir_path_content: str = "./content/", template_path: str = "./template.html", dest_dir_path: str = "./public/"):
    os.makedirs(dest_dir_path, exist_ok=True)
    for target in os.listdir(dir_path_content):
        if os.path.isdir(dir_path_content + target):
            generate_pages_recursive(dir_path_content=dir_path_content + target + '/', dest_dir_path=dest_dir_path + target + '/')
        elif os.path.isfile(dir_path_content + target):
            html_ext = target.replace(".md", ".html")
            generate_page(dir_path_content + target, template_path, dest_dir_path + html_ext)



if __name__ == "__main__":
    main()
