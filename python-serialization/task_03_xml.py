import xml.etree.ElementTree as ET
def serialize_to_xml(dictionary, filename):
    root = ET.Element("data")
    for (key, value) in dictionary.items():
        ET.SubElement(root, key).text = str(value)
    tree = ET.ElementTree(root)
    tree.write(filename)
def deserialize_from_xml(filename):
    root = ET.parse(filename).getroot()
    dictionary = {}
    for child in root:
        value = int(child.text) if child.text.isdigits() else child.text
        dictionary[child.tag] = value
    return dictionary
