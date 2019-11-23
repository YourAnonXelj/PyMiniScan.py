import socket
from colorama import Fore, Style, init

init()
print(Fore.GREEN + Fore.LIGHTGREEN_EX +"""


   ▄███████▄ ▄██   ▄     ▄▄▄▄███▄▄▄▄    ▄█  ███▄▄▄▄    ▄█     ▄████████  ▄████████    ▄████████ ███▄▄▄▄   
  ███    ███ ███   ██▄ ▄██▀▀▀███▀▀▀██▄ ███  ███▀▀▀██▄ ███    ███    ███ ███    ███   ███    ███ ███▀▀▀██▄ 
  ███    ███ ███▄▄▄███ ███   ███   ███ ███▌ ███   ███ ███▌   ███    █▀  ███    █▀    ███    ███ ███   ███ 
  ███    ███ ▀▀▀▀▀▀███ ███   ███   ███ ███▌ ███   ███ ███▌   ███        ███          ███    ███ ███   ███ 
▀█████████▀  ▄██   ███ ███   ███   ███ ███▌ ███   ███ ███▌ ▀███████████ ███        ▀███████████ ███   ███ 
  ███        ███   ███ ███   ███   ███ ███  ███   ███ ███           ███ ███    █▄    ███    ███ ███   ███ 
  ███        ███   ███ ███   ███   ███ ███  ███   ███ ███     ▄█    ███ ███    ███   ███    ███ ███   ███ 
 ▄████▀       ▀█████▀   ▀█   ███   █▀  █▀    ▀█   █▀  █▀    ▄████████▀  ████████▀    ███    █▀   ▀█   █▀ 



Coded By Xelj


""")

ip = str(input("Introduce tu ip -> "))

puerto = int(input("Introduce el puerto ->"))


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


if sock.connect_ex((ip, puerto)):
         print("El puerto", puerto, "esta cerrado")
else:
    print("El puerto", puerto, "esta abierto")
