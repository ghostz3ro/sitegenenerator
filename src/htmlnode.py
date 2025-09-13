

class HtmlNode:
    def __init__(self, tag=None, content=None, children=None, props=None):
        self.tag = tag
        self.content = content
        self.children = children if children else []
        self.props = props if props else {}

    # def add_child(self, child_node):
    #     self.children.append(child_node)

    # def set_attribute(self, key, content):
    #     self.attributes[key] = content

    # def render(self):
#     attr_str = ' '.join(f'{key}="{value}"' for key, value in self.attributes.items())
    #     attr_str = f' {attr_str}' if attr_str else ''
    #     children_str = ''.join(child.render() for child in self.children)
    #     return f'<{self.tag}{attr_str}>{children_str}</{self.tag}>'
    
    def to_html(self):
        raise NotImplementedError("will be implemented in subclasses")
    
    def props_to_html(self):
        return ' '.join(f'{key}="{value}"' for key, value in self.props.items())
    
    def __repr__(self):
        return f"HtmlNode(tag={self.tag}, content={self.content}, children={self.children}, props={self.props})"
    

class LeafNode(HtmlNode):
    def __init__(self, tag=None, content=None, props=None):
        super().__init__(tag=tag, content=content, props=props)

    def to_html(self):
        if self.content is None:
            raise ValueError("content must be defined for LeafNode")
        if self.tag is None:
            return f'{self.content}'
        elif self.tag == "img":
            props_str = f' {self.props_to_html()}' if self.props else ''
            return f'<{self.tag}{props_str}>'
        else:
            props_str = f' {self.props_to_html()}' if self.props else ''
            return f'<{self.tag}{props_str}>{self.content}</{self.tag}>'

    def __repr__(self):
        return f"LeafNode(tag={self.tag}, content={self.content}, props={self.props})"
    

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