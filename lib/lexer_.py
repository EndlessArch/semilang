from rply import LexerGenerator


lg = LexerGenerator()


lg.add('IS', r'is')
lg.add('IF', r'if')
lg.add('THEN', r'then')
lg.add('ELSE', r'else')
lg.add('END', r'end')
lg.add('PRINT', r'print')

lg.add('IDENTIFIER', r'[a-zA-Z_][\w]*')
lg.add('NUMBER', r'\d+')

lg.add('PLUS', r'\+')
lg.add('MINUS', r'\-')
lg.add('MULTIPLY', r'\*')
lg.add('DIVIDE', r'\\')

lg.add('LT', r'>')
lg.add('GT', r'<')


lg.ignore(r'\s+')

lexer = lg.build()
