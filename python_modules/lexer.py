def get_input(program:str):
    clean_input = program.rstrip()

    print(repr(clean_input))

class Token:
    def __init__(self):
        tokens = {
            # Symbols
            "(": "LEFT_PARENTHESIS",
            ")": "RIGHT_PARENTHESIS",
            "{": "LEFT_SQUARE_BRACKET",
            "}": "RIGHT_SQUARE_BRACKET",
            ":": "SEMI_COLON",
            ",": "COMMA",
            "=": "ASSIGNMENT",

            # Data Types
            "int": "DATA_TYPE",
            "double": "DATA_TYPE",
            "str": "DATA_TYPE",
            "bool": "DATA_TYPE",
            "NoneType": "DATA_TYPE",
            
            # Keywords 
            "False": "KEYWORD",
            "True": "KEYWORD",
            "None": "KEYWORD",
            
            "in": "KEYWORD",


            # Conditional
            "if": "KEYWORD",
            "else": "KEYWORD",
            "elif": "KEYWORD",
            
            # Looping
            "while": "KEYWORD",
            "for": "KEYWORD",
            "do": "KEYWORD",
            "break": "KEYWORD",
            
            # Logical Operator
            "and": "KEYWORD",
            "or": "KEYWORD",
            "not": "KEYWORD",
        }

    def detect_string():
        pass
    
