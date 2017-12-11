#-*- coding: UTF-8 -*-

import pymysql
import random
import time

conn = pymysql.connect("localhost", "root", "1234", "off", use_unicode =1, charset = "utf8")
c = conn.cursor()

class Off(): 
    
    def __init__(self):
        print("Witaj miłośniku Off-a!")
        print("Poruszaj się po MENU wpisując odpowiednie znaki: \"(X)\" ")
        print("Dobrej zabawy!")
        time.sleep(1)
        print(" ")
        self.log0()
        #self.main_menu()
    def log0(self):
        
        print("(1)Mam już konto\n(2)Dodaj nowe konto")
        choice_log0 = input("-> ")
        if choice_log0 == "1":
            self.log1()
        elif choice_log0 == "2":
            self.log2()
        else:
            print("Nie dokonano poprawnego wyboru:(\nSpróbuj ponownie! za 1..2..")
            print(" ")
            time.sleep(2)
            self.log0()
            
    def log1(self):   
        existLog = input("Podaj login użytkownika: ")
        existPass = input("Podaj hasło użytkownika: ")
        if c.execute("select login from user where login = %s" ,existLog) and c.execute("select pass from user where pass = %s" ,existPass):
            print("\nWitaj ponownie {}\n".format(existLog))
            time.sleep(1)
            self.main_menu()
        else:
            print("Błędny login lub hasło!")
            self.log1()           
            
    def log2(self):   
        createLogin = input("Podaj login użytkownika: ") 
        if c.execute("select login from user where login = %s",createLogin):
            print("\nLogin zajęty!\nWymyśl coś innego")
            print(" ")
            time.sleep(1)
            self.log2()
        else:
            createPassw = input("Podaj hasło: ")
            c.execute("INSERT INTO user VALUES(null,%s,%s)", (createLogin, createPassw))
            conn.commit()
            print("\nUżytkownik utworzony\n")
            self.menu()
            
    def main_menu(self):
        print("Witaj!\nCo chcesz zrobić?")
        print("\n(1)Playlista\n(2)Tryb Info\n(Q)Wyjść - Do widzenia!")
        choice_main_menu = input("-> ")
        
        if choice_main_menu == "1":
            self.playlist()
         
        elif choice_main_menu == "2":
            self.info()
        elif choice_main_menu == "Q" or "q":
                cy =["Do zobaczenia!", "Cześć", "Elo 320"]
                print(random.choice(cy))
                exit()        
        else:
            print("\nNiepoprawny wybór\nSpróbuj ponownie")
            
   
    def playlist(self):
        print("Wybierz z listy ->")
        print("(1)Wybrana edycja Offa\n(2)Zespół podobny do ulubionego\n(3)Zespoły spod ulubionego gatunku\n(4)Rok założenia\n(5)Ilość słuchaczy\n(Q)Wyjście do MENU GŁÓWNEGO")
        choice1 = input("-> ")
        
        if choice1 == "1":
            self.p1()
                
        if choice1 == "2":
            self.p2()
            
        if choice1 == "3":
            self.p3()
                    
        if choice1 == "4":
            self.p4()
            
        if choice1 == "5":
            self.p5()
            
        if choice1 == "Q" or "q":
            time.sleep(1)
            self.main_menu()                                        
            
    def info(self):
        
        print("Witaj w trybie info! Kopalni wieidzy dla muzycznych geeków.")
        time.sleep(2)
        print("Wybierz z listy ->")
        print("(1)Pełne info o wybranych zespołach\n(2) Najwięcej/najmnniej z: tagu\n(3)Najwięcej/najmnniej z: kraju\n(4)Najwięcej/najmnniej z: miasta\n(Q)Wyjdź do głównego MENU")
        choice1 = input("-> ")        
       
         
            
    def p1(self):
        rok = str(input("Szukany rok?: "))
        ile = int(input("Ile zespołów na liście?: "))
        c.execute("select m.name_band, m.best_song, f.year listeners_kilo from music as m inner join lineup as l on m.id_music = l.id_band inner join festival as f on f.edition = l.id_off where f.year = %s;",rok)
        for i in c.fetchmany(ile):
            print(i)
            
    def p2(self):
        nazwa = str(input("Zespoły podobne do...?: "))
        ile = int(input("Ile zespołów na liście?: "))
        c.execute("select b.tag, b.name_band, m.name_album, m.best_song from band as b left join music as m on b.id_band = m.id_music where tag = (select tag from band where name_band like '%{}%');".format(nazwa))
        for i in c.fetchmany(ile):
            print(i)
            
        time.sleep(0.5)        
        print("Co chcesz teraz zrobić?")
        time.sleep(0.5)  
        print("(E)Eksport jako playlista .txt\n(P)Powrót do Menu Playlista")
        inp = input("dalej")
        if inp == "E":
            self.p1()
        else:
            self.playlist()
            
        
            
Off()  

