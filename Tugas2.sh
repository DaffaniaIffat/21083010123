#!/bin/bash

bil1=100
bil2=28

#memakai let
let a=bil1+bil2
echo "$a"
let b=bil1-bil2
echo "$b"
let c=bil1*bil2
echo "$c"
let d=bil1/bil2
echo "$d"
let e=bil1%bil2
echo "$e"

#memakai expr
expr $bil1 + $bil2
expr $bil1 - $bil2
expr $bil1 / $bil2
expr $bil1 % $bil2
 
#memakai $
a=$(( bil1 + bil2 ))
echo $a
b=$(( bil1 - bil2 ))
echo $b
c=$(( bil1 * bil2 ))
echo $c
d=$(( bil1 / bil2 ))
echo $d
e=$(( bil1 % bil2 ))
echo $e
