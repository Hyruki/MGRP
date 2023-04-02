import gspread
from oauth2client.service_account import ServiceAccountCredentials
import time
import os
import colorama
from colorama import Fore, Style, Back
from datetime import datetime

timehours = datetime.now().strftime("%H:%M:%S")

if timehours <= "18:00:00":
    double_B = f"{Fore.GREEN}Bonjour"
else:
    double_B = f"{Fore.GREEN}Bonsoir"

colorama.init(autoreset=True)

scope = ["https://spreadsheets.google.com/feeds","https://www.googleapis.com/auth/spreadsheets","https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]

creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope)

client = gspread.authorize(creds)

sheet = client.open("DataMoney").sheet1

Quentin = int(sheet.cell(1,2).value)
Jessy = int(sheet.cell(2,2).value)
Enzo = int(sheet.cell(3,2).value)
Evan = int(sheet.cell(4,2).value)
Gio = int(sheet.cell(5,2).value)
Vincent = int(sheet.cell(5,2).value)

usergr1Q = 1
usergr2Q = 2

usergr1J = 2
usergr2J = 2

usergr1En = 3
usergr2En = 2

usergr1Ev = 4
usergr2Ev = 2

usergr1G = 5
usergr2G = 2

usergr1V = 6
usergr2V = 2

os.system('clear')

user_select = input("""XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
XX                                                                          XX
XX   MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM   XX
XX   MMMMMMMMMMMMMMMMMMMMMssssssssssssssssssssssssssMMMMMMMMMMMMMMMMMMMMM   XX
XX   MMMMMMMMMMMMMMMMss'''                          '''ssMMMMMMMMMMMMMMMM   XX
XX   MMMMMMMMMMMMyy''                                    ''yyMMMMMMMMMMMM   XX
XX   MMMMMMMMyy''                                            ''yyMMMMMMMM   XX
XX   MMMMMy''                                                    ''yMMMMM   XX
XX   MMMy'                                                          'yMMM   XX
XX   Mh'                                                              'hM   XX
XX   -                                                                  -   XX
XX                                                                          XX
XX   ::                                                                ::   XX
XX   MMhh.        ..hhhhhh..                      ..hhhhhh..        .hhMM   XX
XX   MMMMMh   ..hhMMMMMMMMMMhh.                .hhMMMMMMMMMMhh..   hMMMMM   XX
XX   ---MMM .hMMMMdd:::dMMMMMMMhh..        ..hhMMMMMMMd:::ddMMMMh. MMM---   XX
XX   MMMMMM MMmm''      'mmMMMMMMMMyy.  .yyMMMMMMMMmm'      ''mmMM MMMMMM   XX
XX   ---mMM ''             'mmMMMMMMMM  MMMMMMMMmm'             '' MMm---   XX
XX   yyyym'    .              'mMMMMm'  'mMMMMm'              .    'myyyy   XX
XX   mm''    .y'     ..yyyyy..  ''''      ''''  ..yyyyy..     'y.    ''mm   XX
XX           MN    .sMMMMMMMMMss.   .    .   .ssMMMMMMMMMs.    NM           XX
XX           N`    MMMMMMMMMMMMMN   M    M   NMMMMMMMMMMMMM    `N           XX
XX            +  .sMNNNNNMMMMMN+   `N    N`   +NMMMMMNNNNNMs.  +            XX
XX              o+++     ++++Mo    M      M    oM++++     +++o              XX
XX                                oo      oo                                XX
XX           oM                 oo          oo                 Mo           XX
XX         oMMo                M              M                oMMo         XX
XX       +MMMM                 s              s                 MMMM+       XX
XX      +MMMMM+            +++NNNN+        +NNNN+++            +MMMMM+      XX
XX     +MMMMMMM+       ++NNMMMMMMMMN+    +NMMMMMMMMNN++       +MMMMMMM+     XX
XX     MMMMMMMMMNN+++NNMMMMMMMMMMMMMMNNNNMMMMMMMMMMMMMMNN+++NNMMMMMMMMM     XX
XX     yMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMy     XX
XX   m  yMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMy  m   XX
XX   MMm yMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMy mMM   XX
XX   MMMm .yyMMMMMMMMMMMMMMMM     MMMMMMMMMM     MMMMMMMMMMMMMMMMyy. mMMM   XX
XX   MMMMd   ''''hhhhh       odddo          obbbo        hhhh''''   dMMMM   XX
XX   MMMMMd             'hMMMMMMMMMMddddddMMMMMMMMMMh'             dMMMMM   XX
XX   MMMMMMd              'hMMMMMMMMMMMMMMMMMMMMMMh'              dMMMMMM   XX
XX   MMMMMMM-               ''ddMMMMMMMMMMMMMMdd''               -MMMMMMM   XX
XX   MMMMMMMM                   '::dddddddd::'                   MMMMMMMM   XX
XX   MMMMMMMM-                                                  -MMMMMMMM   XX
XX   MMMMMMMMM                                                  MMMMMMMMM   XX
XX   MMMMMMMMMy                                                yMMMMMMMMM   XX
XX   MMMMMMMMMMy.                                            .yMMMMMMMMMM   XX
XX   MMMMMMMMMMMMy.                                        .yMMMMMMMMMMMM   XX
XX   MMMMMMMMMMMMMMy.                                    .yMMMMMMMMMMMMMM   XX
XX   MMMMMMMMMMMMMMMMs.                                .sMMMMMMMMMMMMMMMM   XX
XX   MMMMMMMMMMMMMMMMMMss.           ....           .ssMMMMMMMMMMMMMMMMMM   XX
XX   MMMMMMMMMMMMMMMMMMMMNo         oNNNNo         oNMMMMMMMMMMMMMMMMMMMM   XX
XX                                                                          XX
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

    .o88o.                               o8o                .
    888 `"                               `"'              .o8
   o888oo   .oooo.o  .ooooo.   .ooooo.  oooo   .ooooo.  .o888oo oooo    ooo
    888    d88(  "8 d88' `88b d88' `"Y8 `888  d88' `88b   888    `88.  .8'
    888    `"Y88b.  888   888 888        888  888ooo888   888     `88..8'
    888    o.  )88b 888   888 888   .o8  888  888    .o   888 .    `888'
   o888o   8""888P' `Y8bod8P' `Y8bod8P' o888o `Y8bod8P'   "888"      d8'
                                                                .o...P'
                                                                `XER0'

Qui est tu ? : """)

isconnect = True

#sheet.update_cell(1,2, str(Quentin + 1))
def moneymain():
    os.system('clear')
    print(f"""{Fore.RED}
.___  ___.   ______   .__   __.  ___________    ____ .______      .______   
|   \/   |  /  __  \  |  \ |  | |   ____\   \  /   / |   _  \     |   _  \  
|  \  /  | |  |  |  | |   \|  | |  |__   \   \/   /  |  |_)  |    |  |_)  | 
|  |\/|  | |  |  |  | |  . `  | |   __|   \_    _/   |      /     |   ___/  
|  |  |  | |  `--'  | |  |\   | |  |____    |  |     |  |\  \----.|  |      
|__|  |__|  \______/  |__| \__| |_______|   |__|     | _| `._____|| _|      
                                                             \n                                                       
""")
    print(double_B, username, f"{Fore.GREEN}Vous avez actuellement sur votre compte :", user, f"{Fore.GREEN}$\n")

    reponse = input(f"""{Fore.MAGENTA}Que veux tu faire ? : \n
{Fore.BLUE}1. Gérer mon argent \n
{Fore.YELLOW}2. Donner de l'agent\n
{Fore.RED}3. Afficher le classement\n
{Fore.WHITE}: """)

    if reponse == "1":
        os.system('clear')
        money_manage()
    
    elif reponse == "2":
        os.system('clear')
        money_send()
    else:
        moneymain()

#==========================Money========================
 

def money_manage():
        print("""
.___  ___.      ___      .__   __.      ___       _______  _______ 
|   \/   |     /   \     |  \ |  |     /   \     /  _____||   ____|
|  \  /  |    /  ^  \    |   \|  |    /  ^  \   |  |  __  |  |__   
|  |\/|  |   /  /_\  \   |  . `  |   /  /_\  \  |  | |_ | |   __|  
|  |  |  |  /  _____  \  |  |\   |  /  _____  \ |  |__| | |  |____ 
|__|  |__| /__/     \__\ |__| \__| /__/     \__\ \______| |_______|

""")

        getordeletemoney = input("""Voulez vous :\n
    1. Mettre de l'argent\n
    2. Enlever de l'argent\n""")
                         
        if getordeletemoney == "1":
            os.system('clear')
            num_get = input("""
   _______  _______ .___________.
 /  _____||   ____||           |
|  |  __  |  |__   `---|  |----`
|  | |_ | |   __|      |  |     
|  |__| | |  |____     |  |     
 \______| |_______|    |__|     
                                                             
                              \n
Combien voulez vous d'argent ?
: """)
            sheet.update_cell(usergr1, usergr2, str(user + int(num_get)))
        elif getordeletemoney == "2":
            os.system('clear')
            num_delete = input(""" 
.______       _______ .___  ___.   ______   ____    ____  _______ 
|   _  \     |   ____||   \/   |  /  __  \  \   \  /   / |   ____|
|  |_)  |    |  |__   |  \  /  | |  |  |  |  \   \/   /  |  |__   
|      /     |   __|  |  |\/|  | |  |  |  |   \      /   |   __|  
|  |\  \----.|  |____ |  |  |  | |  `--'  |    \    /    |  |____ 
| _| `._____||_______||__|  |__|  \______/      \__/     |_______|
                                                                              
                                                                \n
Combien voulez vous enlever ?
:""")
            sheet.update_cell(usergr1, usergr2, str(user - int(num_delete)))

#====================SEND===================


def money_send():
    user_givemoney = input("""  
  _______  __  ____    ____  _______ 
 /  _____||  | \   \  /   / |   ____|
|  |  __  |  |  \   \/   /  |  |__   
|  | |_ | |  |   \      /   |   __|  
|  |__| | |  |    \    /    |  |____ 
 \______| |__|     \__/     |_______|
                                         \n
Combien voulez vous donnez ? 
: """)
    user_getmoney = input("""     
     _______. _______ .__   __.  _______  
    /       ||   ____||  \ |  | |       \ 
   |   (----`|  |__   |   \|  | |  .--.  |
    \   \    |   __|  |  . `  | |  |  |  |
.----)   |   |  |____ |  |\   | |  '--'  |
|_______/    |_______||__| \__| |_______/ 
                                          
                \n
A qui voulez vous l'envoyer ?
:""")
                           
    if user_getmoney == "Jessy":
        if user >= int(user_givemoney):
            if username != user_getmoney:
                sheet.update_cell(usergr1J, usergr2J, str(int(user_givemoney) + Jessy))
                sheet.update_cell(usergr1, usergr2, str(user - int(user_givemoney)))
                print("L'argent a bien été transférer à Jessy")
                time.sleep(3)
                moneymain()
            else:
                print(f"{Fore.RED}ERROR : Tu ne peux pas envoyer de l'argent sur ton propre compte !!!\n\n")
                time.sleep(3)
                moneymain()
        else:
            print("ERROR : Vous n'avez pas assez d'argent !")
            time.sleep(3)
            moneymain()
    elif user_getmoney == "Enzo":
        if user >= int(user_givemoney):
            if username != user_getmoney:
                sheet.update_cell(usergr1En, usergr2En, str(int(user_givemoney) + Enzo))
                sheet.update_cell(usergr1, usergr2, str(user - int(user_givemoney)))
                print("L'argent a bien été transférer à Enzo")
                time.sleep(3)
                moneymain()
            else:
                print(f"{Fore.RED}ERROR : Tu ne peux pas envoyer de l'argent sur ton propre compte !!!\n\n")
                time.sleep(3)
                moneymain()
        else:
            print("ERROR : Vous n'avez pas assez d'argent !")
            time.sleep(3)
            moneymain()
    elif user_getmoney == "Evan":
        if user >= int(user_givemoney):
            if username != user_getmoney:
                sheet.update_cell(usergr1Ev, usergr2Ev, str(int(user_givemoney) + Evan))
                sheet.update_cell(usergr1, usergr2, str(user - int(user_givemoney)))
                print("L'argent a bien été transférer à Evan")
                time.sleep(3)
                moneymain()
            else:
                print(f"{Fore.RED}ERROR : Tu ne peux pas envoyer de l'argent sur ton propre compte !!!\n\n")
                time.sleep(3)
                moneymain()
        else:
            print("ERROR : Vous n'avez pas assez d'argent !")
            time.sleep(3)
            moneymain()
    elif user_getmoney == "Gio":
        if user >= int(user_givemoney):
            if username != user_getmoney:
                sheet.update_cell(usergr1G, usergr2G, str(int(user_givemoney) + Gio))
                sheet.update_cell(usergr1, usergr2, str(user - int(user_givemoney)))
                print("L'argent a bien été transférer à Gio")
                time.sleep(3)
                moneymain()
            else:
                print(f"{Fore.RED}ERROR : Tu ne peux pas envoyer de l'argent sur ton propre compte !!!\n\n")
                time.sleep(3)
                moneymain()
        else:
            print("ERROR : Vous n'avez pas assez d'argent !")
            time.sleep(3)
            moneymain()
    elif user_getmoney == "Vincent":
        if user >= int(user_givemoney):
            if username != user_getmoney:
                sheet.update_cell(usergr1V, usergr2V, str(int(user_givemoney) + Vincent))
                sheet.update_cell(usergr1, usergr2, str(user - int(user_givemoney)))
                print("L'argent a bien été transférer à Vincent")
                time.sleep(3)
                moneymain()
            else:
                print(f"{Fore.RED}ERROR : Tu ne peux pas envoyer de l'argent sur ton propre compte !!!\n\n")
                time.sleep(3)
                moneymain()


        else:
            print("ERROR : Vous n'avez pas assez d'argent !")
            time.sleep(3)
            moneymain()
    elif user_givemoney == username:
        print(f"{Fore.RED}ERROR : Tu ne peux pas envoyer de l'argent sur ton propre compte !!!\n")


while isconnect:
    if user_select == "admin":
        user = Quentin
        username = user_select
        usergr1 = 1
        usergr2 = 2
        moneymain()
        isconnect = False
    elif user_select == "Jessy":
        user = Jessy
        username = user_select
        usergr1 = 2
        usergr2 = 2
        moneymain()
        isconnect = False
    elif user_select == "Enzo":
        user = Enzo
        username = user_select
        usergr1 = 3
        usergr2 = 2
        moneymain()
        isconnect = False
    elif user_select == "Evan":
        user = Evan
        username = user_select
        usergr1 = 4
        usergr2 = 2
        moneymain()
        isconnect = False
    elif user_select == "Gio":
        user = Gio
        username = user_select
        usergr1 = 5
        usergr2 = 2
        moneymain()
        isconnect = False
    elif user_select == "Vincent":
        user = Vincent
        username = user_select
        usergr1 = 6
        usergr2 = 2
        moneymain()
        isconnect = False
    else:
        print("Nom Invalide Réessaye \n\n")
