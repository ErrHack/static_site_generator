from htmlnode import HTMLNode
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


if __name__ == "__main__":
    main()
