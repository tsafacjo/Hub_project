# -*- coding: utf-8 -*-

from visitor import Visitor


class AstNode :
    
    
    def accept(self, visitor, arg):
        nom = self.__class__.__name__
        nomMethode = getattr(visitor, "visit_" + nom.lower())
        nomMethode(self, arg)

class Root(AstNode):
    
    
    
    def __init__(self):
        
        
          
        self.hardware=None
        self.network=None
        self.service=None
        self.config=None
        self.processing=None 
    
    


    
class Hardware(AstNode):
    
    
    def __init__(self):
        
        self.declarations=[]
        
        
        

class Network(AstNode):

    
        def __init__(self):
            
            
            self.declarations=[]
            
            
            
            
            
class Service (AstNode):

       def __init__(self):
           
           
           self.declarations=[]
           
           
class Configuration(AstNode):           
        
       def __init__(self):
           
           self.statements=[]
           
           
class Processing(AstNode):

        def __init__(self,statements):

                self.statements=statements          
           
               

    
# =============================================================================
# #  DECLARATIONS       
# =============================================================================
        
class Declaration(AstNode):
    
       def __init__(self):
           
                   self.type_=None
                   self.identifier=None
                   self.primaries=[]



            
class Type(AstNode):    
            
    def __init__(self,name):
        
        self.name=name
            
            
            
class Primary(AstNode):
    

    def __init__(self,name=None,value=None):
        
        self.name=name
        self.value=value

      
        
class Statement(AstNode):
    
        def __init__(self):

            self.selectedobject_call_method=None
            self.primaries=[]
            
                    
            



class Assignement(AstNode):
    
        def __init__(self,assigne,expression):
            
            self.assigne=assigne
            self.expression=expression


class Identifier(AstNode):
    
       def __init__(self,name):
           
           self.name=name



