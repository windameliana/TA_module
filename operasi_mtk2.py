import module_lingkaran
import module_segitiga

while True:
    print("\npilih bangun ruang apa? :")
    print("1. lingkaran")
    print("2. segitiga")

    pilih_bangun = input("pilih yang mana(1/2): ")

    if pilih_bangun == "1":
        r = int(input("masukkan nilai r : "))
        # manggil rumus kali yak
        luas_lingkaran = module_lingkaran.luas(r)
        keliling_lingkaran = module_lingkaran.keliling(r)
        print("luas lingkaran :", luas_lingkaran)
        print("keliling lingkaran :", keliling_lingkaran)

    elif pilih_bangun == "2":
        a = int(input("masukkan nilai a : "))
        t = int(input("masukkan nilai t : "))
        sisi = int(input("masukkan nilai sisinya : "))
        # manggil rumus kali yak
        hasil_luas = module_segitiga.luas(a, t)
        hasil_keliling = module_segitiga.keliling(sisi)
        print("luas segitiga :", hasil_luas)
        print("keliling segitiga :", hasil_keliling)

    else:
        print("silahkan cek ulang")
        continue

    stop = input("Mau lagi ? (y/n) : ")
    if stop == "n" or stop == "N":
        break
