def selamla(): print("Merhaba"*2)
def anamenu():


    print("╔═════════════════╗")
    print("║  VEKTOREL APP   ║")
    print("║1-Hesaplamalar   ║")
    print("║2-Oyunlar        ║")
    print("║3-               ║")
    print("║4-               ║")
    print("║Seçiminiz nedir?)║")
    print("╚═════════════════╝")
    secim=input()
    print("Seçiminiz:",secim, "idi.")

    if secim<"1" or secim>"10":
        print("secim 1 ile 10 arasında olmalı")
        anamenu()

    if secim=="1":
        print("Hesaplamaları seçtiniz.")

    if secim=="2": 
        print("Oyunları seçtiniz")

    # selamla()
anamenu()

