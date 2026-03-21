from copy_dir_recursive import copy_dir_recursive
from textnode import TextNode, TextType
from generate_page import generate_page


def main():
    node = TextNode(
        "This is some anchor text",
        TextType.LINK,
        "https://www.boot.dev"
    )
    print(node)
    copy_dir_recursive("static", "public")
    generate_page(
        "content/index.md",
        "template.html",
        "public/index.html"
    )


main()