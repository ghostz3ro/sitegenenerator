from htmlnode import HtmlNode

class ParentNode(HtmlNode):
    def __init__(self, tag, children, props=None):
        super().__init__(props=props)
        self.tag = tag
        self.children = children

    def to_html(self):
        if self.tag is None:
            raise ValueError("tag must be defined for ParentNode")
        if not self.children:
            raise ValueError("children must be defined for ParentNode")
        return f"<{self.tag}>" + ''.join(child.to_html() for child in self.children) + f"</{self.tag}>"

    def __repr__(self):
        return f"ParentNode(tag={self.tag}, children={self.children}, props={self.props})"