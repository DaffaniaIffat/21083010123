#!/bin/bash

echo "Minuman Segar";
echo "1. Milo ice";
echo "2. Ocean Blue";
echo "3. Chocolateh";
echo "4. Soda gembira";
echo "5. Leci tea";
echo "6. Exit";
read -p "Pilihan anda [1-6] :" pill;

if [ $pill -eq 1 ];
then
 echo "Banyak minuman =";
 read jum
 let bayar=jum*10000;
elif [ $angka -eq 2 ];
then 
 echo "Banyak minuman =";
 read jum
 let bayar=jum*8000;
elif [ $angka -eq 3 ];
then
 echo "Banyak minuman =";
 read jum
 let bayar=jum*15000;
elif [ $angka -eq 4 ];
then
 echo "Banyak minuman =";
 read jum
 let bayar=jum*17000;
elif [ $angka -eq 5 ];
then
 echo "Banyak minuman =";
 read jum
 let bayar=jum*90000;
elif [ $angka -eq 6 ];
then
 exit 0
else
 echo "Maaf menu tidak tersedia"
 exit 1
fi

echo "Harga bayar = Rp. $bayar"
echo "Terima Kasih"
