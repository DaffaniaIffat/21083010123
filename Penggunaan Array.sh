#!/bin/bash

# deklarasi array
distroLinux=("Maru" "Moru" "Boba" "Bobi" "Bada")

# random distro
let pilih=$RANDOM%5

# eksekusi
echo "Saya Memilih Distro $pilih, ${distroLinux[$pilih]} !"

