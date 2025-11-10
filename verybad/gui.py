import shutil
import time
import os
from tkinter import *
from PIL import Image, ImageTk
from colorama import *
import webbrowser
import pyperclip
import smtplib
from email.message import EmailMessage




def Donate():
    new_win = Toplevel(window)
    new_win.title('Donate ⚡')
    new_win.geometry("700x300")
    new_win.config(bg="#1E4174")

    Label(
        new_win,
        text="⚡ Lightning Address:",
        fg="white",
        bg="#1E4174",
        font=('Arial', 14, 'bold')
    ).pack(pady=(30, 10))

    lightning_code = "lnbc1p5srrx3pp54q430fqyq77elzqrwnkxhdj98p48v4n4k32p6a2lu6fvt0mw5fwqsp5m0sfu6mcg6sw667xq0pp5f8c7nmel69mtjxazpsayfk2z2483jxqdp9235xzmntwvsyvmmjypvk7atjypzx7mnpw3jjzcqzynxq8zals8sq9qlzqqqqqqqqqqqqqqqqqqqqqqqqqqysgqxtdnpccrm5ae6qp622x4ez3jrgmg9epz8e4kkvm6ashpvfr895d496pahly7q98uz7mxzc0ule9lf3v7e00up3j828ahaxa7nks2trsqzk6wev"

    textbox = Text(
        new_win,
        font=('Consolas', 11),
        width=70,
        height=4,
        wrap="word",
        bg="#F0F0F0",
        relief="ridge",
        bd=3
    )
    textbox.insert("1.0", lightning_code)
    textbox.config(state="disabled")
    textbox.pack(pady=10)

    def copy_code():
        pyperclip.copy(lightning_code)
        messagebox.showinfo("Copied!", "⚡ Lightning address copied to clipboard!")

    Button(
        new_win,
        text="Copy Code",
        command=copy_code,
        font=('Arial', 12, 'bold'),
        fg="#1E4174",
        bg="#DDA94B",
        width=15,
        relief="raised",
        cursor="hand2"
    ).pack(pady=10)

    def copy_code():
        pyperclip.copy(lightning_code)
        messagebox.showinfo("Copied!", "⚡ Lightning address copied to clipboard!")

    copy_btn = tk.Button(
        new_win,
        text="Copy Code",
        command=copy_code,
        font=('Arial', 12, 'bold'),
        fg="#1E4174",
        bg="#DDA94B",
        width=15,
        relief="raised",
        cursor="hand2"
    )
    copy_btn.pack(pady=10)

def send():
    new_win = Toplevel(window)
    new_win.title('Contact Me')
    new_win.geometry("700x300")
    new_win.config(bg="#1E4174")

    Label(new_win, text="From (your email):", fg="white", bg="#1E4174", font=('Arial', 12)).place(x=20, y=20)
    entry_sender = Entry(new_win, font=('Arial', 14), width=40)
    entry_sender.place(x=20, y=50)
    entry_sender.insert(0, "example@domain.test")

    Label(new_win, text="Subject:", fg="white", bg="#1E4174", font=('Arial', 12)).place(x=20, y=95)
    entry_subj = Entry(new_win, font=('Arial', 14), width=40)
    entry_subj.place(x=20, y=125)
    entry_subj.insert(0, "Test from Mailtrap")

    log = Text(new_win, width=80, height=6, font=('Arial', 10))
    log.place(x=20, y=170)

    def send_via_mailtrap_local():
        sender = entry_sender.get().strip()
        if not sender:
            log.insert(END, "Please enter a sender email.\n")
            return

        recipient = "orbitz.business11@gmail.com"
        subject = entry_subj.get().strip() or "No subject"
        body = "This is a test message sent via Mailtrap (sandbox)."

        MAIL_HOST = "sandbox.smtp.mailtrap.io"
        MAIL_PORT = 2525
        MAIL_USER = "d6c0584c440e5d"
        MAIL_PASS = "019de0cf2be92a"

        if not (MAIL_HOST and MAIL_USER and MAIL_PASS):
            log.insert(END, "Mailtrap not configured. Set MAILTRAP_HOST/PORT/USER/PASS env vars.\n")
            return

        msg = EmailMessage()
        msg["From"] = sender
        msg["To"] = recipient
        msg["Subject"] = subject
        msg.set_content(body)

        try:
            with smtplib.SMTP(MAIL_HOST, MAIL_PORT, timeout=10) as server:
                server.starttls()
                server.login(MAIL_USER, MAIL_PASS)
                server.send_message(msg)
            log.insert(END, f" Message sent from {sender} → {recipient}\n")
        except Exception as e:
            log.insert(END, f" Send failed: {e}\n")


    send_btn = Button(
        new_win,
        text="Send (Mailtrap)",
        command=send_via_mailtrap_local,
        font=('Arial', 12, 'bold'),
        fg="#1E4174",
        bg="#DDA94B",
        width=18
    )
    send_btn.place(x=500, y=30)

 
    insta_btn = Button(
        new_win,
        text="Instagram",
        command=lambda: webbrowser.open("https://www.instagram.com/orbitz_11?igsh=MXVhczdmaGZiczRvdg=="),
        font=('Arial', 12, 'bold'),
        fg="white",
        bg="#E1306C",
        width=18
    )
    insta_btn.place(x=500, y=80)


    tiktok_btn = Button(
        new_win,
        text="TikTok",
        command=lambda: webbrowser.open("https://www.tiktok.com/@orbitz_115?_r=1&_t=ZS-91ExTHP2k9F"),
        font=('Arial', 12, 'bold'),
        fg="white",
        bg="#000000",
        width=18
    )
    tiktok_btn.place(x=500, y=130)

    



def info():
    new_win = Toplevel(window)
    new_win.title('Info About Me')
    new_win.geometry("700x500")
    new_win.config(bg="#1E4174")


    label = Label(new_win, 
                  text='Info About Me',
                  font=('Arial', 25, 'bold'),
                  fg="white", 
                  bg="#1E4174")
    label.pack(pady=20)


    info_text = """I’m a cybersecurity enthusiast passionate about ethical hacking, 
digital forensics, and system protection. 
I specialize in identifying vulnerabilities, securing networks, 
and testing systems to strengthen their defenses. 
My goal is to continuously improve my skills 
and help build safer digital environments."""


    text_box = Text(new_win, 
                    font=('Arial', 14), 
                    fg="#DDA94B", 
                    bg="#1E4174",
                    wrap=WORD,
                    width=60, 
                    height=10,
                    bd=0)
    text_box.insert(END, info_text)
    text_box.config(state=DISABLED) 
    text_box.pack(pady=10)

 
    close_button = Button(new_win,
                          text="Close",
                          command=new_win.destroy,
                          font=('Arial', 15, 'bold'),
                          fg="#1E4174",
                          bg="#DDA94B",
                          width=10,
                          height=1)
    close_button.pack(pady=20)

def Try():
    os.startfile("script.vbs")    

def reset():
            with open("script.vbs", "w", encoding="utf-8") as file:
                file.write("")
            textbox.delete("1.0", "end")
            print(Fore.GREEN + "Script reset.")
    
def Star():
    webbrowser.open_new_tab("https://github.com/Orbitz11/VeryBad")

def cmd():
    cmd = entry.get()

    vb_lines = (
        'Set WshShell = CreateObject("WScript.Shell")\n'
        f'Dim WshShell\n\n'        
        f'WshShell.Run "cmd.exe /k {cmd}", 1, False\n\n'
    )
    if not os.path.exists('script.vbs') or os.path.getsize('script.vbs') == 0:
        vb_lines = 'Option Explicit\n' + vb_lines
    with open('script.vbs', 'a', encoding='utf-8') as f:
        f.write(vb_lines)

        print(Fore.GREEN + "Added to script.vbs:")
        print(vb_lines)
        
    textbox.insert(END, vb_lines) 
    textbox.see(END) 
    
def cmd_root():    
                    cmd = entry.get()


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

                    textbox.insert(END, vb_lines) 
                    textbox.see(END) 

def closewin():
                    vb_lines = (
                        f'Dim sh\n\n'
                        f'Set sh = CreateObject("WScript.Shell")\n\n'
                        f'sh.Run "shutdown /l", 0, False\n\n'
                        f'Set sh = Nothing\n\n'
                    )
                    if not os.path.exists('script.vbs') or os.path.getsize('script.vbs') == 0:
                        vb_lines = 'Option Explicit\n' + vb_lines
                    with open('script.vbs', 'a', encoding='utf-8') as f:
                        f.write(vb_lines)

                    print(Fore.GREEN + "Added to script.vbs:")
                    print(vb_lines)

                    textbox.insert(END, vb_lines) 
                    textbox.see(END)
                    
def shutdown():
                    vb_lines = (
                        f'Dim sh\n\n'
                        f'Set sh = CreateObject("WScript.Shell")\n\n'
                        f'sh.Run "shutdown /s /t 0", 0, False\n\n'
                        f'Set sh = Nothing\n\n'
                    )
                    if not os.path.exists('script.vbs') or os.path.getsize('script.vbs') == 0:
                        vb_lines = 'Option Explicit\n' + vb_lines
                    with open('script.vbs', 'a', encoding='utf-8') as f:
                            f.write(vb_lines)

                    print(Fore.GREEN + "Added to script.vbs:")
                    print(vb_lines)

                    textbox.insert(END, vb_lines) 
                    textbox.see(END)
                    
def wallpaper():
            path = entry.get()


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

                textbox.insert(END, vb_lines) 
                textbox.see(END)               
def restart():
                        vb_lines = (
                            f'Dim sh\n\n'
                            f'Set sh = CreateObject("WScript.Shell")\n\n'
                            f'sh.Run "shutdown /r /t 0", 0, False\n\n'
                            f'Set sh = Nothing\n\n'
                        )
                        if not os.path.exists('script.vbs') or os.path.getsize('script.vbs') == 0:
                            vb_lines = 'Option Explicit\n' + vb_lines
                        with open('script.vbs', 'a', encoding='utf-8') as f:
                            f.write(vb_lines)

                        print(Fore.GREEN + "Added to script.vbs:")
                        print(vb_lines)
                
                        textbox.insert(END, vb_lines) 
                        textbox.see(END)
def text():
                    all=entry.get()
                    text, title, num =all.split(',')
                    num=int(num)
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
                  
                    textbox.insert(END, vb_lines) 
                    textbox.see(END)
                                    
def sleeptime():
                        sleep=int(entry.get())
                        sleep=sleep*1000
                        vb_lines = (
                            f'WScript.Sleep {sleep}\n\n'

                        )
                        if not os.path.exists('script.vbs') or os.path.getsize('script.vbs') == 0:
                            vb_lines = 'Option Explicit\n' + vb_lines
                        with open('script.vbs', 'a', encoding='utf-8') as f:
                            f.write(vb_lines)

                        print(Fore.GREEN + "Added to script.vbs:")
                        print(vb_lines)
                        
                        textbox.insert(END, vb_lines) 
                        textbox.see(END)

def Copy():
    with open("script.vbs", "r", encoding="utf-8") as f:
        content = f.read()
        pyperclip.copy(content)    
                           
#main window                       
window = Tk()     
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()                    
window.geometry(f"1366x768")     
window.title('gui')            
# icon = PhotoImage(file='very bad.png')
# window.iconphoto(True ,icon)
window.config(background="#1E4174")

#entry
entry = Entry(window,
              font=('Arial', 30),
              width=23
              )


entry.place(x=15, y=100)

#buttons
cmd=Button(window,
              text='cmd',
              command=cmd,
              font=('Arial',20,'bold'),
              fg="#1E4174",
              bg='#DDA94B',
            #   relief='groove',
            #   bd=10,
              activebackground='#1E4174',
              activeforeground='#DDA94B',
              width=13,
              height=1
              )

cmd.place(x=15, y=170)

cmdroot = Button(
                window,
                text='cmd as root',
                command=cmd_root, 
                font=('Arial', 20, 'bold'),
                fg="#1E4174",
                bg='#DDA94B',
                # relief='groove',
                # bd=10,
                activebackground='#1E4174',
                activeforeground='#DDA94B',
                width=13,
                height=1
                )

cmdroot.place(x=295, y=170)

wallpaper = Button(
                window,
                text='Wallpaper change',
                command=wallpaper, 
                font=('Arial', 20, 'bold'),
                fg="#1E4174",
                bg='#DDA94B',
                # relief='groove',
                # bd=10,
                activebackground='#1E4174',
                activeforeground='#DDA94B',
                width=13,
                height=1
                )

wallpaper.place(x=15, y=260)

shutdown = Button(
                window,
                text='Shut down',
                command=shutdown, 
                font=('Arial', 20, 'bold'),
                fg="#1E4174",
                bg='#DDA94B',
                # relief='groove',
                # bd=10,
                activebackground='#1E4174',
                activeforeground='#DDA94B',
                width=13,
                height=1
                )

shutdown.place(x=295, y=260)

restart = Button(
                window,
                text='restart',
                command=restart, 
                font=('Arial', 20, 'bold'),
                fg="#1E4174",
                bg='#DDA94B',
                # relief='groove',
                # bd=10,
                activebackground='#1E4174',
                activeforeground='#DDA94B',
                width=13,
                height=1
                )

restart.place(x=15, y=350)

text = Button(
                window,
                text='Print Text',
                command=text, 
                font=('Arial', 20, 'bold'),
                fg="#1E4174",
                bg='#DDA94B',
                # relief='groove',
                # bd=10,
                activebackground='#1E4174',
                activeforeground='#DDA94B',
                width=13,
                height=1
                )

text.place(x=295, y=350)

sleeptime = Button(
                window,
                text='Sleep Time',
                command=sleeptime, 
                font=('Arial', 20, 'bold'),
                fg="#1E4174",
                bg='#DDA94B',
                # relief='groove',
                # bd=10,
                activebackground='#1E4174',
                activeforeground='#DDA94B',
                width=13,
                height=1
                )

sleeptime.place(x=295, y=435)

closewind = Button(
                window,
                text='Close all windows',
                command=closewin, 
                font=('Arial', 20, 'bold'),
                fg="#1E4174",
                bg='#DDA94B',
                # relief='groove',
                # bd=10,
                activebackground='#1E4174',
                activeforeground='#DDA94B',
                width=13,
                height=1
                )

closewind.place(x=15, y=435)

soon1 = Button(
                window,
                text='Soon', 
                font=('Arial', 20, 'bold'),
                fg="#1E4174",
                bg='#DDA94B',
                # relief='groove',
                # bd=10,
                activebackground='#1E4174',
                activeforeground='#DDA94B',
                width=13,
                height=1
                )

soon1.place(x=295, y=527)

soon2 = Button(
                window,
                text='Soon', 
                font=('Arial', 20, 'bold'),
                fg="#1E4174",
                bg='#DDA94B',
                # relief='groove',
                # bd=10,
                activebackground='#1E4174',
                activeforeground='#DDA94B',
                width=13,
                height=1
                )

soon2.place(x=15, y=527)

Version=Button(
              window,
              text='Version : 0.1',
              font=('Arial',20,'bold'),
              fg="#1E4174",
              bg='#DDA94B',
            #   relief='groove',
            #   bd=10,
              activebackground='#1E4174',
              activeforeground='#DDA94B',
              width=25,
              height=1
              )

Version.place(x=15, y=20)

star=Button(
              window,
              text='Star On Github',
              command=Star,
              font=('Arial',20,'bold'),
              fg="#1E4174",
              bg='#DDA94B',
            #   relief='groove',
            #   bd=10,
              activebackground='#1E4174',
              activeforeground='#DDA94B',
              width=25,
              height=1
              )

star.place(x=463, y=20)

c=Button(
              window,
              text='Created by: Orbitz',
              command=info,
              font=('Arial',20,'bold'),
              fg="#1E4174",
              bg='#DDA94B',
              activebackground='#1E4174',
              activeforeground='#DDA94B',
              width=25,
              height=1
              )

c.place(x=910, y=20)

Reset=Button(
              window,
              text='Reset Script',
              command=reset,
              font=('Arial',20,'bold'),
              fg="#1E4174",
              bg='#DDA94B',
            #   relief='groove',
            #   bd=10,
              activebackground='#1E4174',
              activeforeground='#DDA94B',
              width=14,
              height=1
              )

Reset.place(x=1097, y=600)

copy=Button(
              window,
              text='Copy Script',
              command=Copy,
              font=('Arial',20,'bold'),
              fg="#1E4174",
              bg='#DDA94B',
            #   relief='groove',
            #   bd=10,
              activebackground='#1E4174',
              activeforeground='#DDA94B',
              width=14,
              height=1
              )

copy.place(x=545, y=600)

Try=Button(
              window,
              text='Try',
              command=Try,
              font=('Arial',20,'bold'),
              fg="#1E4174",
              bg='#DDA94B',
            #   relief='groove',
            #   bd=10,
              activebackground='#1E4174',
              activeforeground='#DDA94B',
              width=14,
              height=1
              )

Try.place(x=820, y=600)

contact=Button(
              window,
              text='Contact Me',
              command=send,
              font=('Arial',20,'bold'),
              fg="#1E4174",
              bg='#DDA94B',
            #   relief='groove',
            #   bd=10,
              activebackground='#1E4174',
              activeforeground='#DDA94B',
            #   width=46,
              height=1
              )

contact.place(x=545, y=670, width=800)

donate=Button(
              window,
              text='Donate',
              command=Donate,
              font=('Arial',20,'bold'),
              fg="#1E4174",
              bg='#DDA94B',
            #   relief='groove',
            #   bd=10,
              activebackground='#1E4174',
              activeforeground='#DDA94B',
            #   height=3
              )

donate.place(x=15, y=600, width=514, height=125)
#text box
textbox=Text(window,
             font=('Arial', 20, 'bold'),
             width=53,
             height=15

            )

textbox.place(x=545, y=100)

window.mainloop()
