from collections import defaultdict
from collections import Counter

texto = "Bem vindo meu nome é Marcelo eu gosto muito de nomes e tenho o meu cachorro e gosto muito de cachorro"
texto = texto.lower()
texto_separado = texto.split()

mapa = {}

for palavra in texto_separado:              # percorre a string palavra por palavra
    ate_agora = mapa.get(palavra, 0)        # se a palavra ainda não foi lida, retorna 0
    mapa[palavra] = ate_agora + 1           # adiciona 1 quando a palavra daquela chave for percorrida
print(mapa)

aparicoes = defaultdict(int)                # defaultdict descarta a necessidade de usar o get,
for word in texto_separado:                 # assim como no int() retorna 0 o defaultdict(int)
    aparicoes[word] += 1                    # retorna 0 se a palavra_atual ainda não estiver no dicionário
print(aparicoes)

novo_mapa = Counter(texto_separado)         # Counter conta e percorre um texto ao mesmo tempo
print(novo_mapa)


class Conta:
    def __init__(self):
        print("Criando uma conta")


contas = defaultdict(Conta)
print(contas["10"])
