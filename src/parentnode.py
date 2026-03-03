from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag=tag, value=None, children=children, props=props)

    def to_html(self):
        if self.tag is None:
            raise ValueError("All parent nodes must have a tag")
        if self.children is None:
            raise ValueError("All parent nodes must have children")
        else:
            children_string = ""
            for child in self.children:
                children_string += child.to_html()

            props_str = self.props_to_html()

            return f"<{self.tag}{props_str}>{children_string}</{self.tag}>"
