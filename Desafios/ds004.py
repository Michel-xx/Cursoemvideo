#salva qualquer coisa do teclado na variavel
tecla = input('Digite qualquer coisa: ')

#depois verifica tudo pra falar o que os caracteres escolhidos são e não são
print('é alphanumerico?')
print(tecla.isalnum())

print('é alphabetico?')
print(tecla.isalpha())

print('está em formato de texto?')
print(tecla.istitle())

print('é numérico?')
print(tecla.isnumeric())

print('é decimal?')
print(tecla.isdecimal())

print('pertence ao conjunto ASCII padrão (de 7 bits)')
print(tecla.isascii())

print('contém apenas numeros?')
print(tecla.isdigit())

print('segue todas as regras de variaveis?')
print(tecla.isidentifier())

print('é apenas espaço?')
print(tecla.isspace())

print('Todas as Letras estão minusculas?')
print(tecla.islower())

print('Todas as letras são maiusculas?')
print(tecla.isupper())

print('todos os caracteres são imprimiveis')
print(tecla.isprintable())

#fala quais caracteres foi escolhidos
print('o caractere escolhido foi "{}"' .format(tecla))