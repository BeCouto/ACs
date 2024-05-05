"""
Programação Estruturada
2024.1
01/04/2024

Gabriel Couto barros
Ciência de Dados e IA, turma: 8001

Exercícios AC6 - beecrowd.1000	 
"""
print("Hello World!")


"""
Exercícios AC6 - beecrowd.1001 
"""
A = int(input())
B = int(input())

X = A + B

print("X =", X)


"""
Exercícios AC6 - beecrowd.1010
"""
total = 0

for i in range(2):
    item = input().split(" ")
    cod = int(item[0])
    qtd = int(item[1])
    valor = float(item[2])
    total = total + qtd * valor

print("VALOR A PAGAR: R$ %.2f" % total)


"""
Exercícios AC6 - beecrowd.1013	 
"""
def main():
    a, b, c = map(int, input().split())
    
    maiorAB = (a + b + abs(a - b)) / 2
    maiorC = (maiorAB + c + abs(maiorAB - c)) / 2
    
    print("{:.0f} eh o maior".format(maiorC))

main()


"""
Exercícios AC6 - beecrowd.1015
"""
import math

def main():
    x1, y1 = map(float, input().split())
    x2, y2 = map(float, input().split())
    
    distancia = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    print("{:.4f}".format(distancia))

main()
