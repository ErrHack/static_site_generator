import unittest

from helperfunctions import split_nodes_delimiter
from textnode import TextNode, TextType

class TestSplitNodeDelimiter(unittest.TestCase):
    def test_bold(self):
        node = TextNode("This is a string with a **bold word**.", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(new_nodes[1].text_type, TextType.BOLD)

    def test_code(self):
        node = TextNode("This is a string with inline `code elements` and more text after.", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], '`', TextType.CODE)
        self.assertEqual(new_nodes[1].text_type, TextType.CODE)

    def test_italic(self):
        node = TextNode("This is a string with an _italic_ word, and more text after.", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], '_', TextType.ITALIC)
        self.assertEqual(new_nodes[1].text_type, TextType.ITALIC)

    def test_length(self):
        node = TextNode("This is a string with a **bold word**.", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(len(new_nodes), 3)

    def test_length_2(self):
        node = TextNode("This is a string with **bold words and nothing after the bold delimiter**", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(len(new_nodes), 3)

    def test_length_3(self):
        node = TextNode("**Nothing before the bold delimiter** with lots of text after. HAHAHAHA", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(len(new_nodes), 3)

    def test_length_4(self):
        node = TextNode("**With all the text is bolds!!!! HAHAHAHA**.", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(len(new_nodes), 3)

    def test_length_5(self):
        node = TextNode("And multiple **separate** words that are **bold**", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(len(new_nodes), 5)
        
    def test_even_odd_indices(self):
        node = TextNode("This is a string with a **bold word**.", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        txt_nodes = new_nodes[0::2]
        bold_nodes = new_nodes[1::2]
        for node in txt_nodes:
            self.assertEqual(node.text_type, TextType.TEXT)
        for node in bold_nodes:
            self.assertEqual(node.text_type, TextType.BOLD)

    def test_even_odd_indices_2(self):
        node = TextNode("This is a string with a **bold word**, and more **bold words**.", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        txt_nodes = new_nodes[0::2]
        bold_nodes = new_nodes[1::2]
        for node in txt_nodes:
            self.assertEqual(node.text_type, TextType.TEXT)
        for node in bold_nodes:
            self.assertEqual(node.text_type, TextType.BOLD)

    def test_empty_str(self):
        node = TextNode("", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], '_', TextType.ITALIC)
        self.assertEqual(new_nodes[0].text, "")

    def test_no_delimiter(self):
        node = TextNode("This is a text node of plain text. No delimters are present.", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], '_', TextType.ITALIC)
        self.assertEqual(new_nodes[0].text, "This is a text node of plain text. No delimters are present.")
        self.assertEqual(new_nodes[0].text_type, TextType.TEXT)

    def test_non_text_TextType(self):
        node = TextNode("This is a text node of **bold** text. Bold delimters are present.", TextType.BOLD)
        new_nodes = split_nodes_delimiter([node], "**", TextType.TEXT)
        self.assertEqual(new_nodes[0].text, "This is a text node of **bold** text. Bold delimters are present.")
        self.assertEqual(new_nodes[0].text_type, TextType.BOLD)

    def test_invalid_markdown(self):
        node = TextNode("This is a text node of **bold** text. **Bold* delimters are present.", TextType.TEXT)
        with self.assertRaises(Exception):
            new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)

    def test_multi_nodes(self):
        node = TextNode("This is a string with a **bold word**.", TextType.TEXT)
        node_2 = TextNode("This is another string with a **bold** word.", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node, node_2], "**", TextType.BOLD)
        new_nodes_1 = new_nodes[0:3]
        new_nodes_2 = new_nodes[3:]
        
        for i in range(len(new_nodes_1)):
            if i % 2 == 0:
                self.assertEqual(new_nodes_1[i].text_type, TextType.TEXT)
            else:
                self.assertEqual(new_nodes_1[i].text_type, TextType.BOLD)
            
        for i in range(len(new_nodes_2)):
            if i % 2 == 0:
                self.assertEqual(new_nodes_2[i].text_type, TextType.TEXT)
            else:
                self.assertEqual(new_nodes_2[i].text_type, TextType.BOLD)
            







if __name__ == "__main__":
    unittest.main()