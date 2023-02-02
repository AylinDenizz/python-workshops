# -*- coding: utf-8 -*-

import sqlite3

def selectOperasyonlari():
    connection = sqlite3.connect("chinook.db")  
    
    
    # ++ order by komutu ++
    # cursor = connection.execute("""select FirstName,LastName from 
    #                             customers where city = 'Prague'
    #                             order by FirstName,LastName desc""")
    
    # for row in cursor :
    #     print ("First Name:" +row[0])
    #     print ("Last Name:" +row[1])
    #     print ("********")
    
    
    # ++ group by komutu ++
    # cursor = connection.execute("""select city,count(*) from Customers
    #                             group by city having count(*)>1 
    #                             order by city desc""")
    
    # for row in cursor :
    #     print ("City=" +row[0])
    #     print ("Count=" + str(row[1]))
    #     print ("********")
    
    cursor = connection.execute("""select FirstName,LastName from Customers
                                where firstName like 'a%' """)
    
    for row in cursor :
        print ("FirstName=" +row[0])
        print ("LastName=" + row[1])
        print ("********")
    
    
    connection.close()
    
# selectOperasyonlari()



def insertCustomer():
    connection = sqlite3.connect("chinook.db")
    connection.execute("""insert into customers
                        (firstName,lastName,city,email) values 
                        ('Engin','Demiroğ', 'Ankara', 'engindemirog@gmail.com')""")
                         
    connection.commit()
    connection.close()
# insertCustomer()



def updateCustomer() :
    connection = sqlite3.connect("chinook.db")
    connection.execute("""update customers set city='İstanbul'
                        where city='Ankara'""")
    connection.commit()
    connection.close()
# updateCustomer( )    

def deleteCustomer() :
    connection = sqlite3.connect("chinook.db")
    connection.execute("""delete from customers where
                       customerid=60""")
                       
    connection.commit()
    connection.close()

# deleteCustomer()

def joinOperasyonlari():
    connection = sqlite3.connect("chinook.db")   
    cursor = connection.execute("""select albums.Title, artists.Name
                                from artists inner join albums on
                                artists.ArtistId = albums.ArtistId""")
    for row in cursor :
        print ("Title=" +row[0])
        print ("Name=" + row[1])
        print ("********")                          
joinOperasyonlari()
