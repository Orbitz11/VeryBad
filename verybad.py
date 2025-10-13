from colorama import Fore, Style, init
import shutil
import time
import os

init(autoreset=True)

logo1 = r"""
 ██▒   █▓▓█████  ██▀███ ▓██   ██▓
▓██░   █▒▓█   ▀ ▓██ ▒ ██▒▒██  ██▒
 ▓██  █▒░▒███   ▓██ ░▄█ ▒ ▒██ ██░
  ▒██ █░░▒▓█  ▄ ▒██▀▀█▄   ░ ▐██▓░
   ▒▀█░  ░▒████▒░██▓ ▒██▒ ░ ██▒▓░
   ░ ▐░  ░░ ▒░ ░░ ▒▓ ░▒▓░  ██▒▒▒ 
   ░ ░░   ░ ░  ░  ░▒ ░ ▒░▓██ ░▒░ 
     ░░     ░     ░░   ░ ▒ ▒ ░░  
      ░     ░  ░   ░     ░ ░     
     ░                   ░ ░     
""".splitlines()

logo2 = r"""
 ▄▄▄▄    ▄▄▄      ▓█████▄ 
▓█████▄ ▒████▄    ▒██▀ ██▌
▒██▒ ▄██▒██  ▀█▄  ░██   █▌
▒██░█▀  ░██▄▄▄▄██ ░▓█▄   ▌
░▓█  ▀█▓ ▓█   ▓██▒░▒████▓ 
░▒▓███▀▒ ▒▒   ▓▒█░ ▒▒▓  ▒ 
▒░▒   ░   ▒   ▒▒ ░ ░ ▒  ▒ 
 ░    ░   ░   ▒    ░ ░  ░ 
 ░            ░  ░   ░    
      ░            ░      
""".splitlines()

def print_side_by_side(l1, l2, color1=Fore.RED, color2=Fore.CYAN):
    cols = shutil.get_terminal_size().columns
    max_len = max(len(l) for l in l1)
    for left, right in zip(l1, l2):
        line = color1 + left.ljust(max_len, " ") + color2 + right
        print(line.center(cols) + Style.RESET_ALL)

def print_header():
    print_side_by_side(logo1, logo2)
    time.sleep(0.5)
    info()
 
    print()  
    
def info():
    cols = shutil.get_terminal_size().columns
    block = (
        Fore.RED + Style.BRIGHT + "[ INFO ]" + Style.RESET_ALL + "\n"
        + Fore.RED + '-' + Fore.CYAN   + " Name     :                     " + Fore.RED + "VeryBad\n"
        + Fore.RED + '-' + Fore.CYAN   + " Version  :                         " + Fore.RED + "0.1\n"
        + Fore.RED + '-' + Fore.CYAN   + " Author   :                      " + Fore.RED + "Orbitz\n"
        + Fore.RED + '-'    + Fore.CYAN   + " GitHub   : " + Fore.RED + "https://github.com/Orbitz11\n"
        + Fore.RED + '-'    + Fore.CYAN   + " Email    : " + Fore.RED + "orbitz.business11@gmail.com\n"
    )

    for line in block.splitlines():
        print(line.center(cols))


if __name__ == "__main__":
    print_header()


def menu():
    while True:
        
        print(Fore.CYAN + Style.BRIGHT + '----------------------------------------------------------------------------------------------------------------------------------------------------------------------')
        print(Fore.RED + 'Choose One Of This Choices')
        print(Fore.CYAN + '----------------------------')
        print('\n')
        print('\n')
        print(Fore.RED + '[' + Fore.CYAN + '00' + Fore.RED + ']' + Fore.CYAN + ' Exit')
        print(Fore.RED + '[' + Fore.CYAN + '01' + Fore.RED + ']' + Fore.CYAN + ' commands')
        print(Fore.RED + '[' + Fore.CYAN + '02' + Fore.RED + ']' + Fore.CYAN + ' print the final script')
        print(Fore.RED + '[' + Fore.CYAN + '03' + Fore.RED + ']' + Fore.CYAN + ' reset script')
        print('\n')
        print('\n')


        choice = int(input('choose : '))

        if choice == 0:
            print('Exit Program, Good Bye\n' )
            time.sleep(3)
            break


        if choice == 1:

            print(Fore.CYAN + Style.BRIGHT + '----------------------------------------------------------------------------------------------------------------------------------------------------------------------')
            print(Fore.RED + 'Choose One Of This Commands')
            print(Fore.CYAN + '----------------------------')
            print('\n')
            print('\n')
            print(Fore.RED + '[' + Fore.CYAN + '00' + Fore.RED + ']' + Fore.CYAN + ' return back')        
            print(Fore.RED + '[' + Fore.CYAN + '01' + Fore.RED + ']' + Fore.CYAN + ' open cmd')
            print(Fore.RED + '[' + Fore.CYAN + '02' + Fore.RED + ']' + Fore.CYAN + ' open cmd as root')
            print(Fore.RED + '[' + Fore.CYAN + '03' + Fore.RED + ']' + Fore.CYAN + ' close all windows')
            print(Fore.RED + '[' + Fore.CYAN + '04' + Fore.RED + ']' + Fore.CYAN + ' restart')
            print(Fore.RED + '[' + Fore.CYAN + '05' + Fore.RED + ']' + Fore.CYAN + ' shut down')
            print(Fore.RED + '[' + Fore.CYAN + '06' + Fore.RED + ']' + Fore.CYAN + ' wallpaper change')
            print(Fore.RED + '[' + Fore.CYAN + '07' + Fore.RED + ']' + Fore.CYAN + ' print text')
            print(Fore.RED + '[' + Fore.CYAN + '08' + Fore.RED + ']' + Fore.CYAN + ' sleep time')        
            print('\n')
            print('\n')
            
            choose=int(input('choose : \n'))
            
            if choose == 0:
                print(Fore.RED + 'back')
            
            
            elif choose == 1:
                print('what you want to write in cmd ?\n')
                print('write [?] for help')
                c=input('choose :\n')
                if c == '?':

                    example=''' 
[01] ipconfig | information about your network (IP, gateway, DNS).
[02] ping | check connectivity to a host and latency.
[03] tracert | trace network route to a host.
[04] nslookup | query DNS for hostnames/IPs.
[05] netstat | show active network connections and ports.
[06] arp | view/manage ARP cache (IP ⇄ MAC).
[07] route | view/modify IP routing table.
[08] netsh | network configuration (advanced: interfaces, firewall, wlan).
[09] hostname | show the computer’s name.
[10] whoami | show current user name and groups.
[11] systeminfo | detailed system information (OS, memory, hotfixes).
[12] tasklist | list running processes.
[13] taskkill | kill a process by PID or name.
[14] sc | manage Windows services (create, start, stop).
[15] schtasks | schedule, view, or run scheduled tasks.
[16] net user | manage local user accounts (create, delete, change pw).
[17] net localgroup | manage local groups and membership.
[18] sfc /scannow | system file checker — repair corrupted system files.
[19] chkdsk | check and repair disk errors.
[20] diskpart | advanced disk/partition management (use with care).
[21] format | format a drive.
[22] dir | list files and folders in current directory.
[23] cd | change directory.
[24] md (mkdir) | make a new directory.
[25] rd (rmdir) | remove a directory (must be empty unless /s).
[26] copy | copy files.
[27] xcopy | copy files and directories (older recursive tool).
[28] robocopy | robust file copy (recommended for large/recursive copies).
[29] attrib | view/change file attributes (hidden, read-only, system).
[30] del (erase) | delete files.
[31] type | display contents of a text file.
[32] more | page through long text output.
[33] find / findstr | search text in files or command output (findstr supports regex).
[34] fc | compare two files (text/binary).
[35] assoc | view/change file association for extensions.
[36] start | open a program or new window from CMD.
[37] runas | run a program as a different user.
[38] powercfg | power settings and hibernation configuration.
[39] gpupdate | refresh Group Policy settings.
[40] gpresult | show applied Group Policy for user/computer.
[41] reg query | read registry values (also reg add / reg delete).
[42] cls | clear the screen.

                    '''
                    print(example)
                    choose1=input('do you want return back (y/n)')
                    if choose1.strip() == 'y':
                        print('back')
                    
                    elif choose1.strip() == 'n':
                        break         

                else:

                    cmd = c.strip()


                    vb_lines = (
                        'Set WshShell = CreateObject("WScript.Shell")\n'
                        f'WshShell.Run "cmd.exe /k {cmd}", 1, False\n\n'
                    )
                    if not os.path.exists('script.vbs') or os.path.getsize('script.vbs') == 0:
                        vb_lines = 'Option Explicit\n' + vb_lines
                    with open('script.vbs', 'a', encoding='utf-8') as f:
                        f.write(vb_lines)

                    print(Fore.GREEN + "Added to script.vbs:")
                    print(vb_lines)

            

            elif choose == 2:
                print('what you want to write in cmd ?\n')
                print('write [?] for help')
                c=input('choose :\n')
                if c == '?':

                    example=''' 
[01] ipconfig | information about your network (IP, gateway, DNS).
[02] ping | check connectivity to a host and latency.
[03] tracert | trace network route to a host.
[04] nslookup | query DNS for hostnames/IPs.
[05] netstat | show active network connections and ports.
[06] arp | view/manage ARP cache (IP ⇄ MAC).
[07] route | view/modify IP routing table.
[08] netsh | network configuration (advanced: interfaces, firewall, wlan).
[09] hostname | show the computer’s name.
[10] whoami | show current user name and groups.
[11] systeminfo | detailed system information (OS, memory, hotfixes).
[12] tasklist | list running processes.
[13] taskkill | kill a process by PID or name.
[14] sc | manage Windows services (create, start, stop).
[15] schtasks | schedule, view, or run scheduled tasks.
[16] net user | manage local user accounts (create, delete, change pw).
[17] net localgroup | manage local groups and membership.
[18] sfc /scannow | system file checker — repair corrupted system files.
[19] chkdsk | check and repair disk errors.
[20] diskpart | advanced disk/partition management (use with care).
[21] format | format a drive.
[22] dir | list files and folders in current directory.
[23] cd | change directory.
[24] md (mkdir) | make a new directory.
[25] rd (rmdir) | remove a directory (must be empty unless /s).
[26] copy | copy files.
[27] xcopy | copy files and directories (older recursive tool).
[28] robocopy | robust file copy (recommended for large/recursive copies).
[29] attrib | view/change file attributes (hidden, read-only, system).
[30] del (erase) | delete files.
[31] type | display contents of a text file.
[32] more | page through long text output.
[33] find / findstr | search text in files or command output (findstr supports regex).
[34] fc | compare two files (text/binary).
[35] assoc | view/change file association for extensions.
[36] start | open a program or new window from CMD.
[37] runas | run a program as a different user.
[38] powercfg | power settings and hibernation configuration.
[39] gpupdate | refresh Group Policy settings.
[40] gpresult | show applied Group Policy for user/computer.
[41] reg query | read registry values (also reg add / reg delete).
[42] cls | clear the screen.

                    '''
                    print(example)
                    choose1=input('do you want return back (y/n)')
                    if choose1.strip() == 'y':
                        print('back')
                    
                    elif choose1.strip() == 'n':
                        break         

                else:

                    cmd = c.strip()


                    vb_lines = (
                        
                        
                        'Dim sh\n'
                        f'Set sh = CreateObject("Shell.Application")\n\n'
                        f'sh.ShellExecute "cmd.exe", "/k {cmd} & pause", "", "runas", 1\n\n'
                        
                    )
                    if not os.path.exists('script.vbs') or os.path.getsize('script.vbs') == 0:
                        vb_lines = 'Option Explicit\n' + vb_lines
                    with open('script.vbs', 'a', encoding='utf-8') as f:
                        f.write(vb_lines)

                    print(Fore.GREEN + "Added to script.vbs:")
                    print(vb_lines)
                    
                    
                    
            elif choose == 3:





                    vb_lines = (
                        f'Dim sh\n\n'
                        f'Set sh = CreateObject("WScript.Shell")\n\n'
                        f'sh.Run "shutdown /l", 0, False\n\n'
                        f'End If\n\n'
                        f'Set sh = Nothing\n\n'
                    )
                    if not os.path.exists('script.vbs') or os.path.getsize('script.vbs') == 0:
                        vb_lines = 'Option Explicit\n' + vb_lines
                    with open('script.vbs', 'a', encoding='utf-8') as f:
                        f.write(vb_lines)

                    print(Fore.GREEN + "Added to script.vbs:")
                    print(vb_lines)

                 
                    choose1=input('do you want return back (y/n)')
                    if choose1.strip() == 'y':
                        print('back')
                    
                    elif choose1.strip() == 'n':
                        break       
                    
                    
            elif choose == 4:
                
                    delay= input(Fore.RED + 'Do You Want Delay ?(y/n)')
                    if delay.strip() == 'n':
                
                        vb_lines = (
                            f'Dim sh\n\n'
                            f'Set sh = CreateObject("WScript.Shell")\n\n'
                            f'sh.Run "shutdown /r /t 0", 0, False\n\n'
                            f'End If\n\n'
                            f'Set sh = Nothing\n\n'
                        )
                        if not os.path.exists('script.vbs') or os.path.getsize('script.vbs') == 0:
                            vb_lines = 'Option Explicit\n' + vb_lines
                        with open('script.vbs', 'a', encoding='utf-8') as f:
                            f.write(vb_lines)

                        print(Fore.GREEN + "Added to script.vbs:")
                        print(vb_lines)

                    
                        choose1=input('do you want return back (y/n)')
                        if choose1.strip() == 'y':
                            print('back')
                        
                        elif choose1.strip() == 'n':
                            break  
                        
                        
                        
                        
                    elif delay == 'y':
                        
                        time=int(input('delay = ? (sec)'))
                        
                        
                        vb_lines = (
                        f'Dim sh\n\n'
                        f'Set sh = CreateObject("WScript.Shell")\n\n'
                        f'sh.Run "shutdown /r /t {time}", 0, False\n\n'
                        f'End If\n\n'
                        f'Set sh = Nothing\n\n'
                        )
                        if not os.path.exists('script.vbs') or os.path.getsize('script.vbs') == 0:
                            vb_lines = 'Option Explicit\n' + vb_lines
                        with open('script.vbs', 'a', encoding='utf-8') as f:
                            f.write(vb_lines)

                        print(Fore.GREEN + "Added to script.vbs:")
                        print(vb_lines)

                    
                        choose1=input('do you want return back (y/n)')
                        if choose1.strip() == 'y':
                            print('back')
                        
                        elif choose1.strip() == 'n':
                            break  
                    
            elif choose == 5:


                    delay= input(Fore.RED + 'Do You Want Delay ?(y/n)')
                    if delay.strip() == 'n':
                
                        vb_lines = (
                            f'Dim sh\n\n'
                            f'Set sh = CreateObject("WScript.Shell")\n\n'
                            f'sh.Run "shutdown /s /t 0", 0, False\n\n'
                            f'End If\n\n'
                            f'Set sh = Nothing\n\n'
                        )
                        if not os.path.exists('script.vbs') or os.path.getsize('script.vbs') == 0:
                            vb_lines = 'Option Explicit\n' + vb_lines
                        with open('script.vbs', 'a', encoding='utf-8') as f:
                            f.write(vb_lines)

                        print(Fore.GREEN + "Added to script.vbs:")
                        print(vb_lines)

                    
                        choose1=input('do you want return back (y/n)')
                        if choose1.strip() == 'y':
                            print('back')
                        
                        elif choose1.strip() == 'n':
                            break  
                        
                        
                        
                        
                    elif delay == 'y':
                        
                        time=int(input('delay = ? (sec)'))
                        
                        
                        vb_lines = (
                        f'Dim sh\n\n'
                        f'Set sh = CreateObject("WScript.Shell")\n\n'
                        f'sh.Run "shutdown /s /t {time}", 0, False\n\n'
                        f'End If\n\n'
                        f'Set sh = Nothing\n\n'
                        )
                        if not os.path.exists('script.vbs') or os.path.getsize('script.vbs') == 0:
                            vb_lines = 'Option Explicit\n' + vb_lines
                        with open('script.vbs', 'a', encoding='utf-8') as f:
                            f.write(vb_lines)

                        print(Fore.GREEN + "Added to script.vbs:")
                        print(vb_lines)

                    
                        choose1=input('do you want return back (y/n)')
                        if choose1.strip() == 'y':
                            print('back')
                        
                        elif choose1.strip() == 'n':
                            break  
                    
                    
            elif choose == 6:
                
                path = input(Fore.RED + 'path : ')


                vb_lines = (
                    'Dim sh, fso, imgPath\n\n'
                    'Set sh = CreateObject("WScript.Shell")\n'
                    'Set fso = CreateObject("Scripting.FileSystemObject")\n\n'
                    f'imgPath = "{path}"\n\n'
                    'If fso.FileExists(imgPath) Then\n'
                    '    sh.RegWrite "HKCU\\Control Panel\\Desktop\\Wallpaper", imgPath\n'
                    '    sh.Run "RUNDLL32.EXE user32.dll,UpdatePerUserSystemParameters", 1, True\n'
                    'End If\n\n'
                    'Set sh = Nothing\n'
                    'Set fso = Nothing\n\n'
                )

                if not os.path.exists('script.vbs') or os.path.getsize('script.vbs') == 0:
                    vb_lines = 'Option Explicit\n' + vb_lines
                with open('script.vbs', 'a', encoding='utf-8') as f:
                    f.write(vb_lines)

                print(Fore.GREEN + "Added to script.vbs:")
                print(vb_lines)

                choose1 = input('do you want return back (y/n): ')
                if choose1.strip().lower() == 'y':
                    print('back')
                elif choose1.strip().lower() == 'n':
                    break



            elif choose == 7:

                    text=input(Fore.RED+'what is the text ?: ')
                    title=input(Fore.RED+'what is the title ?: ')
                    num=int(input(Fore.RED+'how many times to repeat? '))



                    vb_lines = (
                        f'Dim i\n'                        
                        f'For i = 1 To {num}\n'
                        f'    MsgBox "{text}", vbExclamation, "{title}"\n'
                        f'Next\n\n'

                                               
                    )
                    
                    
                    
                    if not os.path.exists('script.vbs') or os.path.getsize('script.vbs') == 0:
                        vb_lines = 'Option Explicit\n' + vb_lines
                    with open('script.vbs', 'a', encoding='utf-8') as f:
                        f.write(vb_lines)

                    print(Fore.GREEN + "Added to script.vbs:")
                    print(vb_lines)

                 
                    choose1=input('do you want return back (y/n)')
                    if choose1.strip() == 'y':
                        print('back')
                    
                    elif choose1.strip() == 'n':
                        break                                              
                    
                    
            elif choose == 8:


                        vb_lines = (
                            f'Dim sh\n\n'
                            f'Set sh = CreateObject("WScript.Shell")\n\n'
                            f'sh.Run "rundll32.exe powrprof.dll,SetSuspendState 0,1,0", 0, False\n\n'
                            f'Set sh = Nothing\n\n'
                        )
                        if not os.path.exists('script.vbs') or os.path.getsize('script.vbs') == 0:
                            vb_lines = 'Option Explicit\n' + vb_lines
                        with open('script.vbs', 'a', encoding='utf-8') as f:
                            f.write(vb_lines)

                        print(Fore.GREEN + "Added to script.vbs:")
                        print(vb_lines)

                    
                        choose1=input('do you want return back (y/n)')
                        if choose1.strip() == 'y':
                            print('back')
                        
                        elif choose1.strip() == 'n':
                            break       

                        
        if choice == 2:
            try:
                with open("script.vbs", "r", encoding="utf-8") as file:
                    content = file.read()
                print(Fore.GREEN + "Script content:")
                print(content)
            except FileNotFoundError:
                print(Fore.RED + "script.vbs not found.")

        if choice == 3:
            with open("script.vbs", "w", encoding="utf-8") as file:
                file.write("")
            print(Fore.GREEN + "Script reset.")









menu()
