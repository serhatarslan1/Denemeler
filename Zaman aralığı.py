while True:
    print ("Sabah (1)")
    print ("Öğlen (2)")
    print ("Akşam (3)")
    print("Gece (4)")
    print("------------")
    print
    secim= input("Zaman dilimi seçin. :")
    isim= input("İsminiz :")

    if secim=="1":
        print ("günaydın", isim)
        print
    elif secim=="2":
        print("Tünaydın", isim)
        print
    elif secim=="3":
        print("İyi Akşamlar", isim)
    elif secim=="4":
        print("İyi Geceler", isim)
        print
    else:
        print("Gün aralığı geçersiz. Program Sonlandırılıyor...")
        break


