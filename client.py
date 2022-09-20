#-----------Bolierplate Code Start -----
from base64 import encode
import socket
from tkinter import *


PORT  = 5500
IP_ADDRESS = '127.0.0.1'
SERVER = None
BUFFER_SIZE = 4096


name = None
listbox =  None
textarea= None
labelchat = None
text_message = None


def connectToServer():
     global name
     global SERVER
     
     cname = name.get()
     SERVER.send(cname,encode())
          

def openChatWindow():

   
    print("\n\t\t\t\tMusic Window")

    #Client GUI starts here
    window=Tk()

    window.title('Music Window')
    window.geometry("500x360")
    window.configure(bg="LightSkyBlue")

    global name
    global listbox
    global textarea
    global labelchat
    global text_message
    global filePathLabel

    selectLabel=Label(window,text="select a song",bg="LightSkyBlue",font=("calibri",8))
    selectLabel.place(x=2,y=1)

    listbox = Listbox(window,height = 10,width = 39,activestyle = 'dotbox', font = ("Calibri",10))
    listbox.place(x=10, y=20)

    scrollbar1 = Scrollbar(listbox)
    scrollbar1.place(relheight = 1,relx = 1)
    scrollbar1.config(command = listbox.yview)

    Play=Button(window,text="Play",bg="SkyBlue",bd=1,font=("calibri",10))
    Play.place(x=20,y=200)

    Stop=Button(window,text="Stop",bg="SkyBlue",bd=1,font=("calibri",10))
    Stop.place(x=200,y=200)

    Upload=Button(window,text="Upload",bg="SkyBlue",bd=1,font=("calibri",10))
    Upload.place(x=20,y=250)

    Download=Button(window,text="Download",bg="SkyBlue",bd=1,font=("calibri",10))
    Download.place(x=200,y=250)

    infoLabel = Label(window, text= "", font = ("Calibri",8))
    infoLabel.place(x=4, y=280)

      
    window.mainloop()




def setup():
    global SERVER
    global PORT
    global IP_ADDRESS

    SERVER = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    SERVER.connect((IP_ADDRESS, PORT))

    openChatWindow()

setup()
