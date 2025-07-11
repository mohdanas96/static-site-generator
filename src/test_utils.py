import unittest
from textnode import TextNode, TextType
import utils
from blocktype import BlockType


class TestUtils(unittest.TestCase):
    def test_split_nodes_delimiter_basic(self):
        # Create a test node
        node = TextNode("This is text with a `code block` word", TextType.NORMAL)

        # Call the function we're testing
        result = utils.split_nodes_delimiter([node], "`", TextType.CODE)

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

    def test_extract_markdown_images(self):
        matches = utils.extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_split_images(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.NORMAL,
        )
        new_nodes = utils.split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.NORMAL),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.NORMAL),
                TextNode(
                    "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
        )

    def test_plain_to_textnodes(self):
        text = "Hy my name is boots"
        nodes = utils.text_to_textnodes(text)
        self.assertListEqual([TextNode("Hy my name is boots", TextType.NORMAL)], nodes)

    def test_bold_text_to_textnodes(self):
        text = "Hy my name is **boots**"
        nodes = utils.text_to_textnodes(text)
        self.assertListEqual(
            [
                TextNode("Hy my name is ", TextType.NORMAL),
                TextNode("boots", TextType.BOLD),
            ],
            nodes,
        )

    def test_all_to_textnodes(self):
        text = "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        nodes = utils.text_to_textnodes(text)
        self.assertListEqual(
            [
                TextNode("This is ", TextType.NORMAL),
                TextNode("text", TextType.BOLD),
                TextNode(" with an ", TextType.NORMAL),
                TextNode("italic", TextType.ITALIC),
                TextNode(" word and a ", TextType.NORMAL),
                TextNode("code block", TextType.CODE),
                TextNode(" and an ", TextType.NORMAL),
                TextNode(
                    "obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"
                ),
                TextNode(" and a ", TextType.NORMAL),
                TextNode("link", TextType.LINK, "https://boot.dev"),
            ],
            nodes,
        )

    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = utils.markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_markdown_to_blocks_with_extra_newlines(self):
        md = """
        

This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items


"""
        blocks = utils.markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )
        
    def test_heading_block_to_heading_type(self):
        block = "# This is a heading"
        type = utils.block_to_block_type(block)
        self.assertEqual(type, BlockType.HEADING)
        
    def test_code_block_to_code_type(self):
        block = "```this is a code block```"
        type = utils.block_to_block_type(block)
        self.assertEqual(type, BlockType.CODE)
        
    def test_quote_block_to_quote_type(self):
        block = "> this is a quote type"
        type = utils.block_to_block_type(block)
        self.assertEqual(type, BlockType.QUOTE)
    
    def test_unordered_list_block_to_unordered_list_type(self):
        block = '''- First item
        - Second item
        - Third item
        '''
        type = utils.block_to_block_type(block)
        self.assertEqual(type, BlockType.UNORDERED_LIST)
        
    def test_ordered_list_block_to_ordered_list_type(self):
        block = '''1. First item
        2. Second item
        3. Third item
        '''
        type = utils.block_to_block_type(block)
        self.assertEqual(type, BlockType.ORDERED_LIST)
    
    def test_paragraph_to_paragraph_type(self):
        block = "This is a pargraph of text"
        type = utils.block_to_block_type(block)
        self.assertEqual(type, BlockType.PARAGRAPH)
        