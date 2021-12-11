import re
import sys
from token import Token





regexExpressions = [


## =============================================================================
## OPÉRATIONS         
## =============================================================================
#         

    (r'\=', 'ASSIGN'),




#==============================================================================
# MOTS CLEFS 
#==============================================================================

    (r'HARDWARE\b', 'HARDWARE_DECLARATION'),  
    (r'NETWORK\b', 'NETWORK_DECLARATION'),
    (r'SERVICE\b', 'SERVICE_DECLARATION'),
    (r'CONFIG\b', 'CONFIG_DECLARATION'),
    (r'PROCESSING\b', 'PROCESSING_DECLARATION'),           
    (r'ARCHITECTURE\b','ARCHITECTURE_DECLARATION'),  

## =============================================================================
##          #  les types
# =============================================================================
       
    (r'Cluster\b', 'CLUSTER'),             
    (r'Network\b', 'NETWORK'),
    (r'Service\b', 'SERVICE'),       
    (r'Computer\b', 'COMPUTER'),
    (r'Service\b', 'SERVICE'),
    (r'Architecture\b', 'ARCHITECTURE'),





## =============================================================================
##          #littéraux
## =============================================================================
#
                            
    (r'\d+\.\d+', 'FLOAT_LIT'),
    (r'\d+', 'INTEGER_LIT'),
    (r'\"[^\"]*\"', 'STRING_LIT'),
    (r'\'[^\"]*\'', 'CHAR_LIT'),

# =============================================================================
#  délimiteurs d'instructions
# =============================================================================


    (r'[ \n\t]+', None),
    (r'#[^\n]*', None),
    (r'\(', 'LPAREN'),
    (r'\)', 'RPAREN'),
    (r'\{', 'LBRACE'),
    (r'\}', 'RBRACE'),
    (r'\[', 'LBRACKET'),
    (r'\]', 'RBRACKET'),
    (r'\;', 'SEMICOLON'),
    (r'\,', 'COMMA'),
    (r'\w+(\.\w+)+', 'SELECTED_NAME'),


## =============================================================================
##         #IDENTIFIANTS 
## =============================================================================
#        
         (r'[a-zA-Z]\w*', 'IDENTIFIER'),   
         

]


class Lexer:

    def __init__(self):
        self.tokens = []

    # inputText = open("testFile.c").readlines()
    def lex(self, inputText):

        lineNumber = 0
        for line in inputText:
            lineNumber += 1
            position = 0
            while position < len(line):
                match = None
                for tokenRegex in regexExpressions:
                    pattern, tag = tokenRegex
                    regex = re.compile(pattern)
                    match = regex.match(line, position)
                    if match:
                        data = match.group(0)
                        if tag:
                            token = Token(tag, data, [lineNumber, position])
                            self.tokens.append(token)
                        break
                if not match:
                    print(inputText[position])
                    print("no match")
                    sys.exit(1)
                else:
                    position = match.end(0)
        print("lexer: analysis successful!")
        return self.tokens
lexer=Lexer()

url="tests/test_parsing.hub"

inputText = open(url).readlines()



tokens=lexer.lex(inputText)

for k in tokens:

    print("kind {} value {} position {}".format(k.kind,k.value,k.position))
