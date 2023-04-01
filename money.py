import gspread
from oauth2client.service_account import ServiceAccountCredentials
import time
import os

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

user_select = input("Qui est tu ? : ")

isconnect = True

#sheet.update_cell(1,2, str(Quentin + 1))
def moneymain():
    print(""" __       __                                         
|  \     /  \                                        
| $$\   /  $$  ______   _______    ______   __    __ 
| $$$\ /  $$$ /      \ |       \  /      \ |  \  |  \
| $$$$\  $$$$|  $$$$$$\| $$$$$$$\|  $$$$$$\| $$  | $$
| $$\$$ $$ $$| $$  | $$| $$  | $$| $$    $$| $$  | $$
| $$ \$$$| $$| $$__/ $$| $$  | $$| $$$$$$$$| $$__/ $$
| $$  \$ | $$ \$$    $$| $$  | $$ \$$     \ \$$    $$
 \$$      \$$  \$$$$$$  \$$   \$$  \$$$$$$$ _\$$$$$$$
                                           |  \__| $$
                                            \$$    $$
                                             \$$$$$$ """)

    reponse = input("""Que veux tu faire ? : \n
1. Gérer mon argent \n
2. Donner de l'agent\n
3. Afficher le classement\n
: """)

#==========================Money========================
 
    if reponse == "1":
        print(""" __       __                                                   
|  \     /  \                                                  
| $$\   /  $$  ______   _______    ______    ______    ______  
| $$$\ /  $$$ |      \ |       \  |      \  /      \  /      \ 
| $$$$\  $$$$  \$$$$$$\| $$$$$$$\  \$$$$$$\|  $$$$$$\|  $$$$$$\
| $$\$$ $$ $$ /      $$| $$  | $$ /      $$| $$  | $$| $$    $$
| $$ \$$$| $$|  $$$$$$$| $$  | $$|  $$$$$$$| $$__| $$| $$$$$$$$
| $$  \$ | $$ \$$    $$| $$  | $$ \$$    $$ \$$    $$ \$$     \
 \$$      \$$  \$$$$$$$ \$$   \$$  \$$$$$$$ _\$$$$$$$  \$$$$$$$
                                           |  \__| $$          
                                            \$$    $$          
                                             \$$$$$$           """)

        getordeletemoney = input("""Voulez vous :\n
    1. Mettre de l'argent\n
    2. Enlever de l'argent\n""")
                         
        if getordeletemoney == "1":
            num_get = input("""
  ______   ________  ________ 
 /      \ |        \|        \
|  $$$$$$\| $$$$$$$$ \$$$$$$$$
| $$ __\$$| $$__       | $$   
| $$|    \| $$  \      | $$   
| $$ \$$$$| $$$$$      | $$   
| $$__| $$| $$_____    | $$   
 \$$    $$| $$     \   | $$   
  \$$$$$$  \$$$$$$$$    \$$   
                              
                              
                              \n
Combien voulez vous d'argent ?
: """)
            sheet.update_cell(usergr1, usergr2, str(user + int(num_get)))
        elif getordeletemoney == "2":
            num_delete = input(""" _______                                                        
|       \                                                       
| $$$$$$$\  ______   ______ ____    ______  __     __   ______  
| $$__| $$ /      \ |      \    \  /      \|  \   /  \ /      \ 
| $$    $$|  $$$$$$\| $$$$$$\$$$$\|  $$$$$$\\$$\ /  $$|  $$$$$$\
| $$$$$$$\| $$    $$| $$ | $$ | $$| $$  | $$ \$$\  $$ | $$    $$
| $$  | $$| $$$$$$$$| $$ | $$ | $$| $$__/ $$  \$$ $$  | $$$$$$$$
| $$  | $$ \$$     \| $$ | $$ | $$ \$$    $$   \$$$    \$$     \
 \$$   \$$  \$$$$$$$ \$$  \$$  \$$  \$$$$$$     \$      \$$$$$$$
                                                                
                                                                
                                                                \n
Combien voulez vous enlever ?
:""")
            sheet.update_cell(usergr1, usergr2, str(user - int(num_delete)))

#====================SEND===================


    elif reponse == "2":
        user_givemoney = input("""  ______   __                      
 /      \ |  \                     
|  $$$$$$\ \$$ __     __   ______  
| $$ __\$$|  \|  \   /  \ /      \ 
| $$|    \| $$ \$$\ /  $$|  $$$$$$\
| $$ \$$$$| $$  \$$\  $$ | $$    $$
| $$__| $$| $$   \$$ $$  | $$$$$$$$
 \$$    $$| $$    \$$$    \$$     \
  \$$$$$$  \$$     \$      \$$$$$$$
                                   
                                   
                                   \n
Combien voulez vous donnez ? 
: """)
        user_getmoney = input("""  ______                             __ 
 /      \                           |  \
|  $$$$$$\  ______   _______    ____| $$
| $$___\$$ /      \ |       \  /      $$
 \$$    \ |  $$$$$$\| $$$$$$$\|  $$$$$$$
 _\$$$$$$\| $$    $$| $$  | $$| $$  | $$
|  \__| $$| $$$$$$$$| $$  | $$| $$__| $$
 \$$    $$ \$$     \| $$  | $$ \$$    $$
  \$$$$$$   \$$$$$$$ \$$   \$$  \$$$$$$$
                                        
                                        
                                        \n
A qui voulez vous l'envoyer ?
:""")
                           
        if user_getmoney == "Jessy":
            if user >= int(user_givemoney):
                sheet.update_cell(usergr1J, usergr2J, str(int(user_givemoney) + Jessy))
                sheet.update_cell(usergr1, usergr2, str(user - int(user_givemoney)))
            else:
                print("Vous n'avez pas assez d'argent !")
                time.sleep(3)
                moneymain()


while isconnect:
    if user_select == "admin":
        user = Quentin
        usergr1 = 1
        usergr2 = 2
        moneymain()
        isconnect = False
    elif user_select == "Jessy":
        user = Jessy
        usergr1 = 2
        usergr2 = 2
        moneymain()
        isconnect = False
    elif user_select == "Enzo":
        user = Enzo
        usergr1 = 3
        usergr2 = 2
        moneymain()
        isconnect = False
    elif user_select == "Evan":
        user = Evan
        usergr1 = 4
        usergr2 = 2
        moneymain()
        isconnect = False
    elif user_select == "Gio":
        user = Gio
        usergr1 = 5
        usergr2 = 2
        moneymain()
        isconnect = False
    elif user_select == "Vincent":
        user = Vincent
        usergr1 = 6
        usergr2 = 2
        moneymain()
        isconnect = False
    else:
        print("Nom Invalide Réessaye \n\n")
