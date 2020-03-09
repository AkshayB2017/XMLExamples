import sys
import xml.etree.ElementTree as ET
i=0
def expression():
    if(tag[i+1]=='constant') or (tag[i+1]=='variable'):
        f.write(text[i+1])
    if(tag[i+1]=='function_call'):
        f.write(text[i+1])
    f.write(";")

def assignment():
    if(tag[i+1]=='variable'):
        f.write(text[i+2])
        f.write('')
        f.write(text[i+3])
        f.write('= ')
        if(tag[i+4]=='expression'):
            expression()
    f.write(";")

def if_expression():
    f.write('if(')
    if(tag[i+1]=='condition'):
        expression()
        f.write(text[i+3])
        expression()
        f.write(')')
        f.write("{\n")
        body()
        f.write("\n}")
def else_expression():
    f.write('else {\n')
    body()
    f.write('\n }')

def for_loop():
    f.write('for(')
    while(tag[i]!='loop_update'):
        if(tag[i]=='loop_initialization'):
            if(tag[i]=='assignment'):
                assignment()
            if(tag[i]=='loop_condition'):
                if(tag[i+1]=='expression'):
                    expression()
        i+=1
    if(tag[i]=='loop_update'):
        if(tag[i+1]=='assignment'):
            assignment()
    f.write(')\n{\n')
    body()
    f.write('\n}')

def function():
    f.write(tag[i+1])
    f.write(tag[i+2])
    i+=3
    if(tag[i]=='func_arg'):
        while(tag[i]!='body'):
            f.write(text[i+1])
            f.write(text[i+2])
            i+=2
    if(tag[i]=='body'):
        body()
def print():
    f.write("cout<<\"")
    f.write(text[i])
    f.write("\"<<endl;")

def input():
    f.write("cin>>\"")
    f.write(text[i])
    f.write("\">>endl;")  

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
for i in range(len(tag)):
    if(tag[i]=='expression'):
        expression(i)
    if(tag[i]=='assignment'):
        assigment(i)
    if(tag[i]=='if'):
        if_expression(i)
    if(tag[i]=='else'):
        else_expression(i)
    if(tag[i]=='print'):
        print_expression(i)
    if(tag[i]=='input'):
        input_expression(i)

