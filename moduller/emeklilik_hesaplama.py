# Kadın için 58, erkek için 60 yaşını doldurmak ve 25 yıldan beri sigortalı bulunmak ve en az 4500 gün prim ödemiş olmak.Bir ay 30 prim günü

import datetime
def emeklilik_menu():

    print("\033[1;32;40m")
    print("╔═════════════════════════════════════════╗")
    print("║        EMEKLİLİK HESAPLAMA              ║")
    print("║                                         ║")
    print("║   1-KADIN EMEKLİLİK                     ║")
    print("║   2-ERKEK EMEKLİLİK                     ║")
    print("║                                         ║")    
    print("║     Cinsiyetiniz nedir?                 ║")
    print("╚═════════════════════════════════════════╝")
    s=int(input("Cinsiyetiniz nedir?"))
    if s==1:
        import moduller.kadin_emeklilik
        moduller.kadin_emeklilik.kadin_emeklilik_menu()
                
    elif s==2:
        import moduller.erkek_emeklilik
        moduller.erkek_emeklilik.erkek_emeklilik_menu()
    
    emeklilik_menu()
emeklilik_menu()


