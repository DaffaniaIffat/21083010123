#!/bin/bash

printf "Jajan apa yang kamu suka ?\n"
printf "donat ?\n"
printf "jus ?\n"
printf "gorengan ?\n"

read Jajan

case "$jajan" in
 "donat")
   echo "Donat buk mah wenak slur!"
   ;;
 "jus")
   echo "Jus e mas Budi mantap bat"
   ;;
 "gorengan")
   echo " gorengane kantin rasane unch-unch"
   ;;
 *)
   echo "Makanan yang kamu suka gaenak hehe"
   ;;
esac

