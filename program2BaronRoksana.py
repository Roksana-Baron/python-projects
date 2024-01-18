print('Aplikacje bazodanowe')

import sys
from os import system, name
from datetime import datetime
import pyodbc

authorName = 'Baron Roksana'

def print_menu():
    print (30*'-')
    print(" MENU GŁÓWNE - SYSTEM: " + name + 'Autor:' + authorName)
    print (30*'-')
    print ("1. Połączenie z bazą danych")
    print ("2. Zapytanie 1: zapytanie wewnętrzne łączące dane z dwóch relacji (tabel) za pomocą WHERE")
    print ("3. Zapytanie 2: zapytanie wewnętrzne łączące dane z dwóch relacji (tabel) za pomocą JOIN")
    print ("4. Zapytanie 3: zapytanie zewnętrzne łączące dane z dwóch relacji (tabel) za pomocą LEFT JOIN")
    print ("5. Zapytanie 4: zapytanie zewnętrzne łączące dane z dwóch relacji (tabel) za pomocą RIGHT JOIN")
    print ("6. Zapytanie 5: zapytanie SQL operacja projekcji")
    print ("7. Zapytanie 6: zapytanie SQL operacja przemianowanie")
    print ("8. Rozłączenie z bazą danych")
    print ("0. Koniec")
    print (30*'-')

def clear():
    if name == 'nt':
        system('cls')
    else:
        system('clear')

def connect():
    server = '155.158.112.85,1433'
    database = 'bazaib'
    username = 'userib'
    password = 'userib123#'
    global connection
    global cursor
    connection = pyodbc.connect(
        'DRIVER={SQL Server}; SERVER='+
        server+';DATABASE='+database+';UID='+username+';PWD='+password)
    cursor = connection.cursor()
    cursor.execute("SELECT @@version;")
    row = cursor.fetchone()
    print(row[0])

def disconnect():
    cursor.close()
    connection.close()

def query_1():
    cursor.execute('SELECT tp.id as idPacjenta, tp.imie, tp.nazwisko, tw.id as idWizyty, tw.data_wizyty ' +
                   'FROM t_pacjent_autoid as tp, t_wizyta tw '+
                   'WHERE tp.id = tw.pacjent_id')
    for row in cursor:
        print(row)

def query_2():
    cursor.execute('SELECT tp.id as idPacjenta, tp.imie, tp.nazwisko, tw.id as idWizyty, tw.data_wizyty '+
                   'FROM t_pacjent_autoid as tp '+
                   'JOIN t_wizyta tw '+
                   'ON tp.id = tw.pacjent_id')
    for row in cursor:
        print(row)
        
def query_3():
    cursor.execute('SELECT tp.id as idPacjenta, tp.imie, tp.nazwisko, tw.id as idWizyty, tw.data_wizyty '+
                   'FROM t_pacjent_autoid as tp '+
                   'LEFT JOIN t_wizyta tw '+
                   'ON tp.id = tw.pacjent_id')
    for row in cursor:
        print(row)
        
def query_4():
    cursor.execute('SELECT tp.id as idPacjenta, tp.imie, tp.nazwisko, tw.id as idWizyty, tw.data_wizyty '+
                   'FROM t_pacjent_autoid as tp '+
                   'RIGHT JOIN t_wizyta tw '+
                   'ON tp.id = tw.pacjent_id')
    for row in cursor:
        print(row)
        
def query_5():
    cursor.execute('SELECT tp.id , tp.imie, tp.nazwisko, tp.data_urodzenia '+
                   'FROM t_pacjent_autoid as tp')
    print(str(cursor.description[0][0])+ ' ' + str(cursor.description[1][0])+' '+
          str(cursor.description[2][0])+ ' ' + str(cursor.description[3][0]))
    for row in cursor:
        print(row)
        
def query_6():
    cursor.execute('SELECT tp.id as Identyfikator, tp.imie as imie, tp.nazwisko as nazwisko, tp.data_urodzenia as "Data urodzenia"'+
                   'FROM t_pacjent_autoid as tp')
    print(str(cursor.description[0][0])+ ' ' + str(cursor.description[1][0])+' '+
          str(cursor.description[2][0])+ ' ' + str(cursor.description[3][0]))
    for row in cursor:
        print(row)
        
        
loop = True
clear()
print_menu()
while loop:
    choice = input('Wybór opcji [1-8] :')
    choice = int(choice)

    if choice == 1:
        clear()
        print_menu()
        connect()
        print ("Nawiązano połączenie...")
    elif choice == 2:
        clear()
        print_menu()
        print ("Zapytanie 1...")
        query_1();
    elif choice == 3:
        clear()
        print_menu()
        print ("Zapytanie 2...")
        query_2();
    elif choice == 4:
        clear()
        print_menu()
        print ("Zapytanie 3...")
        query_3();
    elif choice == 5:
        clear()
        print_menu()
        print ("Zapytanie 4...")
        query_4();
    elif choice == 6:
        clear()
        print_menu()
        print ("Zapytanie 5...")
        query_5();
    elif choice == 7:
        clear()
        print_menu()
        print ("Zapytanie 6...")
        query_6();
    elif choice == 8:
        clear()
        print_menu()
        disconnect()
        print ("Połączenie zakończone...")
    elif choice == 0:
        print ("Koniec...")
        loop = False
        clear()
    else:
        clear()
        print_menu()
        print("Niewłaściwa opcja menu...")
        
                   