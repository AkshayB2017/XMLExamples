import xml.etree.ElementTree as ET
def converterc():
    header_file()
    mapper(i)

def header_file():
    
def mapper(j):
    for i in range(j,len(tag)-1):
        if(tag[i]=='expression'):
            expression(i)
        if(tag[i]=='assignment'):
            assigment(i)
        if(tag[j]=='if'):
            if_expression(i)
        if(tag[i]=='else'):
            else_expression(i)
        if(tag[i]=='print'):
            print_expression(i)
        if(tag[i]=='input'):
            input_expression(i)
        if(tag[i]=='main'):
            main_func(i)
    f.write("return 0;\n")
    f.write("}")
    
def main_func(i):
    

def expression(i):
    

def variable(i):
  
def operator(i):
    f.write(text[i+1])
    i+=1


def assignment(i):
   
def if_expression(i):
   
def else_expression(i):
   

def for_loop(i):
   
def function(i):
    
def print_expression(i):
    

def input_expression(i):
    

file=input("Enter file to be parsed:")
file=file.lstrip()
mytree = ET.parse(file)
myroot = mytree.getroot()

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
i=0
f=open("final.txt","w")
converterc()


