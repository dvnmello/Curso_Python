nota1 = int(input('Escreva a nota do aluno:    '))
nota2 = int(input('Escreva a segunda nota do aluno:    '))

media = (nota1+nota2) / 2

if media >= 7:
    print(f'Aprovado, Parabéns!! Sua nota foi:  {media}')
    if media == 10 :
        print(f'Aprovado com Distinção! Parabéns, você alcançou a nota máxima: {media}')
elif media < 7:
    print (f'Reprovado, Infelizmente não atingiu a média. Sua nota foi:  {media}')

