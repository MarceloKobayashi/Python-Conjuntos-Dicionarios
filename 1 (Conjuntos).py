usuarios_data_science = [1, 2, 3, 4]
usuarios_machine_learning = [5, 2, 4, 6]

assistiram = usuarios_data_science.copy()
assistiram.extend(usuarios_machine_learning)  # usuarios repetidos
print(assistiram)

conjunto_assistiram = set(assistiram)
print(conjunto_assistiram)  # retira os elementos repetidos

# se a ordem não importa, pode-se usar conjuntos já na variável: usuarios_data_science = {1,2,3,4}
# não pode indexar um set, mas é possível percorrer um set:
for i in conjunto_assistiram:
    print(i)

usuario1 = {1, 2, 3, 4}
usuario2 = {5, 2, 4, 6}
uniao_1_2 = usuario1 | usuario2   # faz a função do "OU" nos conjuntos
print(uniao_1_2)

intersecao_1_2 = usuario1 & usuario2  # faz a função do "E" nos conjuntos
print(intersecao_1_2)

subtracao_1_2 = usuario1 - usuario2
print(subtracao_1_2)

uniao_exclusiva = usuario1 ^ usuario2  # união - interseção
print(uniao_exclusiva)
