from random import randint
print(12 * '=', 'jokenpô' ,12 * '=')
lista = ['pedra', 'papel', 'tesoura']
print('[0] PEDRA')
print('[1] PAPEL')
print('[2] TESOURA')
opcao = int(input('Digite a opção que deseja: '))
print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
print('PEDRA..')
print('PAPEL..')
print('TESOURA!!')
print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
computador = randint (0,2)
print('O computador escolheu {}!'.format(lista[computador]))
print('Você escolheu {}!'.format(lista[opcao]))
if computador == 0:
    if opcao == 0:
        print('EMPATE!!')
    elif opcao == 1:
        print('VOCÊ VENCEU!!')
    elif opcao == 2:
        print(' VOCÊ PERDEU!!')
    else:
        print('Opção inválida, digite novamente!!')
elif computador == 1:
    if opcao == 0:
        print('VOCÊ PERDEU!!')
    elif opcao == 1:
        print('EMPATE!!')
    elif opcao == 2:
        print(' VOCÊ GANHOU!!')
    else:
        print('Opção inválida, digite novamente!!')
elif computador == 2:
    if opcao == 0:
        print('VOCÊ PERDEU!!')
    elif opcao == 1:
        print('VOCÊ PERDEU!!')
    elif opcao == 2:
        print(' EMPATE!!') 
    else:
        print('Opção inválida, digite novamente!!')