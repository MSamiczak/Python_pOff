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
        #time.sleep(1)
        #self.log0()
        self.menu()
    
    def log0(self):
        print("(1)Mam już konto\n(2)Dodaj nowe konto\n(q)Wyjdź z programu")
        choice_log0 = input("-> ")
        if choice_log0 == "1":
            self.log1()
        elif choice_log0 == "2":
            self.log2()
        elif choice_log0 == "Q" or choice_log0 == "q":
            exit()    
        else:
            print("Nie dokonano poprawnego wyboru:(\nSpróbuj ponownie! za 1..2..")
            print(" ")
            time.sleep(1)
            self.log0()
            
              
    def log1(self): #logowanie istniejącego uzytkownika
        existLog = input("Podaj login: ")
        existPass = input("Podaj hasło: ")
        if c.execute("select login,pass from user where login = %s and pass = %s",(existLog,existPass)):
            if existLog == "maciek":
                print("Admin!")
            print("\nWitaj ponownie {}\n".format(existLog))
            time.sleep(1)
            self.menu()
        else:
            self.wrong()           
                
    def log2(self):   #nowy user
        createLogin = input("Podaj login: ") 
        if c.execute("select login from user where login = %s",createLogin):
            print("\nLogin zajęty!\nWymyśl coś innego.")
            print(" ")
            time.sleep(1)
            self.log2()
        else:
            createPassw = input("Podaj hasło: ")
            c.execute("INSERT INTO user VALUES(null,%s,%s)", (createLogin, createPassw))
            # c.execute("Dodaję użytkownika bazy z uprawnieniami enter enter")
            #c.execute("CREATE TABLE {} (id int primary key auto_increment, name_band varchar (45), name_album varchar (45), best_song varchar (45), ocena varchar(1));".format(createLogin))
            
            conn.commit()
            print("\nUżytkownik utworzony\n")
            conn.close()
            self.menu()
                
            
    def wrong(self):
        print("Błędny login lub hasło! ")
        print("(1)Ponowne logowanie\n(q)Wyjdź")
        ifWrongchoice = input("-> ")
        if ifWrongchoice == "1":
            self.log1()
        elif ifWrongchoice == "Q" or ifWrongchoice == "q":
            self.log0()
                
            
    def menu(self):
        print("Dokonaj wyboru z listy MENU")
        print("\n(1)Wybrana edycja Off'a\n(2)Podobne do ulubionego\n(3)Wybierz zakres\n(4)Popularne/unikalne\n(q)Wyjście z progamu!")
        choice_menu = input("-> ")
      
        if choice_menu == "1":
            self.m1()
        if choice_menu == "2":
            self.m2()         
        if choice_menu == "3":
            self.m3()       
        if choice_menu == "4":
            self.m4()   
      # if choice1 == "5":
      #       self.p5()
      
        elif choice_menu == "Q" or choice_menu == "q":
            cy =["Do zobaczenia!", "Cześć", "Elo 320", "Kolejne śmieszne pożegnanie", "Jeszcze inne!"]
            print(random.choice(cy))
            exit()   
              
        else:
            print("\nNiepoprawny wybór\nSpróbuj ponownie! za 1..2..")
            time.sleep(1)
            self.menu()
       
       
         
    def m1(self): #Pozcyja m1 
        print("\n*** Wybrana edycja Off'a ***")
        print("\n(A)Rok Festiwalu\n(B)Która edycja Fetiwalu\n(q)Wyjście do MENU")
        choice_m = input("-> ")
        
        if choice_m == "A" or choice_m == "a":
            self.m1_A()
          
        if choice_m == "B" or choice_m == "b":
            self.m1_B()   
        
        if choice1 == "Q" or choice1 == "q":
            self.menu()
            
        else:
            print("\nNiepoprawny wybór\nSpróbuj ponownie! za 1..2..")
            time.sleep(1)
            self.m1()
    
    #Pozycja m2
    def m2(self):
        print("\n*** Podobne do ulubionego ***")
        print("\n(A)Zespołu\n(B)Gatunku muzyki\n(q)Wyjście do MENU")
        choice_m = input("-> ")
        
        if choice_m == "A" or choice_m == "a" or choice_m == "1":
            self.m2_A()
          
        if choice_m == "B" or choice_m == "b":
            self.m2_B()   
        
        if choice_m == "Q" or choice_m == "q":
            self.menu()
          
        else:
            print("\nNiepoprawny wybór\nSpróbuj ponownie! za 1..2..")
            time.sleep(1)
            self.m2()
          
    #Pozycja m3
    def m3(self):
        print("\n*** Wybierz zakres ***")
        print("\n(A)Rok założenia\n(B)Ilość słuchaczy\n(q)Wyjście do MENU")
        choice_m = input("-> ")
        
        if choice_m == "A" or choice_m == "a":
            self.m3_A()
          
        if choice_m == "B" or choice_m == "b":
            self.m3_B()   
        
        if choice1 == "Q" or choice1 == "q":
            self.main_menu()
            
        else:
            print("\nNiepoprawny wybór\nSpróbuj ponownie! za 1..2..")
            time.sleep(1)
            self.m3()
            
      #Pozycja m4      
    def m4(self):
        print("\n*** Popularne/Unikalne ***")
        print("\n(A)Gatunki muzyczne\n(B)Kraj zespołu")
        choice_m = input("-> ")
      
        if choice_m == "A" or choice_m == "a":
            self.m4_A()
        
        if choice_m == "B" or choice_m == "b":
            self.m4_B()   
      
        if choice1 == "Q" or choice1 == "q":
            self.menu()
        
        else:
            print("\nNiepoprawny wybór\nSpróbuj ponownie! za 1..2..")
            time.sleep(1)
            self.m4()  
        
            
    def m1_A(self):
        
        rok = str(input("Szukany rok?: "))
        if c.execute("select year from festival where year = {};".format(rok)):
            pass
        else:
            c.execute("select year from festival group by year asc limit 1;")
            granica1 = ("".join('%s' % x for x in c.fetchall()))
            c.execute("select year from festival group by year desc limit 1;")
            granica2 = ("".join('%s' % x for x in c.fetchall()))            
            print("OffFestival odbywa się od {} r. Ostatnia edycja odbyła się w {} r.".format(granica1, granica2))
            self.m1_A()
            
        ile = int(input("Ile zespołów na liście?: "))
        c.execute("select m.name_band, m.best_song from music as m inner join lineup as l on m.id_music = l.id_band inner join festival as f on f.edition = l.id_off where f.year = %s;",rok)
        results = c.fetchmany(ile)
        print('\n'.join('Band: %s; Best Song: %s' % x for x in results))
        self.outro(results)                
            
            
        def m1_B(self):
            
            edi = str(input("Szukany edycja festiwalu?: "))
            if c.execute("select edition from festival where edition = {};".format(edi)):
                pass
            else:
                c.execute("select edition from festival group by edition desc limit 1;")
                granica2 = ("".join('%s' % x for x in c.fetchall()))            
                print("Do tej pory odbyło się {} edycji festiwalu.".format(granica2))
                self.m1_B()
                
            ile = int(input("Ile zespołów na liście?: "))
            c.execute("select m.name_band, m.best_song from music as m inner join lineup as l on m.id_music = l.id_band inner join festival as f on f.edition = l.id_off where f.year = %s;",rok)
            results = c.fetchmany(ile)
            print('\n'.join('%s %s' % x for x in results))
            self.outro(results)
        
    def m2_A(self):
        nazwa = str(input("Zespoły podobne do...?: "))
        if c.execute("select name_band from band where name_band like'%{}%';".format(nazwa)):
            pass
      
        else:
            print("Przykro mi {} nie występował jeszcze na OFFie.\nWybierz jednego z artystów OFFa".format(nazwa.upper()))
            self.m2_A()
            
        ile = int(input("Ile zespołów na liście?: "))
        c.execute("select b.tag, b.name_band from band as b left join music as m on b.id_band = m.id_music where tag = (select tag from band where name_band like '%{}%');".format(nazwa))
        results = c.fetchmany(ile)
        print('\n'.join('%s %s' % x for x in results))
        self.outro(results)
      
    def m2_B(self):
        tag = str(input("Podaj gatunek...?"))
        if c.execute("select tag from band where tag = '{}';".format(tag)):
            pass
        else:
            print("Przykro mi, jeszcze żaden artysta z gatunku {} nie wystąpił na OffFestivalu.\nKoniecznie poinformuj o tym dyrektora Rojka!".format(tag.upper()))
            self.m2_B()
            
        ile = int(input("Ile zespołów na liście?: "))
        c.execute("SELECT b.tag, b.name_band, m.best_song FROM band AS b LEFT JOIN music AS m ON b.name_band = m.name_band WHERE b.tag LIKE '%{}%';".format(tag))
        results = c.fetchmany(ile)
        print('\n'.join('%s %s %s' % x for x in results))
        self.outro(results)
          
    def m3_A(self):
      
        c.execute("select since from band group by since asc limit 1;")
        granica1 = ("".join('%s' % x for x in c.fetchall()))
    
        c.execute("select since from band group by since desc limit 1;")
        granica2 = ("".join('%s' % x for x in c.fetchall()))        
        
        print("Jaki przedział lat cię interesuje?") # zastąpie to wynikami wpisanymi obok siebie po spacji
        rok1 = input("Podaj 1 rok -> ")
        if c.execute("select since from band where since <= '{}';".format(rok1)):
            pass
        else:
            print("Rok spoza zakresu!\nNa OffFestival'u występowały założone w latach od {} do {} roku".format(granica1,granica2))
            self.m3_A()
            
        rok2 = input("Podaj 2 rok -> ")
        
        if c.execute("select since from band where since >= '{}';".format(rok2)):
            pass
        else:  
            print("Rok spoza zakresu!\nNa OffFestivalu występowały zespoły zakładane od {} do {} roku".format(granica1,granica2))
            self.m3_A()
        
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
            
            
    def m3_B(self):
        
        c.execute("select listeners_kilo from band group by listeners_kilo asc limit 1;")
        granica1 = ("".join('%s' % x for x in c.fetchall()))
    
        c.execute("select listeners_kilo from band group by listeners_kilo desc limit 1;")
        granica2 = ("".join('%s' % x for x in c.fetchall()))
        
        
        
        
        
        
        print("Jaki przedział popularności cię interesuje?") # zastąpie to wynikami wpisanymi obok siebie po spacji
        ran = [x for x in input("Podaj 2 liczby w tysiącach oddzielone spacją: ").split(" ")]
        
        if c.execute("select listeners_kilo from band where listeners_kilo <= '{}';".format(ran[0])):
            pass
        
        else:
            print("Dolny przedział spoza zakresu!\nZespół z najmniejszą popularnością ma {} tys. słuchaczy".format(granica1))
            self.m3_B()
        
        if c.execute("select listeners_kilo from band where listeners_kilo >= '{}';".format(ran[1])):
            pass
        
        else:  
            print("Górny przedział spoza zakresu!\nZespół z największą popularnością ma {} tys. słuchaczy".format(granica2))
            self.m3_B()
        
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
            
    def m4_A(self):

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
            print("Jesteś poza skalą! Korzystaj ze skali od 1 do 5.")
            self.m4_A()
            
            
        c.execute("select b.name_band, best_song from (select tag, count(*) as num from band group by tag) as t join band as b on t.tag = b.tag join music as m on m.id_music = b.id_band where num between {} and {} order by num;".format(a,b))
        results = c.fetchall()
        resCount = c.rowcount
        print('\n'.join('%s %s %s' % x for x in results))
        print("\nWyświetlowno {} wyników".format(resCount))


    def m4_B(self):

        print("Określ jak bardzo popularnych lub unikalnych krajów dla wykonawców poszukujesz.\nOkreśl popularność wpisując znak '+'.\nMożesz podać zaznaczyć skalę od 1 do 5.")
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
            print("Jesteś poza skalą! Korzystaj ze skali od 1 do 5.")
            self.m4_A()
            
            
        c.execute("select b.name_band,m.best_song, k.country from (select country, count(*) as num from band group by country) as k join band as b on k.country = b.country join music as m on m.id_music = b.id_band  where num between {} and {} order by country;".format(a,b))
        results = c.fetchall()
        resCount = c.rowcount
        print('\n'.join('%s %s %s' % x for x in results))
        print("\nWyświetlowno {} wyników".format(resCount))        
        
        
                      
        
        
        
            
                    
            
Off()