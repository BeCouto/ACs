qtd = int(input())
num = []

for _ in range(qtd):
    ent = int(input())
    num.append(ent)

unicos = list(set(num))

for elemento in sorted(unicos):
    print(f"{elemento} aparece {num.count(elemento)} vez(es)")
