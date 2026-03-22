import os
import shutil


def copy_dir_recursive(src, dst):
    if os.path.exists(dst):
        shutil.rmtree(dst)

    os.mkdir(dst)

    def copy_contents(current_src, current_dst):
        for item in os.listdir(current_src):
            src_path = os.path.join(current_src, item)
            dst_path = os.path.join(current_dst, item)

            if os.path.isfile(src_path):
                print(f"Copying file: {src_path} -> {dst_path}")
                shutil.copy(src_path, dst_path)
            else:
                print(f"Creating directory: {dst_path}")
                os.mkdir(dst_path)
                copy_contents(src_path, dst_path)

    copy_contents(src, dst)