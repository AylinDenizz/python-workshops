import sys

liste = [7, 'engin', 0,3]

for x in liste:
    try:
        
        print ("sayı " + str(x))
        sonuc = 1/int(x)       
        print("sonuç :" + str(sonuc))
    except: 
        print(str(x) + "hesaplanamadı")
        print("sistem hatası: " + str(sys.exc_info()[0]))
        
        # sistem hatasının ne olduğu sys kelimesi ile bulunabilir.
        
    finally:
        
        print("işlemler bitti")

    