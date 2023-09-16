
from urllib.request import urlopen
from xml.etree.ElementTree import parse

"""
content 
http://planet.python.org/rss20.xml
<channel>
    <item>
        <link>
        </link>
    </item>
    <item>
        <link>
        </link>
    </item>
</channel>

"""

def rw_xml():
    # parse data from url
    u = urlopen ('http://planet.python.org/rss20.xml')
    doc = parse( u )
    
    # get data from url
    for item in doc.iterfind( 'channel/item' ):
        link  = item.findtext('link')
        print (link)

    print()
    print()
    # get uri = <protocol>://<domainName>/<pathPage>
    # print <domain>
    for item in doc.iterfind( 'channel/item' ):
        link  = item.findtext('link')
        print ( link[8:].split('/')[0] )

if __name__ == '__main__':
    rw_xml()