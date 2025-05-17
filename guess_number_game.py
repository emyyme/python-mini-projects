import random

# 1 ile 100 arasında rastgele sayı üret
secret_number = random.randint(1, 100)
guess = None
guess_limit = 7
guess_count = 0

print("🎯 1 ile 100 arasında bir sayı tuttum. Bakalım tahmin edebilecek misin!")

while guess_count < guess_limit:
    try:
        guess = int(input(f"\nTahmin {guess_count + 1}/{guess_limit}: "))
    except ValueError:
        print("⚠️ Lütfen geçerli bir sayı gir.")
        continue

    guess_count += 1

    if guess == secret_number:
        print(f"🎉 Tebrikler! {guess_count}. denemede bildin!")
        break
    elif guess < secret_number:
        print("🔼 Daha büyük bir sayı dene.")
    else:
        print("🔽 Daha küçük bir sayı dene.")

if guess != secret_number:
    print(f"\n❌ Tahmin hakkın bitti. Doğru cevap: {secret_number}")