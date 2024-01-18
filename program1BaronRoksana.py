print('Aplikacje bazodanowe')

import sys
from os import system, name
import logging
from datetime import datetime
import pyodbc

authorName = 'Baron Roksana'

def print_menu():
    print (30*'-')
    print(" MENU GŁÓWNE - SYSTEM: " + name + 'Autor:' + authorName)
    print (30*'-')
    print ("1. Połączenie z bazą danych")
    print ("2. Zapytanie 1: select id,nazwisko,imie from t_pacjent_autoid")
    print ("3. Zapytanie 2: select id,nazwisko,data,opis from t_pacjent_autoid")
    print ("4. Rozłączenie z bazą danych")
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
    cursor.execute('SELECT id, nazwisko, imie, badanie FROM bazaib.dbo.t_pacjent_autoid')
    for row in cursor:
        print(row)

def query_2():
    cursor.execute('SELECT id, nazwisko, imie, badanie, opis, data, data_mod FROM bazaib.dbo.t_pacjent_autoid')
    for row in cursor:
        print(row)
        
loop = True
clear()
print_menu()
while loop:
    choice = input('Wybór opcji [1-0] :')
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
        
                   
