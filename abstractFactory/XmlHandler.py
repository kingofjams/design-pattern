import xml.dom.minidom


class XmlHandler:
    def __init__(self):
        self.dom = xml.dom.minidom.parse('abc.xml')
        self.root = self.dom.documentElement

    def get_type(self, type):
        sections = self.root.getElementsByTagName('FactorySection')
        for x in sections:
            if x.name == type:
                return x.type

    def get_name(self, name):