from ast import *
from parser import Parser
import sys
import os

class Compiler:

    def __init__(self):
        print ("HUB COMPILER")
        self.parser = Parser()

    def compile(self, filename,nameHtml):
        print ("COMPILING " + filename)
        ast = self.parser.parse(filename)
        self.simple_visit(ast,nameHtml)

    def simple_visit(self, ast,nameHtml):
        #delete the file if exists
        
        if os.path.exists(nameHtml):
            os.remove(nameHtml)
        # we create the  pretty printer in add mod 
        
        pp = open(nameHtml, 'a')
        # starting  pretty printer
        pp.write('<!DOCTYPE html>\n')
        pp.write('<html>\n')
        pp.write('<head>\n')
        pp.write('<meta charset="utf-8" />\n')
        pp.write('<link rel="stylesheet" href="style.css" />\n')
        pp.write('<title>' + nameHtml + '</title>\n')
        pp.write('</head>\n')
        pp.write('<body>\n')
        #viitor creation 
        visitor = Visitor(pp)
        visitor.doIt(ast)
        # end  pretty printer
        pp.write('</body>\n')
        pp.write('</html>')
        # close the file 
        pp.close()

if __name__ == '__main__':
    compiler = Compiler()
    
    # we check if we miss some arguments
    if (len(sys.argv)==1):
        
        
        print( "hub file needed !")
        sys.exit(1)
    elif (len(sys.argv)==2):
        print ("html name needed !")
        sys.exit(1)
    else:
        compiler.compile(sys.argv[1],'Render/'+sys.argv[2])
        

        print( "_______________________________________________________________________________\n")                 
        print( "Compilition completed  with success")    
        print( "Results:\n  \t- visit file :{} \n \t- render:     {}  ".format('Render/'+sys.argv[2], ('Render/'+sys.argv[2]).replace('html','svg') ))           
        