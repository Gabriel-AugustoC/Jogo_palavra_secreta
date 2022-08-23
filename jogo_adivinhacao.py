print('*'*30)
print('* Jogo adivinhação *')
print('*'*30)

numero_secreto = 42

nivel = int(input('Nível 1 = 20 Tentativas\nNível 2 = 10 Tentativas\nNível 3 = 5 Tentativas\nDigite o nível desejado: '))

if nivel == 1:
  total_tentativas = 20
elif nivel == 2:
  total_tentativas = 10
elif nivel == 3:
  total_tentativas = 5

for rodada in range(1, total_tentativas+1):
  print(' tentativas {} de {}'.format(rodada, total_tentativas))

  chute = int(input('Digite um número:\n'))
  print('Você digitou: ', chute)

  acertou = numero_secreto == chute
  menor = numero_secreto < chute
  maior = numero_secreto > chute

  if (acertou):
    print('Você acertou o número secreto')
    break
  elif (menor):
    print('Você errou!! O número secreto é menor que {}'.format(chute))
  elif (maior):
    print('Você errou!! O número secreto é maior que {}'.format(chute))

print('Fim do Jogo!!✌')

