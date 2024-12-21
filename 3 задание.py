# 3 задание
import turtle as t
k = 30
t.up()
t.tracer(0)
for x in range(-20, 30):
    for y in range(-20, 20):
       t.goto(x * k, y * k)
       t.dot(4, 'magenta')
t.speed(1000)
t.tracer(1)
t.goto(-20 * k, 18 * k)
t.down()
for i in range(2):
    t.forward(5 * k)
    t.left(90)
    t.back(13 * k)
    t.left(90)
t.up()
t.back(10 * k)
t.right(90)
t.forward(9 * k)
t.left(90)
t.down()
for i in range(2):
    t.forward(11 * k)
    t.right(90)
    t.forward(9 * k)
    t.right(90)
t.done()


