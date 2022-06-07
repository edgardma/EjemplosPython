from tkinter import *
from pytube import YouTube

root = Tk()
root.geometry('500x300')
root.resizable(0, 0)
root.title("YouTube Downloader")
root.configure(bg="#f2eee3")

Label(root, text='TouTube Video Downloader', font='arial 20 bold', bg="#f2eee3", fg="red").pack()

link = StringVar()
Label(root, text='Pegar el link de YouTube aqui:', font='arial 20 bold', bg="#f2eee3", fg="red").place(x=40, y=60)
link_enter = Entry(root, width=50, textvariable=link).place(x=32, y=90)

def downloader():
    url = YouTube(str(link.get()))
    ## Esto es para poder listar todas las resoluciones del video
    resul = url.streams.all()
    for i in resul:
        print(i)

    ## Se realiza la descarga, el número corresponde a la posición en la lista de resoluciones
    video = url.streams[2]
    video.download()
    Label(root, text='DESCARGADO', font='arial 15 bold', bg="#f2eee3", fg="red").place(x=185, y=210)

Button(root,
       text='DOWNLOAD',
       font='arial 15 bold',
       bg='pale violet red',
       padx=2,
       command=downloader,
       fg="blue").place(x=180, y=150)

root.mainloop()