from colorama import Fore, Style
from sms import SendSms
from time import sleep
from os import system
from requests import get


while 1:
    system("cls||clear")
    print("""{}
                     $$\                           
  
  ⌊veloc OFFICIAL⌉  
 
                            
                        {}by: veloc ◊ 
    """.format(Fore.LIGHTCYAN_EX, Style.RESET_ALL, Fore.LIGHTRED_EX))
    try:
        menu = int(input(Fore.LIGHTMAGENTA_EX + "1. SMS Gönder\n2. Çıkış\n\n" + Fore.LIGHTYELLOW_EX + "Seçim: "))
    except ValueError:
        system("cls||clear")
        print(Fore.LIGHTRED_EX + "Yanliş Yazdin Amk Çocuğu")
        sleep(3)
        continue
    if menu == 1:
        system("cls||clear")
        try:
            print(Fore.LIGHTYELLOW_EX + "Numarayi Yaz +90 Koyma Boslukta Birakma Yoksa Anani Zumzuklarim:"+ Fore.LIGHTGREEN_EX, end="")
            tel_no = int(input())
            if len(str(tel_no)) != 10:
                raise ValueError
        except ValueError:
            system("cls||clear")
            print(Fore.LIGHTRED_EX + "Gerizekali Oç Düzgün Gir Şunu") 
            sleep(3)
            continue
        system("cls||clear")
        try:
            print(Fore.LIGHTYELLOW_EX + "Oç Kaç Tane Göndermek İstiyosun:"+ Fore.LIGHTGREEN_EX, end="")
            kere = int(input())
        except ValueError:
            system("cls||clear")
            print(Fore.LIGHTRED_EX + "aptal oc yanlis yaptin zumzuğu yicen simdi.") 
            sleep(3)
            continue
        system("cls||clear")
        try:
            print(Fore.LIGHTYELLOW_EX + "Gönderme Hizi 0 hizli 10 yavas: "+ Fore.LIGHTGREEN_EX, end="")
            aralik = int(input())
        except ValueError:
            system("cls||clear")
            print(Fore.LIGHTRED_EX + "YA APTAL OROSPU EVLADI YANLIŞ YAPTIN") 
            sleep(3)
            continue
        system("cls||clear")
        sms = SendSms(str(tel_no))
        while sms.adet < kere:
            for attribute in dir(SendSms):
                attribute_value = getattr(SendSms, attribute)
                if callable(attribute_value):
                    if attribute.startswith('__') == False:
                        if sms.adet == kere:
                            break
                        exec("sms."+attribute+"()")
                        sleep(aralik)
        print(Fore.LIGHTRED_EX + "\nSiktir Olup Gitmek İçin 'enter' bas..")
        input()
    elif menu == 2:
        system("cls||clear")
        print(Fore.LIGHTRED_EX + "hadi yallah...")
        break
