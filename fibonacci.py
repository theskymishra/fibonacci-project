def fibonacci(n):
    series =[]
    a,b = 0,1
    for _ in range(n):
        series.append(a)
        a,b = b, a+b
    return series
#n = 10 changed to n = 15
n=15
print("Fibonacci Series:")
print(fibonacci(n))