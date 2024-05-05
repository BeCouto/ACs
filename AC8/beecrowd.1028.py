# Aluno: Gabriel Couto Barros
# matricula 202401000671
while True:
    try:
        N = int(input())
        for _ in range(N):
            F1, F2 = map(int, input().split())
            while F2 != 0:
                F1, F2 = F2, F1 % F2
            print(F1)
    except (EOFError, ValueError):
        break
