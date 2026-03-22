import os
from generate_page import generate_page


def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    for entry in os.listdir(dir_path_content):
        src_path = os.path.join(dir_path_content, entry)
        dst_path = os.path.join(dest_dir_path, entry)

        if os.path.isfile(src_path):
            if src_path.endswith(".md"):
                html_path = dst_path.replace(".md", ".html")

                print(f"Generating page from {src_path} to {html_path}")
                generate_page(src_path, template_path, html_path)
        else:
            os.makedirs(dst_path, exist_ok=True)
            generate_pages_recursive(src_path, template_path, dst_path)