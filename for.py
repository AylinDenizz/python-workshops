# -*- coding: utf-8 -*-

sehirler = ["Ankara","istanbul","manisa"]

for sehir in sehirler:
    print(sehir + " için kod = " + sehir[0:3])
    if sehir != "Ankara":
        print("************")  
        break
    
#break de döngü bitiyor. 
#continue için döngünün o anki durumunu iptal eder.

for sehir in sehirler:
   
    if sehir == "Ankara":
        continue
    print(sehir + " için kod = " + sehir[0:3])


