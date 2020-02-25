import xml.etree.ElementTree as ET



def expression(i):
    if(tag[i+1]=='constant') or (tag[i+1]=='variable'):
        f.write(text[i+1])
    if(tag[i+1]=='function_call'):
        f.write(text[i+1])
    f.write(";")
    i+=2

def assignment(i):
    if(tag[i+1]=='variable'):
        f.write(text[i+2])
        f.write('')
        f.write(text[i+3])
        f.write('= ')
        if(tag[i+4]=='expression'):
            expression()
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
    body()
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
    body()
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
    f.write("\"<<endl;")
    i+=1

def input_expression(i):
    f.write("cin>>\"")
    f.write(text[i])
    f.write("\">>endl;")  
    i+=1


def mapper(i):
    while(i!=len(tag)):
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





file=input("Enter file to be parsed")
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
mapper(i)    