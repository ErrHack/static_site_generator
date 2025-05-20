import re
from htmlnode import HTMLNode
from leafnode import LeafNode
from textnode import TextNode, TextType


def text_node_to_html_node(text_node: TextNode) -> HTMLNode:
    match text_node.text_type:
        case TextType.TEXT:
            return LeafNode(None, text_node.text)
        case TextType.BOLD:
            return LeafNode('b', text_node.text)
        case TextType.ITALIC:
            return LeafNode('i', text_node.text)
        case TextType.CODE:
            return LeafNode("code", text_node.text)
        case TextType.LINK:
            return LeafNode('a', text_node.text, {"href": text_node.url})
        case TextType.IMAGE:
            return LeafNode("img", "", {"src": text_node.url, "alt": text_node.text})
        case _:
            raise Exception(f"EXCEPTION: {text_node.text_type} is not supported!")


def split_nodes_delimiter(old_nodes: list[TextNode], delimiter: str, text_type: TextType) -> list[TextNode]:
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT or delimiter not in node.text:
            new_nodes.append(node)
        else:
            i = 0
            str_lst = node.text.split(delimiter)
            if len(str_lst) % 2 == 0:
                raise Exception("invalid markdown syntax")
            for s in str_lst:
                new_node = TextNode(s, TextType.TEXT) if i % 2 == 0 and s != "" else TextNode(s, text_type)
                if new_node.text != "":
                    new_nodes.append(new_node)
                i += 1
    return new_nodes

def split_nodes_image_or_link(old_nodes: list[TextNode], text_type: TextType) -> list[TextNode]:
    new_nodes = []
    regex = None
    match text_type:
        case TextType.IMAGE:
            regex = r"(!\[[^\[\]]*\]\([^\(\)]*\))"
            extract_markdown = extract_markdown_images
        case TextType.LINK:
            regex = r"(?<!!)(\[[^\[\]]*\]\([^\(\)]*\))"
            extract_markdown = extract_markdown_links
        case _:
            raise ValueError("text_type must either be IMAGE or LINK")
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
        else:
            str_lst = re.split(regex, node.text)
            # print(f"DEBUG: str_lst: {str_lst}")
            if str_lst == []:
                new_nodes.append(node)
            i = 0
            for s in str_lst:
                new_node = TextNode(s, text_type) if i % 2 == 1 and s != "" else TextNode(s, TextType.TEXT)
                # print(f"DEBUG: new_node before extraction: {new_node}")
                if new_node.text_type == text_type:
                    extracted = extract_markdown(new_node.text)
                    new_node.text, new_node.url = extracted[0]
                if new_node.text != "":
                    new_nodes.append(new_node)
                i += 1
    return new_nodes

def extract_markdown_images(text: str) -> list[tuple[str]]:
    return re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)

def extract_markdown_links(text: str) -> list[tuple[str]]:
    return re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)

def split_nodes_image(old_nodes):
    return split_nodes_image_or_link(old_nodes, TextType.IMAGE)

def split_nodes_link(old_nodes):
    return split_nodes_image_or_link(old_nodes, TextType.LINK)

def text_to_textnodes(text: str) -> list[TextNode]:
    return split_nodes_link(
                split_nodes_image(
                    split_nodes_delimiter(
                        split_nodes_delimiter(
                            split_nodes_delimiter(
                                [TextNode(text, TextType.TEXT)],
                                "**", TextType.BOLD
                            ),
                            '_', TextType.ITALIC
                        ),
                        '`', TextType.CODE
                    )
                )
            )

