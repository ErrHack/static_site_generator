import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_eq2(self):
        text = "This is a text node"
        url = "www.google.com"
        text_type = TextType.NORMAL
        node = TextNode(text, text_type, url)
        node2 = TextNode(text, text_type, url)
        self.assertEqual(node, node2)

    def test_not_eq(self):
        text = "This is a text node"
        text2 = "This is a text node "
        url = "www.google.com"
        text_type = TextType.NORMAL
        node = TextNode(text, text_type, url)
        node2 = TextNode(text2, text_type, url)
        self.assertNotEqual(node, node2)

    def test_not_eq2(self):
        text = ""
        text2 = "This is a text node"
        url = "google.com"
        url2 = "www.google.com"
        text_type = TextType.NORMAL
        node = TextNode(text, text_type, url2)
        node2 = TextNode(text2, text_type, url)
        self.assertNotEqual(node, node2)

    def test_not_eq3(self):
        text = 1
        text2 = "This is a text node"
        url = "google.com"
        url2 = "www.google.com"
        text_type = TextType.NORMAL
        text_type2 = TextType.ITALIC
        node = TextNode(text, text_type, url2)
        node2 = TextNode(text2, text_type2, url)
        self.assertNotEqual(node, node2)

    def test_eq3(self):
        text = "**bold**"
        url = "www.google.com"
        text_type = TextType.BOLD
        node = TextNode(text, text_type, url)
        node2 = TextNode(text, text_type, url)
        self.assertEqual(node, node2)



if __name__ == "__main__":
    unittest.main()