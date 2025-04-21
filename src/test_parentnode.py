import unittest
from parentnode import ParentNode
from leafnode import LeafNode

class TestParentNode(unittest.TestCase):
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")
        
    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
        parent_node.to_html(),
        "<div><span><b>grandchild</b></span></div>",
        )
        
    def test_to_html_with_multiple_children(self):
        leaf_node = LeafNode("b", "this is bold")
        grandchild_node = LeafNode("i", "this is italic")
        child_node = ParentNode("h1", [grandchild_node])
        parent_node = ParentNode("div", [child_node, leaf_node])
        self.assertEqual(parent_node.to_html(), "<div><h1><i>this is italic</i></h1><b>this is bold</b></div>")
        
    def test_to_html_with_no_children(self):
        parent_node = ParentNode("div", [])
        with self.assertRaises(ValueError):
            parent_node.to_html()