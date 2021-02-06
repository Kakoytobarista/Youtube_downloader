from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from pytube import YouTube


def clickDownload():
    if getURL.get() == "":
        messagebox.showinfo("ОШИБКА", "ВВЕДИТЕ ССЫЛКУ")
        return
    elif getLoc.get() == "":
        messagebox.showinfo("ОШИБКА", "ВЫБЕРИТЕ РАСПОЛОЖЕНИЕ ФАЙЛА")
        return

    select = listbox.curselection()
    quality = videos[select[0]]
    location = getLoc.get()
    quality.download(location)
    messagebox.showinfo("Скачивание", yt.title + " было успешно завершено!!!")


def setURL():
    url = getURL.get()

    global yt
    yt = YouTube(url)

    global videos
    videos = yt.streams.filter(mime_type = "video/mp4").all()

    count = 1
    for v in videos:
        listbox.insert(END, (str(count) + ". " + str(v)[str(v).find("res="):str(v).find("fps=")] + '"\n\n').replace('"', ''))
        count += 1


def clickBrowse():
    location_of_download = filedialog.askdirectory()
    getLoc.set(location_of_download)


def clickReset():
    getURL.set("")
    getLoc.set("")
    listbox.delete(0, END)


root = Tk()

root.title("YouTube Video Downloader")

root.geometry("900x550")

root.resizable(False, False)

headLabel = Label(root, text="СКАЧИВАНИЕ ВИДЕО С ЮТУБ", font=("Courier", 25)).grid(row=0,column=1,padx=10, pady=10)
urlLabel = Label(root, text="ССЫЛКА", font=("Century Gothic", 15)).grid(row=1, column=0, padx=10, pady=10)
qualityLabel = Label(root, text="КАЧЕСТВО ВИДЕО", font=("Century Gothic", 15)).grid(row=2, column=0, padx=10, pady=10)
locLabel = Label(root, text="РАСПОЛОЖЕНИЕ", font=("Century Gothic", 15)).grid(row=3, column=0, padx=10, pady=10)

getURL = StringVar()
getLoc = StringVar()

urlEntry = Entry(root, font=("Century Gothic", 12), textvariable=getURL, width=50, bd=3, relief=SOLID, borderwidth=1).grid(row=1, column=1, padx=10, pady=10)
locEntry = Entry(root, font=("Century Gothic", 12), textvariable=getLoc, width=50, bd=3, relief=SOLID, borderwidth=1).grid(row=3, column=1, padx=10, pady=10)

listbox = Listbox(root, font=("Century Gothic", 11), width=56, height=12, bd=3, relief=SOLID, borderwidth=1)
listbox.grid(row=2, column=1, padx=10, pady=10)

urlButton = Button(root, text="ДАЛЕЕ", font=("Century Gothic", 10), width=15, relief=SOLID, borderwidth=1, command=setURL).grid(row=1, column=2, padx=10, pady = 10)
browseButton = Button(root, text="ОБЗОР...", font=("Century Gothic", 10), width=15, relief=SOLID, borderwidth=1, command=clickBrowse).grid(row=3, column=2, padx=10, pady = 10)
downloadButton = Button(root, text="СКАЧАТЬ", font=("Century Gothic", 10), width=15, relief=SOLID, borderwidth=1, command=clickDownload).grid(row=4, column=1, padx=10, pady = 10)
resetButton = Button(root, text="ОЧИСТИТЬ ВСЁ", font=("Century Gothic", 10), width=15, relief=SOLID, borderwidth=1, command=clickReset).grid(row=4, column=2, padx=10, pady = 10)

root.mainloop()