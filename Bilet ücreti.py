#25.02.2018
__author__ = "Serhat Arslan"

while True:
    print("Öğrenci (1)")
    print("Tam (2)")
    print("65 Yaş Üzeri(3)")
    print("-------------------")
    print
    seçim= input("Bilet Türü Seçiniz:")

    if seçim=="1":
        print("Öğrenci bilet ücretiniz 1.75 TL.")
    elif seçim=="2":
        print("Tam bilet ücretiniz 2.5 TL.")
    elif seçim=="3":
        print("65 yaş üzeri biletiniz ücretsizdir.")
    else:
        print("Lütfen geçerli bir bilet seçiniz. Program Sonlandı.")
    break


