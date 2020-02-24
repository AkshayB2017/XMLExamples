import sys
import xml.etree.ElementTree as ET

header=['#include<stdio.h>',
'#include<string.h>', 
'#include<conio.h>',
'#include<stdlib.h>',
'#include<math.h>',
'#include<ctype.h>',
'#include<time.h>',
'#include<assert.h>']
#Functions
def print_main():
    f.write('int main(){\n')
def print_end():
    f.write('}\n')
def print_statement(int i):
    f.write('cout<<"')
    f.write(text[i])
    f.write('"<<endl;\n')
def assignment():
    f.write('')







#Main Program
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
for i in range(len(header)):
    f.write(header[i])
for i in range(len(tag)):
    if(tag[i]=='main'):
        print_main()
    if(tag[i]=='end'):
        print_end()
    if(tag[i]=='print')
        print_statement(i)
    if(tag[i]=='assignment'):
        assignment()