from htmlnode import HTMLNode



class ParentNode(HTMLNode):
    def __init__(
            self,
            tag: str, 
            children: list[HTMLNode],
            props: dict[str, str] = None
    ):
        super().__init__(tag, children=children, props=props)

    def to_html(self):
        if self.tag == None:
            raise ValueError("ParentNode must have a tag!")
        if self.children == None:
            raise ValueError("ParentNode must have children!")
        html_str = ""
        for html_node in self.children:
            html_str += html_node.to_html()
        return f"<{self.tag}{self.props_to_html()}>{html_str}</{self.tag}>"