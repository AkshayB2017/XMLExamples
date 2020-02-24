import sys
import xml.etree.ElementTree as ET
file="xmlinput.xml"
mytree=ET.parse(file)
myroot= mytree.getroot()
tag=[]
text=[]
for elem in myroot.iter():
    tag.append(elem.tag)
    text.append(elem.text)


var_count=0
f=open("final.txt","w")
for i in range(len(tag)):
    