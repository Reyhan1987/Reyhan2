import random as r, turtle as t

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
    ks=r.randint(3,7)
    for a in range(ks):
        t.forward(ku)
        t.right(360/ks)

input()


