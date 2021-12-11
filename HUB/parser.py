import sys
from indent import Indent
from ast import *
from lexer import Lexer



class Parser:

    TYPE = ['CLUSTER','COMPUTER', 'NETWORK', 'SERVICE']
    STATEMENT_STARTERS = ['SEMICOLON','LBRACE', 'IDENTIFIER', 'IF', 'WHILE','SELECTED_NAME']
    REL_OP = ['LT', 'LTE', 'GT', 'GTE']
    MUL_OP = ['MUL', 'DIV']
    ADD_OP=['ADD','SUB']
    LITERAL = ['INTEGER_LIT', 'FLOAT_LIT', 'CHAR_LIT','STRING_LIT']
    
    PRIMARY=LITERAL+['IDENTIFIER']


    def __init__(self, verbose=False):
        self.indentator = Indent(verbose)
        self.tokens = []
        self.errors = 0

    def show_next(self, n=1):
        try:
            return self.tokens[n - 1]
        except IndexError:
            print('ERROR: no more tokens left!')
            sys.exit(1)

    def expect(self, kind):
        actualToken = self.show_next()
        actualKind = actualToken.kind
        actualPosition = actualToken.position
        if actualKind == kind:
            return self.accept_it()
        else:
            print('Error at {}: expected {}, got {} instead'.format(str(actualPosition), kind, actualKind))
            sys.exit(1)

    # same as expect() but no error if not correct kind
    def maybe(self, kind):
        if self.show_next().kind == kind:
            return self.accept_it()

    def accept_it(self):
        token = self.show_next()
        output = str(token.kind) + ' ' + token.value
        self.indentator.say(output)
        return self.tokens.pop(0)

    def remove_comments(self):
        result = []
        in_comment = False
        for token in self.tokens:
            if token.kind == 'COMMENT':
                pass
            elif token.kind == 'LCOMMENT':
                in_comment = True
            elif token.kind == 'RCOMMENT':
                in_comment = False
            else:
                if not in_comment:
                    result.append(token)
        return result

    def parse(self,FileName):
        
        try:
            with open(FileName, 'r') as testFile:
                FileData = testFile.readlines()
        except FileNotFoundError:
            print('Error: test file {} does not exist'.format(FileName))
            sys.exit()
    
        lexer = Lexer()
        tokens = lexer.lex(FileData)               
        self.tokens = tokens
        self.tokens = self.remove_comments()   
        ast= Root()
        
        self.indentator.indent('Parsing Program')

# parse Hardware  
        
        hardware=self.parse_hardware()        
        ast.hardware=hardware
        
#parse network

        network=self.parse_network()
        ast.network=network
        
# service service 
        
        service=self.parse_service()        
        ast.service=service    
        
  
# parse configuration 
        

        configuration= self.parse_configuration()         
        ast.configuration=configuration
   
# parse Procssing

        self.parse_processing()                   
        self.indentator.dedent()
        if (self.errors == 1):
            print('WARNING: 1 error found!')
        elif (self.errors > 1):
            print('WARNING: ' + str(self.errors) + ' errors found!')
        else:
            print('parser: syntax analysis successful!')
            
            return ast
                        
 


    def parse_hardware(self):
        
        
        
        self.indentator.indent('Parsing Hardware')        
        
        hardware= Hardware()
        
        self.expect('HARDWARE_DECLARATION')
        
        self.expect('LBRACE')
        
        declarations=self.parse_declarations()
        
        self.expect('RBRACE') 
        
        hardware.declarations.extend(declarations)
        
        self.indentator.dedent()

        
        return hardware


    def parse_network(self):
        
        self.indentator.indent('Parsing Network')                
        
        
        network= Network()
        
        self.expect('NETWORK_DECLARATION')
        
        self.expect('LBRACE')
        
        declarations=self.parse_declarations()
        
        self.expect('RBRACE')
        
        network.declarations.extend(declarations)
        
        self.indentator.dedent()        
        
        return network
        
                
    def parse_service(self):


        self.indentator.indent('Parsing Service')                
           
        service=Service()
        
        self.expect('SERVICE_DECLARATION')
        
        self.expect('LBRACE')
        
        declarations=self.parse_declarations()
        self.expect('RBRACE')
        
        service.declarations.extend(declarations)
        
        self.indentator.dedent()
             
        return service


    def parse_configuration(self):

        self.indentator.indent('Parsing Configuration')    
        
        
        configuration=Configuration()
        
        print('ok config')
        
        self.expect('CONFIG_DECLARATION')

        self.expect('LBRACE')
        
        statements=self.parse_statements()
        
        configuration.statements.extend(statements)
        
        self.expect('RBRACE')

        self.indentator.dedent()
        
        return configuration
        
    def parse_processing(self):
        
        

        self.indentator.indent('Parsing Processing')      
        self.expect('PROCESSING_DECLARATION')
        self.expect('LBRACE')
        self.parse_statements()
        self.expect('RBRACE')        
        self.indentator.dedent()             
        

    def parse_declaration(self):

        self.indentator.indent('Parsing Declaration')    
        
        declaration=Declaration()
        
        self.accept_it()
        
        declaration.identifier =Identifier(self.expect('IDENTIFIER').value)
        
        
        self.expect('ASSIGN') 
        
        if self.show_next().kind in self.TYPE:
            
            declaration.type_=Type( self.accept_it().value)
            
            self.expect('LPAREN')  
            
            if  self.show_next().kind in self.PRIMARY:
                
                    
                  token=  self.accept_it()
                  
                  primary= Primary(token.kind,token.value)
                  
                  declaration.primaries.append(primary)
                  
            
                  while self.show_next().kind=='COMMA':
                        
                        
                        self.accept_it()
                        
        
                        if  self.show_next().kind in self.PRIMARY:
                                                                    
                             
                              token=self.accept_it()
                              
                              primary= Primary(token.kind,token.value)
                              
                              declaration.primaries.append(primary)
                              
                                 
            self.expect('RPAREN')

            
        else :
                
                self.errors+=1
                print("Error  excepts Constructor"+str(self.show_next().position))
                

            
        self.expect('SEMICOLON') 
        
        self.indentator.dedent()            

        return declaration
        
        
    def parse_declarations(self):
        
        declarations=[]
        self.indentator.indent('Parsing Declarations')

        while self.show_next().kind in self.TYPE :
            
            
            declaration=self.parse_declaration()
            declarations.append(declaration)
                        
 
            
        self.indentator.dedent() 
        
        return declarations
        

  

    def parse_statements(self):
        
        
        self.indentator.indent('Parsing Declaration')    
        
        
        self.indentator.indent('Parsing Statements')
        # TODO
        
        statements=[]
        
        while self.show_next().kind in self.STATEMENT_STARTERS:
            
            
            statements.append(self.parse_statement())
            
            
            
                       
        
        self.indentator.dedent()
        
        self.indentator.dedent() 
        
        return statements



    def parse_statement(self):
        
        self.indentator.indent('Parsing Statement ')            
        
        statement=Statement()
        

        
        
        self.indentator.indent('Parsing Statement ici')


        if self.show_next().kind=='LBRACE':
                

                self.parse_block()
                     

                
        elif self.show_next().kind=='SELECTED_NAME':
                
                
               statement.selectedobject_call_method=self.accept_it().value
               
                
               primaries=self.parse_call()
                
               statement.primaries.extend(primaries)

                
                
        else :
         raise NameError('expecting one of #{[:ident,:lparen,:literal]}. Got #{showNext.kind}')
    
        self.indentator.dedent()
        
        
        self.indentator.dedent()         
        
        return statement
  

                    
        
    def parse_call(self):
        

          self.indentator.indent('Parsing call ')               
          primaries=[]
          
          self.indentator.indent('Parsing call')
          self.expect('LPAREN')
          
          
          
            
          if  self.show_next().kind in self.PRIMARY :
                    
                    token=self.accept_it()
                    
                    primary=Primary(token.kind,token.value)
                    
                    primaries.append(primary)
                    

            
                    while self.show_next().kind=='COMMA':
                        
                        
                        self.accept_it()
                        
        
                        if  self.show_next().kind in self.PRIMARY:
                            
                             
                                token=self.accept_it()
                                
                                primary=Primary(token.kind,token.value)
                                
                                primaries.append(primary)                             
                             
                             
                     
                    self.expect('RPAREN')
        
            
          else :
                
                self.errors+=1
                print("Error  excepts Constructor"+str(self.show_next().position))
                
        
            
          self.expect('SEMICOLON') 

                  
        
        
          self.indentator.dedent()
          
          return primaries 



     
