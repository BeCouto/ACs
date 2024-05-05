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
