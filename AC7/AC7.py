"""
Programação Estruturada
2024.1
20/04/2024

Gabriel Couto Barros
Ciência de Dados e IA, turma: 8001

Exercício 1 - AC7 - beecrowd.1132
"""
soma=0
a=int(input())
b=int(input())
if (b>a):
    for n in range(a,(b+1)):
        if (n%13!=0):
            soma+=n
if (a>b):
    for n in range(b,(a+1)):
        if (n%13!=0):
            soma+=n
print(soma)


"""
Exercícios AC6 - beecrowd.1173
"""
n= int(input())
print("N[%d] = %d" %(0,n))
for i in range(1,10):
    n *= 2
    print("N[%d] = %d" %(i,n))


"""
Exercícios AC6 - beecrowd.1180
"""
n = int(input())
lista = list(map(int, input().split()))
p = 0
m = lista[0]
count = 0
for i in lista:
    if (i < m):
        m = i
        p = count
    count += 1
print("Menor valor: %d" % m)
print("Posicao: %d" % p)


"""
Exercícios AC6 - beecrowd.1182
"""
l = int(input())
opera = input()
   

m=[]
for i in range(12):
    m.append([])

for i in range(12):
    for j in range(12):
        x = float(input())
        m[i].append(x)
        

if opera == 'S':
    soma = 0
    for k in range(12):
        soma = soma + m[k][l]
    print(soma)
if opera == 'M':
    med = 0
    soma = 0
    for k in range(12):
        soma = soma + m[k][l]
    med= soma/12
    print('{:.1f}'.format(med))


"""
Exercícios AC6 - beecrowd.1244
"""    
n = int(input())
while n > 0:
    n -= 1
    c = input().split()
    c.sort(key=len, reverse=True)
    for i in range(len(c)):
        print(c[i], end = '')
        if i != len(c)-1:
            print(' ', end = '')
    print()


"""
Exercícios AC6 - beecrowd.1065
""" 
count=0
for i in range(5):
    n = float(input())
    if(n%2==0):
        count=count+1
print("{} valores pares".format(count))


"""
Exercícios AC6 - beecrowd.1408
"""
a= float(input())
if (0<a<=400):
    rea=(((a*15)/100)+a)
    perc= 15
    print("Novo salario: %.2f" %rea)
    print("Reajuste ganho: %.2f" %(rea-a))
    print("Em percentual: " + str(perc) + " %")
elif(400<a<=800):
    rea=(((a*12)/100)+a)
    perc= 12
    print("Novo salario: %.2f" %rea)
    print("Reajuste ganho: %.2f" %(rea-a))
    print("Em percentual: " + str(perc) + " %")
elif(800<a<=1200):
    rea=(((a*10)/100)+a)
    perc= 10
    print("Novo salario: %.2f" %rea)
    print("Reajuste ganho: %.2f" %(rea-a))
    print("Em percentual: " + str(perc) + " %")
elif(1200<a<=2000):
    rea=(((a*7)/100)+a)
    perc= 7
    print("Novo salario: %.2f" %rea)
    print("Reajuste ganho: %.2f" %(rea-a))
    print("Em percentual: " + str(perc) + " %")
else:
    rea=(((a*4)/100)+a)
    perc= 4
    print("Novo salario: %.2f" %rea)
    print("Reajuste ganho: %.2f" %(rea-a))
    print("Em percentual: " + str(perc) + " %")