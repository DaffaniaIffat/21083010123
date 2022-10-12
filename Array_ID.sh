#!/bin/bash

# deklarasi array indirect declaration
distroLinuxDekstop[0]=BlankOn
distroLinuxDekstop[1]=Ubuntu
distroLinuxDekstop[2]=Debian
distroLinuxDekstop[3]=ArchLinux
distroLinuxDekstop[4]=LinuxMint

distroLinuxDekstop[0]=UbuntuServer
distroLinuxDekstop[1]=CentOS
distroLinuxDekstop[2]=FerdoraServer

# cara mengambil nilai array
echo ${distroLinuxDekstop[*]}
echo ${distroLinuxServer[*]}
