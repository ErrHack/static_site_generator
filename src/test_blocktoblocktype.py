import unittest

from block_helpers import block_to_block_type
from block_types import BlockType


class TestBlockToBlockType(unittest.TestCase):
    def test_block_to_block_type_h1(self):
        self.assertEqual(block_to_block_type("# this is a h1 heading in markdown"), BlockType.HEADING)

    def test_block_to_block_type_not_h1(self):
        self.assertEqual(block_to_block_type("#this is not a h1 heading in markdown"), BlockType.PARAGRAPH)

    def test_block_to_block_type_h2(self):
        self.assertEqual(block_to_block_type("## this is a h2 heading in markdown"), BlockType.HEADING)

    def test_block_to_block_type_not_h2(self):
        self.assertEqual(block_to_block_type(" ## this is not a h1 heading in markdown"), BlockType.PARAGRAPH)

    def test_block_to_block_type_h3(self):
        self.assertEqual(block_to_block_type("### this is a h3 heading in markdown"), BlockType.HEADING)

    def test_block_to_block_type_h4(self):
        self.assertEqual(block_to_block_type("#### this is a h4 heading in markdown"), BlockType.HEADING)

    def test_block_to_block_type_h5(self):
        self.assertEqual(block_to_block_type("##### this is a h5 heading in markdown"), BlockType.HEADING)

    def test_block_to_block_type_h6(self):
        self.assertEqual(block_to_block_type("###### this is a h6 heading in markdown"), BlockType.HEADING)

    def test_block_to_block_type_not_h7(self):
        self.assertEqual(block_to_block_type("####### this is not a h7 heading in markdown"), BlockType.PARAGRAPH)

    def test_block_to_block_type_code(self):
        self.assertEqual(block_to_block_type("```some code```"), BlockType.CODE)
    
    def test_block_to_block_type_code2(self):
        self.assertEqual(block_to_block_type("``` ```"), BlockType.CODE)
    
    def test_block_to_block_type_code_new_line(self):
        self.assertEqual(block_to_block_type("```some\ncode```"), BlockType.CODE)

    def test_block_to_block_type_not_code(self):
        self.assertEqual(block_to_block_type("```some code"), BlockType.PARAGRAPH)

    def test_block_to_block_type_not_code2(self):
        self.assertEqual(block_to_block_type("```some code``"), BlockType.PARAGRAPH)

    def test_block_to_block_type_not_code3(self):
        self.assertEqual(block_to_block_type("``some code```"), BlockType.PARAGRAPH)

    def test_block_to_block_type_not_code4(self):
        self.assertEqual(block_to_block_type(" ```some code```"), BlockType.PARAGRAPH)

    def test_block_to_block_type_not_code5(self):
        self.assertEqual(block_to_block_type("` ``some code```"), BlockType.PARAGRAPH)

    def test_block_to_block_type_not_code6(self):
        self.assertEqual(block_to_block_type("```some code`` `"), BlockType.PARAGRAPH)

    def test_block_to_block_type_not_code7(self):
        self.assertEqual(block_to_block_type("``````"), BlockType.PARAGRAPH)

    def test_block_to_block_type_quote(self):
        self.assertEqual(block_to_block_type(">some quoted text\n>in a quote block"), BlockType.QUOTE)

    def test_block_to_block_type_quote2(self):
        self.assertEqual(block_to_block_type(">some quoted text\n>in a quote block\n>in a quote block\n>in a quote block"), BlockType.QUOTE)

    def test_block_to_block_type_quote3(self):
        self.assertEqual(block_to_block_type(">some quoted. text\n>in a? quote block\n>in ?a qu!ote block\n>in a quo!t,e b:lock"), BlockType.QUOTE)

    def test_block_to_block_type_quote4(self):
        self.assertEqual(block_to_block_type("> some quoted. text\n>in a? quote block\n> in ?a qu!ote block\n>in a quo!t,e b:lock"), BlockType.QUOTE)


    def test_block_to_block_type_not_quote(self):
        self.assertEqual(block_to_block_type(">some quoted text\nin a quote block\n>in a quote block\n>in a quote block"), BlockType.PARAGRAPH)

    def test_block_to_block_type_unordered_list(self):
        self.assertEqual(block_to_block_type("- text\n- another text\n- one more texts"), BlockType.UNORDERED_LIST)

    def test_block_to_block_type_not_unordered_list(self):
        self.assertEqual(block_to_block_type("- text\n another text\n- one more texts"), BlockType.PARAGRAPH)

    def test_block_to_block_type_not_unordered_list2(self):
        self.assertEqual(block_to_block_type("- text\n-another text\n- one more texts"), BlockType.PARAGRAPH)

    def test_block_to_block_type_ordered_list(self):
        self.assertEqual(block_to_block_type("1. item1\n2. item2 \n3. item3"), BlockType.ORDERED_LIST)

    def test_block_to_block_type_ordered_list2(self):
        self.assertEqual(block_to_block_type("1. item1"), BlockType.ORDERED_LIST)

    def test_block_to_block_type_not_ordered_list(self):
        self.assertEqual(block_to_block_type("2. item2 \n3. item3"), BlockType.PARAGRAPH)

    def test_block_to_block_type_not_ordered_list2(self):
        self.assertEqual(block_to_block_type("1. item1\n2. item2 \n2. item3"), BlockType.PARAGRAPH)

    def test_block_to_block_type_not_ordered_list3(self):
        self.assertEqual(block_to_block_type("1.item1\n2. item2 \n3. item3"), BlockType.PARAGRAPH)



if __name__ == "__main__":
    unittest.main()