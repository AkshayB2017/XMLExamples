import xml.etree.ElementTree as ET
mytree = ET.parse('helloworld.xml')
myroot = mytree.getroot()
for child in myroot:  
    print(child.tag, child.attrib)
a=[]
b=[]
c=[]
for elem in myroot.iter():
    #print(elem.tag)
    #print(elem.text)
    a.append(elem.tag)
    b.append(elem.text)
    c.append(elem.attrib)
for i in range(len(a)):
    print(a[i],b[i],c[i])
    #print(b[i])

'''

for i in range(len(a)):
    
    #if(elem.tag=='op1'):
    #    print(elem.text)
    if(a[i]=='procedure'):
      print("func(")  
      if(a[i+1]=='parameter'):
          if(a[i+2]=='name' and a[i+3]=='type'):
              print(b[i+3], b[i+2],",")
              i+=3
    if(a[i]=='parameter'):
         if(a[i+1]=='name' and a[i+2]=='type'):
              print(b[i+2], b[i+1])
         if(a[i+3]=='exec'):
              print(")")

    
'''    



'''    
    if myroot[0].tag =='parameter':
           if(myroot[0][1].text)=='int_arr':
               print("int",myroot[1][0].text,"[],\t")
    if myroot[1].tag == 'parameter':
        if(myroot[1][1].text)=='int':
            print("int", myroot[2][0].text,"\t")

    print(elem.tag)

'''
'''
for neighbor in myroot.iter('neighbor'):
    print(neighbor.attrib)

f = open("linearsearch.xml", "r")
for x in f:
 if(x.strip()=="<procedure>"):
   print("function:")
 if(x.strip()=="<parameter>"):
    print("(")
 if(x.strip()=="<type>"):
    print("int")
 if(x.strip()=="<name>"):
    print("list")
'''
'''
print(myroot.tag)
print(myroot[1].tag)
print(myroot[2].tag)
print(myroot[2][0][0].tag)
print(myroot[2][0][0][0].text)
'''
'''
if(myroot.tag=='procedure'):
    print("function(\t")
    if myroot[0].tag =='parameter':
           if(myroot[0][1].text)=='int_arr':
               print("int",myroot[1][0].text,"[],\t")
    if myroot[1].tag == 'parameter':
        if(myroot[1][1].text)=='int':
            print("int", myroot[2][0].text,"\t")
'''