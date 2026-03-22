import os
from generate_page import generate_page


def generate_pages_recursive(dir_path_content, template_path, dest_dir_path, basepath):
    for entry in os.listdir(dir_path_content):
        src_path = os.path.join(dir_path_content, entry)

        if os.path.isfile(src_path):
            if entry.endswith(".md"):
                dst_path = os.path.join(
                    dest_dir_path,
                    entry.replace(".md", ".html")
                )
                generate_page(src_path, template_path, dst_path, basepath)
        else:
            dst_path = os.path.join(dest_dir_path, entry)
            os.makedirs(dst_path, exist_ok=True)
            generate_pages_recursive(src_path, template_path, dst_path, basepath)