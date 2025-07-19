import turtle as t
def kare_ciz():
    for a in range (4):
        t.forward(100)
        t.right(90)

def ucgen_ciz():
    for a in range(3):
        t.forward(100)
        t.right(120)

def cizimmenu():
    print("╔═════════════════╗")
    print("║   CİZİMLER      ║")
    print("║1-Kare ciz       ║")
    print("║2-Desen          ║")
    print("║3-               ║")
    print("║seçiminiz nedir?)║")
    print("╚═════════════════╝")
    sec=int(input("Seçim nedir?")) 
    if sec==1:kare_ciz()
    if sec==2:ucgen_ciz()


