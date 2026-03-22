from copy_dir_recursive import copy_dir_recursive
from textnode import TextNode, TextType
from generate_pages_recursive import generate_pages_recursive


def main():
    node = TextNode(
        "This is some anchor text",
        TextType.LINK,
        "https://www.boot.dev"
    )
    print(node)
    copy_dir_recursive("static", "public")
    generate_pages_recursive(
        "content",
        "template.html",
        "public"
    )


main()