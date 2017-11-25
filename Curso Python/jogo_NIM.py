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
        jogadorRemove = int(input('Quantas pe�as voc� vai tirar? '))
        if jogadorRemove > m or jogadorRemove < 1:
            print()
            print('Oops! Jogada inv�lida! Tente de novo.')
            print()
 
        else:
            jogadaValida = True
 
    return jogadorRemove
 
 
def campeonato():
    numeroRodada = 1
    while numeroRodada <= 3:
        print()
        print('**** Rodada', numeroRodada, '****')
        print()
        partida()
        numeroRodada += 1
    print()
    print('Placar: Voc� 0 X 3 Computador')
 
 
def partida():
    n = int(input('Quantas pe�as? '))
 
    m = int(input('Limite de pe�as por jogada? '))
 
    vezDoPC = False
 
    if n % (m+1) == 0:
        print()
        print('Voc� come�a!')
 
    else:
        print()
        print('Computador come�a!')
        vezDoPC = True
 
    while n > 0:
        if vezDoPC:
            computadorRemove = computador_escolhe_jogada(n, m)
            n = n - computadorRemove
            if computadorRemove == 1:
                print()
                print('O computador tirou uma pe�a')
            else:
                print()
                print('O computador tirou', computadorRemove, 'pe�as')
 
            vezDoPC = False
        else:
            jogadorRemove = usuario_escolhe_jogada(n, m)
            n = n - jogadorRemove
            if jogadorRemove == 1:
                print()
                print('Voc� tirou uma pe�a')
            else:
                print()
                print('Voc� tirou', jogadorRemove, 'pe�as')
            vezDoPC = True
        if n == 1:
            print('Agora resta apenas uma pe�a no tabuleiro.')
            print()
        else:
            if n != 0:
                print('Agora restam,', n, 'pe�as no tabuleiro.')
                print()
 
    print('Fim do jogo! O computador ganhou!')
 
print('Bem-vindo ao jogo do NIM! Escolha:')
print()
 
print('1 - para jogar uma partida isolada')
 
tipoDePartida = int(input('2 - para jogar um campeonato '))
 
if tipoDePartida == 2:
    print()
    print('Voc� escolheu um campeonato!')
    print()
    campeonato()
else:
    if tipoDePartida == 1:
        print()
        partida()
