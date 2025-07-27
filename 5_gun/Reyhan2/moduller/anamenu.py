def anamenu():
    print("╔═════════════════╗")
    print("║  VEKTOREL APP   ║")
    print("║1-Hesaplamalar   ║")
    print("║2-Çizimler       ║")
    print("║3-Oyunlar        ║")
    print("║seçiminiz nedir?)║")
    print("╚═════════════════╝")
    s=int(input("Seçiminiz nedir?"))
    if s==1:
        import moduller.hesaplamalar
        moduller.hesaplamalar.hesapmenu()
    if s==2:
        import moduller.cizimler as ciz
        ciz.cizimmenu()
    
    anamenu

anamenu