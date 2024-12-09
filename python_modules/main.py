import python_modules.lexer as lexer
import keyword

print(f"{keyword.kwlist}\n\n")
with open("sample.txt", "r") as val:
    lexer.get_input(val.read())
