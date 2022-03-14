def buscaMenor(arr):
  menor = arr[0]
  # Armazena o menor valor
  menor_indice = 0
  #Armazena o indice de menor valor
  for i in range(1, len(arr)):
    if arr[i] < menor:
      menor = arr[i]
      menor_indice = i
  return menor_indice

def ordenacaoPorSelecao(arr):
  #Ordenando
  novoArr = []
  for i in range(len(arr)):
    menor = buscaMenor(arr)
    #Encontar o menor elemento e adicionar à nova Lista
    novoArr.append((arr.pop(menor))
  return novoArr
                   
print(ordenacaoPorSelecao([5, 3, 6, 2, 10])                   
