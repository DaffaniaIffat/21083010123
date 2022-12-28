import os
import sys
total = []

def clear_screen():
  os.system('clear' if(os.name=='nt') else 'clear')

def menu_awal():
 while(True):
   print(" Shining Laundry Service ")
   print("****************************")
   print(" 1 Cuci Baju dan Celana ")
   print(" 2 Cuci Selimut dan Bedcover ")
   print(" 3 Cuci Sprei ")
   print(" 4 Nota ")
   print(" 5 Keluar Menu ")
   try:
     a=int(input("pilih layanan: "))
     print()
     if(a==1):
       cuci_bajucelana()
       kembali()
     elif(a==2):
       cuci_selimutbedcover()
       kembali()
     elif(a==3):
       cuci_sprei()
       kembali()
     elif(a==4):
       akhir()
       break
     elif(a==5):
       keluar()
       break
     else:
       print("Masukkan pilihan:")
       kembali()
       continue
   except ValueError:
     print("Silahkan Pilih Layanan yang Tersedia !")
     kembali()
     continue

def cuci_bajucelana():
  print(" No |    Berat      | Harga")
  print("*****************************")
  print(" 1 | 1 kilo         | 5000 ")
  print(" 2 | 2 kilo         | 10000")
  print(" 3 | 3 - 5 kilo     | 30000")
  print(" 4 | 6 - 8 kilo     | 45000")
  print(" 5 | 9 - 10 kilo    | 50000")
  NamaPelanggan=input("Masukkan Nama Anda :")
  kode=int(input("Masukkan kode berat barang :"))
  if(kode==1):
    berat1=int(input("Masukkan jumlah berat baju dan celana : "))
    harga1=5000
    total.append(harga1)
    tanya()
  elif(kode==2):
    berat2=int(input("Masukkan jumlah berat baju dan celana : "))
    harga2=10000
    total.append(harga2)
    tanya()
  elif(kode==3):
    berat3=int(input("Masukkan jumlah berat baju dan celana : "))
    harga3=30000
    total.append(harga3)
    tanya()
  elif(kode==4):
    berat4=int(input("Masukkan jumlah berat baju dan celana : "))
    harga4=45000
    total.append(harga4)
    tanya()
  elif(kode==5):
    berat5=int(input("Masukkan jumlah berat baju dan celana : "))
    harga5=50000
    total.append(harga5)
    tanya()
  return

def cuci_selimutbedcover():
  print(" No |      Jumlah       | Harga ")
  print("***********************************")
  print(" 1 | 1 selimut/Bedcover | 10000")
  print(" 2 | 2 selimut/Bedcover | 20000")
  print(" 3 | 3 selimut/Bedcover | 30000")
  print(" 4 | 4 selimut/Bedcover | 40000")
  print(" 5 | 5 selimut/Bedcover | 50000")
  NamaPelanggan=input("Masukkan Nama Anda :")
  kode=int(input("Masukkan Kode Jumlah Barang :"))
  if(kode==1):
    jumlah1=int(input("Masukkan jumlah selimut atau bedcover : ")) 
    harga1=10000
    total.append(harga1)
    tanya()
  elif(kode==2):
    jumlah2=int(input("Masukkan jumlah selimut atau bedcover : "))
    harga2=20000
    total.append(harga2)
    tanya()
  elif(kode==3):
    jumlah3=int(input("Masukkan jumlah selimut atau bedcover : "))
    harga3=30000
    total.append(harga3)
    tanya()  
  elif(kode==4):
    jumlah4=int(input("Masukkan jumlah selimut atau bedcover : "))
    harga4=40000
    total.append(harga4)
    tanya()
  elif(kode==5):
    jumlah5=int(input("Masukkan jumlah selimut atau bedcover : "))
    harga5=50000
    total.append(harga5)
    tanya()
  return

def cuci_sprei():
  print(" No | Jumlah | Harga ")
  print("**********************")
  print(" 1 | 1 sprei | 2000 ")
  print(" 2 | 2 sprei | 4000 ")
  print(" 3 | 3 sprei | 6000 ")
  print(" 4 | 4 sprei | 8000 ")
  print(" 5 | 5 sprei | 10000 ")
  NamaPelanggan=input("Masukkan Nama Anda :")
  kode=int(input("Masukkan Kode Jumlah Barang :"))
  if(kode==1):
    jumlah1=int(input("Masukkan jumlah sprei : "))
    harga1=2000
    total.append(harga)
    tanya()
  elif(kode==2):
    jumlah2=int(input("Masukkan jumlah sprei : "))
    harga2=4000
    total.append(harga)
    tanya()
  elif(kode==3):
    jumlah3=int(input("Masukkan jumlah sprei : "))
    harga3=6000
    total.append(harga3)
    tanya()
  elif(kode==4):
    jumlah4=int(input("Masukkan jumlah sprei : "))
    harga4=8000
    total.append(harga4)
    tanya()
  elif(kode==5):
    jumlah5=int(input("Masukkan jumlah sprei : "))
    harga5=10000
    total.append(harga5)
    tanya()
  return

def tanya():
  print("\n****************************************")
  tanya = input("apakah anda ingin laundry yang lain [ya/tidak] : ")
  print("****************************************")
  if(tanya=="ya"):
    menu_awal()
  elif(tanya=="tidak"):
    keluar()
  else:
    print("silahkan pilih menu yang lain!")

def kembali():
  print("\n")
  input("Tekan tombol apa saja untuk kembali")
  clear_screen()

def keluar():
  print("************************************")
  print("            Terimakasih             ")
  print("  Telah Memakai Jasa laundry Kami   ")
  print("************************************")

def akhir():
  for harga in total:
    print("SubTotal: ", sum(total))
    diskon=0
    totalharga=sum(total)
    if(totalharga >= 30000) and (totalharga < 50000):
      diskon=totalharga*10/100
    elif(totalharga >= 50000) and (totalharga < 80000):
      diskon=totalharga*15/100
    elif(totalharga >= 80000):
      diskon=totalharga*20/100
    else:
      diskon=0
    print("Diskon Pelanggan: ", diskon)
    totalakhir=totalharga-diskon
    print("Total: ", totalakhir)
    print("********************************")
    bayar=int(input("Jumlah Pembayaran : "))
    print("********************************")
    kembalian=bayar-totalakhir
    print("Jumlah Kembalian: ", kembalian)
    break
menu_awal()
