import unittest

from helperfunctions import extract_title


class TestExtractTitlel(unittest.TestCase):
    def test_extract_title_with_empty_md(self):
        md = ""
        with self.assertRaises(Exception):
            extract_title(md)
    
    def test_exctract_title_with_h1(self):
        md = """
# This is a heading

This is a paragraph of text. It has some **bold** and _italic_ words inside of it.

- This is the first list item in a list block
- This is a list item
- This is another list item
"""

        title = extract_title(md)
        self.assertEqual(
            title,
            "This is a heading"
        )

    def test_extract_title_no_heading(self):
        md = """

This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here, and possibly an empty block at the end.

"""

        with self.assertRaises(Exception):
            title = extract_title(md)

    def test_extract_title_no_h1_heading(self):
        md = """
### This is not a h1 heading

This is a paragraph of text. It has some **bold** and _italic_ words inside of it.

- This is the first list item in a list block
- This is a list item
- This is another list item
"""

        with self.assertRaises(Exception):
            title = extract_title(md)

    def test_extract_title_with_spaces_in_h1_heading(self):
        md = """
#     This is a heading with extra spaces        

This is a paragraph of text. It has some **bold** and _italic_ words inside of it.

- This is the first list item in a list block
- This is a list item
- This is another list item
"""

        title = extract_title(md)
        self.assertEqual(
            title,
            "This is a heading with extra spaces"
        )



if __name__ == "__main__":
    unittest.main()