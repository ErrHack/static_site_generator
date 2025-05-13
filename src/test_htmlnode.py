import unittest
from htmlnode import HTMLNode
from leafnode import LeafNode
from parentnode import ParentNode

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

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )
    
    def test_to_html_with_multi_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        tag = 'a'
        value = "link to google"
        props = {"href": "https://www.google.com", "target": "_blank"}
        grandchild_node_2 = LeafNode(tag, value, props)
        child_node = ParentNode("span", [grandchild_node, grandchild_node_2])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            '<div><span><b>grandchild</b><a href="https://www.google.com" target="_blank">link to google</a></span></div>',
        )

    def test_to_html_nested_divs(self):
        tag_div = "div"
        tag_h2 = "h2"
        tag_section = "section"
        props_key_class = "class"
        props_val_level_6 = "level-6"
        props_val_level_5 = "level-5"
        props_val_level_4 = "level-4"
        props_val_level_3 = "level-3"
        props_val_level_2 = "level-2"
        props_val_level_1 = "level-1"
        val_h2 = "6 Levels Deep"
        val_level_6 = "Level 6"
        val_level_5 = "Level 5"
        val_level_4 = "Level 4"
        val_level_3 = "Level 3"
        val_level_2 = "Level 2"
        val_level_1 = "Level 1"
        leaf_val_5 = LeafNode(None, value=val_level_5)
        leaf_val_4 = LeafNode(None, value=val_level_4)
        leaf_val_3 = LeafNode(None, value=val_level_3)
        leaf_val_2 = LeafNode(None, value=val_level_2)
        leaf_val_1 = LeafNode(None, value=val_level_1)
        grandchild_6 = LeafNode(tag_div, val_level_6, {props_key_class: props_val_level_6})
        parent_5 = ParentNode(tag_div, [leaf_val_5, grandchild_6], {props_key_class: props_val_level_5})
        parent_4 = ParentNode(tag_div, [leaf_val_4, parent_5], {props_key_class: props_val_level_4})
        parent_3 = ParentNode(tag_div, [leaf_val_3, parent_4], {props_key_class: props_val_level_3})
        parent_2 = ParentNode(tag_div, [leaf_val_2, parent_3], {props_key_class: props_val_level_2})
        parent_1 = ParentNode(tag_div, [leaf_val_1, parent_2], {props_key_class: props_val_level_1})
        leaf_h2 = LeafNode(tag_h2, val_h2)
        parent_section = ParentNode(tag_section, [leaf_h2, parent_1])
        self.assertEqual(
            parent_section.to_html(),
            '<section><h2>6 Levels Deep</h2><div class="level-1">Level 1<div class="level-2">Level 2<div class="level-3">Level 3<div class="level-4">Level 4<div class="level-5">Level 5<div class="level-6">Level 6</div></div></div></div></div></div></section>'
        )

    def test_to_html_no_children(self):
        parent_node = ParentNode("div", None)
        with self.assertRaises(ValueError):
            parent_node.to_html()
        
    def test_to_html_no_tag(self):
        child_node = LeafNode("div", "value")
        parent_node = ParentNode(None, [child_node])
        with self.assertRaises(ValueError):
            parent_node.to_html()

if __name__ == "__main__":
    unittest.main()