"""
Programação Estruturada
2024.1
12/05/2024

Gabriel Couto Barros
Ciência de Dados e IA, turma: 8001

Exercício 1 - AC10 - beecrowd.1258
"""
class Camiseta:
    def __init__(self, n, c, t):
        self.nome = n
        self.cor = c
        self.tamanho = t


def comp(a, b):
    if(a.cor == b.cor):
        if(a.tamanho == b.tamanho):
            if(a.nome < b.nome):
                return -1
            if(a.nome > b.nome):
                return 1
            return 0
        if(a.tamanho > b.tamanho):
            return -1
        return 1
    if(a.cor < b.cor):
        return -1
    return 1


def particao(V, inicio, fim):
    pivo = V[fim - 1]
    i = inicio
    for j in range(inicio, fim):
        if(comp(V[j], pivo) < 0):
            V[j], V[i] = V[i], V[j]
            i += 1

    if(comp(pivo, V[i]) < 0):
        V[fim - 1], V[i] = V[i], V[fim - 1]

    return i


def quickSort(V, inicio, fim):
    if(fim > inicio):
        posicaoPivo = particao(V, inicio, fim)
        quickSort(V, inicio, posicaoPivo)
        quickSort(V, posicaoPivo + 1, fim)


first = True
while True:
    try:
        N = int(input())

        if(N == 0):
            break

        if(first):
            first = False
        else:
            print('')

        camisetas = []
        for _ in range(N):
            nome = input()
            cor, tamanho = input().strip().split(' ')

            camisetas.append(Camiseta(nome, cor, tamanho))

        quickSort(camisetas, 0, len(camisetas))

        for camiseta in camisetas:
            print(f'{camiseta.cor} {camiseta.tamanho} {camiseta.nome}')
    except EOFError:
        break

"""
Exercícios 2 - AC10 - beecrowd.1260
"""
def process_cases(test_cases):
    results = []
    for case in test_cases:
        tree_counts = {}
        total_trees = len(case)
        for tree in case:
            tree_counts[tree] = tree_counts.get(tree, 0) + 1
        sorted_species = sorted(tree_counts)
        case_result = [f"{species} {(tree_counts[species] / total_trees) * 100:.4f}" for species in sorted_species]
        results.append(case_result)
    return results

def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split("\n")
    num_cases = int(data[0])
    cases, current_case = [], []
    for line in data[2:]:
        if line.strip():
            current_case.append(line.strip())
        elif current_case:
            cases.append(current_case)
            current_case = []
    if current_case:
        cases.append(current_case)
    results = process_cases(cases)
    for i, result in enumerate(results):
        print("\n".join(result))
        if i < len(results) - 1:
            print("")

if __name__ == "__main__":
    main()





"""
Exercícios 3 - AC10 - beecrowd.2518
""" 
import math
while True:
    try:
        deg = int(input())
        h, c, l = input().split()

        hip = math.sqrt((int(c)**2)+(int(h)**2))
        hip *= (int(l)/100*int(deg))/100
        print('%.4f'%hip)

    except EOFError:
        break
    