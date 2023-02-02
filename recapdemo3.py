# -*- coding: utf-8 -*-

sayi = int(input("sayı giriniz: "))

for x in range(2,sayi):
    if (sayi % x) == 0:
        print ("bu sayı asal değildir")
        break 
    else :
        print("bu sayı asaldır")
        break
    
#veya bullion kullanırak çalışabilir.

sayi = int(input("sayı giriniz: "))
asalMi = True
for x in range(2,sayi):
    if (sayi % x) == 0:
        asalMi = False
        break 
if asalMi == True: 
    print("bu sayı asaldır")
else:
    print ("bu sayı asal değildir")
        

    