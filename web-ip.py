import socket

hostname = input("Enter website address: ")

'''website ip ;)  |
                 \_/'''
print(f'The {hostname} IP address is {socket.gethostbyname(hostname)}')                
