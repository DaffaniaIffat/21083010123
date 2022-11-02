#!/bin/bash

identitas() {
   parameter1=$1
   parameter2=$2
   parameter3=$3
   echo "$parameter1"
   echo "$parameter2"
   echo "$parameter3"
}

echo "Masukkan Panjang : "
read a
echo "Masukkan Lebar : "
read b
let luas=$a*$b
echo "Luas Persegi : 
$luas "
read c
