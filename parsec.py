import sys
import xml.etree.ElementTree as ET
i=0
file=input("Enter file to be parsed")
mytree = ET.parse(file)
myroot = mytree.getroot()
for child in myroot:  
    i+=1
    #print(child.tag, child.attrib)
tag=[]
text=[]
attribute=[]
for elem in myroot.iter():
    #print(elem.tag)
    #print(elem.tag)
    #print(elem.attrib)
    #print(elem.text)
    tag.append(elem.tag)
    text.append(elem.text)
    attribute.append(elem.attrib)
var_count=0

for key, value in attribute[1]: 
    print (key, value) 

