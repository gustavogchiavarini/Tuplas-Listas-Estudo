total_par = 0

n = (int(input('Digite um número: ')),
     int(input('Digite outro número: ')),
     int(input('Digite mais um número: ')),
     int(input('Digite o último número: ')))

print(f'Você digitou os valores : {n}')


print(f'O valor 9 apareceu {n.count(9)} vezes. ')
if 3 in n:
    print(f'O valor 3 apareceu na {n.index(3) + 1}° posição.')
else:
    print('O número 3 não foi encontrado. ')

    
for numero in n:
    if numero % 2 == 0:
        total_par += 1

print(f'Os valores pares digitados foram {total_par}.')