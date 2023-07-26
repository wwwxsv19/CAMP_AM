def f(a, b):
    return a+b, a-b, a*b, a//b

a, b = map(int, input().split())

print(f(a, b))
