def anamenu():
    print("\n\nANA MENU")
    print("1-Hesaplamalar")
    print("2-Oyunlar")
    print("3-Çizimler")
    s=input("Seçiminiz")
    if s=="1":
        import cc_hesaplamalar
        cc_hesaplamalar.hesapmenu()
    if s=="2":
        import bb_oyunlar
    if s=="3":
        import d_cizimler
        d_cizimler.cizim_menu()

    anamenu()

anamenu()
