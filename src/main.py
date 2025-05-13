from htmlnode import HTMLNode
from leafnode import LeafNode
from parentnode import ParentNode
from textnode import TextNode, TextType


def main():
    text_node = TextNode("Dummy Text", TextType.NORMAL, "https://www.google.com")
    text_node_2 = TextNode("Dummy Text", TextType.NORMAL, "https://www.google.com")
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





if __name__ == "__main__":
    main()
