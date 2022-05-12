from importlib.resources import path
import socket
import os
import sys
from datetime import datetime
import time
import requests
import pyperclip
from pathlist.path import pathes
from colorama import Fore

#Functions ... 
# Main Codes...
def main():
    os.system('cls || clear')
    print(Fore.LIGHTMAGENTA_EX+'''
    ______              ______ 
    |   __ \.--.--.----.|   __ \ 
    |    __/|  |  |   _||    __/
    |___|   |_____|__|  |___|  
                                v 1.0

        '''+ Fore.RESET)

# Port Scanner Codes ...
def PortScanner1():
    try:
        RemoteServer = input(str(f'{Fore.LIGHTWHITE_EX}Enter a remote host to scan: {Fore.MAGENTA}'))
        FromPort = int(input(f'{Fore.LIGHTWHITE_EX}From port: {Fore.LIGHTMAGENTA_EX}'))
        UpPort = int(input(f'{Fore.LIGHTWHITE_EX}Up port: {Fore.LIGHTMAGENTA_EX}'))+1
        RemoteServerIP = socket.gethostbyname(RemoteServer)

        os.system('cls || clear')
        main()
        print (Fore.LIGHTWHITE_EX + '-'* 60)
        print (f'Please wait for scan host {RemoteServer}')
        print ('-'* 60)

        OpenPortList = []
        start = datetime.now()
        try:
            for port in range(FromPort,UpPort):  
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                result = sock.connect_ex((RemoteServerIP, port))
                if result == 0:
                    print(f'{Fore.LIGHTWHITE_EX}Port {port}: {Fore.LIGHTGREEN_EX}Open{Fore.RESET}')
                    OpenPortList.append(port)            
                else:
                    print(f'{Fore.LIGHTWHITE_EX}Port {port}:    {Fore.LIGHTRED_EX}Close{Fore.RESET}')
                sock.close()

        except KeyboardInterrupt:
            print (f'{Fore.LIGHTYELLOW_EX}\nYou pressed Ctrl+C{Fore.RESET}')
            sys.exit()

        except socket.gaierror:
            print(f'{Fore.LIGHTRED_EX}Hostname could not be resolved...Exiting{Fore.RESET}')
            sys.exit()

        except socket.error:
            print(f'{Fore.LIGHTRED_EX}Could not connect to server{Fore.RESET}')
            sys.exit()

        finish = datetime.now()
        total =  finish - start

        print(f'{Fore.LIGHTWHITE_EX}Scanning Completed in: {Fore.LIGHTGREEN_EX}{total}{Fore.RESET}')
        time.sleep(3)
    except:
        print(Fore.RED +'Error!'+ Fore.RESET)
        time.sleep(2)
    MainScript()

def PortScanner2():
    try:
        RemoteServer = input(str(f'{Fore.LIGHTWHITE_EX}Enter a remote host to scan: {Fore.MAGENTA}'))
        RemoteServerIP = socket.gethostbyname(RemoteServer)

        os.system('cls || clear')
        main()
        print (Fore.LIGHTWHITE_EX + '-'* 60)
        print (f'Please wait for scan host {RemoteServer}')
        print ('-'* 60)

        OpenPortList = []
        start = datetime.now()
        try:
            for port in range(1, 65534):  
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                result = sock.connect_ex((RemoteServerIP, port))
                if result == 0:
                    print(f'{Fore.LIGHTWHITE_EX}Port {port}: {Fore.LIGHTGREEN_EX}Open{Fore.RESET}')
                    OpenPortList.append(port)            
                else:
                    print(f'{Fore.LIGHTWHITE_EX}Port {port}:    {Fore.LIGHTRED_EX}Close{Fore.RESET}')
                sock.close()

        except KeyboardInterrupt:
            print (f'{Fore.LIGHTYELLOW_EX}\nYou pressed Ctrl+C{Fore.RESET}')
            sys.exit()

        except socket.gaierror:
            print(f'{Fore.LIGHTRED_EX}Hostname could not be resolved...Exiting{Fore.RESET}')
            sys.exit()

        except socket.error:
            print(f'{Fore.LIGHTRED_EX}Could not connect to server{Fore.RESET}')
            sys.exit()

        finish = datetime.now()
        total =  finish - start

        print(f'{Fore.LIGHTGREEN_EX}Scanning Completed in: {Fore.LIGHTGREEN_EX}{total}{Fore.RESET}')
        time.sleep(3)
    except:
        print(Fore.RED +'Error!'+ Fore.RESET)
        time.sleep(2)
    MainScript()

# Get IP Address Code ...
def GetIpAddress():
    try:
        target = input(Fore.LIGHTMAGENTA_EX + '! ' + Fore.LIGHTWHITE_EX + 'Enter a target address: ' + Fore.LIGHTMAGENTA_EX)
        address = socket.gethostbyname(target)
        os.system('cls || clear')
        main()
        print(f"{Fore.LIGHTGREEN_EX}your target IP address is : {Fore.LIGHTMAGENTA_EX + address + Fore.LIGHTWHITE_EX}")
        print ('-'* 60)
        print(f'''
            {Fore.LIGHTMAGENTA_EX}1>{Fore.LIGHTWHITE_EX} Copy address to clipboard
            {Fore.LIGHTMAGENTA_EX}2>{Fore.LIGHTRED_EX} Back 
            ''')
        choice = input(f'{Fore.LIGHTWHITE_EX}Enter your choice: {Fore.LIGHTMAGENTA_EX}')
        if choice == '1':
            pyperclip.copy(address)
            os.system('cls || clear')
            main()
            print(f'{Fore.LIGHTGREEN_EX + address} Copied!')
            time.sleep(2)
    except KeyboardInterrupt:
        print (f'{Fore.LIGHTYELLOW_EX}\nYou pressed Ctrl+C{Fore.RESET}')
        sys.exit()
    except:
        print(Fore.RED +'Error!'+ Fore.RESET)
        time.sleep(2)
    MainScript()

# API alive Checker ...
def ApiAliveChecker():
    try:
        main()
        print(f'{Fore.LIGHTWHITE_EX}example: {Fore.LIGHTMAGENTA_EX}https://example.com/api/?token=233902:627a0a567ec780.50560976')
        api = input(f'! {Fore.LIGHTWHITE_EX}Enter a API address: {Fore.LIGHTMAGENTA_EX}')
        res = requests.get(api)
        if res.status_code == 200:
            os.system('cls || clear')
            main()
            print('-'*60)
            print(Fore.LIGHTGREEN_EX + 'API is alive!')
            time.sleep(2)
        else:
            os.system('cls || clear')
            main()
            print('-'*60)
            print(Fore.LIGHTRED_EX + 'error or dead')
            time.sleep(2)
    except KeyboardInterrupt:
        print (f'{Fore.LIGHTYELLOW_EX}\nYou pressed Ctrl+C{Fore.RESET}')
        sys.exit()
    except:
        print(Fore.RED +'Error!'+ Fore.RESET)
        time.sleep(2)
    MainScript()

# Admin page founder ...
def AdminPageFounder():
    main()
    target = input(Fore.LIGHTWHITE_EX + 'Enter your target address(like: example.com): '+ Fore.LIGHTMAGENTA_EX)
    print(Fore.LIGHTWHITE_EX + '-'*60)
    target_link = f'https://{target}'
    start = datetime.now()
    try:
        for root in pathes:
            req = requests.get(f'{target_link}/{root}')
            if req.status_code == 200:
                os.system('cls || clear')
                finish = datetime.now()
                total = finish - start
                main()
                print(f'{Fore.LIGHTGREEN_EX}found!{Fore.LIGHTWHITE_EX} address name is: {target_link}/{root}')
                print(f'Scanning Completed in: {Fore.LIGHTGREEN_EX}{total}')
                print(Fore.LIGHTWHITE_EX + '-'*60)
                print(f'''
                    {Fore.LIGHTMAGENTA_EX}1>{Fore.LIGHTWHITE_EX} Copy address to clipboard
                    {Fore.LIGHTMAGENTA_EX}2>{Fore.LIGHTRED_EX} Back
                    ''')
                choice = input(Fore.LIGHTWHITE_EX + 'Enter your choice: '+ Fore.LIGHTMAGENTA_EX)
                if choice == '1':
                    os.system('cls || clear')
                    main()
                    print(f'{Fore.LIGHTGREEN_EX + target_link}/{root} Copied!')
                    time.sleep(2)
                MainScript()
            else:
                print(f' {Fore.LIGHTWHITE_EX + target_link}/{root} - {Fore.LIGHTRED_EX}not found!{Fore.LIGHTWHITE_EX} trying again...')
    except KeyboardInterrupt:
        print (f'{Fore.LIGHTYELLOW_EX}\nYou pressed Ctrl+C{Fore.RESET}')
        sys.exit()
    except:
        print(Fore.RED +'Error!'+ Fore.RESET)
        time.sleep(2)
        MainScript()
# Main Script ... 
def MainScript():
    try:
        main()
        print(f'''
            {Fore.MAGENTA}1>{Fore.LIGHTWHITE_EX} Port Scanner
            {Fore.MAGENTA}2>{Fore.LIGHTWHITE_EX} Get IP Address
            {Fore.MAGENTA}3>{Fore.LIGHTWHITE_EX} API Alive Checker
            {Fore.MAGENTA}4>{Fore.LIGHTWHITE_EX} Admin page finder
            {Fore.MAGENTA}5>{Fore.RED} exit {Fore.RESET} 
            ''')
        choice = input(Fore.LIGHTWHITE_EX + 'type your choice: '+ Fore.LIGHTMAGENTA_EX)

        if choice == '1':
            main()
            print(f'''
            {Fore.MAGENTA}1>{Fore.LIGHTWHITE_EX} Personalized(choice port yourself)
            {Fore.MAGENTA}2>{Fore.LIGHTWHITE_EX} Default(scan port 1 up 65534)
            {Fore.MAGENTA}3>{Fore.LIGHTRED_EX} Back{Fore.RESET}
                ''')
            choice = input('type your cohice: ')
            
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
        elif choice == '5':
            sys.exit()
        else:
            main()
            print(f'{Fore.RED}please choice a valid number...{Fore.RESET}')
            time.sleep(2)
            MainScript()
    except KeyboardInterrupt:
        print (f'{Fore.LIGHTYELLOW_EX}\nYou pressed Ctrl+C{Fore.RESET}')
        sys.exit()
MainScript()