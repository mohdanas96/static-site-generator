from htmlnode import HtmlNode


class ParentNode(HtmlNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag=tag, children=children, props=props)

    def to_html(self):
        if self.tag == None:
            raise ValueError("tag is required")

        if len(self.children) == 0:
            raise ValueError("no children nodes to convert")

        child_html = ""
        for node in self.children:
            # recursively call .to_html() on all childrens
            child_html += node.to_html()

        return f"<{self.tag}{self.props_to_html()}>{child_html}</{self.tag}>"
