from os import getpid
from time import time, sleep
from multiprocessing import cpu_count, Pool, Process

def cetak(i):
 print(1, "Ganjil", "- ID proses", getpid())
 print(2, "Genap", "- ID proses", getpid())
 print(3, "Ganjil", "- ID proses", getpid())
 sleep(1)

print("Sekuensial")
sekuensial_awal = time()
for i in range(1):
 cetak(i)
sekuensial_akhir = time()

print("multiprocessing.Process")
kumpulan_proses = []
process_awal = time()
for i in range(1):
 p = Process(target=cetak, args=(i,))
 kumpulan_proses.append(p)
 p.start()
for i in kumpulan_proses:
 p.join()
process_akhir = time()

print("multiprocessing.Pool")
pool_awal = time()
pool = Pool()
pool.map(cetak, range(0,1))
pool.close()
pool_akhir = time()

print("Waktu eksekusi sekuensial :", sekuensial_akhir - sekuensial_awal, "detik")
print("Waktu eksekusi multiprocessing.Process :", process_akhir - process_awal, "detik")
print("Waktu eksekusi multiprocessing.Pool :", pool_akhir - pool_awal, "detik")

