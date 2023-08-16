usuarios = {1, 2, 3, 4, 5, 6, 7}

usuarios.add(8)  # ao invés do append, utiliza-se o "ADD" nos conjuntos
print(usuarios)

frozenset({10, 11, 12})  # frozenset é um conjunto imutável

texto = "Bem vindo meu nome é Marcelo eu gosto muito de nomes e tenho o meu cachorro e gosto muito de cachorro"
separado = texto.split()  # separa a string palavra por palavra
conjunto_texto = set(separado)  # junta as palavras em um conjunto
print(separado)
print(conjunto_texto)
