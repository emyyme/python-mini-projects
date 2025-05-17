def toplama(x, y):
    return x + y
def cikarma(x, y):
    return x - y
def carpma(x, y):
    return x * y
def bolme(x, y):
    if y == 0:
        return "Hata: 0'a bölünemez!"
    return x / y

print("İşlem Seçin:")
print("1. Toplama (+)")
print("2. Çıkarma (-)")
print("3. Çarpma (*)")
print("4. Bölme (/)")

secim = input("Seçiminizi girin (1/2/3/4): ")

sayi1 = float(input("1. sayıyı girin: "))
sayi2 = float(input("2. sayıyı girin: "))

if secim == '1':
    print(f"Sonuç: {toplama(sayi1, sayi2)}")
elif secim == '2':
    print(f"Sonuç: {cikarma(sayi1, sayi2)}")
elif secim == '3':
    print(f"Sonuç: {carpma(sayi1, sayi2)}")
elif secim == '4':
    print(f"Sonuç: {bolme(sayi1, sayi2)}")
else:
    print("Geçersiz seçim!")