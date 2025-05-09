from textnode import TextNode, TextType


def main():
    text_node = TextNode("Dummy Text", TextType.NORMAL, "https://www.google.com")
    print(f"DEBUG: dummy text node: {text_node}")


if __name__ == "__main__":
    main()
