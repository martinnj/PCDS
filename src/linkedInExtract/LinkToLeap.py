# from xml.dom import minidom
# from BeautifulSoup import BeautifulSoup
import xml.etree.ElementTree as ET

class LinkedInExtraction(object):
    id = 
    first_name = 
    last_name = 
    headline = 
    profile_url =

class Education(object):
    id

xml = """ <?xml version="1.0" encoding="UTF-8"?>
            <person>
                <id>1R2RtA</id>
                <first-name>Frodo</first-name>
                <last-name>Baggins</last-name>
                <headline>Jewelery Repossession in Middle Earth</headline>
                <site-standard-profile-request>
                    <url>https://www.linkedin.com/profile/view?id=</url>
                </site-standard-profile-request>
            </person>
    """

tree = ET.parse('test.xml')
root = tree.getroot()
for child in root:
    if (child.tag == "site-standard-profile-request"):
        for subChild in child:
            print subChild.text
    print child.tag, child.text


def extractPerson(root):
    for child in root:
        if(child.tag == "site-standard-profile-request"):
            



# bsXML = BeautifulSoup(xml)

# print bsXML.person.findAll("id")

# def getText(nodelist):
    # rc = []
    # for node in nodelist:
        # if node.nodeType == node.TEXT_NODE:
            # rc.append(node.data)
    # return ''.join(rc)

# xmldoc = minidom.parse('test.xml')
# print getText(xmldoc)
# print getText(xmldoc.childNodes)
# print xmldoc.childNodes.childNode
# itemlist = xmldoc.getElementsByTagName('id') 
# print len(itemlist)
# print itemlist[0]
# print itemlist[0].attributes['id'].value
# print itemlist[0].value
# print itemlist[0].attributes['name'].value
# for s in itemlist :
        # print s.attributes['name'].value

