def markdown_to_blocks(markdown):
    # Split by double newline
    raw_blocks = markdown.split("\n\n")

    blocks = []
    for block in raw_blocks:
        stripped = block.strip()
        if stripped:  # remove empty blocks
            blocks.append(stripped)

    return blocks