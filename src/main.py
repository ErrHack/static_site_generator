from helperfunctions import extract_markdown_images, extract_markdown_links, split_nodes_delimiter
from htmlnode import HTMLNode
from leafnode import LeafNode
from parentnode import ParentNode
from textnode import TextNode, TextType


def main():
    text_node = TextNode("Dummy Text", TextType.TEXT, "https://www.google.com")
    text_node_2 = TextNode("Dummy Text", TextType.TEXT, "https://www.google.com")
    text_node_3 = TextNode("Some Different **Dummy** Text", TextType.BOLD, "https://www.boot.dev")
    print(f"DEBUG: dummy text node: {text_node}")
    print(f"\ttext node 1 == text node 2: {text_node_2 == text_node}")
    print(f"\ttext node 3 == text node 2: {text_node_2 == text_node_3}")

    html_node = HTMLNode(props={"href": "https://www.google.com", "target": "_blank"})
    print(f"DEBUG: html_node.props_to_html(): {html_node.props_to_html()}")
    print(f"\thtml_node repr: {html_node}")
    leaf_node = LeafNode('p', "this is a paragraph leaf node")
    print(f"DEBUG: leaf_node p: {leaf_node.to_html()}")
    leaf_node2 = LeafNode('a', "link to google", props={"href": "https://www.google.com", "target": "_blank"})
    print(f"DEBUG: leaf_node a: {leaf_node2.to_html()}")

    tag = 'a'
    value = "this is the string value in an anchor element"
    props = {"href": "https://www.google.com", "target": "_blank"}
    node = LeafNode(tag, value, props)
    print(f"DEBUG: {node}")

    node = ParentNode(
        "p",
        [
            LeafNode("b", "Bold text"),
            LeafNode(None, "Normal text"),
            LeafNode("i", "italic text"),
            LeafNode(None, "Normal text"),
        ],
    )
    print(f"DEBUG: node.to_html(): {node.to_html()}")

    s = "*this is a string*. *more bold"
    split_str = s.split('*')
    print(f"split_str: {split_str}")

    node = TextNode("This is a string with a **bold word**.", TextType.TEXT)
    new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
    print(f"DEBUG: split_nodes_delimiter -> new_nodes: {new_nodes}")

    text = "This is text with a [rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
    print(f"DEBUG: \n\textract_markdown_images(text): {extract_markdown_links(text)}")

    s = "#### heading but it has multiple spaces."
    num_h = s.find(' ')
    print(f"DEBUG: THIS IS num_h: {num_h} and this is split at first space: {s.split(' ', 1)[1]}")

    s = "```some code```"
    print(f"DEBUG: strip backticks: {s.strip('`')}")



if __name__ == "__main__":
    main()
