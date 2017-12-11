#-*- coding: UTF-8 -*-

import pymysql
import random
import time
from os import *
import io


conn = pymysql.connect("localhost", "root", "1234", "off", use_unicode =1, charset = "utf8")
c = conn.cursor()

class Off(): 
    def __init__(self):
        #print("Witaj w askOFF!")
        #time.sleep(0.5)
        #print("Poruszaj się po MENU wpisując odpowiednie znaki: \"(X)\"\nprzypisane pozycjom na liście.  ")
        #time.sleep(0.5)
        #print("\nDobrej zabawy!")
        #print(" ")
        time.sleep(1)
        #self.log0()
        #self.p1()
        self.main_menu()
        
    #def log0(self):
        
        #print("(1)Mam już konto\n(2)Dodaj nowe konto\n(Q)Wyjdź z programu")
        #choice_log0 = input("-> ")
        #if choice_log0 == "1":
            #self.log1()
        #elif choice_log0 == "2":
            #self.log2()
        #elif choice_log0 == "Q" or choice_log0 == "q":
            #exit()    
        #else:
            #print("Nie dokonano poprawnego wyboru:(\nSpróbuj ponownie! za 1..2..")
            #print(" ")
            #time.sleep(2)
            #self.log0()
            
    #def log1(self): #logowanie istniejącego uzytkownika
        #existLog = input("Podaj login użytkownika: ")
        #existPass = input("Podaj hasło użytkownika: ")
        #if c.execute("select login,pass from user where login = %s and pass = %s",(existLog,existPass)):
            #if existLog == "maciek":
                #print("Admin!")
            #print("\nWitaj ponownie {}\n".format(existLog))
            #time.sleep(1)
            #self.main_menu()
        #else:
            #self.wrong()           
            
    #def log2(self):   #nowy user
        #createLogin = input("Podaj login użytkownika: ") 
        #if c.execute("select login from user where login = %s",createLogin):
            #print("\nLogin zajęty!\nWymyśl coś innego.")
            #print(" ")
            #time.sleep(1)
            #self.log2()
        #else:
            #createPassw = input("Podaj hasło: ")
            #c.execute("INSERT INTO user VALUES(null,%s,%s)", (createLogin, createPassw))
            ## c.execute("Dodaję użytkownika bazy z uprawnieniami enter enter")
            ##c.execute("CREATE TABLE {} (id int primary key auto_increment, name_band varchar (45), name_album varchar (45), best_song varchar (45), ocena varchar(1));".format(createLogin))
            
            #conn.commit()
            #print("\nUżytkownik utworzony\n")
            #conn.close()
            #self.main_menu()
            
            
    #def wrong(self):
        #print("Błędny login lub hasło! ")
        #print("(1)Ponowne logowanie\n(Q)Wyjdź")
        #ifWrongchoice = input("-> ")
        #if ifWrongchoice == "1":
            #self.log1()
        #elif ifWrongchoice == "Q" or ifWrongchoice == "q":
            #self.log0()
        
            
    def main_menu(self):
    
        print("Witaj!\nCo chcesz zrobić?")
        print("\n(1)Playlista\n(2)Tryb Info\n(Q)Wyjść z progamu!")
        choice_main_menu = input("-> ")
        
        if choice_main_menu == "1":
            self.playlist()
         
        elif choice_main_menu == "2":
            self.info()
        elif choice_main_menu == "Q" or choice_main_menu == "q":
                cy =["Do zobaczenia!", "Cześć", "Elo 320", "Kolejne śmieszne pożegnanie", "Jeszcze inne!"]
                print(random.choice(cy))
                exit()        
        else:
            print("\nNiepoprawny wybór\nSpróbuj ponownie! za 1..2..")
            time.sleep(1)
            self.main_menu()
    
            
   
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
        if choice1 == "Q" or choice1 == "q":
            self.main_menu()
        else:
            print("\nNiepoprawny wybór\nSpróbuj ponownie! za 1..2..")
            time.sleep(1)
            self.playlist()
         
                       
    def info(self):
        
        print("Witaj w trybie info! Kopalni wiedzy dla offowych geeków.")
        time.sleep(2)
        print("Wybierz z listy ->")
        print("(1)Pełne info o wybranych zespołach\n(2) Najwięcej/najmnniej z: gatunku\n(3)Najwięcej/najmnniej z: kraju\n(4)Najwięcej/najmnniej z: miasta\n(Q)Wyjście do MENU GŁÓWNEGO")
        choice1 = input("-> ")        
       
     
    def outro(self,results):
        time.sleep(0.5)        
        print("Co chcesz teraz zrobić?\n")
        time.sleep(0.5)  
        print("(E)Eksport jako playlista.txt\n(Q)Powrót do Menu Playlista")
        outro_choice = input("-> ")
        if outro_choice == "E" or outro_choice == "e":
            self.export(results)
        elif outro_choice == "Q" or outro_choice == "q":
            self.playlist()
        else:
            print("\nNiepoprawny wybór\nSpróbuj ponownie! za 1..2..")
            time.sleep(1)
            self.outro(results)
                   
    def export(self,results):
        plName = str(input("Jak chcesz nazwać playlistę?\n-> "))
        
        if ("{}.txt".format(plName)) in listdir('.'):
            print("Nazwa zajęta. Podaj inną nazwę.")
            self.export(results)
        else:    
            io.open("{}.txt".format(plName),"a").write('\n'.join('%s %s' % x for x in results))
            print("Zapisano!")
            time.sleep(2)
            self.playlist()
           
        
    def p1(self):
        
        rok = str(input("Szukany rok?: "))
        if c.execute("select year from festival where year = {};".format(rok)):
            pass
        else:
            c.execute("select year from festival group by year asc limit 1;")
            granica1 = ("".join('%s' % x for x in c.fetchall()))
            c.execute("select year from festival group by year desc limit 1;")
            granica2 = ("".join('%s' % x for x in c.fetchall()))            
            print("OffFestival odbywa się od {} r. Ostatnia edycja odbyła się w {} r.".format(granica1, granica2))
            self.p1()
            
        ile = int(input("Ile zespołów na liście?: "))
        c.execute("select m.name_band, m.best_song from music as m inner join lineup as l on m.id_music = l.id_band inner join festival as f on f.edition = l.id_off where f.year = %s;",rok)
        results = c.fetchmany(ile)
        print('\n'.join('%s %s' % x for x in results))
        self.outro(results)        
            
    def p2(self):
        nazwa = str(input("Zespoły podobne do...?: "))
        if c.execute("select name_band from band where name_band like'%{}%';".format(nazwa)):
            pass
        else:
            print("Przykro mi {} nie występował jeszcze na OFFie.\nWybierz jednego z artystów OFFa".format(nazwa.upper()))
            self.p2()
        ile = int(input("Ile zespołów na liście?: "))
        c.execute("select b.tag, b.name_band from band as b left join music as m on b.id_band = m.id_music where tag = (select tag from band where name_band like '%{}%');".format(nazwa))
        results = c.fetchmany(ile)
        print('\n'.join('%s %s' % x for x in results))
        self.outro(results)  
            
    def p3(self): #spod ulubionego tagu
        tag = str(input("Podaj gatunek\n-> "))
        if c.execute("select tag from band where tag = '{}';".format(tag)):
            pass
        else:
            print("Przykro mi, jeszcze żaden artysta z gatunku {} nie wystąpił na OffFestivalu.\nKoniecznie poinformuj o tym dyrektora Rojka!".format(tag.upper()))
            self.p3()
        ile = int(input("Ile zespołów na liście?: "))
        c.execute("SELECT b.tag, b.name_band, m.best_song FROM band AS b LEFT JOIN music AS m ON b.name_band = m.name_band WHERE b.tag LIKE '%{}%';".format(tag))
        results = c.fetchmany(ile)
        print('\n'.join('%s %s %s' % x for x in results))
        self.outro(results)  
        
    def p4(self): 
        
        c.execute("select since from band group by since asc limit 1;")
        granica1 = ("".join('%s' % x for x in c.fetchall()))
    
        c.execute("select since from band group by since desc limit 1;")
        granica2 = ("".join('%s' % x for x in c.fetchall()))        
        
        print("Jaki przedział lat cię interesuje?")
        rok1 = input("Podaj 1 rok -> ")
        if c.execute("select since from band where since = '{}';".format(rok1)):
            pass
        else:
            print("Rok spoza zakresu!\nNa OffFestivalu występowały zespoły zakładane od {} do {} roku".format(granica1,granica2))
            self.p4()
            
        rok2 = input("Podaj 2 rok -> ")
        
        if c.execute("select since from band where since = '{}';".format(rok2)):
            pass
        else:  
            print("Rok spoza zakresu!\nNa OffFestivalu występowały zespoły zakładane od {} do {} roku".format(granica1,granica2))
            self.p4()
        
        ile = int(input("Ile zespołów na liście?: "))     # czesty blad : builtins.ValueError: invalid literal for int() with base 10: '<'   
        self.sort(rok1,rok2,ile)
        
    def sort(self,rok1,rok2, ile):    
        print("(>)Rosnąco\n(<)Malejąco")
        sort = str(input("-> "))
        if sort == ">":
            sort = "asc"
        elif sort =="<":
            sort = "desc"
        else:
            print("Źle wybrany symbol sortowania!")
            self.sort(rok1,rok2, ile)
            
        c.execute("select b.name_band, m.best_song, b.since from band as b left join music as m on b.id_band = m.id_music where b.since between {} and {} order by b.since {};".format(rok1,rok2,sort))
        disp = c.fetchmany(ile)
        c.execute("select b.name_band, m.best_song from band as b left join music as m on b.id_band = m.id_music where b.since between {} and {} order by b.since {};".format(rok1,rok2,sort))
        results = c.fetchmany(ile)        
        print('\n'.join('%s %s %s' % x for x in disp))
        self.outro(results)            

    def p5(self): #czy tu jakiś input - TAK jak z since. Zespół o najmniejszej liczbie sluchaczy ma: , a najbardziej pop. ma {} + sort
        nazwa = str(input("Zespoły podobne do...?: "))
        ile = int(input("Ile zespołów na liście?: "))
        c.execute("select b.name_band, m.name_album, m.best_song, listeners_kilo as sluchacze from band as b left join music as m on b.id_band = m.id_music order by sluchacze desc;")
        for i in c.fetchmany(ile):
            print(i)             
        self.outro()     
            
               
Off()  