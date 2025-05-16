import unittest

from helperfunctions import text_node_to_html_node
from textnode import TextNode, TextType



class TestTextToHTML(unittest.TestCase):
    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_bold(self):
        text_node = TextNode("This is a text node with bold text", TextType.BOLD)
        html_node = text_node_to_html_node(text_node)
        self.assertEqual(html_node.tag, 'b')
        self.assertEqual(html_node.value, "This is a text node with bold text")

    def test_italic(self):
        text_node = TextNode("This is a text node with italic text", TextType.ITALIC)
        html_node = text_node_to_html_node(text_node)
        self.assertEqual(html_node.tag, 'i')
        self.assertEqual(html_node.value, "This is a text node with italic text")

    def test_code(self):
        text_node = TextNode("This is a text node with code text", TextType.CODE)
        html_node = text_node_to_html_node(text_node)
        self.assertEqual(html_node.tag, "code")
        self.assertEqual(html_node.value, "This is a text node with code text")

    def test_link(self):
        tag = 'a'
        anchor_text = "This is a text node with a link"
        href_prop = {"href": "www.google.com"}
        text_node = TextNode(anchor_text, TextType.LINK, href_prop["href"])
        html_node = text_node_to_html_node(text_node)
        self.assertEqual(html_node.tag, tag)
        self.assertEqual(html_node.value, anchor_text)
        self.assertEqual(html_node.props, href_prop)

    def test_image(self):
        tag = "img"
        html_node_value = ""
        html_node_props = {"src": "/path/to/image.png", "alt": "alt text from text_node.text"}
        text_node = TextNode(html_node_props["alt"], TextType.IMAGE, html_node_props["src"])
        html_node = text_node_to_html_node(text_node)
        self.assertEqual(html_node.tag, tag)
        self.assertEqual(html_node.value, html_node_value)
        self.assertEqual(html_node.props, html_node_props)

    def test_unknown_type(self):
        tag = "image"
        html_node_value = ""
        html_node_props = {"src": "/path/to/image.png", "alt": "alt text from text_node.text"}
        text_node = TextNode(html_node_props["alt"], tag, html_node_props["src"])
        with self.assertRaises(Exception):
            text_node_to_html_node(text_node)


if __name__ == "__main__":
    unittest.main()