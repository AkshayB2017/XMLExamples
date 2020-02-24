import sys
import xml.etree.ElementTree as ET
indent=0

def print_main():
    f.write("if __name__== \"__main__\":\n  main() \n def main():")
    global indent
    indent+=1
def print_statement():
    for j in range(indent):
        f.write('')
    f.write("print(\"")
    f.write(text[i])
    f.write("\")")
    print("\t"*indent,"print(\"",text[i],"\")")
def input_statement():
    for j in range(indent):
        f.write('')
    f.write("input(\"")
    f.write(text[i])
    f.write("\")")
    print("\t"*indent,"input(\"",text[i],"\")")
def initialize_int():
    var_count=1
    for j in indent:
        f.write('')
    f.write(text[i+1])
    f.write(" ")
    f.write(text[i+2])
    print("\t"*indent,text[i+1]," ",text[i+2])
    for j in range(i+1,len(tag)):
        if tag[j]=='variable':
            print(",",text[j+2])
            f.write(",")
            f.write(text[j+2])
def open_bracket():
    print("(")
    f.write("(")
def close_bracket():
    print(")")
    f.write(")")
#def expression():

def assignment():
    print("\t"*indent,text[i+2],text[i+3],text[i+1])
    for j in range(indent):
        f.write('')
    f.write(text[i+2])
    f.write(text[i+3])
    f.write(text[i+1])



    #print("\t",text[i+3],"=",text[i+1],"",text[i+4],text[i+2])
#def variable_define(int i):
#    print("\t")



file=input("Enter file to be parsed")
mytree = ET.parse(file)
myroot = mytree.getroot()
for child in myroot:  
    print(child.tag, child.attrib)
tag=[]
text=[]
for elem in myroot.iter():
    #print(elem.tag)
    #print(elem.text)
    tag.append(elem.tag)
    text.append(elem.text)
var_count=0
f=open("final.txt","w")
for i in range(len(tag)):
    if(tag[i]=='main'):
        print_main()
        f.write("\n")
    if(tag[i]=='write'):
        print_statement()
        f.write("\n")
    if(tag[i]=='input'):
        input_statement()
        f.write("\n")
    if(tag[i]=='variable' and var_count==0 and text[i+1]=='int'):
        initialize_int()
        f.write("\n")
    if(tag[i]=='initialize'):
        print("\t",text[i+1]," ",text[i+2])
        f.write("\n")
    if(tag[i]=='assignment'):
        assignment()
        f.write("\n")
        
    if(tag[i]=='open_bracket'):
        open_bracket()
    if(tag[i]=='close_bracket'):
        close_bracket()
    if(tag[i]=='expression'):
        expression()
    if(tag[i]=='assignment'):
        assignment()
  #      if(tag[i+1]=='variable'):

   #     else if(tag[i+1]=='constant'):

    
        '''
        assignment cases:
        c=tag+text
        c=tag-text
        c=tag*text
        c=tag/text
        c=tag%text
        text=c
        text=text+c
        text=text-c
        text=text*c
        text=text/c
        text=text%c

        '''


    
    
