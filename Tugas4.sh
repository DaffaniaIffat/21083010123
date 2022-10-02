#!/bin/bash

echo -n "Input :"
read i

while [ $i -gt 0 ];
do 
  echo "$i";
  let i=$i-2
done
 
