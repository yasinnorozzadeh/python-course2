import xml.etree.ElementTree as ET
mytree = ET.parse('food.xml')
myroot = mytree.getroot()
for x in myroot.findall('food'):
    item =x.find('item').text
    price = x.find('price').text
    print(item, price)

for description in myroot.iter('description'):
     new_desc = str(description.text)+'wil be served'
     description.text = str(new_desc)
     description.set('updated', 'yes')
 
mytree.write('new.xml')
myroot[0].remove(myroot[0][0])
mytree.write('output6.xml')
myroot[0].clear()
mytree.write('output7.xml')