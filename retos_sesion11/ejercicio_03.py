especies = dict((('canino', '🐶'), ('felino', '🐱'), ('aves', ['🐦', '🦅'])))
print(especies)

aves_valor = especies.pop('aves')
print(especies)

especies['felino'] = '🐈'
print(especies)

especies['caninos'] = ['🐶', '🐕']
del especies['canino']
print(especies)