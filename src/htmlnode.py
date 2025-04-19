class HtmlNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
        
    def to_html(self):
        raise NotImplementedError()
    
    def props_to_html(self):
        text_prop = ''
        if self.props:
            for key, value in self.props.items():
                text_prop += f" {key}={value}"
        return text_prop
            
    def __repr__(self):
        return f"HtmlNode({self.tag}, {self.value}, {self.children}, {self.props})"