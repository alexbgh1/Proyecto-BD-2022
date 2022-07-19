import os

continuar = 1
while(continuar):
    try:
        os.popen("mysqldump.exe -u root -ppassword sophia3 > sophia3Copia.sql") #root -> password
    except:
        print("Error")
    continuar = int(input("Presione 0 para parar:"))
