import socket
import os
import sys
from datetime import datetime
import time
import requests
import pyperclip
from passlist.passwords import passe

#Functions ... 
# Main Codes...
def main():
    os.system('cls || clear')
    print('''
    ______              ______ 
    |   __ \.--.--.----.|   __ \ 
    |    __/|  |  |   _||    __/
    |___|   |_____|__|  |___|  
                                v 1.0(beta)

        ''')

# Port Scanner Codes ...
def PortScanner1():
    RemoteServer = input(str('Enter a remote host to scan: '))
    FromPort = int(input('From port: '))
    UpPort = int(input('Up port: '))+1
    RemoteServerIP = socket.gethostbyname(RemoteServer)

    os.system('cls || clear')
    main()
    print ('-'* 60)
    print (f'Please wait for scan host {RemoteServer}')
    print ('-'* 60)

    OpenPortList = []
    start = datetime.now()
    try:
        for port in range(FromPort,UpPort):  
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            result = sock.connect_ex((RemoteServerIP, port))
            if result == 0:
                print(f'Port {port}: 	Open')
                OpenPortList.append(port)            
            else:
                print(f'Port {port}:    Close')
            sock.close()

    except KeyboardInterrupt:
        print ('You pressed Ctrl+C')
        sys.exit()

    except socket.gaierror:
        print('Hostname could not be resolved...Exiting')
        sys.exit()

    except socket.error:
        print('Could not connect to server')
        sys.exit()

    finish = datetime.now()
    total =  finish - start

    print('-' * 60)
    print('Open ports list: ')
    for lists in OpenPortList:
        print(lists)
    print(f'Scanning Completed in: {total}')
    time.sleep(3)
    MainScript()

def PortScanner2():
    RemoteServer = input(str('Enter a remote host to scan: '))
    RemoteServerIP = socket.gethostbyname(RemoteServer)

    os.system('cls || clear')
    main()
    print ('-'* 60)
    print (f'Please wait for scan host {RemoteServer}')
    print ('-'* 60)

    OpenPortList = []
    start = datetime.now()
    try:
        for port in range(1, 65534):  
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            result = sock.connect_ex((RemoteServerIP, port))
            if result == 0:
                print(f'Port {port}: 	Open')
                OpenPortList.append(port)            
            else:
                print(f'Port {port}:    Close')
            sock.close()

    except KeyboardInterrupt:
        MainScript()

    except socket.gaierror:
        print('Hostname could not be resolved...Exiting')
        sys.exit()

    except socket.error:
        print('Could not connect to server')
        sys.exit()

    finish = datetime.now()
    total =  finish - start

    print('-' * 60)
    print('Open ports list: ')
    for lists in OpenPortList:
        print(lists)
    print(f'Scanning Completed in: {total}')
    time.sleep(3)
    MainScript()

# Get IP Address Code ...
def GetIpAddress():
    target = input('Enter a target address: ')
    address = socket.gethostbyname(target)
    os.system('cls || clear')
    main()
    print(f"your target IP address is : {address}")
    print ('-'* 60)
    print('''
          1> Copy address to clipboard
          2> Back
          ''')
    choice = input('Enter your choice: ')
    if choice == '1':
        pyperclip.copy(address)
        os.system('cls || clear')
        main()
        print(f'{address} Copied!')
        time.sleep(2)
    MainScript()

# API alive Checker ...
def ApiAliveChecker():
    main()
    print('example: https://example.com/api/?token=233902:627a0a567ec780.50560976')
    api = input('Enter a API address: ')
    res = requests.get(api)
    if res.status_code == 200:
        os.system('cls || clear')
        main()
        print('-'*60)
        print('API is alive!')
        time.sleep(2)
    else:
        os.system('cls || clear')
        main()
        print('-'*60)
        print('error or dead')
        time.sleep(2)
    MainScript()

# Admin page founder ...
def AdminPageFounder():
    main()
    target = input('Enter your target address(like: example.com): ')
    print('-'*60)
    target_link = f'https://{target}'
    start = datetime.now()
    try:
        for root in passe:
            req = requests.get(f'{target_link}/{root}')
            if req.status_code == 200:
                os.system('cls || clear')
                finish = datetime.now()
                total = finish - start
                main()
                print(f'found! address name is: {target_link}/{root}')
                print(f'Scanning Completed in: {total}')
                print('-'*60)
                print('''
                    1> Copy address to clipboard
                    2> Back
                    ''')
                choice = input('Enter your choice')
                if choice == '1':
                    os.system('cls || clear')
                    main()
                    print(f'{target_link}/{root} Copied!')
                    time.sleep(2)
                MainScript()
            else:
                print(f' {target_link}/{root} - not found! trying again...')
    except:
        print('Error!')
        time.sleep(2)
        MainScript()
# Main Script ... 
def MainScript():
    main()
    print('''
        1> Port Scanner
        2> Get IP Address
        3> API Alive Checker
        4> Admin page founder
        5> exit 
        ''')
    choice = input('type your choice: ')

    if choice == '1':
        main()
        print('''
        1> Personalized(choice port yourself)
        2> Default(scan port 1 up 65534)
        3> Back
            ''')
        choice = input('type your cohice:')
        
        if choice == '1':
            main()
            PortScanner1()
        elif choice == '2':
            main()
            PortScanner2()
        MainScript()
    elif choice == '2':
        main()
        GetIpAddress()
    elif choice == '3':
        main()
        ApiAliveChecker()
    elif choice == '4':
        main()
        AdminPageFounder()
    else:
        print('bye!')
        
MainScript()