import xml.etree.ElementTree as ET
def header_file():
    f.write('#include<stdio.h>\n')
    f.write('#include<stdlib.h>\n')
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
    f.write("int main()\n{\n")

def expression(i):
    if(tag[i+1]=='constant'):
        f.write(text[i+1])
        i+=1
    if(tag[i+1]=='variable'):
        f.write(text[i+2])
        if(tag[i+3]=='operator'):
            f.write(text[i+3])
            if(tag[i+4]=='expression'):
                expression(i+4)
            if(tag[i+4]=='variable'):
                f.write(text[i+5])
                i+=5


    if(tag[i+1]=='function_call'):
        f.write(text[i+1])
    f.write(";")
def variable(i):
    if(tag[i+1]=='var_name'):
        f.write(text[i+1])
        i+=1
        f.write(';\n')
    if(tag[i+1]=='var_type'):
        f.write(text[i+1])
        f.write('')
        f.write(text[i+2])
        f.write(';\n')
        i+=2
def operator(i):
    f.write(text[i+1])
    i+=1


def assignment(i):
    if(tag[i+1]=='variable'):
        f.write(text[i+2])
        f.write('')
        f.write(text[i+3])
        f.write('=')
        if(tag[i+4]=='expression'):
            expression(i)
            
    f.write(";")

def if_expression(i):
    f.write('if(')
    if(tag[i+1]=='condition'):
        expression()
        f.write(text[i+3])
        expression()
        f.write(')')
        f.write("{\n")
        mapper(i)
        f.write("\n}")
    
def else_expression(i):
    f.write('else {\n')
    mapper(i)
    f.write('\n }')

def for_loop(i):
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
    mapper(i)
    f.write('\n}')

def function(i):
    f.write(tag[i+1])
    f.write(tag[i+2])
    i+=3
    if(tag[i]=='func_arg'):
        while(tag[i]!='body'):
            f.write(text[i+1])
            f.write(text[i+2])
            i+=2
    if(tag[i]=='body'):
        mapper(i)
def print_expression(i):
    f.write("cout<<\"")
    f.write(text[i])
    f.write("\"<<endl;\n")
    

def input_expression(i):
    f.write("cin>>")
    f.write(text[i])
    f.write(">>endl;\n")  
    i+=1

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
header_file()

mapper(i)    


