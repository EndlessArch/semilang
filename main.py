from lib.lexer_ import lexer
from lib.parser_ import parser


example_code = '''
a is 1
b is 2 + 1 * 3
print a + b
'''

example_code_2 = '''
a is 10
b is 20
if a+b > 10 then
  print a*b
else
  print b-a
end
'''

tokens = lexer.lex(example_code_2)

# print(list(lexer.lex(example_code)))

ast = parser.parse(tokens)

print(ast.getast())
