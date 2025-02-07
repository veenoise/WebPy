from lexer import Token

class Parser:
    def __init__(self, token_list):
        self.token_list = token_list
        self.cursor = 0
        self.syntax_error = []
        self.tokens = Token([]).tokens
        self.line_number = 1
        self.indent = 0
        self.required_indent = False
        self.correct_indents = []
        self.wrong_indents = [] 
        self.do_keyword = False 
        self.do_indent = 0
        self.current_line_indent = 0
        
    def parse(self):
        while self.cursor < len(self.token_list):
            try:
                self.indent_check()
                self.function()
                self.declaration()
                self.iterative()
                self.app()
                self.cursor += 1
            except IndexError:
                break
        # for i in self.syntax_error:
        #     print(i)

        return self.syntax_error


    def cursor_to_next_line(self):
        current_line = self.token_list[self.cursor][2]
        while (self.cursor < len(self.token_list) and 
            self.token_list[self.cursor][2] == current_line):
            self.cursor += 1

    def buffer_cursor_to_next_line(self):
        current_line = self.token_list[self.cursor][2]
        tmp_index = self.cursor
        while (tmp_index < len(self.token_list) and 
            self.token_list[tmp_index][2] == current_line):
            tmp_index += 1
        return tmp_index

    def indent_level(self):
        tab_count = 0
        while self.cursor < len(self.token_list):
            if self.token_list[self.cursor][1] == "INDENT":
                tab_count += 1
                self.cursor += 1

            else:
                # Store in memory indent level of do loop
                if self.token_list[self.cursor + 1][1] == "DO_LP":
                    self.do_indent = tab_count

                return tab_count
        # Store in memory indent level of do loop
        if self.token_list[self.cursor + 1][1] == "DO_LP":
            self.do_indent = tab_count

        return tab_count  


    def indent_check(self):
        real_indent = self.indent_level()
        self.current_line_indent = real_indent
        if self.do_keyword:
            # print(f"real_indent: {real_indent}; supposed_indent: {self.indent}; {self.token_list[self.cursor]}")
            if self.required_indent and real_indent == self.indent and self.token_list[self.cursor][2] not in self.correct_indents:
                self.correct_indents.append(self.token_list[self.cursor][2])
                self.required_indent = (True if self.token_list[self.cursor + 1][1] == "NEW_LINE" else False)
                
            elif self.required_indent == False and real_indent <= self.indent and real_indent > self.do_indent and self.token_list[self.cursor][2] not in self.correct_indents:
                self.correct_indents.append(self.token_list[self.cursor][2])
                self.indent = real_indent

            else:
                if self.token_list[self.cursor][2] not in self.correct_indents and self.token_list[self.cursor][2] not in self.wrong_indents:
                    if self.token_list[self.cursor][1] == "WHILE_LP" and self.token_list[self.cursor + 2][1] == "NEW_LINE" and self.current_line_indent == self.do_indent:
                        return

                    self.syntax_error.append(f"SyntaxError at line {self.token_list[self.cursor][2]}: Invalid Indentation")
                    self.wrong_indents.append(self.token_list[self.cursor][2])

        else:
            if self.required_indent and real_indent == self.indent and self.token_list[self.cursor][2] not in self.correct_indents:
                self.correct_indents.append(self.token_list[self.cursor][2])
                self.required_indent = (True if self.token_list[self.cursor + 1][1] == "NEW_LINE" else False)
                # print(f"real_indent: {real_indent}; supposed_indent: {self.indent}; {self.token_list[self.cursor]}")
            elif self.required_indent == False and real_indent <= self.indent and self.token_list[self.cursor][2] not in self.correct_indents:
                self.correct_indents.append(self.token_list[self.cursor][2])
                self.indent = real_indent

            else:
                if self.token_list[self.cursor][2] not in self.correct_indents and self.token_list[self.cursor][2] not in self.wrong_indents:
                    self.syntax_error.append(f"SyntaxError at line {self.token_list[self.cursor][2]}: Invalid Indentation")
                    self.wrong_indents.append(self.token_list[self.cursor][2])

    def declaration(self):
        # Variable Declaration and Initialization
        # Example: 
        # x:int = 43
        if self.token_list[self.cursor][1] == "IDENTIFIER":
            self.cursor += 1

            if self.token_list[self.cursor][1] != "COLON":
                self.syntax_error.append(f"SyntaxError at line {self.token_list[self.cursor][2]}: Missing ':'")
                self.cursor_to_next_line()

            else:
                self.cursor += 1

                if self.token_list[self.cursor][1] not in self.tokens["Data_Type"].values():
                    self.syntax_error.append(f"SyntaxError at line {self.token_list[self.cursor][2]}: Invalid Data Type or No Data Type Supplied")
                    self.cursor_to_next_line()

                else:
                    self.cursor += 1

                    if self.token_list[self.cursor][1] != "ASSIGNMENT":
                        self.syntax_error.append(f"SyntaxError at line {self.token_list[self.cursor][2]}: Missing Assignment Operator")
                        self.cursor_to_next_line()
                    
                    else:
                        self.cursor += 1

                        if self.token_list[self.cursor][1] not in self.tokens["Data_Value"].values():
                            self.syntax_error.append(f"SyntaxError at line {self.token_list[self.cursor][2]}: Missing Value")
                            self.cursor_to_next_line()

                        else:
                            self.cursor += 1

                            if self.token_list[self.cursor][1] != "NEW_LINE":
                                self.syntax_error.append(f"SyntaxError at line {self.token_list[self.cursor][2]}: Missing Newline")
                                self.cursor_to_next_line()

    
    def iterative(self):
        # Looping syntax: For loop
        # Example:
        # for i:int in range(12):
        #     print("hello")
        if self.token_list[self.cursor][1] == "FOR_LP":
            self.cursor += 1
            self.indent += 1
            self.required_indent = True
            
            if self.token_list[self.cursor][1] != "IDENTIFIER":
                self.syntax_error.append(f"SyntaxError at line {self.token_list[self.cursor][2]}: Missing IDENTIFIER")
                self.cursor_to_next_line()
            
            else:
                self.cursor += 1

                if self.token_list[self.cursor][1] != "COLON":
                    self.syntax_error.append(f"SyntaxError at line {self.token_list[self.cursor][2]}: Missing ':'")
                    self.cursor_to_next_line()

                else:
                    self.cursor += 1

                    if self.token_list[self.cursor][1] not in self.tokens["Data_Type"].values():
                        self.syntax_error.append(f"SyntaxError at line {self.token_list[self.cursor][2]}: Invalid Data Type or No Data Type Supplied")
                        self.cursor_to_next_line()
                    
                    else:
                        self.cursor += 1

                        if self.token_list[self.cursor][1] != "IN":
                            self.syntax_error.append(f"SyntaxError at line {self.token_list[self.cursor][2]}: Missing 'in' keyword")
                            self.cursor_to_next_line()
                            
                        else:
                            self.cursor += 1

                            if self.token_list[self.cursor][1] == "RANGE_FN":
                                self.cursor += 1

                                if self.token_list[self.cursor][1] != "LEFT_PARENTHESIS":
                                    self.syntax_error.append(f"SyntaxError at line {self.token_list[self.cursor][2]}: Missing '('")
                                    self.cursor_to_next_line()
                                
                                else:
                                    self.cursor += 1

                                    if self.token_list[self.cursor][1] not in self.tokens["Data_Value"].values():
                                        self.syntax_error.append(f"SyntaxError at line {self.token_list[self.cursor][2]}: Missing Value")
                                        self.cursor_to_next_line()

                                    else:
                                        self.cursor += 1

                                        if self.token_list[self.cursor][1] != "RIGHT_PARENTHESIS":
                                            self.syntax_error.append(f"SyntaxError at line {self.token_list[self.cursor][2]}: Missing ')'")
                                            self.cursor_to_next_line()

                                        else:
                                            self.cursor += 1

                                            if self.token_list[self.cursor][1] != "COLON":
                                                self.syntax_error.append(f"SyntaxError at line {self.token_list[self.cursor][2]}: Missing ':'")
                                                self.cursor_to_next_line()

                                            else:
                                                self.cursor += 1

                                                if self.token_list[self.cursor][1] != "NEW_LINE":
                                                    self.syntax_error.append(f"SyntaxError at line {self.token_list[self.cursor][2]}: Missing Newline")
                                                    self.cursor_to_next_line()

                            elif self.token_list[self.cursor][1] == "IDENTIFIER":
                                self.cursor += 1

                                if self.token_list[self.cursor][1] != "COLON":
                                    self.syntax_error.append(f"SyntaxError at line {self.token_list[self.cursor][2]}: Missing ':'")
                                    self.cursor_to_next_line()

                                else:
                                    self.cursor += 1

                                    if self.token_list[self.cursor][1] != "NEW_LINE":
                                        self.syntax_error.append(f"SyntaxError at line {self.token_list[self.cursor][2]}: Missing Newline")
                                        self.cursor_to_next_line()

                            else:
                                self.syntax_error.append(f"SyntaxError at line {self.token_list[self.cursor][2]}: Missing Iterable Item")
                                self.cursor_to_next_line()

        # Looping syntax: While loop
        # Example:
        # while True:
        #     print("hello")
        elif self.token_list[self.cursor][1] == "WHILE_LP":
            self.cursor += 1
            self.indent += 1
            self.required_indent = True

            if self.token_list[self.cursor][1] not in self.tokens["Reserved_Word"].values():
                self.syntax_error.append(f"SyntaxError at line {self.token_list[self.cursor][2]}: Missing or Invalid Value")
                self.cursor_to_next_line()
            
            else:
                self.cursor += 1

                if self.token_list[self.cursor][1] != "COLON":
                    if self.do_keyword and self.token_list[self.cursor][1] == "NEW_LINE":
                        if self.do_indent == self.current_line_indent:
                            self.do_keyword = False
                            self.do_indent = 0
                            return 

                    self.syntax_error.append(f"SyntaxError at line {self.token_list[self.cursor][2]}: Missing ':'")
                    self.cursor_to_next_line()

                else:
                    self.cursor += 1

                    if self.token_list[self.cursor][1] != "NEW_LINE":
                        self.syntax_error.append(f"SyntaxError at line {self.token_list[self.cursor][2]}: Missing Newline")
                        self.cursor_to_next_line()


        # Looping syntax: Do While loop
        # Example:
        # do:
        #     print("hello")
        # while True
        elif self.token_list[self.cursor][1] == "DO_LP":
            self.cursor += 1
            self.indent += 1
            self.required_indent = True
            self.do_keyword = True
            
            if self.token_list[self.cursor][1] != "COLON":
                self.syntax_error.append(f"SyntaxError at line {self.token_list[self.cursor][2]}: Missing ':'")
                self.cursor_to_next_line()

            else:
                self.cursor += 1

                if self.token_list[self.cursor][1] != "NEW_LINE":
                    self.syntax_error.append(f"SyntaxError at line {self.token_list[self.cursor][2]}: Missing Newline")
                    self.cursor_to_next_line()

    def app(self):
        # App object syntax
        # Example:
        # app.get("/", homepage_function)
        if self.token_list[self.cursor][1] == "APP_FN":
            self.cursor += 1

            if self.token_list[self.cursor][1] != "DOT":
                self.syntax_error.append(f"SyntaxError at line {self.token_list[self.cursor][2]}: Missing '.'")
                self.cursor_to_next_line()

            else:
                self.cursor += 1

                if self.token_list[self.cursor][0] not in ['get', 'post', 'put', 'patch', 'delete']:
                    self.syntax_error.append(f"SyntaxError at line {self.token_list[self.cursor][2]}: Missing or Invalid Method")
                    self.cursor_to_next_line()

                else:
                    self.cursor += 1

                    if self.token_list[self.cursor][1] != "LEFT_PARENTHESIS":
                        self.syntax_error.append(f"SyntaxError at line {self.token_list[self.cursor][2]}: Missing '('")
                        self.cursor_to_next_line()
                    
                    else:
                        self.cursor += 1

                        if self.token_list[self.cursor][1] != "STRING":
                            self.syntax_error.append(f"SyntaxError at line {self.token_list[self.cursor][2]}: Missing Endpoint")
                            self.cursor_to_next_line() 

                        else:
                            self.cursor += 1

                            if self.token_list[self.cursor][1] != "COMMA":
                                self.syntax_error.append(f"SyntaxError at line {self.token_list[self.cursor][2]}: Missing ','")
                                self.cursor_to_next_line() 
                            
                            else:
                                self.cursor += 1

                                if self.token_list[self.cursor][1] != "IDENTIFIER":
                                    self.syntax_error.append(f"SyntaxError at line {self.token_list[self.cursor][2]}: Missing Identifier")
                                    self.cursor_to_next_line()

                                else:
                                    self.cursor += 1

                                    if self.token_list[self.cursor][1] != "RIGHT_PARENTHESIS":
                                        self.syntax_error.append(f"SyntaxError at line {self.token_list[self.cursor][2]}: Missing ')'")
                                        self.cursor_to_next_line()
                                    
                                    else:
                                        self.cursor += 1

                                        if self.token_list[self.cursor][1] != "NEW_LINE":
                                            self.syntax_error.append(f"SyntaxError at line {self.token_list[self.cursor][2]}: Missing Newline")
                                            self.cursor_to_next_line()

    def function(self):
        # def syntax
        # Example:
        # def homepage_function:any():
        #     return "hello world"
        if self.token_list[self.cursor][1] == "FUNC":
            self.cursor += 1
            self.indent += 1
            self.required_indent = True

            if self.token_list[self.cursor][1] != "IDENTIFIER":
                self.syntax_error.append(f"SyntaxError at line {self.token_list[self.cursor][2]}: Missing Identifier")
                self.cursor_to_next_line()

            else:
                self.cursor += 1

                if self.token_list[self.cursor][1] != "COLON":
                    self.syntax_error.append(f"SyntaxError at line {self.token_list[self.cursor][2]}: Missing ':'")
                    self.cursor_to_next_line()

                else:
                    self.cursor += 1

                    if self.token_list[self.cursor][1] not in self.tokens["Data_Type"].values():
                        self.syntax_error.append(f"SyntaxError at line {self.token_list[self.cursor][2]}: Invalid Data Type or No Data Type Supplied")
                        self.cursor_to_next_line()

                    else:
                        self.cursor += 1

                        if self.token_list[self.cursor][1] != "LEFT_PARENTHESIS":
                            self.syntax_error.append(f"SyntaxError at line {self.token_list[self.cursor][2]}: Missing '('")
                            self.cursor_to_next_line()

                        else:
                            self.cursor += 1

                            if self.token_list[self.cursor][1] != "RIGHT_PARENTHESIS":
                                self.syntax_error.append(f"SyntaxError at line {self.token_list[self.cursor][2]}: Missing ')'")
                                self.cursor_to_next_line()

                            else:
                                self.cursor += 1

                                if self.token_list[self.cursor][1] != "COLON":
                                    self.syntax_error.append(f"SyntaxError at line {self.token_list[self.cursor][2]}: Missing ':'")
                                    self.cursor_to_next_line()
                                
                                else:
                                    self.cursor += 1

                                    if self.token_list[self.cursor][1] != "NEW_LINE":
                                        self.syntax_error.append(f"SyntaxError at line {self.token_list[self.cursor][2]}: Missing Newline")
                                        self.cursor_to_next_line()

