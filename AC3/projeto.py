# AC3
# Exercício 1: triângulos
# Aluno: Gabriel Couto Barros

# valores do triangulo
a = float(input("Informe o comprimento do lado a: "))
b = float(input("Informe o comprimento do lado b: "))
c = float(input("Informe o comprimento do lado c: "))

# Funçao do triangulo
def laterais(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        if a == b == c:
            return "Equilátero"
        elif a == b or a == c or b == c:
            return "Isósceles"
        else:
            return "Escaleno"
    else:
        return "Não é triângulo"
    
# resultado        
triangulo = laterais(a, b, c)
print("O triângulo é:", triangulo)

# funçao teste
def tipo_triangulo():
    print(laterais(4, 4, 4)) # Equilátero
    print(laterais(2, 4, 4)) # Isósceles
    print(laterais(3, 4, 5)) # Escaleno
    print(laterais(1, 1, 4)) # Não é um triângulo

tipo_triangulo()

#exercicio 2
#dia da semanada
def dia_semana(num):
    dia = ("Domingo", "Segunda-feira", "Terça-feira", "Quarta-feira", "Quinta-feira", "Sexta-feira", "Sábado")
    if 1 <= num <= 7:
        return dia[num - 1]
    else:
        return "Erro"

num = int(input("Digite um número de 1 a 7: "))
nome = dia_semana(num)

if nome:
    print("O dia da semana é:", nome)
else:
    print("Número inválido")

# exercicio 3
# calculadora
def calculadora():
    print("soma (1), subtração (2), multiplicação (3), divisão (4)")
    operando = input("escolha uma operação: ")

    if operando in ('1', '2', '3', '4'):
        x = float(input("escolha o primeiro número: "))
        y = float(input("escolha o segundo número: "))
  
        if operando == '1':
            return x + y
        elif operando == '2':
            return x - y
        elif operando == '3':
            return x * y
        elif operando == '4':
            if y != 0:
                return x / y
            else:
                return "Erro: Divisão por zero."
    else:
        return "Operação inválida."

# Teste da função calculadora
print(calculadora())
