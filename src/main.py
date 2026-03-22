from copy_dir_recursive import copy_dir_recursive
from textnode import TextNode, TextType
from generate_pages_recursive import generate_pages_recursive
import sys


def main():
    basepath = sys.argv[1] if len(sys.argv) > 1 else "/"

    generate_pages_recursive(
        "content",
        "template.html",
        "docs",
        basepath,
    )


main()