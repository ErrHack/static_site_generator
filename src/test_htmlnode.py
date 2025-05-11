import unittest
from htmlnode import HTMLNode

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



if __name__ == "__main__":
    unittest.main()