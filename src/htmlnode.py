

class HtmlNode:
    def __init__(self, tag=None, attributes=None, children=None, props=None):
        self.tag = tag
        self.attributes = attributes if attributes else {}
        self.children = children if children else []
        self.props = props if props else {}

    # def add_child(self, child_node):
    #     self.children.append(child_node)

    # def set_attribute(self, key, value):
    #     self.attributes[key] = value

    # def render(self):
    #     attr_str = ' '.join(f'{key}="{value}"' for key, value in self.attributes.items())
    #     attr_str = f' {attr_str}' if attr_str else ''
    #     children_str = ''.join(child.render() for child in self.children)
    #     return f'<{self.tag}{attr_str}>{children_str}</{self.tag}>'
    
    def to_html(self):
        raise NotImplementedError("Not implemented yet")
    
    def props_to_html(self):
        return ' '.join(f'{key}="{value}"' for key, value in self.props.items())
    
    def __repr__(self):
        return f"HtmlNode(tag={self.tag}, attributes={self.attributes}, children={self.children}, props={self.props})"