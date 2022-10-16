#!/bin/bash

echo -n "Input :"
read nama

declare -a ni

i=0
while [ $i -lt $nama ]
do
 read a[$i]
 ni[$i]=${a[$i]}
 i=`expr $i + 1`
done

x=0
for t in ${ni[@]}
do
 let p+=$t
done

echo " "
echo "IPS mhs = $p / $nama"
echo "IPK mhs = $((p / nama))"
