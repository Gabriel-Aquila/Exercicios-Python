frase = str(input('Digite uma frase: ')).upper().strip()
print('A letra A aparece: ', frase.count('A'))
print('A letra A aparece primeiro na posição: ', frase.find('A')+1)
print('A letra A aparece por ultimo na posição: ', frase.rfind('A')+1)
