import random as r, turtle as t
# for a in range (4):
#     t.forward(100)
#     t.right(90)

t.speed(10)
for b in range(r.randint(5,20)):
    renkler=["red","green","blue"]
    ku=r.randint(50,150)
    x=r.randint(-300,300)
    y=r.randint(-300,300)
    t.color(r.choice(renkler))
    t.up()
    t.goto(x,y)
    t.down()
    for a in range(4):
        t.forward(ku)
        t.right(90)

input()

