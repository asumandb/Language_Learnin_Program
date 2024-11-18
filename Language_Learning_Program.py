kelimeler = {}
print("Dil Öğrenme Programı")
print("1.Kelime Ekle")
print("2.Kelime Testi")
print("3.Cümle Kurma")
print("4.Çıkış")

while True:
    secim = input("Lütfen Bir Seçenek Girin:")
    if secim == "1":
        kelime = input("Lütfen Eklemek İstediğiniz Kelimeyi Girin:")
        anlam = input("Kelimenin Anlamını Girin:").strip()
        kelimeler[kelime] = anlam
        print(f"{kelime} eklendi.")

    elif secim == "2":
        if not kelimeler:
            print("Önce Kelime Eklemelisin!")
            continue
        print("Kelime Oyuna Hoşgeldiniz!")
        puan = 0
        for kelime,anlam in kelimeler.items():
            cevap = input(f"{anlam}:").strip()

            if cevap.lower() == kelime.lower():
                print("Doğru!")
                puan+=1

            else:
                print("Yanlış Cevap Girdiniz!")
        print(f"Test Tamamlandı")

    elif secim == "3":
        if not kelimeler:
            print("Önce Kelime Eklemesin!")
            continue
        print("Cümle Kurma Alıştırması")
        kelimeler_listesi = list(kelimeler.keys())
        print("Aşağıdaki Kelimelerle Bir Cümleyi Girin:")
        print("," .join(kelimeler_listesi))
        cumle = input("Oluşturduğunuz Cümleyi Girin:")
        print(f"Oluşturduğunuz Cümle: {cumle}")

    elif secim == "4":
        break

    else:
        print("Geçersiz Seçenek! Lütfen 1, 2, 3 veya 4 girin.")
        
