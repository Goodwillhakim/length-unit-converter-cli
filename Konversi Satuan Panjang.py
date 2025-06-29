print("=" *41)
print("         Konversi Satuan Panjang")  
print("=" *41)

#Pengambilan Data

Nilai=float(input("Masukan Nilai: "))

print("1.Kilometer")
print("2.Hectometer")
print("3.Decameter")
print("4.Meter")
print("5.Decimeter")
print("6.Centimeter")
print("7.Milimeter")
Awal = input("Masukan Nomor Yang Mewakili Satuan Awal: ")
if Awal not in  ('1','2','3','4','5','6','7') :
    print("Nomor Tidak Valid")
    exit()
elif Awal in ('1','2','3','4','5','6','7') :
    print ("Kamu Memilih Satuan",Awal)
print("1.Kilometer")
print("2.Hectometer")
print("3.Decameter")
print("4.Meter")
print("5.Decimeter")
print("6.Centimeter")
print("7.Milimeter")
Tujuan= input("Masukan Nomor Yang Mewakili Satuan Tujuan: ")
if Tujuan not in  ('1','2','3','4','5','6','7') :
    print("Nomor Tidak Valid")
    exit()
elif Tujuan in ('1','2','3','4','5','6','7') :
    print ("Kamu Memilih Satuan",Tujuan)

Konversi = {
    '1':1000,
    '2':100,
    '3':10,
    '4':1,
    '5':0.1,
    '6':0.01,
    '7':0.001,
    }
    
print("=" *41)
print("         Konversi Satuan Panjang")  
print("=" *41)   
    
#Hasil 

Hasil = Nilai * Konversi[Awal] / Konversi[Tujuan]
print(f"Hasil Konversi: {Nilai} Dari Satuan {Awal} = {Hasil} Ke Satuan {Tujuan}")
    






