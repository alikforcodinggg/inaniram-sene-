def toplma():
    a = int(input("Birinci ededi daxil edin: "))
    b = int(input("Ikinci ededi daxil edin: "))
    cem = a + b
    print("Ededlerin cemi:", cem)

def cixma():
    a = int(input("Birinci ededi daxil edin: "))
    b = int(input("Ikinci ededi daxil edin: "))
    ferq = a - b
    print("Ededlerin ferqi:", ferq)
def vurma():
    a = int(input("Birinci ededi daxil edin: "))
    b = int(input("Ikinci ededi daxil edin: "))
    hasil = a * b
    print("Ededlerin hasili:", hasil)
def bolme():
    a = int(input("Birinci ededi daxil edin: "))
    b = int(input("Ikinci ededi daxil edin: "))
    if b != 0:
        bolum = a / b
        print("Ededlerin bolumu:", bolum)
    else:
        print("Sifira bolme mumkun deyil.")
def main():
    while True:
        print("\nEmeliyyat secin:")
        print("1. Toplama")
        print("2. Cixma")
        print("3. Vurma")
        print("4. Bolme")
        print("5. Cixis")

        secim = input("Seciminizi daxil edin (1-5): ")

        if secim == '1':
            toplma()
        elif secim == '2':
            cixma()
        elif secim == '3':
            vurma()
        elif secim == '4':
            bolme()
        elif secim == '5':
            print("Proqramdan cixilir.")
            break
        else:
            print("Yanlis secim, yeniden cehd edin.")
def run():
    main()
run()