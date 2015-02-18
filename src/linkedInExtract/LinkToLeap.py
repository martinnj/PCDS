from xml.dom import minidom

xmldoc = minidom.parse('test.xml')
print xmldoc
print getText(xmldoc.childNodes)
print xmldoc.childNodes.childNodes
# itemlist = xmldoc.getElementsByTagName('id') 
# print len(itemlist)
# print itemlist[0]
# print itemlist[0].attributes['id'].value
# print itemlist[0].value
# print itemlist[0].attributes['name'].value
# for s in itemlist :
        # print s.attributes['name'].value
