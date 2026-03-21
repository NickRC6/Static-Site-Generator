from htmlnode import HTMLNode, ParentNode, LeafNode
from markdown_to_blocks import markdown_to_blocks
from blocktype import block_to_block_type, BlockType
from text_to_textnodes import text_to_textnodes
from text_node_to_html_node import text_node_to_html_node


def text_to_children(text):
    text_nodes = text_to_textnodes(text)
    return [text_node_to_html_node(node) for node in text_nodes]


def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    children = []

    for block in blocks:
        block_type = block_to_block_type(block)

        if block_type == BlockType.PARAGRAPH:
            text = block.replace("\n", " ")
            children.append(ParentNode("p", text_to_children(text)))

        elif block_type == BlockType.HEADING:
            level = len(block.split(" ")[0])
            text = block[level + 1:]
            children.append(ParentNode(f"h{level}", text_to_children(text)))

        elif block_type == BlockType.CODE:
            content = block[3:-3].lstrip("\n")
            code_node = LeafNode("code", content)
            children.append(ParentNode("pre", [code_node]))

        elif block_type == BlockType.QUOTE:
            lines = [line.lstrip(">").lstrip() for line in block.split("\n")]
            text = " ".join(lines)
            children.append(ParentNode("blockquote", text_to_children(text)))

        elif block_type == BlockType.UNORDERED_LIST:
            items = []
            for line in block.split("\n"):
                text = line[2:]
                items.append(ParentNode("li", text_to_children(text)))
            children.append(ParentNode("ul", items))

        elif block_type == BlockType.ORDERED_LIST:
            items = []
            for line in block.split("\n"):
                text = line.split(". ", 1)[1]
                items.append(ParentNode("li", text_to_children(text)))
            children.append(ParentNode("ol", items))

    return ParentNode("div", children)