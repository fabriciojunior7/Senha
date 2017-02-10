import time, os

os.system("cls")

caracteresValidos = []
minha_tabela = []

for i in range(32, 127):
	caracteresValidos.append(chr(i))

#Minusculos
for l in caracteresValidos[65: 91]:
	minha_tabela.append(l)
#Numeros
for l in caracteresValidos[16: 26]:
	minha_tabela.append(l)
#Maiusculos
for l in caracteresValidos[33: 59]:
	minha_tabela.append(l)
#Simbolos
for l in caracteresValidos:
	if(l not in minha_tabela):
		minha_tabela.append(l)


#print len(minha_tabela)
#print minha_tabela

def buscador(senha):

	sigla = "Segundos"
	pos_letras = []
	for l in senha:
		for ll in range(len(minha_tabela)):
			if(l == minha_tabela[ll]):
				pos_letras.append(ll+1)
				break

	nova_pos_letras = []
	for i in range(len(pos_letras), 0, -1):
		nova_pos_letras.append(pos_letras[i-1])

	tentativas_totais = 0
	i = 0

	for e in nova_pos_letras:
		if(i == 0):
			tentativas_totais += e
		else:
			tentativas_totais += (e) * 95**i

		i += 1
	#print tentativas_totais
	rasao4 = 0.78
	tempo_real = (tentativas_totais*rasao4) / 857376.0
	if(tempo_real >= 60 and tempo_real < 3600):
		tempo_real /= 60
		sigla = "Minutos"
	elif(tempo_real >= 3600 and tempo_real < 86400):
		tempo_real /= 3600
		sigla = "Horas"
	elif(tempo_real >= 86400 and tempo_real < 31536000):
		tempo_real /= 86400
		sigla = "Dias"
	elif(tempo_real >= 31536000):
		tempo_real /= 31536000
		sigla = "Anos"
	
	print("Tempo Aproximado de Busca: %.3f %s" % (tempo_real, sigla))

	lista_indices = [0]
	casa_atual = 0

	print("...")

	while(True):
		teste = ""
		for i in lista_indices:
			teste += minha_tabela[i]

		if(teste == senha):
			#os.system("cls")
			print("\n==================================================\nACHADO: %s" % teste)
			break
		else:
			lista_indices[casa_atual] += 1

		if(lista_indices[casa_atual] == len(minha_tabela)):
			if(len(lista_indices) != 1):
				for i in range(len(lista_indices), 0, -1):

					if(i - 1 == 0 and lista_indices[i-1] >= len(minha_tabela)):
						lista_indices[0] = 0
						casa_atual += 1
						lista_indices.append(0)
						print("Testando senhas com: %i caracteres" % len(lista_indices))

					elif(lista_indices[i-1] >= len(minha_tabela)):
						lista_indices[i-1] = 0
						lista_indices[i-2] += 1

			else:
				lista_indices[-1] = 0
				casa_atual += 1
				lista_indices.append(0)
				print("Testando senhas com: 1 caracteres")
				print("Testando senhas com: %i caracteres" % len(lista_indices))


		#print lista_indices
		#print teste








def main():

	while(True):
		validacao = True
		print("\n")
		senha = raw_input("Senha a ser descoberta: ")

		for l in senha:
			if(l not in caracteresValidos):
				print("Caracteres Invalidos")
				validacao = False

		if(len(senha) <= 20 and validacao == True):
			return(senha)

		else:
			print("ERRO")
			time.sleep(2.0)
			os.system("cls")










while(True):

	senha = main()
	os.system("cls")
	tempo_inicio = time.time()
	buscador(senha)
	print("Tempo Gasto: %.3f Segundos\n==================================================" % (time.time() - tempo_inicio))