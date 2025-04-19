from textnode import Textnode, TextType

def main():
    textnode = Textnode("hello world", TextType.BOLD_TEXT)
    print(textnode)
    
main()