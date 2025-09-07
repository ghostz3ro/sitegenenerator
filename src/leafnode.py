from htmlnode import HtmlNode

class LeafNode(HtmlNode):
    def __init__(self, tag=None, content=None, props=None):
        super().__init__(tag=tag, content=content, props=props)

    def to_html(self):
        if not self.content:
            raise ValueError("content must be defined for LeafNode")
        if self.tag is None:
            return f'{self.content}'
        else:
            return f'<{self.tag}>{self.content}</{self.tag}>'

    def __repr__(self):
        return f"LeafNode(tag={self.tag}, content={self.content}, props={self.props})"
    
