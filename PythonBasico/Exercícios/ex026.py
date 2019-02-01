frase = str(input('Digite uma frase: ')).strip()
print('A letra A aparece {} vezes'.format(frase.lower().count('a')))
print('A letra A aparece pela primeira vez na posição {}'.format(frase.lower().find('a')))
print('A letra A aparece pela ultima vez na posição {}'.format(frase.lower().rfind('a')))
