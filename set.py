# -*- coding: utf-8 -*-
#listelere benzerdir.
#en önemli özelliği indexsiz ve sırasız elemanlardan oluşur..
#Veri tekrarı söz konusu olamaz.
#Bu veri yapısı performanslı bir data sağlar.

mySet = {"Engin","Derin","Salih"}
print(mySet)

for student in mySet:
    print(student)
    
if "Derin" in mySet:
    print("Listede var")
    
mySet.add("Ali")
#listeye ekleme yapmak için yapılır.

mySet.update(["merve","mert","Selin"])
print(mySet)

mySet.remove("Selin")
print(mySet)

mySet.discard("Selin")
print(mySet)
#Bu fonk. sayesinde selin kelimesini bulamasada hata vermez.

x = mySet.clear()
#listeden bir öğeyi siler.pop kullanılmaz. Çünkü o rastgele bir öğeyi siler.

del mySet
#listeyi silmeye yarar.

