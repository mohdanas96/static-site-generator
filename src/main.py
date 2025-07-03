from textnode import TextNode, TextType, text_node_to_html_node

def main():
    textnode = TextNode("hello world", TextType.BOLD)
    print(text_node_to_html_node(textnode))
    
main()