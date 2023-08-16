from collections import Counter

texto1 = "por fim, vamos colocar tudo em pratica para vermos algum exemplo diferente"
texto2 = "entao o que eu queria fazer agora nao é um contador de palavras, eu fazer um contador de letras"

# for letra, frequencia in letras1.items():       -percorre o dicionário de letras e anota a chave(str) e a quantidade
# tupla = (letra, frequencia/total_letras1)    -de vezes que ela aparece. Forma uma tupla com a chave e a quantia de
# print(tupla)                                 -vezes que a letra apareceu dividido pelo total de letras


def analisa_frequencia_de_letras(texto):
    letras = Counter(texto.lower())                 # percorre todas as letras e conta elas
    total_de_caracteres = sum(letras.values())      # soma a quantidade de letras

    proporcoes = [(letra, frequencia / total_de_caracteres) for letra, frequencia in letras.items()]  # lista de tuplas
    proporcoes = Counter(dict(proporcoes))                                                           # dicionario
    mais_comuns = proporcoes.most_common(10)
    for caractere, proporcao in mais_comuns:
        print("{} => {:.2f}%".format(caractere, proporcao * 100))


print(analisa_frequencia_de_letras(texto1))
print(analisa_frequencia_de_letras(texto2))
