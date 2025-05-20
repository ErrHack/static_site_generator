import unittest

from helperfunctions import text_to_textnodes
from textnode import TextNode, TextType


class TestTextToTextnode(unittest.TestCase):
    def test_text_to_textnode(self):
        text = "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        node_lst = text_to_textnodes(text)
        self.assertListEqual(
                                [
                        TextNode("This is ", TextType.TEXT),
                        TextNode("text", TextType.BOLD),
                        TextNode(" with an ", TextType.TEXT),
                        TextNode("italic", TextType.ITALIC),
                        TextNode(" word and a ", TextType.TEXT),
                        TextNode("code block", TextType.CODE),
                        TextNode(" and an ", TextType.TEXT),
                        TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
                        TextNode(" and a ", TextType.TEXT),
                        TextNode("link", TextType.LINK, "https://boot.dev"),
                    ],
                    node_lst
        )

    def test_text_to_textnode_different_order(self):
        text = "This is an _italic_ word with **bold text** and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        node_lst = text_to_textnodes(text)
        self.assertListEqual(
                                [
                        TextNode("This is an ", TextType.TEXT),
                        TextNode("italic", TextType.ITALIC),
                        TextNode(" word with ", TextType.TEXT),
                        TextNode("bold text", TextType.BOLD),
                        TextNode(" and a ", TextType.TEXT),
                        TextNode("code block", TextType.CODE),
                        TextNode(" and an ", TextType.TEXT),
                        TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
                        TextNode(" and a ", TextType.TEXT),
                        TextNode("link", TextType.LINK, "https://boot.dev"),
                    ],
                    node_lst
        )

    def test_text_to_textnode_remove_type(self):
        text = "This is a regular word with **bold text** and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        node_lst = text_to_textnodes(text)
        self.assertListEqual(
                                [
                        TextNode("This is a regular word with ", TextType.TEXT),
                        TextNode("bold text", TextType.BOLD),
                        TextNode(" and a ", TextType.TEXT),
                        TextNode("code block", TextType.CODE),
                        TextNode(" and an ", TextType.TEXT),
                        TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
                        TextNode(" and a ", TextType.TEXT),
                        TextNode("link", TextType.LINK, "https://boot.dev"),
                    ],
                    node_lst
        )

    def test_text_to_textnode_change_order_and_types_with_multiple_links(self):
        text = "This is **bold text** with another **bold word** and a `code block` before a [link to google](www.google.com) and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        node_lst = text_to_textnodes(text)
        self.assertListEqual(
                                [
                        TextNode("This is ", TextType.TEXT),
                        TextNode("bold text", TextType.BOLD),
                        TextNode(" with another ", TextType.TEXT),
                        TextNode("bold word", TextType.BOLD),
                        TextNode(" and a ", TextType.TEXT),
                        TextNode("code block", TextType.CODE),
                        TextNode(" before a ", TextType.TEXT),
                        TextNode("link to google", TextType.LINK, "www.google.com"),
                        TextNode(" and an ", TextType.TEXT),
                        TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
                        TextNode(" and a ", TextType.TEXT),
                        TextNode("link", TextType.LINK, "https://boot.dev"),
                    ],
                    node_lst
        )

    def test_text_to_textnode_something_at_the_beginning(self):
        text = "_why italic at the beginning_, but this is **bold text** with another **bold word** and a `code block` before a [link to google](www.google.com) and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        node_lst = text_to_textnodes(text)
        self.assertListEqual(
                                [
                        TextNode("why italic at the beginning", TextType.ITALIC),
                        TextNode(", but this is ", TextType.TEXT),
                        TextNode("bold text", TextType.BOLD),
                        TextNode(" with another ", TextType.TEXT),
                        TextNode("bold word", TextType.BOLD),
                        TextNode(" and a ", TextType.TEXT),
                        TextNode("code block", TextType.CODE),
                        TextNode(" before a ", TextType.TEXT),
                        TextNode("link to google", TextType.LINK, "www.google.com"),
                        TextNode(" and an ", TextType.TEXT),
                        TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
                        TextNode(" and a ", TextType.TEXT),
                        TextNode("link", TextType.LINK, "https://boot.dev"),
                    ],
                    node_lst
        )

if __name__ == "__main__":
    unittest.main()