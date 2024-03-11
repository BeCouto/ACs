# AC1
# Equação de segundo grau:
# ax^2+bx = 0
# Aluno: Gabriel Couto Barros

# Valores dos coeficientes
a = int(input("Informe o parâmetro a da equação: "))
b = int(input("Informe o parâmetro b da equação: "))
c = int(input("Informe o parâmetro c da equação: "))

# Valor de delta
delta = b**2 - 4*a*c
print("o valor de delta é: ", delta)

# Valores das raizes
x1 = (-b + delta**0.5) / (2*a)
x2 = (-b - delta**0.5) / (2*a)
print("A primeira raiz da equação é: ", x1)
print("A segunda raiz da equação é: ", x2)

# AC1
# Calcular se o ano é Bissexto ou não
# Aluno: Gabriel Couto Barros

ano = int(input("Informe o ano: "))
print((ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0))
