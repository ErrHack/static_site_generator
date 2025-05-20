def markdown_to_blocks(markdown: str) -> list[str]:
    block_lst = markdown.split("\n\n")
    return [block.strip(" \n") for block in block_lst]