


class HTMLNode:
    def __init__(
            self,
            tag: str = None,
            value: str = None,
            children: list["HTMLNode"] = None,
            props: dict[str, str] = None
    ):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError("to_html has not been implemented by a child class")
    
    def props_to_html(self):
        if self.props == None: return ""
        return "".join(list(map((lambda x: " " + '="'.join(x) + '"'), self.props.items())))
    
    def __repr__(self):
        return f"HTMLNode(tag={self.tag}, value={self.value}, children={self.children}, props={self.props})"
    
    def __eq__(self, other):
        return (
            self.tag == other.tag and
            self.value == other.value and
            self.children == other.children and
            self.props == other.props
        )