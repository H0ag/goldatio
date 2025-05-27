# Importing libraries and insert in the terminal, what I'm importing for all modules

print("Loading datetime module...")
import datetime                                                                                                                                 #<-- importing datetime to get the local time
print(f"[{str(datetime.datetime.now().hour).zfill(2)}:{str(datetime.datetime.now().minute).zfill(2)}] Loading Time module...")
import time                                                                                                                                     #<-- Importing time to make pause in the program
print(f"[{str(datetime.datetime.now().hour).zfill(2)}:{str(datetime.datetime.now().minute).zfill(2)}] Loading Tkinter module...")
from tkinter import *                                                                                                                           #<-- Importing tkinter to make the GUI (Graphic User Interface)
print(f"[{str(datetime.datetime.now().hour).zfill(2)}:{str(datetime.datetime.now().minute).zfill(2)}] Loading Tkinter.scrolledtext module...")
from tkinter import scrolledtext                                                                                                                #<-- Importing scrolledtext from tkinter to make the text area
print(f"[{str(datetime.datetime.now().hour).zfill(2)}:{str(datetime.datetime.now().minute).zfill(2)}] Loading Tkinter.messagebox module...")
from tkinter import messagebox                                                                                                                  #<-- Importing messagebox from tkinter to show error message for example or info message...
print(f"[{str(datetime.datetime.now().hour).zfill(2)}:{str(datetime.datetime.now().minute).zfill(2)}] Loading Tkinter.filedialog module...")
from tkinter import filedialog                                                                                                                  #<-- Importing filedialog from tkinter to request to User to insert a file dest
print(f"[{str(datetime.datetime.now().hour).zfill(2)}:{str(datetime.datetime.now().minute).zfill(2)}] Loading Wikipedia module...")
import wikipedia                                                                                                                                #<-- Importing wikipedia to make the search
print(f"[{str(datetime.datetime.now().hour).zfill(2)}:{str(datetime.datetime.now().minute).zfill(2)}] Loading Paperclip module...")
import pyperclip                                                                                                                                #<-- Importing paperclip to copy some text in the clipboard
print(f"[{str(datetime.datetime.now().hour).zfill(2)}:{str(datetime.datetime.now().minute).zfill(2)}] Loading Googletrans module...")
from googletrans import Translator                                                                                                              #<-- Importing translator to translate the result in english
print(f"[{str(datetime.datetime.now().hour).zfill(2)}:{str(datetime.datetime.now().minute).zfill(2)}] Loading os module...")
import os                                                                                                                                       #<-- Importing os to check if some dir exist like appdata...
print(f"[{str(datetime.datetime.now().hour).zfill(2)}:{str(datetime.datetime.now().minute).zfill(2)}] Loading cv2 module...")
import cv2                                                                                                                                      #<-- Importing cv2 to play video
print(f"[{str(datetime.datetime.now().hour).zfill(2)}:{str(datetime.datetime.now().minute).zfill(2)}] Loading socket module...")
import socket                                                                                                                                   #<-- Importing socket to send mails
print(f"[{str(datetime.datetime.now().hour).zfill(2)}:{str(datetime.datetime.now().minute).zfill(2)}] Loading smtplib module...")
import smtplib                                                                                                                                  #<-- Importing smtplib to send the mail
print(f"[{str(datetime.datetime.now().hour).zfill(2)}:{str(datetime.datetime.now().minute).zfill(2)}] Loading email.message module...")
from email.message import EmailMessage                                                                                                          #<-- Importing EmailMessage to send the mail
print(f"[{str(datetime.datetime.now().hour).zfill(2)}:{str(datetime.datetime.now().minute).zfill(2)}] Loading webbrowser module...\n\n\n")      
import webbrowser                                                                                                                               #<-- Importing webbrowser to send the user in a web page (instgram)


MYDIR = ("Appdata")                                                                                                                             #<-- Define "appdata"
print(f"[{str(datetime.datetime.now().hour).zfill(2)}:{str(datetime.datetime.now().minute).zfill(2)}] Checking if appdata dir existing")        #<-- Insert in the terminal "checking if the dir is existing" to informing the user.
CHECK_MY_FOLDER = os.path.isdir(MYDIR)

def instaperso():                                                                                                                               #<-- create a function to assign with command to send the user in my personal instagram account    
    webbrowser.open_new("https://www.instagram.com/malel_____/")                                                                                #<-- Open the web with my page

def instapro():                                                                                                                                 #<-- create a function to assign with a command to send the user in the goldatio instagram account
    webbrowser.open_new("https://www.instagram.com/goldati0/")                                                                                  #<-- Open the web with the goldatio page

def aboutapp():                                                                                                                                 #<-- Create a function to insert the documentation in the text area
    search_bar.delete(0, END)                                                                                                                   #<-- Delete the content of the search bar
    search_bar.insert(INSERT, "Documentation")                                                                                                  #<-- Insert in the search bar "Documentation"
    text_area.delete('1.0', END)                                                                                                                #<-- Delete the content of the text area
    text_area.insert(INSERT,                                                                                                                    #<-- Insert the doc content is the text area
    """
============= Documentation =============
This application is made to make your 
life easier This app interface was         
made with python's tkinter module.
You can see above a searchbar
(to do your research 🙃😂) below the        
button to search assign to the <return>
button, then above a text field to 
display you your search result. And above
a button to if you wish, copy the result 
to your clipboard

    """
    )

def email_alert(subject, body, to):                                                                                                             #<-- Create the function to send the mail
    msg = EmailMessage()                                                                                                                        #<-- define msg (shortcut to say EmailMessage)
    msg.set_content(body)                                                                                                                       #<-- Set what's the content of the mail
    msg['subject'] = subject                                                                                                                    #<-- Set the subject of the mail
    msg['to'] = to                                                                                                                              #<-- Set to dest of the mail

    user = "goldatio.prod@gmail.com"                                                                                                            #<-- starting the smtp server with defining the mail who send the mail
    msg['from'] = user                                                                                                                          #<-- So... set the mail sender
    password = "icfgnulneoywuzkk"                                                                                                               #<-- And set the secret key for send a mail with a prog

    server = smtplib.SMTP("smtp.gmail.com", 587)                                                                                                #<-- Setting the smtp server
    server.starttls()
    server.login(user, password)                                                                                                                #<-- show to the server what's the user, and the password
    server.send_message(msg)                                                                                                                    #<-- And finaly, send the mail

    server.quit()                                                                                                                               #<-- Close the server

    messagebox.showinfo("Sent!", "Goldatio can comfirm you, that your mail has been transmeted to the customer.")                               #<-- Create a message to say to the user that the mail has been transmated

def email_writing():                                                                                                                            #<-- Create the function to check if the mail is correct (check if the mail has content...)
    email = username_entry.get()                                                                                                                #<-- Get the content of the dest and assign it in a variable
    subject = subject_entry.get()                                                                                                               #<-- Get the subject of the mail and assign it in a variable
    content = content_area.get('1.0', END)                                                                                                      #<-- Get the content of the mail and assign it in a variable
    email_content_len = len(email)                                                                                                              #<-- Get the number of caracteres of the content
    subject_content_len = len(subject)                                                                                                          #<-- Get the number of caractere of the subject
    if email_content_len > 1 and subject_content_len > 1:                                                                                       #<-- If the number of caractere of the content and the subject are > 1, pass to the next, else show an error message
        if email.endswith("@gmail.com"):                                                                                                        #<-- If the end of the email, end with "@gmail.com" pass to the next, else, show an error message
            email_alert(subject, content, email)                                                                                                #<-- Because all the criteria are good, then call the function to send the above mail 
        else:
            messagebox.showerror('missing information', 'Please insert "@gmail.com" at the end of your email address')
    else:
        messagebox.showerror('Complete fields', "Oops... plz complete all fields before submit.")


def email_writing_event(event):                                                                                                                 #<-- Create the same function to send the mail, but now to work with <return> touch
    email = username_entry.get()                                                                                                                #<-- Get the content of the dest and assign it in a variable
    password = password_entry.get()                                                                                                             #<-- Get the subject of the mail and assign it in a variable
    content = content_area.get('1.0', END)                                                                                                      #<-- Get the content of the mail and assign it in a variable
    email_content_len = len(email)                                                                                                              #<-- Get the number of caracteres of the content
    password_content_len = len(password)                                                                                                        #<-- Get the number of caractere of the subject
    if email_content_len > 1 and password_content_len > 1:                                                                                      #<-- If the number of caractere of the content and the subject are > 1, pass to the next, else show an error message
        if email.endswith("@gmail.com"):                                                                                                        #<-- If the end of the email, end with "@gmail.com" pass to the next, else, show an error message          
            email_alert(password, content, email)                                                                                               #<-- Because all the criteria are good, then call the function to send the above mail 
        else:
            messagebox.showerror('missing information', 'Please insert "@gmail.com" at the end of your email address')
    else:
        messagebox.showerror('Complete fields', "Oops... plz complete all fields before submit.")

def test_connection():                                                                                                                          #<-- Create a function, to check if the machine is connected
    print(f"[{str(datetime.datetime.now().hour).zfill(2)}:{str(datetime.datetime.now().minute).zfill(2)}] Checking connection")                 #<-- Insert in the terminal "checking connection", to informing the user
    try:                                                                                                                                        #<-- Try to connect to google, if it work, you're connected, else, you're not
        socket.create_connection(('Google.com', 80))
        return True
    except OSError:
        return False

result_connection = test_connection()                                                                                                           #<-- Assign "result_connection" to test_connection(to run the function)

if result_connection == True:                                                                                                                   #<-- If the result is True, you're connected, else, you're not...
    pass
else:
    yesno = messagebox.askyesno("Connection", "You're not online!\nDo you want continue?")                                                      #<-- If the result is False, ask to the user, if he want continue
    if yesno == True:                                                                                                                           #<-- If the user say "yes", the app will continue to run
        print(f"[{str(datetime.datetime.now().hour).zfill(2)}:{str(datetime.datetime.now().minute).zfill(2)}] Connnection True")                #<-- Insert in the terminal, "Connection True"
    else:                                                                                                                                       #<-- Else, the app will be closed
        print(f"[{str(datetime.datetime.now().hour).zfill(2)}:{str(datetime.datetime.now().minute).zfill(2)}] Connection False")                #<-- Insert in the terminal "Connection False"
        time.sleep(2)                                                                                                                           #<-- Wait 2 seconds with the module time
        exit()                                                                                                                                  #<-- Close the app

if not CHECK_MY_FOLDER:                                                                                                                         #<-- check if de folder is existing, else, create it
    os.makedirs(MYDIR)                                                                                                                          #<-- Create it
else:
    pass


translator = Translator()                                                                                                                       #<-- Define Tranlator, in translator

def aboutme():                                                                                                                                  #<-- Create the function "About me", to show to the user, who I am
    messagebox.showinfo("About me", """My name's Mael, I'm 14, I'm french\n
                                       I program now since ~1 years ago.\n\n
                                       Instagram (Personal): https://www.instagram.com/malel_____/\n
                                       Instagram (Goldatio): https://www.instagram.com/goldati0/\n
                                       """)                                                                                                     #<-- Create a messagebox

print(f"[{str(datetime.datetime.now().hour).zfill(2)}:{str(datetime.datetime.now().minute).zfill(2)}] Creating window")                         #<-- Insert in the terminal "Creating window"
root = Tk()                                                                                                                                     #<-- Create the window
root.title('Goldatio')                                                                                                                          #<-- Define the title of the window
root.geometry('350x350')                                                                                                                        #<-- Set the geometry of the window
root.resizable(0, 0)                                                                                                                            #<-- Make the window unresizable
root.config(bg='#A89331')                                                                                                                       #<-- Set the background color of the window
root.iconbitmap("icons/logoPNGico.ico")                                                                                                         #<-- Define the icon of the window

def change_size():                                                                                                                              #<-- Create a function to change the geometry of the window, when the user want
    win_size_width = root.winfo_width()                                                                                                         #<-- Get the width size of the window
    win_size_height = root.winfo_height()                                                                                                       #<-- Get the hight size of the window

    if win_size_width == 350 and win_size_height == 350:                                                                                        #<-- If the geometry is = to 350x350 size up the window and the fonts size
        print(f"[{str(datetime.datetime.now().hour).zfill(2)}:{str(datetime.datetime.now().minute).zfill(2)}] Changing geometry...")            #<-- Insert in the terminal "Changing geometry" to informing the user
        root.geometry('720x550')                                                                                                                #<-- Set the geometry of the window to 720x550
        search_bar.config(font=("Arial", 15))                                                                                                   #<-- Change the font size of the search bar
        text_area.config(font=("Arial", 15))                                                                                                    #<-- Change the font size of the text area
        copy_button.config(font=("Arial", 15, "bold"))                                                                                          #<-- Change the font size of the copy button
        search_buttton.config(font=("Arial", 15, "bold"))                                                                                       #<-- Change the font size of the search button
    else:                                                                                                                                       #<-- ELSE, so if the geometry is not = to 350x350 it should be 750x550, so size down the geometry of the window
        print(f"[{str(datetime.datetime.now().hour).zfill(2)}:{str(datetime.datetime.now().minute).zfill(2)}] Changing geometry...")            #<-- Insert in the terminal "changing geometry"
        root.geometry('350x350')                                                                                                                #<-- Set the geometry of the window to 350x350
        search_bar.config(font=("Arial", 10))                                                                                                   #<-- Change the font size of the search bar
        text_area.config(font=("Arial", 10))                                                                                                    #<-- Change the font size of the text area
        copy_button.config(font=("Arial", 10, "bold"))                                                                                          #<-- Change the font size of the copy button
        search_buttton.config(font=("Arial", 10, "bold"))                                                                                       #<-- Change the font size of the search button

def onOpen():                                                                                                                                   #<-- Create a function to ask to the user file he want open, and open it
    print(f"[{str(datetime.datetime.now().hour).zfill(2)}:{str(datetime.datetime.now().minute).zfill(2)}] Opening file")                        #<-- Insert in the terminal "Opening file"
    filename = filedialog.askopenfilename(initialdir="/", title="Lets open file", filetypes=(("Text Files", ".txt"), ("All Files", "*.*")))     #<-- Ask to the user what file he want open
    try:                                                                                                                                        #<-- Try to open the file and read it
        myfile = open(filename, "r")                                                                                                            #<-- opening file
        text_area.delete('1.0', END)                                                                                                            #<-- Delete the content of the text area
        text_area.insert(INSERT, myfile.read())                                                                                                 #<-- Insert in the text area the content of the file opened
    except:                                                                                                                                     #<-- if the file doen't exist, make an error message
        print(f"""[{str(datetime.datetime.now().hour).zfill(2)}:{str(datetime.datetime.now().minute).zfill(2)}] Error... 
                                                                                                                Emplacement doesn't exist...""")
    

def onSave():                                                                                                                                   #<-- Create a function to ask to the user where he want save the file.txt
    print(f"[{str(datetime.datetime.now().hour).zfill(2)}:{str(datetime.datetime.now().minute).zfill(2)}] Saving file...")                      #<-- Insert in the terminal "Saving file"
    saveas = filedialog.asksaveasfilename(initialdir = "/",title = "Save as",filetypes = (("Text Files","*.txt"), ("All files","*.*")))         #<-- Ask to the user where he want save the file
    saveas_len = len(saveas)                                                                                                                    #<-- Get number of caractere of the location, and, if it > 1, pass to the next, else, error message
    if saveas_len > 1:                                                                                                                          #<-- If numbers of characteres are > 1 pass to tye next
        try:                                                                                                                                    #<-- Try to save the file
            content = text_area.get("1.0", END)                                                                                                 #<-- Get the content of the text_area
            save = open(f"{saveas}.txt", 'w+', encoding='UTF-8')                                                                                #<-- Create a txt file where the user want, and write the content of the text_area
            save.write(content)                                                                                                                 #<-- Write in the file the content of the text area
            messagebox.showinfo('Saved Goldatio', f'File has been saved: {saveas}.txt')                                                         #<-- When the file is saved, show an info message, that the file has been saved where the user wanted.
            print(f"[{str(datetime.datetime.now().hour).zfill(2)}:{str(datetime.datetime.now().minute).zfill(2)}] File has been saved: {saveas}.txt")#Insert in the terminal, "File saved: ~~~~~~~~.txt"
        except:                                                                                                                                 #<-- If the location doen't exist...
            print(f"[{str(datetime.datetime.now().hour).zfill(2)}:{str(datetime.datetime.now().minute).zfill(2)}] Oops it seems that an error has occurred.\n Try to define your extension...")#Insert in the termianal, "Oops..."
            messagebox.showerror('Error Goldatio', 'Oops it seems that an error has occurred.\n Try to define your extension...')               #<-- make an error message
    else:
        pass

def on_enter(e):                                                                                                                                #<-- Create a function, when the mouse is hover a button, change the background color of the button
    valid_button['background'] = '#402414'                                                                                                      #<-- Get the valid button with the properti 'background', and set the background to: #402414

def on_leave(e):                                                                                                                                #<-- Create a function, when the mouse is not hever a button, chnage the background color 
    valid_button['background'] = '#6e3e22'                                                                                                      #<-- Get the valid button with the properti 'background', and set the background to: #6e3e22

def send():                                                                                                                                     #<-- Create a function, with the GUI to send the mail
    global username_entry                                                                                                                       #<-- share the username_entry
    global subject_entry                                                                                                                        #<-- share the subject entry
    global valid_button                                                                                                                         #<-- share the valid button
    global content_area                                                                                                                         #<-- share the content area

    print(f"[{str(datetime.datetime.now().hour).zfill(2)}:{str(datetime.datetime.now().minute).zfill(2)}] Sending window opened...")            #<-- Insert in the terminal "sending window opened..."

    text_to_insert = text_area.get('1.0', END)                                                                                                  #<-- Get the content of the text area
    subject = search_bar.get()                                                                                                                  #<-- Get the content of the search bar

    rot = Toplevel(root)                                                                                                                        #<-- Define the new root (Top level(popup))
    rot.title("Send Email")                                                                                                                     #<-- Set the title of the new root
    rot.geometry("500x400")                                                                                                                     #<-- Set the geometry of the new root
    rot.resizable(0, 0)                                                                                                                         #<-- Make the window unresizable
    rot.config(bg="#A89331")                                                                                                                    #<-- Set the background color of the new root
    rot.iconbitmap("icons/logoPNGico.ico")                                                                                                      #<-- Set the icon of the new root

    username_label = Label(rot, bg='#A89331', font=('Arial', 10, "bold"), text="To")                                                            #<-- Create the username label (text)
    username_label.place(x=380, y=30)                                                                                                           #<-- place the label on the window

    username_entry = Entry(rot, bg='#6e3e22', font=('Arial', 15, 'bold'), width=30)                                                             #<-- Create the username entry (input field)
    username_entry.place(x=30, y=30)                                                                                                            #<-- Place the entry on the window

    subject_label = Label(rot, bg='#A89331', font=('Arial', 10, 'bold'), text="Subject")                                                        #<-- Create the subject label (text)
    subject_label.place(x=380, y=65)                                                                                                            #<-- Place the label

    subject_entry = Entry(rot, bg='#6e3e22', font=('Arial', 15, 'bold'), width=30)                                                              #<-- Create the subject entry (input field)
    subject_entry.place(x=30, y=65)                                                                                                             #<-- Place the entry on the window

    content_area = scrolledtext.ScrolledText(rot, bg='#A89331', font=('arial', 15, 'bold'), width=30, height=10)                                #<-- Create the content area
    content_area.place(x=30, y=100)                                                                                                             #<-- Place the content area on the window

    valid_button = Button(rot, bg='#6e3e22', font=('Arial', 15), text="Submit", bd=1, highlightthickness=0, fg='black',                         #<-- Create button to valid the mail
        width=28, command=email_writing)
    valid_button.place(x=30, y=350)                                                                                                             #place the button on the window

    valid_button.bind("<Enter>", on_enter)                                                                                                      #<-- Create bind, when the mouse is hover the button, change the background
    valid_button.bind("<Leave>", on_leave)                                                                                                      #<-- Create bind, when the mouse is not hover the button, change the background
    content_area.delete('1.0', END)                                                                                                             #<-- Delete all the content of the text area
    content_area.insert(INSERT, text_to_insert)                                                                                                 #<-- Insert the text to send (the same text that in the content area)
    subject_entry.insert(INSERT, subject)                                                                                                       #<-- Insert in the subject field, the title of the content
    rot.bind("<Return>", email_writing_event)                                                                                                   #<-- Create a shortcut, press <Return> button to execute the same command that the button

    rot.mainloop()                                                                                                                              #<-- Mainloop the window


def copy():                                                                                                                                     #<-- Create a function to copy text area content in the clipboard using pyperclip librarie
    copying = text_area.get('1.0', END)                                                                                                         #<-- Get the text to copy (text area)
    pyperclip.copy(copying)                                                                                                                     #<-- Copy to the clipboard the content
    print(f"[{str(datetime.datetime.now().hour).zfill(2)}:{str(datetime.datetime.now().minute).zfill(2)}] text copied: {copying}")              #<-- Insert in th terminal, "text copied" to informing the user

def search(event):                                                                                                                              #<-- Create THE main function, TO SEARCH
    searching = search_bar.get()                                                                                                                #<-- Get what the user want search, (search bar content)
    search_len = len(searching)                                                                                                                 #<-- Get the number of caracteres of the search bar
    if search_len > 1:                                                                                                                          #<-- check if the number of caracteres are > 1
        if searching == "Documentation":                                                                                                        #<-- If the user search "Documentation", create a specific function and not web search
            aboutapp()                                                                                                                          #<-- Call aboutapp function
        else:
            try:
                result = wikipedia.summary((searching + "()"), sentences=28)                                                                    #<-- Use wikipedia to search and get 28 sentences
                text_area.delete('1.0', END)                                                                                                    #<-- Delete all the content of the text area
                translated = translator.translate(result, dest='english')                                                                       #<-- Translate the result in english
                text_area.insert(INSERT, translated.text)                                                                                       #<-- Insert in the text area, the result
            except:                                                                                                                             #<-- If here is an error like page doesn't exist... say
                text_area.delete('1.0', END)                                                                                                    #<-- Delete the content of the text area
                text_area.insert(INSERT, "Oops...")                                                                                             #<-- Insert in the text area "Oops"
                rresult_connection = test_connection()                                                                                          #<-- Checking if the connection is ok
                if rresult_connection == True:                                                                                                  #<-- if connection is true
                    messagebox.showerror('Error Goldatio', "Oops... This page doesn't exist :(")                                                #<-- show message box, page doesn't exist
                else:
                    messagebox.showerror("Offline", "Oops... Your device's offline... :(")                                                      #<-- Device not online
    else:
        pass

def search_button_function():                                                                                                                   #<-- Create function, to search but with the button
    searching = search_bar.get()                                                                                                                #<-- Get what the user want search, (search bar content)
    search_len = len(searching)                                                                                                                 #<-- Get the number of caracteres of the search bar
    if search_len > 1:                                                                                                                          #<-- check if the number of caracteres are > 1
        if searching == "Documentation":                                                                                                        #<-- If the user search "Documentation", create a specific function and not web search
            aboutapp()                                                                                                                          #<-- Call aboutapp function
        elif searching == "Doc":                                                                                                                #<-- If the user search "Doc", create a specific function and not web search
            aboutapp()                                                                                                                          #<-- Call aboutapp function
        else:
            try:                                                                                                                                #<-- If here is an error like page doesn't exist... say
                result = wikipedia.summary((searching + "()"), sentences=28)                                                                    #<-- Use wikipedia to search and get 28 sentences
                text_area.delete('1.0', END)                                                                                                    #<-- Delete all the content of the text area
                translated = translator.translate(result, dest='english')                                                                       #<-- Translate the result in english                                                                 
                text_area.insert(INSERT, translated.text)                                                                                       #<-- Insert in the text area, the result
            except:                                                                                                                             #<-- If here is an error like page doesn't exist... say
                text_area.delete('1.0', END)                                                                                                    #<-- Delete the content of the text area
                text_area.insert(INSERT, "Oups...")                                                                                             #<-- Insert in the text area "Oops"
                rresult_connection = test_connection()                                                                                          #<-- Checking if the connection is ok
                if rresult_connection == True:                                                                                                  #<-- if connection is true
                    messagebox.showerror('Error Goldatio', "Oups... This page doesn't exist :(")                                                #<-- show message box, page doesn't exist
                else:
                    messagebox.showerror("Offline", "Oops... Your device's offline... :(")                                                      #<-- Device not online
    else:
        pass

search_bar = Entry(root, width=30, bg="#a89331", font=("Arial", 10, 'bold'))                                                                    #<-- Create the main search bar
search_bar.pack(side=TOP)                                                                                                                       #<-- Place the search bar on the window et place it in the top

search_buttton = Button(root, text='Search', command=search_button_function, bg='#6e3e22', font=("Arial", 10, 'bold'))                          #<-- Create the main search button who will call the search button function
search_buttton.pack(side=TOP, fill=X)                                                                                                           #<-- Place the button in the top, but the serach bar in too on the top, so, it will auto placed under the search because it's define after define the search bar

text_area = scrolledtext.ScrolledText(root, font=("Arial", 10), bg='#a89331', width=45, height=12)                                              #<-- Create the main text_ area
text_area.pack(expand=YES, fill='both')                                                                                                         #<-- Place the text area on the window in the top, and fill = Both, to take all the place

copy_button = Button(root, text='Copy to clipboard.', command=copy, bg='#6e3e22', font=("Arial", 10, 'bold'))                                   #<-- Create the copy button
copy_button.pack(side=BOTTOM, fill=X)                                                                                                           #<-- Place the button in the Bottom, and fill all the X axis

search_bar.bind('<Return>', search)                                                                                                             #<-- Create the bind for the search

menubar = Menu(root)                                                                                                                            #<-- Create the top menubar and place in all command like exit and more...
file_menu = Menu(menubar, tearoff=0)                                                                                                            #<-- Create the menu FILE

file_menu.add_command(label='Save', command=onSave)                                                                                             #<-- Add a command to FILE, and it is to save a file, with text: "Save"
file_menu.add_command(label='Open', command=onOpen)                                                                                             #<-- Add a command to FILE, and it is to Open a file, with text: "Open"
file_menu.add_command(label='Exit', command=root.quit)                                                                                          #<-- Add a command to FILE, and it is to Exit the window, with text: "Exit" 

view_menu = Menu(menubar, tearoff=0)                                                                                                            #<-- Create menu VIEW

view_menu.add_command(label='Switch size', command=change_size)                                                                                 #<-- Add command to VIEW to switch the size

about = Menu(menubar, tearoff=0)                                                                                                                #<-- Create menu ABOUT

about.add_command(label="About me", command=aboutme)                                                                                            #<-- Add command to ABOUT to call the funtion About me
about.add_command(label='About App', command=aboutapp)                                                                                          #<-- Add command to ABOUT to call the function About App

Send = Menu(menubar, tearoff=0)                                                                                                                 #<-- Create menu Send

Send.add_command(label="Send by Email", command=send)                                                                                           #<-- Add command to SEND, to send by a mail

sm = Menu(menubar, tearoff=0)                                                                                                                   #<-- Create menu SM (Social Media)

sm.add_command(label="Instagram (Personal)", command=instaperso)                                                                                #<-- Add command to SM to send the user on my personal insta page
sm.add_command(label="Instagram (Goldatio)", command=instapro)                                                                                  #<-- Add command to SM to send the user on the Goldatio insta page

menubar.add_cascade(label='File', menu=file_menu)                                                                                               #<-- Add the file menu to the menu bar
menubar.add_cascade(label='View', menu=view_menu)                                                                                               #<-- Add the view menu to the menu bar
menubar.add_cascade(label="About", menu=about)                                                                                                  #<-- Add the About menu to the menu bar
menubar.add_cascade(label="Send", menu=Send)                                                                                                    #<-- Add the Send menu to the menu bar
menubar.add_cascade(label="Social Medias", menu=sm)                                                                                             #<-- Add the SM menu to the menu bar

root.config(menu=menubar)                                                                                                                       #<-- Define the menu bar on the window
root.mainloop()                                                                                                                                 #<-- Mainloop the main window