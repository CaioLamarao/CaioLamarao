'''
Algoritmo que visa realizar pesquisas dentro de uma lista de N elementos
da forma mais rápida possível
'''

def pesquisa_binaria(lista, item):
    baixo = 0
    alto = len(lista) - 1
    # Dividir o espaço amostral em 2 para que a análise ocorra de forma gradual
    while baixo <= alto:
        meio = (baixo + alto)//2
        chute = lista[meio]
        # Rearranjando a amostra de forma que a função siga reduzindo o espaço a ser pesquisado
        if chute == item:
            return meio
        if chute > item:
            alto = meio - 1
        else:
            baixo = meio + 1

    return None

minha_lista: [float] = [1, 3, 5, 7, 9]

print(pesquisa_binaria(minha_lista, 3))
print(pesquisa_binaria(minha_lista, -1))
