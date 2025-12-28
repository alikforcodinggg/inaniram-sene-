
users = {
    1: {"name": "Alik", "history": [], "favorites": [], "basket": [], "balance": 24.0},
    2: {"name": "Nihad", "history": [], "favorites": [], "basket": [], "balance": 10.0},
    3: {"name": "Lenin", "history": [], "favorites": [], "basket": [], "balance": 123445654.0},
    4: {"name": "Memis", "history": [], "favorites": [], "basket": [], "balance": 3.0},
}


products = {
    101: {"name": "alma", "price": 1.2, "category": "meyvə"},
    102: {"name": "banan", "price": 1.5, "category": "meyvə"},
    201: {"name": "çörək", "price": 0.8, "category": "ərzaq"},
    202: {"name": "yumurta", "price": 2.4, "category": "ərzaq"},
    301: {"name": "cola", "price": 1.7, "category": "içki"},
    302: {"name": "fanta", "price": 1.6, "category": "içki"},
    401: {"name": "ayaqqabi","price":59,  "category": "geyim"} ,
    402: {"name": "koynek",  "price":12,  "category": "geyim"} ,
    403: {"name": "jaket"   ,"price":45,  "category": "geyim"} ,

}

categories = ["meyvə", "ərzaq", "içki","geyim"]



def select_user():
    print("İstifadəçilər:")
    for uid, data in users.items():
        print(uid, "-", data["name"])
    uid = int(input("ID daxil edin: "))
    if uid in users:
        print("Giriş edildi:", users[uid]["name"])
        print("Balans:", users[uid]["balance"], "AZN")
        return uid
    else:
        print("Belə istifadəçi yoxdur!")
        return select_user()

def show_products():
    print("\n--- Məhsullar ---")
    for pid, p in products.items():
        print(f"{pid} | {p['name']} | {p['price']} AZN | {p['category']}")

def show_categories():
    print("\n--- Kateqoriyalar ---")
    for c in categories:
        print("- " + c)

def show_by_category(cat):
    print(f"\n--- {cat} kateqoriyası ---")
    for pid, p in products.items():
        if p["category"] == cat:
            print(f"{pid} | {p['name']} | {p['price']} AZN")

def add_history(uid, text):
    users[uid]["history"].append(text)

def add_favorite(uid, pid):
    if pid not in users[uid]["favorites"]:
        users[uid]["favorites"].append(pid)
        add_history(uid, f"Favoriyə əlavə edildi: {products[pid]['name']}")
        print("Favoriyə əlavə edildi!")
    else:
        print("Bu məhsul artıq favoridədir.")

def show_favorites(uid):
    favs = users[uid]["favorites"]
    if not favs:
        print("Favorilər boşdur!")
        return
    print("\n--- Favorilər ---")
    for pid in favs:
        p = products[pid]
        print(f"{pid} | {p['name']} | {p['price']} AZN")

def add_to_basket(uid, pid):
    if pid in products:
        users[uid]["basket"].append(pid)
        add_history(uid, f"Səbətə əlavə edildi: {products[pid]['name']}")
        print("Səbətə əlavə olundu!")
    else:
        print("Belə məhsul yoxdur!")

def show_basket(uid):
    basket = users[uid]["basket"]
    if not basket:
        print("Səbət boşdur!")
        return 0
    print("\n--- Səbət ---")
    total = 0
    for pid in basket:
        p = products[pid]
        print(f"{pid} | {p['name']} | {p['price']} AZN")
        total += p["price"]
    print("Ümumi:", total, "AZN")
    return total

def add_balance(uid):
    print("\n--- Balansı artır ---")
    amount = float(input("Məbləğ daxil edin: "))
    if amount <= 0:
        print("Yanlış məbləğ!")
        return
    users[uid]["balance"] += amount
    add_history(uid, f"Balans artırıldı: {amount} AZN")
    print("Yeni balans:", users[uid]["balance"], "AZN")

def pay(uid):
    total = show_basket(uid)
    if total == 0:
        return

    balance = users[uid]["balance"]
    print("Balansınız:", balance, "AZN")

    if balance < total:
        print("❌ Balans kifayət etmir!")
        print("💡 Xahiş olunur balansı artırın.")
        return

    conf = input("Ödənişi təsdiq edin? (bəli/xeyr): ")
    if conf == "bəli":
        users[uid]["balance"] -= total
        add_history(uid, f"Ödəniş edildi: {total} AZN")
        users[uid]["basket"].clear()
        print("✔️ Ödəniş tamamlandı!")
        print("Qalan balans:", users[uid]["balance"], "AZN")
    else:
        print("Ödəniş ləğv edildi.")

def show_history(uid):
    print("\n--- Tarixçə ---")
    if not users[uid]["history"]:
        print("Tarixçə boşdur.")
        return
    for h in users[uid]["history"]:
        print("-", h)



def menu(uid):
    while True:
        print("\n======== MINI MARKET ========")
        print("1. Məhsullara bax")
        print("2. Kateqoriyalara bax")
        print("3. Kateqoriyaya görə məhsullar")
        print("4. Səbətə əlavə et")
        print("5. Səbətə bax")
        print("6. Ödəniş et")
        print("7. Favoriyə əlavə et")
        print("8. Favorilərə bax")
        print("9. Tarixçəyə bax")
        print("10. Balansı artır")
        print("0. Çıxış")

        secim = input("Seçim: ")

        if secim == "1":
            show_products()

        elif secim == "2":
            show_categories()

        elif secim == "3":
            cat = input("Kateqoriya adı: ")
            show_by_category(cat)

        elif secim == "4":
            pid = int(input("Məhsul ID: "))
            add_to_basket(uid, pid)

        elif secim == "5":
            show_basket(uid)

        elif secim == "6":
            pay(uid)

        elif secim == "7":
            pid = int(input("Məhsul ID: "))
            add_favorite(uid, pid)

        elif secim == "8":
            show_favorites(uid)

        elif secim == "9":
            show_history(uid)

        elif secim == "10":
            add_balance(uid)

        elif secim == "0":
            print("Çıxış edildi.")

            break

        else:
            print("Yanlış seçim!")


user_id = select_user()
menu(user_id)