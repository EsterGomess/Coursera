print ("Bem-vindo ao jogo do NIM Escolha:")
print ("1  para jogar uma partida isolada")
print ("2  para jogar um campeonato")
mododejogo = input ()


def computador_escolhe_jogada(n,m):
	if n%(m+1)==0:
		return m
	else:
		return n%(m+1)

def jogador_escolhe_jogada(n,m):
	while True:
		jogada = input ("Informe quantas pecas retirar")
		if jogada<=m:
			return jogada
			
def partida():
	primeiro=False
	n = input ("Quantas pecas? ")
	m = input ("Limite de pecas por jogada? ")
	if n%(m+1):
		primeiro=True
		print ("Computador começa")
	while n>0:
		if primeiro:
			pc=computador_escolhe_jogada(n,m)
			print ("O computador tirou", pc, "pecas")
			n=n-pc
			print ("Agora restam ", n, " pecas no tabuleiro")
			if n==0:
				break
			jg=jogador_escolhe_jogada(n,m)
			print ("Voce tirou", jg, "pecas")
			n=n-jg
			print ("Agora restam ", n, " pecas no tabuleiro")
		else:
			pc=jogador_escolhe_jogada(n,m)
			print ("Voce tirou", jg, "pecas")
			n=n-jg
			print ("Agora restam ", n, " pecas no tabuleiro")
			jg=computador_escolhe_jogada(n,m)
			print ("O computador tirou", pc, "pecas")
			n=n-pc
			print ("Agora restam ", n, " pecas no tabuleiro")
	print ("O computador ganhou")
	print ("Final do campeonato")
	print ("Placar : Voce 0 x 3 Computador")
		
if (mododejogo == 1):
	partida()
