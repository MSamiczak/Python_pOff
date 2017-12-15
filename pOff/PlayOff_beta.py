#-*- coding: UTF-8 -*-

import pymysql
import random
import time
import datetime
from os import *
import io
import daneDoLogowania

conn = pymysql.connect(daneDoLogowania.daneDoLog["host"], daneDoLogowania.daneDoLog["user"], daneDoLogowania.daneDoLog["pass"], daneDoLogowania.daneDoLog["db"], use_unicode = 1, charset ="utf8")

c = conn.cursor()

class Off(): 
    def __init__(self):
        time.sleep(1)
        play = ("      @@               "," @@@  @@    @@@  @@  @@","@@ @@ @@   @@ @@ @@  @@","@@ @@ @@   @@ @@ @@  @@","@@@@@ @@@@ @@@@@@ @@@@ ","@@@@   @@@  @@@@@  @@  ","@@                 @@  ","@@                 @@  " )
        off=("        @@@  @@@ "," @@@   @@   @@   ","@@@@@ @@@@ @@@@  ","@@ @@  @@   @@   ","@@@@@  @@   @@   "," @@@   @@   @@   ")
        print(('\n'.join('%s' % x for x in play)))
        time.sleep(1)
        print('\n'.join(('%s'.center(30," ")) % x for x in off))
        time.sleep(0.5)
        print("\n\n")
        print("Witaj w PLayOff!")
        print(" ")
        time.sleep(0.5)
        print("Poruszaj się po MENU wpisując odpowiednie znaki: \"(X)\" przypisane pozycjom na liście.")
        time.sleep(0.5)
        print("-".center(100,"-"))
        print("\nDobrej zabawy!")
        print(" ")
        time.sleep(1)
        self.log0()
        #self.menu()


    def log0(self):
        print("(1)Mam już konto\n(2)Dodaj nowe konto\n(q)Wyjdź z programu")
        choice_log0 = input("-> ")
        if choice_log0 == "1":
            self.log1()
        elif choice_log0 == "2":
            self.log2()
        elif choice_log0 == "Q" or choice_log0 == "q":
            cu =["Do zobaczenia!", "Cześć!", "Elo 320!", "Tschus!", "Bye!", "Buenos Aires!", "CU!", "Dzb"]
            print(random.choice(cu))
            exit()   

        else:
            print("\nNiepoprawny wybór\nSpróbuj ponownie! za 1..2..")
            time.sleep(1)
            self.log0()            


    def log1(self): #logowanie istniejącego uzytkownika
        existLog = input("Podaj login: ")
        existPass = input("Podaj hasło: ")
        if c.execute("select login,pass from user where login = %s and pass = %s and user_group = 1",(existLog,existPass)):
            print("\nWitaj Lordzie Administratorze!\n")
            time.sleep(1)
            self.menuADMIN(existLog)
        if c.execute("select login,pass from user where login = %s and pass = %s and user_group = 2",(existLog,existPass)):     
            print("\nWitaj ponownie ***{}***\n".format(existLog))
            time.sleep(1)
            self.menu(existLog)
        else:
            self.wrong(existLog)           

    def log2(self):   #nowy user
        createLog = input("Podaj login: ") 
        if c.execute("select login from user where login = %s", createLog):
            print("\nLogin zajęty!\nWymyśl coś innego.")
            print(" ")
            time.sleep(1)
            self.log2()
        else:
            createPassw = input("Podaj hasło: ")
            c.execute("INSERT INTO user VALUES(null,%s,%s,2)", (createLog, createPassw))
            #c.execute("CREATE TABLE {} (id int primary key auto_increment, name_band varchar (45), name_album varchar (45), best_song varchar (45), ocena varchar(1));".format(createLogin))
            
            conn.commit()
            print("Użytkownik utworzony\n")
            print("\nWitaj w PlayOff ***{}***\n".format(createLog))
            time.sleep(1)
            conn.close()
            conn.ping()
            existLog =  createLog
            self.menu(existLog)


    def wrong(self,existLog):
        print("Błędny login lub hasło! ")
        print("(1)Ponowne logowanie\n(q)Cofnij")
        ifWrongchoice = input("-> ")
        if ifWrongchoice == "1":
            self.log1()
        elif ifWrongchoice == "Q" or ifWrongchoice == "q":
            self.log0()
        else:
            print("\nNiepoprawny wybór\nSpróbuj ponownie! za 1..2..")
            time.sleep(1)
            self.wrong()


    def menu(self,existLog):
        print("Dokonaj wyboru z listy MENU")
        print("\n(1)Wybrana edycja Offa\n(2)Podobne do ulubionego\n(3)Wybierz zakres\n(4)Popularne/unikalne\n(q)Wyjście z programu")
        choice_menu = input("-> ")

        if choice_menu == "1":
            self.m1(existLog)
        if choice_menu == "2":
            self.m2(existLog)         
        if choice_menu == "3":
            self.m3(existLog)       
        if choice_menu == "4":
            self.m4(existLog)

        elif choice_menu == "Q" or choice_menu == "q":
            cu =["Do zobaczenia!", "Cześć!", "Elo 320!", "Tschus!", "Bye!", "Buenos Aires!", "CU!", "Dzb"]
            print(random.choice(cu))
            exit()   

        else:
            print("\nNiepoprawny wybór\nSpróbuj ponownie! za 1..2..")
            time.sleep(1)
            self.menu(existLog)   

    def menuADMIN(self,existLog):
        print("Dokonaj wyboru z listy MENU")
        print("\n(1)Wybrana edycja Offa\n(2)Podobne do ulubionego\n(3)Wybierz zakres\n(4)Popularne/unikalne\n($)Narzędzia administracyjne\n(q)Wyjście z programu")
        choice_menu = input("-> ")

        if choice_menu == "1":
            self.m1(existLog)
        if choice_menu == "2":
            self.m2(existLog)         
        if choice_menu == "3":
            self.m3(existLog)       
        if choice_menu == "4":
            self.m4(existLog)
        if choice_menu == "$":
            self.mA(existLog)            


        elif choice_menu == "Q" or choice_menu == "q":
            cu =["Do zobaczenia!", "Cześć!", "Elo 320!", "Tschus!", "Bye!", "Buenos Aires!", "CU!", "Dzb"]
            print(random.choice(cu))
            exit()   

        else:
            print("\nNiepoprawny wybór\nSpróbuj ponownie! za 1..2..")
            time.sleep(1)
            self.menuADMIN(existLog)

    # Wybrana edycja Offa      

    def m1(self,existLog):  
        print("\n*** Wybrana edycja Offa ***")
        print("\n(A)Rok Festiwalu\n(B)Która edycja Festiwalu\n(q)Cofnij")
        choice_m = input("-> ")

        if choice_m == "A" or choice_m == "a":
            self.m1A(existLog)

        if choice_m == "B" or choice_m == "b":
            self.m1B(existLog)   

        if choice_m == "Q" or choice_m == "q":
            if c.execute("select login,pass from user where login = %s and user_group = 1",(existLog)):
                self.menuADMIN(existLog)
            else:
                self.menu(existLog)

        else:
            print("\nNiepoprawny wybór\nSpróbuj ponownie! za 1..2..")
            time.sleep(1)
            self.m1(existLog)

    #Podobne do ulubionego       


    def m2(self,existLog):
        print("\n*** Podobne do ulubionego ***")
        print("\n(A)Zespołu\n(B)Gatunku muzyki\n(q)Cofnij")
        choice_m = input("-> ")

        if choice_m == "A" or choice_m == "a" or choice_m == "1":
            self.m2A(existLog)

        if choice_m == "B" or choice_m == "b":
            self.m2B(existLog)   

        if choice_m == "Q" or choice_m == "q":
            if c.execute("select login,pass from user where login = %s and user_group = 1",(existLog)):
                self.menuADMIN(existLog)
            else:
                self.menu(existLog)

        else:
            print("\nNiepoprawny wybór\nSpróbuj ponownie! za 1..2..")
            time.sleep(1)
            self.m2(existLog)

    #Wybierz zakres

    def m3(self,existLog):
        print("\n*** Wybierz zakres ***")
        print("\n(A)Rok założenia\n(B)Ilość słuchaczy\n(q)Cofnij")
        choice_m = input("-> ")

        if choice_m == "A" or choice_m == "a":
            self.m3A(existLog)

        if choice_m == "B" or choice_m == "b":
            self.m3B(existLog)   

        if choice_m == "Q" or choice_m == "q":
            if c.execute("select login,pass from user where login = %s and user_group = 1",(existLog)):
                self.menuADMIN(existLog)
            else:
                self.menu(existLog)

        else:
            print("\nNiepoprawny wybór\nSpróbuj ponownie! za 1..2..")
            time.sleep(1)
            self.m3(existLog)

# Popularne/unikalne

    def m4(self,existLog):
        print("\n*** Popularne/Unikalne ***")
        print("\n(A)Gatunki muzyczne\n(B)Kraj zespołu\n(q)Cofnij")
        choice_m = input("-> ")

        if choice_m == "A" or choice_m == "a":
            self.m4A(existLog)

        if choice_m == "B" or choice_m == "b":
            self.m4B(existLog)   

        if choice_m == "Q" or choice_m == "q":
            if c.execute("select login,pass from user where login = %s and user_group = 1",(existLog)):
                self.menuADMIN(existLog)
            else:
                self.menu(existLog)
        else:
            print("\nNiepoprawny wybór\nSpróbuj ponownie! za 1..2..")
            time.sleep(1)
            self.m4(existLog)  


    def mA(self,existLog):
        
        conn.ping()

        print("\n*** Narzędzia administracyjne ***")
        print("\n(1)Dodaj rekord\n(2)Usuń rekord\n(q)Cofnij")
        choice_mA = input("-> ")       

        if choice_mA == "1":
            self.mAdmin_1(existLog)
    
        if choice_mA == "2":
            self.mAdmin_s(existLog)   
    
        if choice_mA == "Q" or choice_mA == "q":
            self.menuADMIN(existLog)

        else:
            print("\nNiepoprawny wybór\nSpróbuj ponownie! za 1..2..")
            time.sleep(1)
            self.mA(existLog)              
        
    def mAdmin_s(self,existLog):
        
        print("Funkcjonalność w budowie!\nTe i inne powalające funkcjonalności juz wkrótce!")
        self.mA(existLog)
        time.sleep(1)

    def mAdmin_1(self,existLog):
        print("\n*** Dodawanie Wykonawcy ***")
        print("Postępuj zgodnie z instrukcjami")
        print("Jeśli w trakcie uzupełniania arkusza zdecydujesz się wyjść wpisz: $$exit")
        self.name_band(existLog)

    def name_band(self,existLog):    
        name_band = input("Nazwa Wykonawcy: ")
        if c.execute("select name_band from band where name_band = %s",name_band):
            print("\nWykonawca o podanej nazwie znajduje się już w bazie Offa.")
            self.name_band(existLog)
        if len(name_band) == 0:
            print("Pole nie może pozostać puste.")
            self.name_band(existLog)
        if name_band == "$$exit":
            self.mA(existLog)
        self.country(existLog, name_band)    
    def country(self,existLog,name_band):       
        country = input("Kraj: ")
        if len(country) == 0:
            print("Pole nie może pozostać puste.")
            self.country(existLog,name_band)
        if len(country) >3:
            print("Podaj informację o kraju w formie skrótu (np. PL, GER).")
            self.country(existLog,name_band)            
        if country == "$$exit":
            self.mAdmin_1(existLog)
        self.city(existLog,name_band,country)
    def city(self,existLog,name_band,country):  
        city = input("Miasto: ")
        if city == "$$exit":
            self.mAdmin_1(existLog)
        self.tag(existLog,name_band,country,city)    
    def tag(self,existLog,name_band,country,city):        
        tag = input("Wykonywany gatunek: ")
        if len(tag) == 0:
            print("Pole nie może pozostać puste.")
            self.tag(existLog,name_band,country,city)
        if tag == "$$exit":
            self.mAdmin_1(existLog)
        self.since(existLog,name_band,country,city,tag)    
    def since(self,existLog,name_band,country,city,tag):
        now = datetime.datetime.now()
        since = input("Na scenie od roku: ")
        if len(since) == 0:
            print("Pole nie może pozostać puste.")
            self.since(name_band,country,city,tag)
        if not since.isdigit():
            print("Wprowadź liczbę.")
            self.since(existLog,name_band,country,city,tag)
        if len(since) < 4:
            print("Podaj rok założenia w postaci 4-cyfrowej")
            self.since(existLog,name_band,country,city,tag)
        if since > str(now.year):
            print("Mamy {} rok. Podaj odpowiednią datę.".format(now.year))
            self.since(existLog,name_band,country,city,tag)      
        if since == "$$exit":
            self.mAdmin_1(existLog) 
        self.listeners_kilo(existLog,name_band,country,city,tag,since)    
    def listeners_kilo(self,existLog,name_band,country,city,tag,since):
        try:
            listeners_kilo = float(input("Ilość słuchaczy podana w tys.: "))
        except ValueError:
            print("Podaj liczbę. Używaj separatora '.'")
            self.listeners_kilo(existLog,name_band,country,city,tag,since)
        if listeners_kilo == "$$exit":
            self.mAdmin_1(existLog)
        #if not listeners_kilo.isdigit():
            #print("Wprowadź liczbę.")    
            self.listeners_kilo(existLog,name_band,country,city,tag,since)
        self.name_album(existLog,name_band,country,city,tag,since,listeners_kilo)    
    def name_album(self,existLog,name_band,country,city,tag,since,listeners_kilo):        
        name_album = ("Najlepszy album: ")
        if len(name_album) == 0:
            print("Pole nie może pozostać puste.")
            self.name_album(existLog,name_band,country,city,tag,since,listeners_kilo)
        if name_album == "$$exit":
            self.mAdmin_1(existLog)
        self.best_song(existLog,name_band,country,city,tag,since,listeners_kilo,name_album)    
    def best_song(self,existLog,name_band,country,city,tag,since,listeners_kilo,name_album):        
        best_song = ("Najbardziej popularny utwór: ")
        if len(best_song) == 0:
            print("Pole nie może pozostać puste.")
            self.best_song(existLog,name_band,country,city,tag,since,listeners_kilo,name_album)
        if best_song == "$$exit":
            self.mAdmin_1(existLog) 
            
        c.execute("INSERT INTO band VALUES(null,%s,%s,%s,%s,%s,%s)",(name_band, city, country, tag, since, listeners_kilo))
        c.execute("INSERT INTO music VALUES(null,%s,%s,%s)",(name_band, name_album, best_song))
        conn.commit()
        print("Dodano wykonawcę!\n")
        conn.close()

        print("Podaj, na której edycji festiwalu wystąpił.")
        id_off = input("-> ")
        if id_off.isdigit():
            pass
        if len(id_off) in range(1,3):
            pass
        else:
            print("Źle wprowadzony numer edycji")
        conn.ping()    
        conn.commit()
        c.execute("select id_band from band where name_band = %s ;",name_band)
        id_band = c.fetchall()
        c.execute("INSERT INTO lineup VALUES(null,%s,%s,%s)",(id_band, name_band, id_off))
        print("Poprawnie zakończyłeś dodawanie rekordu!")
        conn.close() 

        self.mA(existLog)


    # Rok edycji Offa           
    def m1A(self,existLog):
        try:
            rok = int(input("Szukany rok?: "))
            #if not rok.isdigit():
                
        except ValueError: 
            print("Podaj rok. W zapisie 4-cyfrowym.")
            self.m1A(existLog)

        if c.execute("select year from festival where year = {};".format(rok)):
            self.sort_m1A(existLog,rok)

        else:
            c.execute("select year from festival group by year asc limit 1;")
            granica1 = ("".join('%s' % x for x in c.fetchall()))
            c.execute("select year from festival group by year desc limit 1;")
            granica2 = ("".join('%s' % x for x in c.fetchall()))            
            print("OffFestival odbywa się od {} r. Ostatnia edycja odbyła się w {} r.".format(granica1, granica2))
            self.m1A(existLog)
    #sortowanie początek

    def sort_m1A(self,existLog,rok):    
        try:
            ile = int(input("* Ilość wyników? -> "))
        except ValueError:
            print("Podaj liczbę")
            self.sort_m1A(existLog,rok)
        sort0 = input("\n*** Wyświetlanie wyników ***\n(A)Alfabtycznie\t(B)Wg Popularności\n-> ")
        if sort0 == "A" or sort0 =="a":
            self.m1A_Alfa(existLog,rok,ile)
        elif sort0 == "B" or sort0 == "b":
            self.m1A_Pop(existLog,rok,ile)
        else:
            print("Zły wybór. Spróbuj ponownie")
            self.sort_m1A(existLog,rok)

    #def sortA(self,existLog,rok):

        #sortA = input("* Alfabetycznie rosnąco/malejąco (a/z) -> ")

        #if sortA =="A" or sortA =="a":
            #alf = "asc"

        #elif sortA =="Z" or sortA =="z":
            #alf = "desc"
        #else:
            #print("Zły wybór. Spróbuj ponownie")
            #self.sortA(existLog,rok)
        #ile = int(input("* Ilość wyników? -> "))
        #self.m1A_Alfa(existLog,rok,ile)

    #def sortB(self,rok):

        #sortB = input("* Popularność rosnąco/malejąco (a/z) -> ")

        #if sortB =="A" or sortB =="a":
            #alf = "asc"

        #elif sortB =="Z" or sortB =="z":
            #alf = "desc"
        #else:
            #print("Zły wybór. Spróbuj ponownie")
            #self.sortA(rok)
        #ile = int(input("* Ilość wyników? -> "))
        #self.m1A_Pop(alf,rok,ile)        


    ## sortowanie koniec                  

    def m1A_Alfa(self,existLog,rok,ile):

        c.execute("select b.name_band, b.country, b.city,b.since, b.listeners_kilo, b.tag, m.name_album, m.best_song from music as m inner join lineup as l on m.id_music = l.id_band inner join festival as f on f.edition = l.id_off join band as b on b.id_band=m.id_music where f.year = {} order by name_band {};".format(rok, "asc"))
        disp = c.fetchmany(ile)
        c.execute("select m.name_band, m.best_song from music as m inner join lineup as l on m.id_music = l.id_band inner join festival as f on f.edition = l.id_off join band as b on b.id_band=m.id_music where f.year = {} order by name_band {};".format(rok, "asc"))
        results = c.fetchmany(ile)
        resCount = c.rowcount
        print('\n\n'.join('#Wykonawca: %s | #Kraj: %s | #Miasto: %s | #Założony: %s | #Ilość fanów: %s tys \n#Gatunek: %s | #Album: %s | #Utwór: %s' % x for x in disp))     
        time.sleep(1)
        print("\n-----Wyświetlono {} wyników. Dla podanego zapytania istnieje {} wyników-----\n".format(len(disp),resCount))
        self.outro(existLog, results)

    def m1A_Pop(self,existLog,rok,ile):   
        c.execute(" select b.name_band, b.country, b.city,b.since, b.listeners_kilo, b.tag, m.name_album, m.best_song from music as m inner join lineup as l on m.id_music = l.id_band inner join festival as f on f.edition = l.id_off join band as b on b.id_band=m.id_music where f.year = {} order by listeners_kilo {};".format(rok,"asc"))
        disp = c.fetchmany(ile)
        c.execute("select m.name_band, m.best_song from music as m inner join lineup as l on m.id_music = l.id_band inner join festival as f on f.edition = l.id_off join band as b on b.id_band=m.id_music where f.year = {} order by listeners_kilo {};".format(rok,"asc"))
        results = c.fetchmany(ile)
        resCount = c.rowcount
        print('\n\n'.join('#Wykonawca: %s | #Kraj: %s | #Miasto: %s | #Założony: %s | #Ilość fanów: %s tys \n#Gatunek: %s | #Album: %s | #Utwór: %s' % x for x in disp))     
        time.sleep(1)
        print("\n------Wyświetlono {} wyników. Dla podanego zapytania istnieje {} wyników-----\n".format(len(disp),resCount))
        self.outro(existLog, results)


# Numer edycji Offa

    def m1B(self,existLog):
        try:
            edi = int(input("Szukana edycja festiwalu?: "))
        except ValueError:
            print("Podaj nr edycji")
            self.m1B(existLog)
        if c.execute("select edition from festival where edition = {};".format(edi)):
            self.sort_m1B(existLog, edi)
        else:
            c.execute("select edition from festival group by edition desc limit 1;")
            granica2 = ("".join('%s' % x for x in c.fetchall()))            
            print("Do tej pory odbyło się {} edycji festiwalu.".format(granica2))
            self.m1B(existLog)       

    #sortowanie początek

    def sort_m1B(self,existLog,edi): 
        try:
            ile = int(input("* Ilość wyników? -> "))
        except ValueError:
            print("Podaj liczbę")
            self.sort_m1B(existLog,edi)
        sort0 = input("\n*** Wyświetlanie wyników ***\n(A)Alfabtycznie\t(B)Wg Popularności\n-> ")

        if sort0 == "A" or sort0 =="a":
            self.m1B_Alfa(existLog, edi,ile)
        elif sort0 == "B" or sort0 == "b":
            self.m1B_Pop(existLog, edi,ile)
        else:
            print("Zły wybór. Spróbuj ponownie")
            self.sort_m1B(existLog)

    def m1B_Alfa(self,existLog,edi,ile):    
        c.execute("select b.name_band, b.country, b.city,b.since, b.listeners_kilo, b.tag, m.name_album, m.best_song from music as m inner join lineup as l on m.id_music = l.id_band inner join festival as f on f.edition = l.id_off join band as b on b.id_band = m.id_music where f.edition = {} order by name_band {};".format(edi,"asc"))
        disp = c.fetchmany(ile)
        c.execute("select m.name_band, m.best_song from music as m inner join lineup as l on m.id_music = l.id_band inner join festival as f on f.edition = l.id_off where f.edition = {} order by name_band {};".format(edi,"asc"))
        results = c.fetchmany(ile)
        resCount = c.rowcount
        print('\n\n'.join('#Wykonawca: %s | #Kraj: %s | #Miasto: %s | #Założony: %s | #Ilość fanów: %s tys \n#Gatunek: %s | #Album: %s | #Utwór: %s' % x for x in disp))     
        time.sleep(1)
        print("\n------Wyświetlono {} wyników. Dla podanego zapytania istnieje {} wyników-----\n".format(len(disp),resCount))
        self.outro(existLog, results)

    def m1B_Pop(self,existLog,edi,ile):    
        c.execute("select b.name_band, b.country, b.city,b.since, b.listeners_kilo, b.tag, m.name_album, m.best_song from music as m inner join lineup as l on m.id_music = l.id_band inner join festival as f on f.edition = l.id_off join band as b on b.id_band = m.id_music where f.edition = {} order by listeners_kilo {};".format(edi,"asc"))
        disp = c.fetchmany(ile)
        c.execute("select b.name_band, m.best_song from music as m inner join lineup as l on m.id_music = l.id_band inner join festival as f on f.edition = l.id_off join band as b on b.id_band = m.id_music where f.edition = {} order by listeners_kilo {};".format(edi,"asc"))
        results = c.fetchmany(ile)
        resCount = c.rowcount
        print('\n\n'.join('#Wykonawca: %s | #Kraj: %s | #Miasto: %s | #Założony: %s | #Ilość fanów: %s tys \n#Gatunek: %s | #Album: %s | #Utwór: %s' % x for x in disp))     
        time.sleep(1)
        print("\n------Wyświetlono {} wyników. Dla podanego zapytania istnieje {} wyników-----\n".format(len(disp),resCount))
        self.outro(existLog, results)


#Podobne do ulubionego zespołu
    def m2A(self, existLog):
        nazwa = str(input("Zespoły podobne do...?: "))
        if c.execute("select name_band from band where name_band like'%{}%';".format(nazwa)):
            self.sort_m2A(existLog, nazwa)

        else:
            print("Przykro mi, wykonawca podobny do {} nie występował jeszcze na OFFie.\nSpróbuj ponownie.".format(nazwa.upper()))
            self.m2A(existLog)

    #sorotwanie początek

    def sort_m2A(self,existLog,nazwa):   
        try:
            ile = int(input("* Ilość wyników? -> "))
        except ValueError:
            print("Podaj liczbę")
            self.sort_m2A(existLog,nazwa)
        sort0 = input("\n*** Wyświetlanie wyników ***\n(A)Alfabtycznie\t(B)Wg Popularności\n-> ")
        try:
            if sort0 == "A" or sort0 =="a":
                self.m2A_Alfa(existLog,nazwa,ile)
            elif sort0 == "B" or sort0 == "b":
                self.m2A_Pop(existLog,nazwa,ile)
            else:
                print("Zły wybór. Spróbuj ponownie")
                self.sort_m2A(existLog,nazwa)
        except pymysql.err.InternalError:
            print("Zbyt wiele wyników! Podaj przynajmniej 3 litery z nazwy.")
            self.m2A(existLog)
            
    # sortowanie koniec              

    def m2A_Alfa(self,existLog,nazwa,ile):             

        c.execute("select b.name_band, b.country, b.city,b.since, b.listeners_kilo, b.tag, m.name_album, m.best_song from band as b left join music as m on b.id_band = m.id_music where tag = (select tag from band where name_band like '%{}%' order by name_band {});".format(nazwa,"asc"))
        disp = c.fetchmany(ile)
        c.execute("select b.name_band, m.best_song from band as b left join music as m on b.id_band = m.id_music where tag = (select tag from band where name_band like '%{}%' order by name_band {});".format(nazwa,"asc"))
        results = c.fetchmany(ile)        
        resCount = c.rowcount
        print('\n\n'.join('#Wykonawca: %s | #Kraj: %s | #Miasto: %s | #Założony: %s | #Ilość fanów: %s tys \n#Gatunek: %s | #Album: %s | #Utwór: %s' % x for x in disp))     
        time.sleep(1)
        print("\n------Wyświetlono {} wyników. Dla podanego zapytania istnieje {} wyników-----\n".format(len(disp),resCount))
        self.outro(existLog,results) 


    def m2A_Pop(self,existLog,nazwa,ile):             

        c.execute("select b.name_band, b.country, b.city,b.since, b.listeners_kilo, b.tag, m.name_album, m.best_song from band as b left join music as m on b.id_band = m.id_music where tag = (select tag from band where name_band like '%{}%' order by listeners_kilo {});".format(nazwa,"asc"))
        disp = c.fetchmany(ile)
        c.execute("select b.name_band, m.best_song from band as b left join music as m on b.id_band = m.id_music where tag = (select tag from band where name_band like '%{}%'order by listeners_kilo {});".format(nazwa,"asc"))
        results = c.fetchmany(ile)        
        resCount = c.rowcount
        print('\n\n'.join('#Wykonawca: %s | #Kraj: %s | #Miasto: %s | #Założony: %s | #Ilość fanów: %s tys \n#Gatunek: %s | #Album: %s | #Utwór: %s' % x for x in disp))     
        time.sleep(1)
        print("\n------Wyświetlono {} wyników. Dla podanego zapytania istnieje {} wyników-----\n".format(len(disp),resCount))
        self.outro(existLog, results)


#Podobne do ulubionego gatunku

    def m2B(self,existLog):
        tag = str(input("Podaj gatunek...? "))
        if c.execute("select tag from band where tag = '{}';".format(tag)):
            self.sort_m2B(existLog,tag)
        else:
            print("Przykro mi, jeszcze żaden artysta z gatunku {} nie wystąpił na OffFestivalu.\nKoniecznie poinformuj o tym dyrektora Rojka!".format(tag.upper()))
            self.m2B(existLog)

    #sorotwanie początek

    def sort_m2B(self,existLog,tag): 
        try:
            ile = int(input("* Ilość wyników? -> "))
        except ValueError:
            print("Podaj liczbę")
            self.sort_m2B(existLog,tag)
        sort0 = input("\n*** Wyświetlanie wyników ***\n(A)Alfabtycznie\t(B)Wg Popularności\n-> ")

        if sort0 == "A" or sort0 =="a":
            self.m2B_Alfa(existLog,tag,ile)
        elif sort0 == "B" or sort0 == "b":
            self.m2B_Pop(existLog,tag,ile)
        else:
            print("Zły wybór. Spróbuj ponownie")
            self.sort_m2B(existLog,tag,ile)

    # sortowanie koniec               

    def m2B_Alfa(self,existLog,tag, ile):           

        c.execute("select b.name_band, b.country, b.city,b.since, b.listeners_kilo, b.tag, m.name_album, m.best_song FROM band AS b LEFT JOIN music AS m ON b.name_band = m.name_band WHERE b.tag LIKE '%{}%' order by name_band {};".format(tag, "asc"))
        disp = c.fetchmany(ile)
        c.execute("SELECT b.name_band, m.best_song FROM band AS b LEFT JOIN music AS m ON b.name_band = m.name_band WHERE b.tag LIKE '%{}%' order by name_band {};".format(tag,"asc"))
        results = c.fetchmany(ile)        
        resCount = c.rowcount
        print('\n\n'.join('#Wykonawca: %s | #Kraj: %s | #Miasto: %s | #Założony: %s | #Ilość fanów: %s tys \n#Gatunek: %s | #Album: %s | #Utwór: %s' % x for x in disp))     
        time.sleep(1)
        print("\n------Wyświetlono {} wyników. Dla podanego zapytania istnieje {} wyników-----\n".format(len(disp),resCount))
        self.outro(existLog, results) 

    def m2B_Pop(self,existLog,tag, ile):           
        conn.ping()
        c.execute("select b.name_band, b.country, b.city,b.since, b.listeners_kilo, b.tag, m.name_album, m.best_song FROM band AS b LEFT JOIN music AS m ON b.name_band = m.name_band WHERE b.tag LIKE '%{}%' order by listeners_kilo {};".format(tag,"asc"))
        disp = c.fetchmany(ile)
        c.execute("SELECT b.name_band, m.best_song FROM band AS b LEFT JOIN music AS m ON b.name_band = m.name_band WHERE b.tag LIKE '%{}%' order by listeners_kilo {};".format(tag,"asc"))
        results = c.fetchmany(ile)        
        resCount = c.rowcount
        print('\n\n'.join('#Wykonawca: %s | #Kraj: %s | #Miasto: %s | #Założony: %s | #Ilość fanów: %s tys \n#Gatunek: %s | #Album: %s | #Utwór: %s' % x for x in disp))     
        time.sleep(1)
        print("\n------Wyświetlono {} wyników. Dla podanego zapytania istnieje {} wyników-----\n".format(len(disp),resCount))
        self.outro(existLog, results)

#Rok Założenia - zakres

    def m3A(self,existLog):

        c.execute("select since from band group by since asc limit 1;")
        granica1 = ("".join('%s' % x for x in c.fetchall()))

        c.execute("select since from band group by since desc limit 1;")
        granica2 = ("".join('%s' % x for x in c.fetchall()))        

        print("Jaki przedział lat cię interesuje?")
        rok1 = input("Podaj dolny przedział zakresu-> ")
        if rok1.isdigit():
            pass
        if len(rok1) == 4:
            pass
        if c.execute("select since from band where since <= '{}';".format(rok1)):
            pass
        else:
            print("Rok spoza zakresu!\nNa OffFestival'u występowały założone w latach od {} do {} roku".format(granica1,granica2))
            self.m3A(existLog)
        try:    
            rok2 = int(input("Podaj górny przedział zakresu -> "))
            if c.execute("select since from band where since >= '{}';".format(rok2)):
                pass
            else:  
                print("Rok spoza zakresu!\nNa OffFestivalu występowały zespoły zakładane od {} do {} roku".format(granica1,granica2))
                self.m3A(existLog)
        except ValueError: 
            print("Podaj rok.")
            self.m3A(existLog)
             
        self.sort_m3A(existLog, rok1,rok2) 

    #sorotwanie początek

    def sort_m3A(self,existLog,rok1,rok2):
        try:
            ile = int(input("* Ilość wyników? -> "))
        except ValueError:
            print("Podaj liczbę")
            self.sort_m3A(existLog,rok1,rok2)
        sort0 = input("\n*** Wyświetlanie wyników ***\n(A)Alfabtycznie\t(B)Wg Popularności\n-> ")

        if sort0 == "A" or sort0 =="a":
            self.m3A_Alfa(existLog, rok1, rok2,ile)
        elif sort0 == "B" or sort0 == "b":
            self.m3A_Pop(existLog, rok1,rok2,ile)
        else:
            print("Zły wybór. Spróbuj ponownie")
            self.sort_m3A(existLog, rok1,rok2,ile)

    # sortowanie koniec


    def m3A_Alfa(self,existLog, rok1,rok2,ile):
        c.execute("select b.name_band, b.country, b.city,b.since, b.listeners_kilo, b.tag, m.name_album, m.best_song from band as b left join music as m on b.id_band = m.id_music where b.since between {} and {} order by name_band {};".format(rok1,rok2,"asc"))
        disp = c.fetchmany(ile)
        c.execute("select b.name_band, m.best_song from band as b left join music as m on b.id_band = m.id_music where b.since between {} and {} order by name_band {};".format(rok1,rok2,"asc"))
        results = c.fetchmany(ile) 
        resCount = c.rowcount
        print('\n\n'.join('#Wykonawca: %s | #Kraj: %s | #Miasto: %s | #Założony: %s | #Ilość fanów: %s tys \n#Gatunek: %s | #Album: %s | #Utwór: %s' % x for x in disp))     
        time.sleep(1)
        print("\n------Wyświetlono {} wyników. Dla podanego zapytania istnieje {} wyników-----\n".format(len(disp),resCount))
        self.outro(existLog, results)


    def m3A_Pop(self,existLog,rok1,rok2,ile):
        c.execute("select b.name_band, b.country, b.city,b.since, b.listeners_kilo, b.tag, m.name_album, m.best_song from band as b left join music as m on b.id_band = m.id_music where b.since between {} and {} order by listeners_kilo {};".format(rok1,rok2,"asc"))
        disp = c.fetchmany(ile)
        c.execute("select b.name_band, m.best_song from band as b left join music as m on b.id_band = m.id_music where b.since between {} and {} order by listeners_kilo {};".format(rok1,rok2,"asc"))
        results = c.fetchmany(ile) 
        resCount = c.rowcount
        print('\n\n'.join('#Wykonawca: %s | #Kraj: %s | #Miasto: %s | #Założony: %s | #Ilość fanów: %s tys \n#Gatunek: %s | #Album: %s | #Utwór: %s' % x for x in disp))     
        time.sleep(1)
        print("\n------Wyświetlono {} wyników. Dla podanego zapytania istnieje {} wyników-----\n".format(len(disp),resCount))
        self.outro(existLog, results)


#Popularność zakres

    def m3B(self,existLog):

        c.execute("select listeners_kilo from band group by listeners_kilo asc limit 1;")
        granica1 = ("".join('%s' % x for x in c.fetchall()))

        c.execute("select listeners_kilo from band group by listeners_kilo desc limit 1;")
        granica2 = ("".join('%s' % x for x in c.fetchall()))


        print("Jaki przedział popularności cię interesuje?") 
        try:
            ran1 = float(input("Podaj dolny przedział: ")) 

        except ValueError:
            print("Podaj liczbę. Używaj separatora '.'")
            self.m3B(existLog) 
            
        try:    
            ran2 = float(input("Podaj górny przedział: ")) 

        except ValueError:
            print("Podaj liczbę. Używaj separatora '.'")
            self.m3B(existLog)                 
            
            
        if c.execute("select listeners_kilo from band where listeners_kilo <= '{}';".format(ran1)):
            pass

        else:
            print("Dolny przedział spoza zakresu!\nZespół z najmniejszą popularnością ma {} tys. słuchaczy".format(granica1))
            self.m3B(existLog)

        if c.execute("select listeners_kilo from band where listeners_kilo >= '{}';".format(ran2)):
            pass

        else:  
            print("Górny przedział spoza zakresu!\nZespół z największą popularnością ma {} tys. słuchaczy".format(granica2))
            self.m3B(existLog)

        self.sort_m3B(existLog,ran1,ran2)    


    #sorotwanie początek

    def sort_m3B(self,existLog,ran1, ran2): 
        try:
            ile = int(input("* Ilość wyników? -> "))
            
        except ValueError:
            print("Podaj liczbę")
            self.sort_m3B(existLog,ran1, ran2)
        sort0 = input("\n*** Wyświetlanie wyników ***\n(A)Alfabtycznie\t(B)Wg Popularności\n-> ")

        if sort0 == "A" or sort0 =="a":
            self.m3B_Alfa(existLog, ran1, ran2,ile)
        elif sort0 == "B" or sort0 == "b":
            self.m3B_Pop(existLog,ran1,ran2,ile)
        else:
            print("Zły wybór. Spróbuj ponownie")
            self.sort_m3B(existLog, ran1,ran2,ile)


    #sortowanie koniec

    def m3B_Alfa(self,existLog,ran1,ran2,ile):
        c.execute("select b.name_band, b.country, b.city,b.since, b.listeners_kilo, b.tag, m.name_album, m.best_song from band as b left join music as m on b.id_band = m.id_music where b.listeners_kilo between {} and {} order by name_band {};".format(ran1,ran2,"asc"))
        disp = c.fetchmany(ile)
        c.execute("select b.name_band, m.best_song from band as b left join music as m on b.id_band = m.id_music where b.listeners_kilo between {} and {} order by name_band {};".format(ran1,ran2,"asc"))
        results = c.fetchmany(ile) 
        resCount = c.rowcount
        print('\n\n'.join('#Wykonawca: %s | #Kraj: %s | #Miasto: %s | #Założony: %s | #Ilość fanów: %s tys \n#Gatunek: %s | #Album: %s | #Utwór: %s' % x for x in disp))     
        time.sleep(1)
        print("\n------Wyświetlono {} wyników. Dla podanego zapytania istnieje {} wyników-----\n".format(len(disp),resCount))
        self.outro(existLog, results) 

    def m3B_Pop(self,existLog,ran1, ran2,ile):
        c.execute("select b.name_band, b.country, b.city,b.since, b.listeners_kilo, b.tag, m.name_album, m.best_song from band as b left join music as m on b.id_band = m.id_music where b.listeners_kilo between {} and {} order by listeners_kilo {};".format(ran1,ran2,"asc"))
        disp = c.fetchmany(ile)
        c.execute("select b.name_band, m.best_song from band as b left join music as m on b.id_band = m.id_music where b.since between {} and {} order by listeners_kilo {};".format(ran1,ran2,"asc"))
        results = c.fetchmany(ile) 
        resCount = c.rowcount
        print('\n\n'.join('#Wykonawca: %s | #Kraj: %s | #Miasto: %s | #Założony: %s | #Ilość fanów: %s tys \n#Gatunek: %s | #Album: %s | #Utwór: %s' % x for x in disp))     
        time.sleep(1)
        print("\n------Wyświetlono {} wyników. Dla podanego zapytania istnieje {} wyników-----\n".format(len(disp),resCount))
        self.outro(existLog, results)    


#popularne/unikalne - gatunki

    def m4A(self,existLog):

        print("Określ jak bardzo popularnych lub unikalnych gatunków poszukujesz.\nOkreśl popularność wpisując znak '+'.\nMożesz podać zaznaczyć skalę od 1 do 5.")
        popG = str(input("-> "))

        #if popG != "+":
            #print("Use plus '+' please!")
            #time.sleep(1)
            #self.m4            

        #else:
            #pass

        res = popG.count("+")
        print("Ustawiono skalę na {}".format(res))

        if res == 1:
            a = 1
            b = 6
        if res == 2:
            a = 7
            b = 12            
        if res == 3:
            a = 21
            b = 22            
        if res == 4:
            a = 22
            b = 25  
        if res == 5:
            a = 25
            b = 30

        elif res not in range (1,6):
            print(" ")
            print("Jesteś poza skalą! Korzystaj ze skali od 1 do 5".center(80,"-"))
            print(" ")
            self.m4A(existLog)

        self.sort_m4A(existLog,a,b)

#sorotwanie początek

    def sort_m4A(self,existLog,a,b):
        try:
            ile = int(input("* Ilość wyników? -> "))
        except ValueError:
            print("Podaj liczbę")
            self.sort_m4A(existLog,a,b)
        sort0 = input("\n*** Wyświetlanie wyników ***\n(A)Alfabtycznie\t(B)Wg Popularności\n-> ")

        if sort0 == "A" or sort0 =="a":
            self.m4A_Alfa(existLog,a,b,ile)
        elif sort0 == "B" or sort0 == "b":
            self.m4A_Pop(existLog,a,b,ile)
        else:
            print("Zły wybór. Spróbuj ponownie")
            self.sort_m4A(existLog,a,b)

    #sortowanie koniec


    def m4A_Alfa(self,existLog,a,b,ile):
        c.execute("select b.name_band, b.country, b.city,b.since, b.listeners_kilo, b.tag, m.name_album, m.best_song from (select tag, count(*) as num from band group by tag) as t join band as b on t.tag = b.tag join music as m on m.id_music = b.id_band where num between {} and {} order by name_band asc;".format(a,b)) 
        disp = c.fetchmany(ile) 
        c.execute("select b.name_band, best_song from (select tag, count(*) as num from band group by tag) as t join band as b on t.tag = b.tag join music as m on m.id_music = b.id_band where num between {} and {} order by name_band asc;".format(a,b))
        results = c.fetchmany(ile) 
        resCount = c.rowcount
        print('\n\n'.join('#Wykonawca: %s | #Kraj: %s | #Miasto: %s | #Założony: %s | #Ilość fanów: %s tys \n#Gatunek: %s | #Album: %s | #Utwór: %s' % x for x in disp))     
        time.sleep(1)
        print("\n------Wyświetlono {} wyników. Dla podanego zapytania istnieje {} wyników-----\n".format(len(disp),resCount))
        self.outro(existLog,results)

    def m4A_Pop(self,existLog,a,b,ile): 

        c.execute("select b.name_band, b.country, b.city,b.since, b.listeners_kilo, b.tag, m.name_album, m.best_song from (select tag, count(*) as num from band group by tag) as t join band as b on t.tag = b.tag join music as m on m.id_music = b.id_band where num between {} and {} order by listeners_kilo asc;".format(a,b)) 
        disp = c.fetchmany(ile) 
        c.execute("select b.name_band, best_song from (select tag, count(*) as num from band group by tag) as t join band as b on t.tag = b.tag join music as m on m.id_music = b.id_band where num between {} and {} order by listeners_kilo asc;".format(a,b))
        results = c.fetchmany(ile) 
        resCount = c.rowcount
        print('\n\n'.join('#Wykonawca: %s | #Kraj: %s | #Miasto: %s | #Założony: %s | #Ilość fanów: %s tys \n#Gatunek: %s | #Album: %s | #Utwór: %s' % x for x in disp))     
        time.sleep(1)
        print("\n------Wyświetlono {} wyników. Dla podanego zapytania istnieje {} wyników-----\n".format(len(disp),resCount))
        self.outro(existLog,results) 

#popularne/unikalne - kraj pochodzenia

    def m4B(self,existLog):

        print("Określ jak bardzo popularnych lub unikalnych krajów pochodzenia wykonawców poszukujesz.\nOkreśl popularność wpisując znak '+'.\nMożesz podać zaznaczyć skalę od 1 do 5.")
        popG = str(input("-> "))

        res = popG.count("+")
        print("Ustawiono skalę na {}".format(res))

        # zła tu skala
        if res == 1:
            a = 1
            b = 5
        if res == 2:
            a = 6
            b = 9            
        if res == 3:
            a = 10
            b = 65            
        if res == 4:
            a = 65
            b = 85  
        if res == 5:
            a = 85
            b = 95

        elif res not in range (1,6):
            print(" ")
            print("Jesteś poza skalą! Korzystaj ze skali od 1 do 5".center(80,"-"))
            print(" ")
        self.sort_m4B(existLog,a,b)


#sorotwanie początek

    def sort_m4B(self,existLog,a,b):
        try:
            ile = int(input("* Ilość wyników? -> "))
        except ValueError:
            print("Podaj liczbę")
            self.sort_m4B(existLog,a,b)            
        sort0 = input("\n*** Wyświetlanie wyników ***\n(A)Alfabtycznie\t(B)Wg Popularności\n-> ")

        if sort0 == "A" or sort0 =="a":
            self.m4B_Alfa(existLog,a,b,ile)
        elif sort0 == "B" or sort0 == "b":
            self.m4B_Pop(existLog,a,b,ile)
        else:
            print("Zły wybór. Spróbuj ponownie")
            self.sort_m4B(existLog,a,b)

    # sortowanie koniec


    def m4B_Alfa(self,existLog,a,b,ile): 


        c.execute("select b.name_band, b.country, b.city,b.since, b.listeners_kilo, b.tag, m.name_album, m.best_song from (select country, count(*) as num from band group by country) as k join band as b on k.country = b.country join music as m on m.id_music = b.id_band  where num between {} and {} order by name_band asc;".format(a,b))   
        disp = c.fetchmany(ile) 
        c.execute("select b.name_band,m.best_song from (select country, count(*) as num from band group by country) as k join band as b on k.country = b.country join music as m on m.id_music = b.id_band  where num between {} and {} order by name_band asc;".format(a,b))
        results = c.fetchmany(ile) 
        resCount = c.rowcount
        print('\n\n'.join('#Wykonawca: %s | #Kraj: %s | #Miasto: %s | #Założony: %s | #Ilość fanów: %s tys \n#Gatunek: %s | #Album: %s | #Utwór: %s' % x for x in disp))     
        time.sleep(1)
        print("\n------Wyświetlono {} wyników. Dla podanego zapytania istnieje {} wyników-----\n".format(len(disp),resCount))
        self.outro(existLog, results)     


    def m4B_Pop(self,existLog,a,b,ile): 


        c.execute("select b.name_band, b.country, b.city,b.since, b.listeners_kilo, b.tag, m.name_album, m.best_song from (select country, count(*) as num from band group by country) as k join band as b on k.country = b.country join music as m on m.id_music = b.id_band  where num between {} and {} order by listeners_kilo asc;".format(a,b))   
        disp = c.fetchmany(ile) 
        c.execute("select b.name_band,m.best_song from (select country, count(*) as num from band group by country) as k join band as b on k.country = b.country join music as m on m.id_music = b.id_band  where num between {} and {} order by listeners_kilo asc;".format(a,b))
        results = c.fetchmany(ile) 
        resCount = c.rowcount
        print('\n\n'.join('#Wykonawca: %s | #Kraj: %s | #Miasto: %s | #Założony: %s | #Ilość fanów: %s tys \n#Gatunek: %s | #Album: %s | #Utwór: %s' % x for x in disp))     
        time.sleep(1)
        print("\n------Wyświetlono {} wyników. Dla podanego zapytania istnieje {} wyników-----\n".format(len(disp),resCount))
        self.outro(existLog,results)    


    def outro(self,existLog,results):
        time.sleep(1)        
        print("Czy chcesz?\n")
        time.sleep(0.5)  
        print("(E)Eksportować jako playlistę.txt\n(q)Cofnij")
        outro_choice = input("-> ")
        if outro_choice == "E" or outro_choice == "e":
            self.export(existLog,results)
        elif outro_choice == "Q" or outro_choice == "q":
            if c.execute("select login,pass from user where login = %s and user_group = 1",(existLog)):
                self.menuADMIN(existLog)
            else:
                self.menu(existLog)
        else:
            print("\nNiepoprawny wybór\nSpróbuj ponownie! za 1..2..")
            time.sleep(1)
            self.outro(existLog, results)
        self.export(existLog, results)

    def export(self,existLog,results):
        plName = str(input("Jak chcesz nazwać playlistę?\n-> "))

        if ("{}.txt".format(plName)) in listdir('.'):
            print("Niestety podana nazwa jest zajęta. Podaj inną nazwę.")
            self.export(existLog, results)
        else:    
            io.open("{}.txt".format(plName),"a").write('\n'.join('%s - %s' % x for x in results))
            print("Zapisano!")
            time.sleep(2)
            if c.execute("select login,pass from user where login = %s and user_group = 1",(existLog)):
                self.menuADMIN(existLog)
            else:
                self.menu(existLog)      


Off()



