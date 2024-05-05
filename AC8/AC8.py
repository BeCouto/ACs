# Aluno: Gabriel Couto Barros
# matricula 202401000671

"""
Programação Estruturada
2024.1
05/05/2024

Gabriel Couto Barros
Ciência de Dados e IA, turma: 8001

Exercício 1 - AC8 - beecrowd.1028
"""
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


"""
Programação Estruturada
2024.1
05/05/2024

Gabriel Couto Barros
Ciência de Dados e IA, turma: 8001

Exercício 2 - AC8 - beecrowd.1087
"""
while True:
    X1, Y1, X2, Y2 = map(int, input().split())
    if X1 == 0 and X2 == 0 and Y1 == 0 and Y2 == 0:
        break
    if X1 == X2 and Y1 == Y2:
        print("0")
    elif abs(X1 - X2) == abs(Y1 - Y2):
        print("1")
    elif X1 == X2 or Y1 == Y2:
        print("1")
    else:
        print("2")


"""
Programação Estruturada
2024.1
05/05/2024

Gabriel Couto Barros
Ciência de Dados e IA, turma: 8001

Exercício 3 - AC8 - beecrowd.1161
"""
def le_info():
    try:
        m, n = map(int, input().split())
        return m, n
    except EOFError:
        return None, None

def calcula_fatorial(n):
    fatorial = 1
    if n == 0:
        return 1
    for i in range(1, n + 1):
        fatorial *= i
    return fatorial

while True:
    m, n = le_info()
    if m is None:
        break
    soma_fatorial = calcula_fatorial(m) + calcula_fatorial(n)
    print(soma_fatorial)


"""
Programação Estruturada
2024.1
05/05/2024

Gabriel Couto Barros
Ciência de Dados e IA, turma: 8001

Exercício 4 - AC8 - beecrowd.1170 
"""

n = int(input())

for _ in range(n):
    x = float(input())
    dias = 0
    while x > 1:
        x /= 2
        dias += 1
    print(f"{dias} dias")


"""
Programação Estruturada
2024.1
05/05/2024

Gabriel Couto Barros
Ciência de Dados e IA, turma: 8001

Exercício 5 - AC8 - beecrowd.1171 
"""
qtd = int(input())
num = []

for _ in range(qtd):
    ent = int(input())
    num.append(ent)

unicos = list(set(num))

for elemento in sorted(unicos):
    print(f"{elemento} aparece {num.count(elemento)} vez(es)")


"""
Programação Estruturada
2024.1
05/05/2024

Gabriel Couto Barros
Ciência de Dados e IA, turma: 8001

Exercício 6 - AC8 - beecrowd.1221 
"""
import math

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, math.isqrt(num) + 1):
        if num % i == 0:
            return False
    return True

n = int(input())

for _ in range(n):
    p = int(input())
    if is_prime(p):
        print("Prime")
    else:
        print("Not Prime")


"""
Programação Estruturada
2024.1
05/05/2024

Gabriel Couto Barros
Ciência de Dados e IA, turma: 8001

Exercício 7 - AC8 - beecrowd.1329 
"""
while True:
    N = int(input())
    if N == 0:
        break
    
    results = input().split()
    Mary_wins = results.count('0')
    John_wins = results.count('1')
    
    print("Mary won", Mary_wins, "times and John won", John_wins, "times")


"""
Programação Estruturada
2024.1
05/05/2024

Gabriel Couto Barros
Ciência de Dados e IA, turma: 8001

Exercício 8 - AC8 - beecrowd.1555 
"""
casos = int(input())

for _ in range(casos):
    x, y = map(int, input().split())

    rafael = (3*x)**2 + y**2
    beto = 2*(x**2) + (5*y)**2
    carlos = -100*x + y**3

    if rafael > beto and rafael > carlos:
        print("Rafael ganhou")
    elif beto > rafael and beto > carlos:
        print("Beto ganhou")
    else:
        print("Carlos ganhou")

