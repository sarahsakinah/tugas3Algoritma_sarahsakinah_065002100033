# -*- coding: utf-8 -*-
"""
Created on Wed Nov 24 23:52:57 2021

@author: Hp
"""

import sys

def main():
    print("Daftar Hotkey\nj->Jabodetabek\ndj->Pulau Jawa\nlj->Luar Jawab")
    tujuan= bacavalidinput1("Tujuan Barang(q-quit)= ")
    lourd = bacavalidinput2("Masukan lourd Barang = ")
def baner():
    print("PROGRAM MENGHITUNG BIAYA PENGIRIMAN")

def bacavalidinput1(s):
    while True:
        global tujuan
        global preis
        tujuan=input(s)    
        if tujuan == "jdk":
            print("Jabodetabek")
            preis=10000
            break
        elif tujuan=="sarah":
            sys.exit(0)
        elif tujuan == "dpj":
            print("Dalam Pulau Jawa")
            preis=25000
            break
        elif tujuan == "lpj":
            print("Luar pulau Jawa")
            preis=50000
            break
    return preis    
def bacavalidinput2(s):
    while True:
        global lourd
        global preis1
        lourd=int(input(s))
        if lourd >0 and lourd <= 20:
            preis1 = 15000
            break
        elif lourd > 20:
            preis1 = 15000 +((lourd-20)*1500)
            break
    return preis1,lourd
def Rincian():
    print("xxxxxxxxxxxxxxx Rincian Biaya xxxxxxxxxxxxxxx")
    print(f'1.tujuan  = {tujuan}                 Rp.{preis}')
    print(f'2.lourd   = {lourd}kg               Rp.{preis1}')
    print(f'3.PPN 10% =                    Rp.{int((preis+preis1)*(10/100))}')
    print(f'4.Total   =                    Rp.{int(preis+preis1+(preis+preis1)*(10/100))}')
    print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
if __name__ == '__main__':
    baner()
    main()
    Rincian()