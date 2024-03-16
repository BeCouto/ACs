#AC2
# Aluno: Gabriel Couto Barros
# matricula 202401000671
#Exercício 1: revisite a AC1

# Funçao e o valor de delta
def eq_seg_grau(a, b, c):
    delta = b**2 - 4*a*c
    if delta > 0:
        x1 = (-b + delta**0.5) / (2*a)
        x2 = (-b - delta**0.5) / (2*a)
        return x1, x2
    elif delta == 0:
        # Uma raiz real (raiz dupla)
        x = -b / (2*a)
        return x
    else:
        return "Não ha raízes reais"
# Valores dos coeficientes
a = int(input("Informe o parâmetro a da equação: "))
b = int(input("Informe o parâmetro b da equação: "))
c = int(input("Informe o parâmetro c da equação: "))

raizes = eq_seg_grau(a, b, c)
print("As raízes são:", raizes)


# Bissexto (ano)
def bissexto(ano):
    return (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0)
ano = int(input("Informe o ano: "))
print(bissexto(ano))

#Exercício 2:
#funçao para calcular o salario
def calcula_salario(valor_hora, num_horas, irpf=0.275):
    salario_bruto   = valor_hora * num_horas
    desconto_irpf   = salario_bruto * irpf
    salario_liquido = salario_bruto - desconto_irpf
    return round(salario_liquido) # Valor arredondado

#Valores da função:
valor_por_hora  = float(input("Informe o valor do salário por hora: "))          # Quantidade de ganho por hora
num_horas       = float(input("Informe o número de horas trabalhadas no mês: ")) # Quantidade de horas trabalhadas
salario_liquido = calcula_salario(valor_por_hora, num_horas, irpf=0.275)         # Resultados com imposto 
print("Salário líquido R$:",(salario_liquido))
