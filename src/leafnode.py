from htmlnode import HtmlNode

class LeafNode(HtmlNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, [], props)
        
    def to_html(self):
        attributes_value = ""
        
        if self.value == "":
            raise ValueError()
        
        if self.tag == None:
            return self.value
        
        if self.props == None:
            return f"<{self.tag}>{self.value}</{self.tag}>"
        
        for key, value in self.props.items():
            attributes_value += f' {key}="{value}"'
            
        return f"<{self.tag}{attributes_value}>{self.value}</{self.tag}>"