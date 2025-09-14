# Menu Pilihan
print(" Menu:")
print("1. Cek Tarif Tol")
print("2. Tambah Data Jalan Tol")
print("3.  Ubah Tarif Tol")
mulai = int(input("pilih menu 1/2/3: "))


# Untuk menampilkan kode daerah
if mulai == 1:
    print(" Daftar Daerah: ")
    print("1. Jawa")
    print("2. Sumatra")
    print("3. Kalimantan")
    print("4. Bali")
    nama_daerah = ("Daerah", "Jawa", "Sumatra", "Kalimantan", "Bali")

    # untuk cek tarif tol
    daerah = int(input("Pilih Daerah: "))

# jika memilih daerah jawa
    if daerah == 1:
        print(" Daftar jalan tol pada daerah", nama_daerah[daerah])
        print("1. Tanggerang-Merak")
        print("2. Jakarta-Cikampek")
        print("3. Cikampek-Palimanan")
        tol_jawa = ["", "Tanggerang-Merak", "Jakarta-Cikampek", "Cikampek-Palimanan"]
        jawa= int(input("pilih jalan tol: "))
        print(" golongan kendaraan: ")
        print("1. Golongan I(sedan,jip,pick up,truk kecil,bus)")
        print("2. Golongan II(truk muatan besar dengan 2 gandar)")
        print("3. Golongan III(truk muatan besar dengan 3 gandar)")
        print("4. Golongan IV(truk besar dengan 4 gandar)")
        print("5. Golongan V(truk besar dengan 5 gandar)")
        print("6. Golongan VI(kendaraan bermotor roda 2)")
        tarif_jawa = ["", 6500, 15000, 18000, 20000, 30000, 2000]
        gol_jawa = int(input("pilih golongan kendaraan: "))
        if jawa == 1:
            print("tarif tol", tol_jawa[jawa], "golongan", gol_jawa, "adalah Rp.", tarif_jawa[gol_jawa])
        elif jawa == 2:
            print("tarif tol", tol_jawa[jawa], "golongan", gol_jawa, "adalah Rp.", tarif_jawa[gol_jawa])
        elif jawa == 3:
            print("tarif tol", tol_jawa[jawa], "golongan", gol_jawa, "adalah Rp.", tarif_jawa[gol_jawa])
        else:
            print("Pilihan tidak valid.")

# jika memilih daerah sumatra
    elif daerah == 2:
        print(" Daftar jalan tol pada daerah", nama_daerah[daerah])
        print("1. Palembang-Indralaya")
        print("2. Indralaya-Muara Enim")
        tol_sumatra = ["", "Palembang-Indralaya", "Indralaya-Muara Enim"]
        sumatra = int(input("pilih jalan tol: "))
        print(" golongan kendaraan: ")
        print("1. Golongan I(sedan,jip,pick up,truk kecil,bus)")
        print("2. Golongan II(truk muatan besar dengan 2 gandar)")
        print("3. Golongan III(truk muatan besar dengan 3 gandar)")
        print("4. Golongan IV(truk besar dengan 4 gandar)")
        print("5. Golongan V(truk besar dengan 5 gandar)")
        print("6. Golongan VI(kendaraan bermotor roda 2)")
        tarif_sumatra = ["", 9000, 14000, 20000, 30000, 40000, 2000]
        gol_sumatra = int(input("pilih golongan kendaraan: "))
        if sumatra == 1:
            print("tarif tol", tol_sumatra[sumatra], "golongan", gol_sumatra, "adalah Rp.", tarif_sumatra[gol_sumatra])
        elif sumatra == 2:
            print("tarif tol", tol_sumatra[sumatra], "golongan", gol_sumatra, "adalah Rp.", tarif_sumatra[gol_sumatra])
        else:
            print("Pilihan tidak valid.")

# jika memilih daerah kalimantan
    elif daerah == 3:
        print(" Daftar jalan tol pada daerah", nama_daerah[daerah])
        print("1. Balikpapan-Samarinda")
        tol_kalimantan = ["", "Balikpapan-Samarinda"]
        kalimantan = int(input("pilih jalan tol: "))
        print(" golongan kendaraan: ")
        print("1. Golongan I(sedan,jip,pick up,truk kecil,bus)")
        print("2. Golongan II(truk muatan besar dengan 2 gandar)")
        print("3. Golongan III(truk muatan besar dengan 3 gandar)")
        print("4. Golongan IV(truk besar dengan 4 gandar)")
        print("5. Golongan V(truk besar dengan 5 gandar)")
        print("6. Golongan VI(kendaraan bermotor roda 2)")
        tarif_kalimantan = ["", 15000, 25000, 35000, 45000, 55000, 2000]
        gol_kalimantan = int(input("pilih golongan kendaraan: "))
        if kalimantan == 1:
            print("tarif tol", tol_kalimantan[kalimantan], "golongan", gol_kalimantan, "adalah Rp.", tarif_kalimantan[gol_kalimantan])
        else:
            print("Pilihan tidak valid.")

# jika memilih daerah bali
    elif daerah == 4:
        print(" Daftar jalan tol pada daerah", nama_daerah[daerah])
        print("1. I Gusti Ngurah Rai-Benoa-Nusa Dua")
        tol_bali = ["", "I Gusti Ngurah Rai-Benoa-Nusa Dua"]
        bali = int(input("pilih jalan tol: "))
        print(" golongan kendaraan: ")
        print("1. Golongan I(sedan,jip,pick up,truk kecil,bus)")
        print("2. Golongan II(truk muatan besar dengan 2 gandar)")
        print("3. Golongan III(truk muatan besar dengan 3 gandar)")
        print("4. Golongan IV(truk besar dengan 4 gandar)")
        print("5. Golongan V(truk besar dengan 5 gandar)")
        print("6. Golongan VI(kendaraan bermotor roda 2)")
        tarif_bali = ["", 7000, 12000, 17000, 22000, 27000, 2000]
        gol_bali = int(input("pilih golongan kendaraan: "))
        if bali == 1:
            print("tarif tol", tol_bali[bali], "golongan", gol_bali, "adalah Rp.", tarif_bali[gol_bali])
        else:
            print("Pilihan tidak valid.")
    else:
        print("Pilihan tidak valid.")

# untuk menambah data jalan tol
elif mulai == 2:
    print(" Daftar Daerah: ")
    print("1. Jawa")
    print("2. Sumatra")
    print("3. Kalimantan")
    print("4. Bali")
    nama_daerah = ("Daerah", "Jawa", "Sumatra", "Kalimantan", "Bali")
    daerah = int(input("Pilih Daerah: "))

# jika memilih daerah jawa
    if daerah == 1:
        tol_jawa = ["", "Tanggerang-Merak", "Jakarta-Cikampek", "Cikampek-Palimanan"]
        print("Daftar jalan tol pada daerah", nama_daerah[daerah], "pada saat ini:")
        print(tol_jawa)
        tol_jawa_baru = input(" Masukkan nama jalan tol baru: ")
        print(" update jalan tol pada daerah", nama_daerah[daerah], ":")
        tol_jawa.append(tol_jawa_baru)
        print(tol_jawa)

# jika memilih daerah sumatra
    elif daerah == 2:
        tol_sumatra = ["", "Palembang-Indralaya", "Indralaya-Muara Enim"]
        print("Daftar jalan tol pada daerah", nama_daerah[daerah], "pada saat ini:")
        print(tol_sumatra)
        tol_sumatra_baru = input(" Masukkan nama jalan tol baru: ")
        print(" update jalan tol pada daerah", nama_daerah[daerah], ":")
        tol_sumatra.append(tol_sumatra_baru)
        print(tol_sumatra)

# jika memilih daerah kalimantan
    elif daerah == 3:
        tol_kalimantan = ["", "Balikpapan-Samarinda"]
        print("Daftar jalan tol pada daerah", nama_daerah[daerah], "pada saat ini:")
        print(tol_kalimantan)
        tol_kalimantan_baru = input(" Masukkan nama jalan tol baru: ")
        print(" update jalan tol pada daerah", nama_daerah[daerah], ":")
        tol_kalimantan.append(tol_kalimantan_baru)
        print(tol_kalimantan)

# jika memilih daerah bali
    elif daerah == 4:
        tol_bali = ["", "I Gusti Ngurah Rai-Benoa-Nusa Dua"]
        print("Daftar jalan tol pada daerah", nama_daerah[daerah], "pada saat ini:")
        print(tol_bali)
        tol_bali_baru = input(" Masukkan nama jalan tol baru: ")
        print(" update jalan tol pada daerah", nama_daerah[daerah], ":")
        tol_bali.append(tol_bali_baru)
        print(tol_bali)
    else:
        print("Pilihan tidak valid.")


# untuk mengubah tarif tol
elif mulai == 3:
    print(" Daftar Daerah: ")
    print("1. Jawa")
    print("2. Sumatra")
    print("3. Kalimantan")
    print("4. Bali")
    nama_daerah = ("Daerah", "Jawa", "Sumatra", "Kalimantan", "Bali")
    daerah = int(input("Pilih Daerah: "))

# jika memilih daerah jawa
    if daerah == 1:
        tarif_jawa = ["", 6500, 15000, 105000, 20000, 30000, 2000]
        print("Tarif tol saat ini pada daerah", nama_daerah[daerah], ":")
        print("Golongan I", tarif_jawa[1])
        print("Golongan II", tarif_jawa[2])
        print("Golongan III", tarif_jawa[3])
        print("Golongan IV", tarif_jawa[4])
        print("Golongan V", tarif_jawa[5])
        print("Golongan VI", tarif_jawa[6])
        tarif_lama = int(input("Masukkan golongan kendaraan yang tarifnya ingin diubah (1-6): "))
        tarif_baru = int(input("Masukkan tarif tol baru: "))
        tarif_jawa[tarif_lama] = tarif_baru
        print("Update tarif tol pada daerah", nama_daerah[daerah], ":")
        print(tarif_jawa)

# jika memilih daerah sumatra
    elif daerah == 2:
        tarif_sumatra = ["", 9000, 14000, 20000, 30000, 40000, 2000]
        print("Tarif tol saat ini pada daerah", nama_daerah[daerah], ":")
        print("Golongan I", tarif_sumatra[1])
        print("Golongan II", tarif_sumatra[2])
        print("Golongan III", tarif_sumatra[3])
        print("Golongan IV", tarif_sumatra[4])
        print("Golongan V", tarif_sumatra[5])
        print("Golongan VI", tarif_sumatra[6])
        tarif_lama = int(input("Masukkan golongan kendaraan yang tarifnya ingin diubah (1-6): "))
        tarif_baru = int(input("Masukkan tarif tol baru: "))
        tarif_sumatra[tarif_lama] = tarif_baru
        print("Update tarif tol pada daerah", nama_daerah[daerah], ":")
        print(tarif_sumatra)

# jika memilih daerah kalimantan
    elif daerah == 3:
        tarif_kalimantan = ["", 15000, 25000, 35000, 45000, 55000, 2000]
        print("Tarif tol saat ini pada daerah", nama_daerah[daerah], ":")
        print("Golongan I", tarif_kalimantan[1])
        print("Golongan II", tarif_kalimantan[2])
        print("Golongan III", tarif_kalimantan[3])
        print("Golongan IV", tarif_kalimantan[4])
        print("Golongan V", tarif_kalimantan[5])
        print("Golongan VI", tarif_kalimantan[6])
        tarif_lama = int(input("Masukkan golongan kendaraan yang tarifnya ingin diubah (1-6): "))
        tarif_baru = int(input("Masukkan tarif tol baru: "))
        tarif_kalimantan[tarif_lama] = tarif_baru
        print("Update tarif tol pada daerah", nama_daerah[daerah], ":")
        print(tarif_kalimantan)

# jika memilih daerah bali
    elif daerah == 4:
        tarif_bali = ["", 7000, 12000, 17000, 22000, 27000, 2000]
        print("Tarif tol saat ini pada daerah", nama_daerah[daerah], ":")
        print("Golongan I", tarif_bali[1])
        print("Golongan II", tarif_bali[2])
        print("Golongan III", tarif_bali[3])
        print("Golongan IV", tarif_bali[4])
        print("Golongan V", tarif_bali[5])
        print("Golongan VI", tarif_bali[6])
        tarif_lama = int(input("Masukkan golongan kendaraan yang tarifnya ingin diubah (1-6): "))
        tarif_baru = int(input("Masukkan tarif tol baru: "))
        tarif_bali[tarif_lama] = tarif_baru
        print("Update tarif tol pada daerah", nama_daerah[daerah], ":")
        print(tarif_bali)
    else:
        print("Pilihan tidak valid.")
else:    
    print("Pilihan tidak valid.")











