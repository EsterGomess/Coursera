# encoding: utf-8
print ("Bem-vindo ao jogo do NIM Escolha:")
print ("1  para jogar uma partida isolada")
print ("2  para jogar um campeonato")
mododejogo = input ()

def computador_escolhe_jogada (n,m):
	if n%(m+1)==0:
		return m
	else:
		return n%(m+1)
	
def jogador_escolhe_jogada(n,m):
	while True:
		jogada = input ("Quantas peças você vai tirar?")
		if jogada<=m:
			return jogada
		else: 
			print ("Oops! Jogada inválida! Tende de Novo")
			pass
			
def partida():
	primeiro=False
	n = input ("Quantas peças? ")
	m = input ("Limite de peças por jogada? ")
	if n%(m+1):
		primeiro=True
		print ("Computador começa")
	while n>0:
		if primeiro:
			pc=computador_escolhe_jogada(n,m)
			print ("O computador tirou", pc, "peças")
			n=n-pc
			if (n>0):
				print ("Agora restam ", n, " peças no tabuleiro")
			if n==0:
				break
			jg=jogador_escolhe_jogada(n,m)
			print ("Voce tirou", jg, "peças")
			n=n-jg
			if (n>0):
				print ("Agora restam ", n, " peças no tabuleiro")
		else:
			jg=jogador_escolhe_jogada(n,m)
			print ("Voce tirou", jg, "peças")
			n=n-jg
			if (n>0):
				print ("Agora restam ", n, " peças no tabuleiro")
			pc=computador_escolhe_jogada(n,m)
			print ("O computador tirou", pc, "peças")
			n=n-pc
			if (n>0):
				print ("Agora restam ", n, " peças no tabuleiro")
	print ("Fim do jogo! O computador ganhou!")

def campeonato():
	print ("**** Rodada 1 ****")
	partida()
	print ("**** Rodada 2 ****")
	partida()
	print ("**** Rodada 3 ****")
	partida()
	print ("**** Final do campeonato ****")
	print ("Placar : Você 0 x 3 Computador")

if (mododejogo == 1):
	partida()
	
if (mododejogo == 2):
	campeonato()
	

