from xml.etree import ElementTree
content_list = []


def parse(path):
    file_open = open(path, 'rt')
    tree = ElementTree.parse(file_open)
    for node in tree.iter():
        content = node.tag, node.text
        content_list.append(content)
    for i in content_list:
        print(i)

print(parse('/home/ubuntu/Downloads/nasa.xml'))
