import colorama
from colorama import Fore, Style
print(Fore.RED + '''           _             _        
      __      __  ___ | |__         (_) _ __  
      \ \ /\ / / / _ \| '_ \  _____ | || '_ \ 
       \ V  V / |  __/| |_) ||_____|| || |_) |
        \_/\_/   \___||_.__/        |_|| .__/ 
                                       |_|    ''')
import socket

hostname = input("Enter website address: ")

'''website ip ;)  |
                 \_/'''
print(f'The {hostname} IP address is {socket.gethostbyname(hostname)}')                
