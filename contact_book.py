def kisiyi_ekle():
    ad = input("Ad: ")
    telefon = input("Telefon: ")
    with open("contacts.txt", "a") as dosya:
        dosya.write(f"{ad},{telefon}\n")
    print("✅ Kişi rehbere eklendi.")

def kisileri_goster():
    try:
        with open("contacts.txt", "r") as dosya:
            kisiler = dosya.readlines()
            if not kisiler:
                print("📭 Rehber boş.")
                return
            print("\n📇 Kayıtlı Kişiler:")
            for satir in kisiler:
                ad, telefon = satir.strip().split(",")
                print(f"- {ad} : {telefon}")
    except FileNotFoundError:
        print("❗️ Rehber dosyası bulunamadı.")

def menu():
    while True:
        print("\n--- Kişi Rehberi ---")
        print("1. Kişi Ekle")
        print("2. Kişileri Göster")
        print("3. Çıkış")
        secim = input("Seçim yap (1/2/3): ")

        if secim == "1":
            kisiyi_ekle()
        elif secim == "2":
            kisileri_goster()
        elif secim == "3":
            print("📤 Programdan çıkılıyor...")
            break
        else:
            print("⚠️ Geçersiz seçim. Lütfen tekrar deneyin.")

# Programı başlat
menu()