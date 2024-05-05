"""
Programação Estruturada
2024.1
05/05/2024

Gabriel Couto Barros
Ciência de Dados e IA, turma: 8001

Exercício 1 - AC9 - beecrowd.1016
"""
def tempo_para_atingir_distancia(km):
    minutos = (km * 2)  
    return minutos

if __name__ == "__main__":
    km = int(input())
    minutos = tempo_para_atingir_distancia(km)
    print(minutos, "minutos")


"""
Exercícios 2 - AC9 - beecrowd.1153
""" 
def main():
    N = int(input())
    factorial = 1

    for i in range(N, 0, -1):
        factorial *= i
    
    print(factorial)

if __name__ == "__main__":
    main()


"""
Exercícios 3 - AC9 - beecrowd.1281
""" 
def main():
    N = int(input())

    for _ in range(N):
        M = int(input())
        frutas = []
        precos = []

        for _ in range(M):
            fruta, preco = input().split()
            frutas.append(fruta)
            precos.append(float(preco))

        P = int(input())
        resposta = 0.0

        for _ in range(P):
            fruta, quantidade = input().split()
            quantidade = int(quantidade)

            for j in range(M):
                if fruta == frutas[j]:
                    resposta += quantidade * precos[j]
                    break

        print("R$ {:.2f}".format(resposta))

if __name__ == "__main__":
    main()


"""
Exercícios 4 - AC9 - beecrowd.2006	
""" 
def main():
    
    tea_type = int(input())

    answers = list(map(int, input().split()))

    correct_guesses = answers.count(tea_type)

    print(correct_guesses)

if __name__ == "__main__":
    main()


"""
Exercícios 5 - AC9 - beecrowd.2339		
""" 
def main():
    c, p, f = map(int, input().split())

    if p >= c * f:
        print("S")
    else:
        print("N")

if __name__ == "__main__":
    main()


"""
Exercícios 6 - AC9 - beecrowd.2388			
""" 
def main():
    N = int(input())
    distancia_total = 0

    for _ in range(N):
        T, V = map(int, input().split())
        distancia_total += T * V

    print(distancia_total)

if __name__ == "__main__":
    main()


"""
Exercícios 7 - AC9 - beecrowd.2413				
"""
while True:
    try:
        t = int(input())
        primeiro_link = t * 4
        print(primeiro_link)
    except EOFError:
        break


"""
Exercícios 8 - AC9 - beecrowd.3048				
"""
N = int(input())
sequencia = [int(input()) for _ in range(N)]

consecutivos = 1 
atual = sequencia[0]

for i in range(1, N):
    if sequencia[i] != atual:
        consecutivos += 1
    atual = sequencia[i]

print(consecutivos)

