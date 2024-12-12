import re

class Token:
    def __init__(self, source_code):
        self.tokens = {
            "Delimiter": {
                "(": "LEFT_PARENTHESIS",
                ")": "RIGHT_PARENTHESIS",
                "{": "LEFT_CURLY_BRACKET",
                "}": "RIGHT_CURLY_BRACKET",
                "[": "LEFT_SQUARE_BRACKET",
                "]": "RIGHT_SQUARE_BRACKET",
                ";": "SEMI_COLON",
                ":": "COLON",
                ",": "COMMA",
                ".": "DOT",
            },
            
            "Arithmetic_Operator": {
                "+": "ADD",
                "-": "SUBTRACT",
                "/": "DIVIDE",
                "*": "MULTIPLY",
                "//": "FLOOR_DIVISION",
                "%": "MODULO",
                "**": "POWER",
            },

            "Assignment_Operator": {
                "=": "ASSIGNMENT",    
                "+=": "ASSIGNMENT_ADD",
                "-=": "ASSIGNMENT_SUBTRACT", 
                "*=": "ASSIGNMENT_MULTIPLY", 
                "/=": "ASSIGNMENT_DIVIDE",
                "//=": "ASSIGNMENT_FLOOR", 
                "%=": "ASSIGNMENT_MODULO", 
                "**=": "ASSIGNMENT_POWER", 
            },

            "Relational_Operator": {
                "<": "LESS_THAN",
                ">": "GREATER_THAN",
                "==": "EQUAL",
                ">=": "LESS_THAN_EQUAL",
                "<=": "GREATER_THAN_EQUAL",
                "!=": "NOT_EQUAL"
            },

            "Logical_Operator": {
                "and": "AND",
                "or": "OR",
                "not": "NOT",
            },
            
            "Spacing": {
                "\\t": "INDENT",
                "\\n": "NEW_LINE",

            },
            
            "Data_Type": {
                "int": "KEYWORD",
                "double": "KEYWORD",
                "str": "KEYWORD",
                "bool": "KEYWORD",
                "NoneType": "KEYWORD",
                "any": "KEYWORD",
            },
            
            "Reserved_Word": {
                "False": "KEYWORD",
                "True": "KEYWORD",
                "None": "KEYWORD",
            },

            "Noise_Word": {
                "integer": "KEYWORD",
                "string": "KEYWORD",
                "boolean": "KEYWORD",
                "anything": "KEYWORD",
            },
            
            "Native_Function": {
                "print": "KEYWORD",
                "input": "KEYWORD",
                "range": "KEYWORD",
                "app": "KEYWORD",
                "request": "KEYWORD",
                "open": "KEYWORD",
            },

            "Conditional": {
                "if": "KEYWORD",
                "else": "KEYWORD",
                "elif": "KEYWORD",
            },
            
            "Looping": {
                "while": "KEYWORD",
                "for": "KEYWORD",
                "do": "KEYWORD",
            },
            
            "Misc": {
                "return": "KEYWORD",
                "in": "KEYWORD",
                "break": "KEYWORD",
                "continue": "KEYWORD",
            }
        }

        self.keyword_key = [
            "Logical_Operator",
            "Data_Type",
            "Reserved_Word",
            "Noise_Word",
            "Native_Function",
            "Conditional",
            "Looping",
            "Misc"
        ]

        self.keyword = []

        for i in self.keyword_key:
            self.keyword.extend(list(self.tokens[i].keys()))
        
        # Use this for testing
        # self.source_code = repr(source_code)[1:-1]
        
        self.source_code = str(source_code)[2:-1]
        self.cursor = 0
        self.buffer = ""
        self.delimiter_buffer = ""
        self.line_number = 1
        self.token_list = []
        self.error = ""

    def tokenize(self):
        while self.cursor < len(self.source_code):
            # Handle error
            if not self.error == "":
                break
            
            # Newline
            if self.is_newline():
                pass

            # Indent
            elif self.source_code[self.cursor] == " ":
                try:
                    if self.is_indent(self.source_code[self.cursor:self.cursor + 4]):
                        self.cursor += 4
                        continue

                except:
                    pass
            
            # Single-line Comment
            elif self.source_code[self.cursor] == "#":
                self.handle_single_line_comment()

            # Multi-line Comment and Single Quote String
            elif self.source_code[self.cursor] == "'":
                try:
                    if self.source_code[self.cursor + 1] == "'":
                        try:
                            if self.source_code[self.cursor + 2] == "'":
                                self.cursor += 2
                                
                                self.handle_multi_line_comment()
                            else:
                                lexeme_str = self.is_str(self.source_code[self.cursor])
                                if not lexeme_str:
                                    self.error = f"LexicalError: Unclosed string starting at line {self.line_number}."
                                    break
                        except:
                            lexeme_str = self.is_str(self.source_code[self.cursor])
                            if not lexeme_str:
                                self.error = f"LexicalError: Unclosed string starting at line {self.line_number}."
                                break
                    else:
                        lexeme_str = self.is_str(self.source_code[self.cursor])
                        if not lexeme_str:
                            self.error = f"LexicalError: Unclosed string starting at line {self.line_number}."
                            break
                except:
                    lexeme_str = self.is_str(self.source_code[self.cursor])
                    if not lexeme_str:
                        self.error = f"LexicalError: Unclosed string starting at line {self.line_number}."
                        break

            # Multi-line Comment Escape Character and Single Quote String Escape Character
            elif self.source_code[self.cursor] == "\\":
                try:
                    if self.source_code[self.cursor + 1] == "'":
                        try:
                            if self.source_code[self.cursor + 2] == "\\":
                                try:
                                    if self.source_code[self.cursor + 3] == "'":
                                        try:
                                            if self.source_code[self.cursor + 4] == "\\":
                                                try:
                                                    if self.source_code[self.cursor + 5] == "'":
                                                        self.cursor += 5
                                
                                                        self.handle_multi_line_comment_escape_char()
                                                    else:
                                                        lexeme_str = self.is_str_escape_char(self.source_code[self.cursor + 1])
                                                        if not lexeme_str:
                                                            self.error = f"LexicalError: Unclosed string starting at line {self.line_number}."
                                                            break
                                                except:
                                                    lexeme_str = self.is_str_escape_char(self.source_code[self.cursor + 1])
                                                    if not lexeme_str:
                                                        self.error = f"LexicalError: Unclosed string starting at line {self.line_number}."
                                                        break
                                            else:
                                                lexeme_str = self.is_str_escape_char(self.source_code[self.cursor + 1])
                                                if not lexeme_str:
                                                    self.error = f"LexicalError: Unclosed string starting at line {self.line_number}."
                                                    break
                                        except:
                                            lexeme_str = self.is_str_escape_char(self.source_code[self.cursor + 1])
                                            if not lexeme_str:
                                                self.error = f"LexicalError: Unclosed string starting at line {self.line_number}."
                                                break
                                    else:
                                        lexeme_str = self.is_str_escape_char(self.source_code[self.cursor + 1])
                                        if not lexeme_str:
                                            self.error = f"LexicalError: Unclosed string starting at line {self.line_number}."
                                            break
                                except:
                                    lexeme_str = self.is_str_escape_char(self.source_code[self.cursor + 1])
                                    if not lexeme_str:
                                        self.error = f"LexicalError: Unclosed string starting at line {self.line_number}."
                                        break
                            else:
                                lexeme_str = self.is_str_escape_char(self.source_code[self.cursor + 1])
                                if not lexeme_str:
                                    self.error = f"LexicalError: Unclosed string starting at line {self.line_number}."
                                    break
                        except:
                            lexeme_str = self.is_str_escape_char(self.source_code[self.cursor + 1])
                            if not lexeme_str:
                                self.error = f"LexicalError: Unclosed string starting at line {self.line_number}."
                                break
                except:
                    pass

            # Arithmetic Operator, Assigment Operator, and Relational Operator
            elif self.source_code[self.cursor] == "+":
                try:
                    if self.source_code[self.cursor + 1] == "=":
                        self.token_list.append(("+=", self.tokens["Assignment_Operator"]["+="]))
                    else:
                        self.token_list.append((self.source_code[self.cursor], self.tokens["Arithmetic_Operator"][self.source_code[self.cursor]]))
                except:
                    self.token_list.append((self.source_code[self.cursor], self.tokens["Arithmetic_Operator"][self.source_code[self.cursor]]))
            
            elif self.source_code[self.cursor] == "-":
                try:
                    if self.source_code[self.cursor + 1] == "=":
                        self.token_list.append(("-=", self.tokens["Assignment_Operator"]["-="]))
                        self.cursor += 1

                    else:
                        self.token_list.append((self.source_code[self.cursor], self.tokens["Arithmetic_Operator"][self.source_code[self.cursor]]))
                except:
                    self.token_list.append((self.source_code[self.cursor], self.tokens["Arithmetic_Operator"][self.source_code[self.cursor]]))
            
            elif self.source_code[self.cursor] == "*":
                try:
                    if self.source_code[self.cursor + 1] == "=":
                        self.token_list.append(("*=", self.tokens["Assignment_Operator"]["*="]))
                        self.cursor += 1
                    
                    elif self.source_code[self.cursor + 1] == "*":
                        try:
                            if self.source_code[self.cursor + 2] == "=":
                                self.token_list.append(("**=", self.tokens["Assignment_Operator"]["**="]))
                                self.cursor += 2
                            else:
                                self.token_list.append(("**", self.tokens["Arithmetic_Operator"]["**"]))        
                                self.cursor += 1
                        except:
                            self.token_list.append(("**", self.tokens["Arithmetic_Operator"]["**"]))        
                            self.cursor += 1
                    else:
                        self.token_list.append((self.source_code[self.cursor], self.tokens["Arithmetic_Operator"][self.source_code[self.cursor]]))
                except:
                    self.token_list.append((self.source_code[self.cursor], self.tokens["Arithmetic_Operator"][self.source_code[self.cursor]]))
            
            elif self.source_code[self.cursor] == "/":
                try:
                    if self.source_code[self.cursor + 1] == "=":
                        self.token_list.append(("/=", self.tokens["Assignment_Operator"]["/="]))
                        self.cursor += 1
                    
                    elif self.source_code[self.cursor + 1] == "/":
                        try:
                            if self.source_code[self.cursor + 2] == "=":
                                self.token_list.append(("//=", self.tokens["Assignment_Operator"]["//="]))
                                self.cursor += 2
                            else:
                                self.token_list.append(("//", self.tokens["Arithmetic_Operator"]["//"]))
                                self.cursor += 1
                        except:
                            self.token_list.append(("//", self.tokens["Arithmetic_Operator"]["//"]))
                            self.cursor += 1

                    else:
                        self.token_list.append((self.source_code[self.cursor], self.tokens["Arithmetic_Operator"][self.source_code[self.cursor]]))
                except:
                    self.token_list.append((self.source_code[self.cursor], self.tokens["Arithmetic_Operator"][self.source_code[self.cursor]]))

            elif self.source_code[self.cursor] == "%":
                try:
                    if self.source_code[self.cursor + 1] == "=":
                        self.token_list.append(("%=", self.tokens["Assignment_Operator"]["%="]))
                        self.cursor += 1
                    else:
                        self.token_list.append((self.source_code[self.cursor], self.tokens["Arithmetic_Operator"][self.source_code[self.cursor]]))                        
                except:
                    self.token_list.append((self.source_code[self.cursor], self.tokens["Arithmetic_Operator"][self.source_code[self.cursor]]))

            elif self.source_code[self.cursor] == "=":
                try:
                    if self.source_code[self.cursor + 1] == "=":
                        self.token_list.append(("==", self.tokens["Relational_Operator"]["=="]))        
                        self.cursor += 1
                    else:
                        self.token_list.append((self.source_code[self.cursor], self.tokens["Assignment_Operator"][self.source_code[self.cursor]]))        
                except:
                    self.token_list.append((self.source_code[self.cursor], self.tokens["Assignment_Operator"][self.source_code[self.cursor]]))    

            elif self.source_code[self.cursor] == "<":
                try:
                    if self.source_code[self.cursor + 1] == "=":
                        self.token_list.append(("<=", self.tokens["Relational_Operator"]["<="]))        
                        self.cursor += 1
                    else:
                        self.token_list.append((self.source_code[self.cursor], self.tokens["Relational_Operator"][self.source_code[self.cursor]]))        
                except:
                    self.token_list.append((self.source_code[self.cursor], self.tokens["Relational_Operator"][self.source_code[self.cursor]]))    

            elif self.source_code[self.cursor] == ">":
                try:
                    if self.source_code[self.cursor + 1] == "=":
                        self.token_list.append((">=", self.tokens["Relational_Operator"][">="]))        
                        self.cursor += 1
                    else:
                        self.token_list.append((self.source_code[self.cursor], self.tokens["Relational_Operator"][self.source_code[self.cursor]]))        
                except:
                    self.token_list.append((self.source_code[self.cursor], self.tokens["Relational_Operator"][self.source_code[self.cursor]]))
            
            elif self.source_code[self.cursor] == "!":
                try:
                    if self.source_code[self.cursor + 1] == "=":
                        self.token_list.append(("!=", self.tokens["Relational_Operator"]["!="]))        
                        self.cursor += 1
                    else:
                        self.token_list.append((self.source_code[self.cursor], self.tokens["Relational_Operator"][self.source_code[self.cursor]]))        
                except:
                    self.token_list.append((self.source_code[self.cursor], self.tokens["Relational_Operator"][self.source_code[self.cursor]]))    


            # String and Multiline Comment
            elif self.source_code[self.cursor] in ["'", '"']:
                lexeme_str = self.is_str(self.source_code[self.cursor])
                if not lexeme_str:
                    self.error = f"LexicalError: Unclosed string starting at line {self.line_number}."
                    break
            
            # Int and Double
            elif self.source_code[self.cursor] in map(str, list(range(10))):
                lexeme_double =  self.is_double()
                if not lexeme_double:
                    self.is_int()

            # Double With Whole Number is 0
            elif self.source_code[self.cursor] == ".":
                lexeme_double = self.is_double_leading_dot()
                if not lexeme_double:
                    self.token_list.append((self.source_code[self.cursor], self.tokens["Delimiter"][self.source_code[self.cursor]]))    

            # Delimiters
            elif self.source_code[self.cursor] in self.tokens["Delimiter"].keys():
                self.token_list.append((self.source_code[self.cursor], self.tokens["Delimiter"][self.source_code[self.cursor]]))

            # Identifier and Keyword
            elif re.search(r"^[_\w]", self.source_code[self.cursor]):
                self.determine_identifier_or_keyword()

            elif self.source_code[self.cursor] == " ":
                pass

            else:
                self.error = f"LexicalError: Cannot tokenize {self.source_code[self.cursor]} in line {self.line_number}."

            self.cursor +=1

    def is_indent(self, statement:str):
        if re.search(r"^ {4}$", statement) != None:
            self.token_list.append(("\t", self.tokens["Spacing"]["\\t"]))
            return True

    def is_newline(self):
        if self.source_code[self.cursor] == "\\":
            try:
                if self.source_code[self.cursor + 1] == "n":
                    self.token_list.append(("\n", self.tokens["Spacing"]["\\n"]))
                    self.line_number += 1
                    self.cursor += 1
                    return True
                
            except:
                pass
    
    def handle_single_line_comment(self):
        while self.cursor < len(self.source_code):
            if self.is_newline():
                break

            self.cursor += 1

    def handle_multi_line_comment(self):
        if self.cursor + 1 < len(self.source_code):
            self.cursor += 1

        while self.cursor < len(self.source_code):
            if self.source_code[self.cursor] == "'":
                try:
                    if self.source_code[self.cursor + 1] == "'":
                        try:
                            if self.source_code[self.cursor + 2] == "'":
                                self.cursor += 2
                                break
                        except:
                            pass
                except:
                    pass
            
            if self.is_newline():
                pass
            
            self.cursor += 1

    def handle_multi_line_comment_escape_char(self):
        if self.cursor + 1 < len(self.source_code):
            self.cursor += 1

        while self.cursor < len(self.source_code):
            if self.source_code[self.cursor] == "\\":
                try:
                    if self.source_code[self.cursor + 1] == "'":
                        try:
                            if self.source_code[self.cursor + 2] == "\\":
                                try:
                                    if self.source_code[self.cursor + 3] == "'":
                                        try:
                                            if self.source_code[self.cursor + 4] == "\\":
                                                try:
                                                    if self.source_code[self.cursor + 5] == "'":
                                                        self.cursor += 5
                                                        break
                                                except:
                                                    pass
                                        except:
                                            pass
                                except:
                                    pass
                        except:
                            pass
                except:
                    pass
            
            if self.is_newline():
                pass
            
            self.cursor += 1
        

    def is_int(self):
        string_match = re.search(r"^\d+", self.source_code[self.cursor:])
        if string_match:
            self.token_list.append((string_match.group(0), "INTEGER"))
            self.cursor += string_match.end() - 1
            return True
        return False

    def is_double(self):
        string_match = re.search(r"^\d+\.\d*", self.source_code[self.cursor:])
        if string_match:
            self.token_list.append((string_match.group(0), "DOUBLE"))
            self.cursor += string_match.end() - 1
            return True
        return False
    
    def is_double_leading_dot(self):
        string_match = re.search(r"^\.\d+", self.source_code[self.cursor:])
        if string_match:
            self.token_list.append((string_match.group(0), "DOUBLE"))
            self.cursor += string_match.end() - 1
            return True
        return False
        
    def is_str(self, quote:str):
        self.cursor += 1
        curr_line_number = self.line_number
        is_valid = False
        while self.cursor < len(self.source_code):
            self.is_newline()

            if not self.line_number == curr_line_number:
                self.line_number = curr_line_number
                break

            if self.source_code[self.cursor] == quote:
                is_valid = True
                break
            
            self.buffer += self.source_code[self.cursor]
            self.cursor += 1
        
        # Error Handling
        if not is_valid: 
            self.buffer = ""
            
            return False
        
        else:
            self.token_list.append((self.buffer, "STRING"))
            self.buffer = ""   
            return True 
    
    def is_str_escape_char(self, quote:str):
        self.cursor += 2
        curr_line_number = self.line_number
        is_valid = False
        while self.cursor < len(self.source_code):
            self.is_newline()

            if not self.line_number == curr_line_number:
                self.line_number = curr_line_number
                break
            
            if self.source_code[self.cursor] == "\\":
                try:
                    if self.source_code[self.cursor + 1] == quote:
                        is_valid = True
                        self.cursor += 1
                        break
                    else:
                        pass
                except:
                    pass

            self.buffer += self.source_code[self.cursor]
            self.cursor += 1
        
        # Error Handling
        if not is_valid: 
            self.buffer = ""
            
            return False
        
        else:
            self.token_list.append((self.buffer, "STRING"))
            self.buffer = ""   
            return True 
    
    def determine_identifier_or_keyword(self):
        string_match = re.search(r"^[_\w][_\w\d]*", self.source_code[self.cursor:])
        if string_match:
            # Detemine if keyword
            for i in self.keyword_key:
                if string_match.group(0) in self.tokens[i].keys():
                    self.token_list.append((string_match.group(0), self.tokens[i][string_match.group(0)]))
                    self.cursor += string_match.end() - 1
                    return "KEYWORD"
            
            # Output as identifier
            self.token_list.append((string_match.group(0), "IDENTIFIER"))
            self.cursor += string_match.end() - 1
            return "IDENTIFIER"