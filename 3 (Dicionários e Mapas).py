texto = "Bem vindo meu nome é Marcelo eu gosto muito de nomes e tenho o meu cachorro e gosto muito de cachorro"
# MAPAS!

mapa = {                           # pode-se usar:
    "Marcelo": 1,                          # mapa = dict(Marcelo = 1, cachorro = 2)
    "cachorro": 1,
    "meu": 2
}
print(type(mapa))
print(mapa["Marcelo"])

funcao_get = mapa.get("sla", 0)    # a função get faz com que mostre o valor se o string não estiver presente no dicionário
print(funcao_get)

mapa["Marcelo"] = 2  # adiciona um valor a uma variável
del mapa["cachorro"]    # deleta um valor

for elemento in mapa:  # percorre as chaves do dicionário. pode-se usar o:
    print(elemento)         # for elemento in mapa.keys(): print(elemento)

for quantidade in mapa.values():  # percorre a quantidade de cada chave
    print(quantidade)

for elemento_quantidade in mapa.items():    # percorre o dicionário todo e faz tuplas com a chave e o valor
    print(elemento_quantidade)

for chave, valor in mapa.items():   # percorre o dicionário todo e printa isso
    print(chave, "=", valor)

lista = ["palavra {}".format(chave) for chave in mapa.keys()]   # faz uma lista com as chaves
print(lista)

mapa2 = {
    "cachorro": 2,
    "arroz": 3
}
mapa.update(mapa2)          # update adiciona os itens do mapa2 no mapa, se as chaves forem iguais o valor do mapa2 prevalece
print(mapa)
