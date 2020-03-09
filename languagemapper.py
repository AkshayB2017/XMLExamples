from .mappercpp import convertercpp
from .mapperc import converterc
from .mapperjava import converterjava
from .mapperpython import converterpython
file= open("intermediate.xml","r")
#Integrate with Django code as per how to access the language item from database @Aman
language='C' #Modify here


if(language=='C'):
    converterc()

if(language=='Python'):
    converterpython()

if(language=='CPP'):
    convertcpp()

if(language=='Java'):
    converterjava()

