# -*- coding: utf-8 -*-
ogrenci1 = "engin"
ogrenci2 = "derin"
ogrenci3 = "salih"

#Bunlar için listelerden faydalanıyoruz.

ogrenciler = ["Engin","Derin","Salih","Aylin"]

print(ogrenciler[1])

#yeni bir eleman eklemek istendiğinde

ogrenciler.append("Ahmet")
print(ogrenciler)

# bir eleman çıkartılmak istendiğinde

ogrenciler.remove("Salih")
print(ogrenciler)

ogrenciler[0] = "Veli"

print(ogrenciler)

Sehirler = list(("Ankara", "İstanbul", "Ankara"))
print(Sehirler)
print(len(Sehirler))

#diğer fonksiyonlar

#print(Sehirler.clear())
#print(Sehirler)
print(Sehirler.count("Ankara"))

#print("Ankara indexi =" + str(Sehirler.index("Ankara")))
#Sehirler.pop(1)
#print(Sehirler)
#Sehirler.insert(0, "İstanbul")
#print(Sehirler)
#Sehirler.reverse()


#!!!! Diziler referans değildir.
#Bu sebeple aşağıda sehirler2 yi değiştirdiğimizde
#Sehirler de değişmektedir.

sehirler2 = Sehirler
sehirler2[0] =  "İzmir"
print(Sehirler)

#Bu sebeple aşağıdaki işlem yapılmalıdır.

Sehirler3 = Sehirler.copy()
print(Sehirler3)

#dizileri birbirine eklemek için;
Sehirler.extend(Sehirler3)
print(Sehirler)

#A'dan z'ye sıralamak için;
Sehirler.sort()

