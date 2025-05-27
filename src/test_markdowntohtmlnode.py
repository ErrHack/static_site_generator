import unittest

from helperfunctions import markdown_to_html_node


class TestMarkdownToHTMLNode(unittest.TestCase):
    def test_paragraphs(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )

    def test_codeblock(self):
        md = """
```
This is text that _should_ remain
the **same** even with inline stuff
```
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
        )

    def test_heading_h1(self):
        md = """

# Main Title

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h1>Main Title</h1></div>"
        )

    def test_heading_h2(self):
        md = """
## Chapter 2: Getting Started

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h2>Chapter 2: Getting Started</h2></div>"
        )

    def test_heading_h3(self):
        md = """
### Section 3.1: `Code Integration`
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h3>Section 3.1: <code>Code Integration</code></h3></div>"
        )

    def test_heading_h4(self):
        md = """

#### **Important Notes** and Guidelines
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h4><b>Important Notes</b> and Guidelines</h4></div>"
        )

    def test_heading_h5(self):
        md = """
##### _Emphasis_ on **Bold** Concepts
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h5><i>Emphasis</i> on <b>Bold</b> Concepts</h5></div>"
        )

    def test_heading_h6(self):
        md = """
###### ~~Deprecated~~ Methods and `new_function()`
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h6>~~Deprecated~~ Methods and <code>new_function()</code></h6></div>"
        )

    def test_heading_h1_2(self):
        md = """
# **Project** _Alpha_: `initialize()` Function
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h1><b>Project</b> <i>Alpha</i>: <code>initialize()</code> Function</h1></div>"
        )

    def test_heading_h2_2(self):
        md = """
## ~~Old~~ **New** API Documentation
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h2>~~Old~~ <b>New</b> API Documentation</h2></div>"
        )

    def test_heading_h3_2(self):
        md = """
### Section A: **Bold** and _Italic_ `code_samples`
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h3>Section A: <b>Bold</b> and <i>Italic</i> <code>code_samples</code></h3></div>"
        )

    def test_heading_h4_2(self):
        md = """
#### [Link Text](https://example.com) with **formatting**
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            '<div><h4><a href="https://example.com">Link Text</a> with <b>formatting</b></h4></div>'
        )

    def test_heading_h5_2(self):
        md = """
##### Task List: ~~completed~~ → **in progress** → _pending_
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h5>Task List: ~~completed~~ → <b>in progress</b> → <i>pending</i></h5></div>"
        )

    def test_blockquote(self):
        md = """
>This is a single-line block quote
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><blockquote><p>This is a single-line block quote</p></blockquote></div>"
        )

    def test_simple_blockquote(self):
        md = """
> This is a simple blockquote.
> It spans two lines.
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><blockquote><p>This is a simple blockquote.</p><p>It spans two lines.</p></blockquote></div>"
        )

    def test_multi_line_blockquote_with_formatting(self):
        md = """
> This is a simple blockquote with **bold tex**.
> It spans two lines and has `inline_code_text`.
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><blockquote><p>This is a simple blockquote with <b>bold tex</b>.</p><p>It spans two lines and has <code>inline_code_text</code>.</p></blockquote></div>"
        )

    def test_unordered_list(self):
        md = """
- list item 1
- a second list item
- another list item
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ul><li>list item 1</li><li>a second list item</li><li>another list item</li></ul></div>"
        )

    def test_unordered_list_with_formatting(self):
        self.maxDiff = None
        md = """
- list item 1 with _italic phrase_
- a second list item with a [link to google](www.google.com) and a **bold** word
- another list item with `inline_code_text`
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            '<div><ul><li>list item 1 with <i>italic phrase</i></li><li>a second list item with a <a href="www.google.com">link to google</a> and a <b>bold</b> word</li><li>another list item with <code>inline_code_text</code></li></ul></div>'
        )

    def test_ordered_list(self):
        self.maxDiff = None
        md = """
1. first item
2. second item
3. third item
4. fourth item
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ol><li>first item</li><li>second item</li><li>third item</li><li>fourth item</li></ol></div>"
        )

    def test_ordered_list_with_formatting(self):
        self.maxDiff = None
        md = """
1. first item that has a [link to google](www.google.com)
2. second item with `inline_code_text` and a **bold** word
3. this third item has an _italic phrase_
4. **fourth** item _is_ `weird_stuff`
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            '<div><ol><li>first item that has a <a href="www.google.com">link to google</a></li><li>second item with <code>inline_code_text</code> and a <b>bold</b> word</li><li>this third item has an <i>italic phrase</i></li><li><b>fourth</b> item <i>is</i> <code>weird_stuff</code></li></ol></div>'
        )

    def test_mutiple_blocks(self):
        self.maxDiff = None
        md = """
# Main Title

This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

## Chapter 2: Getting Started

- list item 1 with _italic phrase_
- a second list item with a [link to google](www.google.com) and a **bold** word
- another list item with `inline_code_text`


### Section 3.1: `Code Integration`

```
This is text that _should_ remain
the **same** even with inline stuff
```

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            '<div><h1>Main Title</h1><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p><h2>Chapter 2: Getting Started</h2><ul><li>list item 1 with <i>italic phrase</i></li><li>a second list item with a <a href="www.google.com">link to google</a> and a <b>bold</b> word</li><li>another list item with <code>inline_code_text</code></li></ul><h3>Section 3.1: <code>Code Integration</code></h3><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>'
        )