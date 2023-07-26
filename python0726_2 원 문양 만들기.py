import turtle as t

print('--- 정다각형 만들기 ---')

n = int(input('n 입력 : '))

t.shape("turtle")
t.color("pink")

t.down()

for x in range(n):
    t.fd(50)
    t.lt(360/n)

t.end_fill()
