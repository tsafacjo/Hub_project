from ast import *

from render import *


class Visitor:
    

    def __init__(self, pp):
        
        
        self.pp = pp
        
        self.indentation = 0
               
        render_file_name=pp.name.replace('.html','.svg')
        
        self.render=Render(render_file_name) 
        

    # define   indentations

    def indent(self):
        self.indentation += 2

    def desindent(self):
        self.indentation -= 2

    # Foncion pour lancer le visiteur
    

    def doIt(self, ast):
        print( "----------------------VISITOR----------------------")
                
        self.render.init_render()
        
        self.visit_root(ast, None)
        
        self.render.close_render()
        
        print( "----------------------VISIT COMPLETED WITH SUCCCESS----------------------")
    
        

    # fonction pour afficher dans le terminal
    def say(self, txt):
        
        print( " " +str(self.indentation) + txt)

        
    def visit_declaration(self,declaration, args=None):
        
        self.say("visit_declaration")
        
        self.indent()
        
        self.pp.write(' <br/> <span class="autre"> type {}  identifier {} <span>ident {} </span></span>'.format(declaration.type_.name,declaration.identifier.name,self.indentation))
     
        if len(declaration.primaries)>0 :
            
            
            for primary in declaration.primaries :
                                
                  primary.accept(self,args)
                  
        self.pp.write(' <br/>  </span></span>')
                
#    start render 
             
        self.render.draw_item(declaration)                           
        self.desindent()
            

            
    def visit_statement(self,statement, args=None):
        
        self.say("visit_statement")
        
        self.indent()

        self.pp.write(' <br/> <span class="autre"> call fonction  {}  <span>ident {}   paramètres </span></span>'.format(statement.selectedobject_call_method,self.indentation))
              
        if len(statement.primaries)>0 :
                        
            for primary in statement.primaries :
                                
                  primary.accept(self,args)
               
        self.pp.write('  </span></span>')

#       Start rendering 
        
        self.render.draw_item(statement)
        
        self.desindent()     



    
    def visit_identifier(self, id, args=None):
        
        self.say("visit_identifier")
        
        self.indent()
        
        self.say(id.name)

        self.pp.write(' <br/> <span class="autre">Identifier   Name :{}  <span>ident {}</span></span> '.format(id.name,self.indentation))
        
        self.desindent()

        
    def visit_primary(self, primary, args=None):
        
        self.say("visit_primary")
        
        self.indent()
        
        self.say(primary.name)
        
        self.pp.write(' <br><span class="autre"> Primary  value :  {}   <span>   ident {} </span></span>'.format(primary.value,self.indentation))
        
        self.desindent()        
                
        
        
    def visit_hardware(self,hardware, args=None):
        
        self.say("visit_hardware")
        
        self.indent()
        
        self.desindent()
        
        self.pp.write('<p>')
        
        self.pp.write('<br/> <h2 class="autre"> visit   {}  <span> ident {} </span>  </h2>'.format('hardware',self.indentation))
              
        if len(hardware.declarations)>0:
            
            for declaration in hardware.declarations:
                
                declaration.accept(self,args)
                
        self.pp.write(' </p>')                
    

            
        
    def visit_network(self,network,args=None):
        
        self.say("visit_network")
        
        self.indent()

        self.pp.write('<p>')
        
        self.pp.write('<br/> <h2 class="autre"> visit   {} <span>ident {}</span></h2>'.format('Network',self.indentation))
                   
        if len(network.declarations)>0:
            
            for declaration in network.declarations:
                
                declaration.accept(self,args)
        
        self.desindent() 
        
        self.pp.write(' </p>')       
        
        
        
        
    def visit_service(self,service,args=None):
        
        self.say("visit_service")
        
        self.indent()

        self.pp.write('<br/> <h2 class="autre"> visit   {} <span>ident {}</span></h2>'.format('service',self.indentation))            
        
        if len(service.declarations)>0:
            
            for declaration in service.declarations:
                
                declaration.accept(self,args)
                
                
        self.desindent()
              
        self.pp.write(' </p>')  
                               
        
    def visit_configuration(self,configuration, args=None):
        
        self.say("visit_Configuration")
        
        self.indent()

        self.pp.write('<br/> <h2 class="autre"> visit   {} <span>ident {}</span></h2>'.format('Configuration',self.indentation))     
        
        if len(configuration.statements)>0:
            
            print(len(configuration.statements))
            
            for statement in  configuration.statements:
                
                statement.accept(self,args)
                                
        self.desindent() 
        
        

    
    def visit_root(self, root, args=None):
        
        self.say("visit_root")
        self.indent()
        self.pp.write('<p>Root\n')
        
        if root.hardware:
               
            root.hardware.accept(self,args)

        if root.network:
                             
            root.network.accept(self,args)
                                    
        if root.service:
                                   
            root.service.accept(self,args)
            
            
        if root.configuration:
                       
            root.configuration.accept(self,args) 
                            
        self.pp.write('</p>\n')
                
        self.desindent()
        
        
        
 