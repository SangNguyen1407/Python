"""
print Json

{
    'test1': 'http://www.w3.org/1999/xhtml', 
    'test2': 'http://www.w3.org/1999/xhtml', 
    'test3': 'http://www.w3.org/1999/xhtml', 
    'test4': 'http://www.w3.org/1999/xhtml'}
}
"""
import json

class XMLNamespaces:
    def __init__(self, **args):
        self.namespaces = {}
        for name, uri in args.items():
            self.register(name, uri)

    def write_json_file(self):
        with open('mydata.txt', 'w', encoding='utf-8') as wf:
            json.dump( self.namespaces, wf )

    def register(self, name, uri):
        self.namespaces['test1'] = uri
        self.namespaces['test2'] = uri
        self.namespaces['test3'] = uri
        self.namespaces['test4'] = uri
        print ( self.namespaces )
        self.write_json_file()

if __name__ == '__main__':
    ns = XMLNamespaces(html='http://www.w3.org/1999/xhtml')