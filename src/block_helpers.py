import re
from block_types import BlockType


def markdown_to_blocks(markdown: str) -> list[str]:
    block_lst = markdown.split("\n\n")
    return [block.strip(" \n") for block in block_lst if block]

def block_to_block_type(block: str) -> BlockType:
    match block[0]:
        case '#':
            return BlockType.HEADING if re.match(r"(?<!#)[#]{1,6}[ ]+.+", block) != None else BlockType.PARAGRAPH
        case '`':
            return BlockType.CODE if re.match(r"(?<!`)```(?!`)((?:(?!```)[\s\S])+?)```(?!`)", block) != None else BlockType.PARAGRAPH
        case '>':
            lines = block.split('\n')
            for line in lines:
                if line[0] != '>': return BlockType.PARAGRAPH
            return BlockType.QUOTE
        case '-':
            lines = block.split('\n')
            for line in lines:
                if re.match(r"^- ", line) == None: return BlockType.PARAGRAPH
            return BlockType.UNORDERED_LIST
        case '1':
            lines = block.split('\n')
            i = 1
            for line in lines:
                if re.match(r"^\d\. ", line) == None or line[0] != str(i): return BlockType.PARAGRAPH
                i += 1
            return BlockType.ORDERED_LIST
        case _:
            return BlockType.PARAGRAPH