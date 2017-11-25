# encoding: utf-8

def computador_escolhe_jogada(n, m):
    computadorRemove = 1
 
    while computadorRemove != m:
        if (n - computadorRemove) % (m+1) == 0:
            return computadorRemove
 
        else:
            computadorRemove += 1
 
    return computadorRemove
 
 
def usuario_escolhe_jogada(n, m):
    jogadaValida = False
 
    while not jogadaValida:
        jogadorRemove = int(input('Quantas peças você vai tirar? '))
        if jogadorRemove > m or jogadorRemove < 1:
             
            print('Oops! Jogada inválida! Tente de novo.')
             
 
        else:
            jogadaValida = True
 
    return jogadorRemove
 
 
def campeonato():
    numeroRodada = 1
    while numeroRodada <= 3:
         
        print('**** Rodada', numeroRodada, '****')
         
        partida()
        numeroRodada += 1
     
    print('Placar: Você 0 X 3 Computador')
 
 
def partida():
    n = int(input('Quantas peças? '))
 
    m = int(input('Limite de peças por jogada? '))
 
    vezDoPC = False
 
    if n % (m+1) == 0:
         
        print('Você começa!')
 
    else:
         
        print('Computador começa!')
        vezDoPC = True
 
    while n > 0:
        if vezDoPC:
            computadorRemove = computador_escolhe_jogada(n, m)
            n = n - computadorRemove
            if computadorRemove == 1:
                 
                print('O computador tirou uma peça')
            else:
                 
                print('O computador tirou', computadorRemove, 'peças')
 
            vezDoPC = False
        else:
            jogadorRemove = usuario_escolhe_jogada(n, m)
            n = n - jogadorRemove
            if jogadorRemove == 1:
                 
                print('Você tirou uma peça')
            else:
                 
                print('Você tirou', jogadorRemove, 'peças')
            vezDoPC = True
        if n == 1:
            print('Agora resta apenas uma peça no tabuleiro.')
             
        else:
            if n != 0:
                print('Agora restam,', n, 'peças no tabuleiro.')
                 
 
    print('Fim do jogo! O computador ganhou!')
 
print('Bem-vindo ao jogo do NIM! Escolha:')
 
 
print('1 - para jogar uma partida isolada')
 
tipoDePartida = int(input('2 - para jogar um campeonato '))
 
if tipoDePartida == 2:
     
    print('Você escolheu um campeonato!')
     
    campeonato()
else:
    if tipoDePartida == 1:
         
        partida()
