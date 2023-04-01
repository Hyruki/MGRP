import gspread
from oauth2client.service_account import ServiceAccountCredentials
import os

scope = ["https://spreadsheets.google.com/feeds","https://www.googleapis.com/auth/spreadsheets","https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]

creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope)

client = gspread.authorize(creds)

sheet = client.open("DataMoney").sheet1

Quentin = int(sheet.cell(1,2).value)
Jessy = int(sheet.cell(2,2).value)
Enzo = int(sheet.cell(3,2).value)


#sheet.update_cell(1,2, str(Quentin + 1))

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
3. Mettre à jour mon argent\n
: """)
     
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
        num_get = input("""  ______   ________  ________ 
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
        sheet.update_cell(1,2, str(Quentin+int(num_get)))
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
        sheet.update_cell(1,2, str(Quentin - int(num_delete)))