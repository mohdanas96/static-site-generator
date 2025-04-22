import unittest
from textnode import TextNode, TextType
from utils import split_nodes_delimiter, extract_markdown_images, extract_markdown_links

class TestUtils(unittest.TestCase):
    def test_split_nodes_delimiter_basic(self):
        # Create a test node
        node = TextNode("This is text with a `code block` word", TextType.NORMAL)

        # Call the function we're testing
        result = split_nodes_delimiter([node], "`", TextType.CODE)

        # Expected output: 3 nodes
        assert len(result) == 3

        # Check the first node
        assert result[0].text == "This is text with a "
        assert result[0].text_type == TextType.NORMAL

        # Check the second node
        assert result[1].text == "code block"
        assert result[1].text_type == TextType.CODE

        # Check the third node
        assert result[2].text == " word"
        assert result[2].text_type == TextType.NORMAL

        print("Basic test passed!")
        
    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)
