# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

mesaj = "Merhaba Dünya"

print(mesaj[2:5])

yeniMesaj2 = mesaj[len(mesaj)-1]
print(yeniMesaj2)

#lower/upper
print(mesaj.upper())
print(mesaj.lower())
#upper ve lower karakterlerin büyük ve 
#küçük harfe dönüşmesini sağlar.

#replace
mesaj = mesaj.replace("ü" , "u")
print(mesaj.replace("a" , "e"))

#split ve stip
bilgi = " Aylin Deni 25 İmir ". strip()
print(bilgi.split())
print(bilgi.split(" "))

#input
#aşağıdaki şekilde kullanıcıdan bilgi alınabilir.

ad = input ("Adını?")
            
            