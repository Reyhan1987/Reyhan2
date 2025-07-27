def cizim_menu():
    print("\n\nÇİZİM MENU")
    print("1-Kare")
    print("2-Desen")
    print("3-Üçgen")
    s=input("Seçiminiz?")
    if s=="1":kareciz()
    if s=="3":ucgenciz()
def kareciz():
    import turtle
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(100)
    turtle.right(90)
def ucgenciz():
    import turtle
    turtle.forward(100)
    turtle.right(120)
    turtle.forward(100)
    turtle.right(120)
    turtle.forward(100)
    turtle.right(120)

