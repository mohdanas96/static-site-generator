import unittest

from htmlnode import HtmlNode
from textnode import TextNode, TextType

class TestHtmlNode(unittest.TestCase):
    def test_props_to_html(self):
        props_test = {
            "href": "https://google.com",
            "target": "_blank"
        }
        html_node = HtmlNode("<a>", props=props_test)
        props_html = html_node.props_to_html()
        self.assertEqual(props_html, f" href={props_test['href']} target={props_test['target']}")
        
    def test_repr_(self):
        children_nodes = [HtmlNode(tag="<a>", value="Click me"), TextNode(text="Hello world", text_type=TextType.BOLD)]
        html_node = HtmlNode(tag="<div>", value="div tag", children=children_nodes, props={"id:main-div, lang:en"})
        self.assertEqual(html_node.__repr__(), "HtmlNode(<div>, div tag, [HtmlNode(<a>, Click me, None, None), TextNode(Hello world, TextType.BOLD, None)], {'id:main-div, lang:en'})")
        
    def test_missing_values(self):
        html_node = HtmlNode(tag="<a>", value="Click me")
        assert html_node.tag is "<a>"
        assert html_node.value is "Click me"
        assert html_node.children is None
        assert html_node.props is None
        
if __name__ == "__main__":
    unittest.main()