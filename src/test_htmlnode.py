import unittest
from htmlnode import HTMLNode
from leafnode import LeafNode

class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        val = "some val"
        p = {"href": "https://www.google.com", "target": "_blank"}
        node = HTMLNode(value=val, props=p)
        node2 = HTMLNode(value=val, props=p)
        self.assertEqual(node, node2)

    def test_not_eq(self):
        val = "some val"
        p = {"href": "https://www.google.com", "target": "_blank"}
        node = HTMLNode(value=val, props=p)
        node2 = HTMLNode(props=p)
        self.assertNotEqual(node, node2)

    def test_props_leading_space(self):
        val = "some val"
        p = {"href": "https://www.google.com", "target": "_blank"}
        node = HTMLNode(value=val, props=p)
        props_str = node.props_to_html()
        self.assertEqual(props_str[0], ' ')

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_a(self):
        tag = 'a'
        value = "this is the string value in an anchor element"
        props = {"href": "https://www.google.com", "target": "_blank"}
        node = LeafNode(tag, value, props)
        node_str = '<a href="https://www.google.com" target="_blank">this is the string value in an anchor element</a>'
        self.assertEqual(node.to_html(), node_str)

    def test_leaf_to_html_none_value(self):
        tag = 'p'
        value = None
        props = None
        node = LeafNode(tag, value, props)
        with self.assertRaises(ValueError):
            node.to_html()

    def test_leaf_to_html_none_tag(self):
        tag = None
        value = "the tag is none"
        props = None
        node = LeafNode(tag, value, props)
        self.assertEqual(node.to_html(), value)
        



if __name__ == "__main__":
    unittest.main()