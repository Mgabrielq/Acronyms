import time
import random

def binary_search(number, num_list):
    left = 0
    right = len(num_list) - 1

    while left <= right:
        mid = (left + right) // 2
        if num_list[mid] == number:
            return mid
        elif num_list[mid] < number:
            left = mid + 1
        else:
            right = mid - 1

    return -1  # Retorna -1 se o número não for encontrado

# Criando um array com um milhão de itens
big_list = list(range(1, 500000))

# Número que queremos encontrar (escolhido aleatoriamente dentro do intervalo do array)
number_to_find = random.randint(1, 500000)

# Ordenando a lista para usar a pesquisa binária
big_list.sort()

# Medindo o tempo de execução
start_time = time.time()
result = binary_search(number_to_find, big_list)
end_time = time.time()

if result != -1:
    print(f"O número {number_to_find} está na posição {result} do array.")
else:
    print(f"O número {number_to_find} não está no array.")

execution_time = end_time - start_time
print(f'O programa levou {execution_time:.6f} segundos para ser executado.')
