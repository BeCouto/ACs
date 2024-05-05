while True:
    N = int(input())
    if N == 0:
        break
    
    results = input().split()
    Mary_wins = results.count('0')
    John_wins = results.count('1')
    
    print("Mary won", Mary_wins, "times and John won", John_wins, "times")
