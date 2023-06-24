import tkinter as tk
from tkinter import*
from tkinter import filedialog
from tkinter import messagebox
from tkinter import ttk, filedialog
import numpy
import pandas as pd

root = tk.Tk()
root.geometry('600x600')

root.title('Dijital Ajandam')
root.tk_setPalette('white')
root.resizable(False,False)

ku = tk.PhotoImage(file='ekran.png')
buyukku = ku.subsample(1,1)
def bildirim_sayfa():
    def Open():
        filename = filedialog.askopenfilename(title="Open a File",
                                              filetypes=(("xlxs files",".*xlsx"),
                                                         ("All Files", "*.*")))
        if filename:
            try:
                filename = r"{}".format(filename)
                df = pd.read_excel(filename)

            except:
                messagebox.showerror("error", "bu dosyaya erişilemiyor")
        
        tree.delete()

        tree['column'] = list(df.columns)
        tree['show'] = "headings"

        for col in tree ['column']:
            tree.heading(col,text=col)


        df_rows = df.to_numpy().tolist()
        for row in df_rows:
            tree.insert("","end",values=row)

    heading_lb = tk.Label(main_frame, text=' // Dijital Anımsatıcım', font=('Lucida Console', 14), fg='#6A5ACD')
    heading_lb.pack(anchor=tk.W, padx=5)
    
    bildirim_frame = tk.Frame(main_frame)
    bildirim_frame.pack(pady=25)

    tree = ttk.Treeview(main_frame)
    tree.pack()
    tree.place(x=47, y=186)

    button = Button(main_frame, text='Anımsatıcımı Aç',width=35, height=2, font=('Lucida Console', 15), fg="#E6E6FA", bg="#6A5ACD", command=Open)
    button.pack(padx=10, pady=20)
    button.place(x=32,y=464)

    note_image_lb = tk.Label(bildirim_frame, image=buyukku)
    note_image_lb.pack(padx=10)

note = tk.PhotoImage(file='internet.png')
buyuknote = note.subsample(5,5)

def link_sayfa():
    def save_file():
        open_file = filedialog.asksaveasfile(mode='w', defaultextension='.txt')
        if open_file is None:
            return
        text = str(metin.get(1.0, END))
        open_file.write(text)
        open_file.close()

    def open_file():
        file=filedialog.askopenfile(mode='r', filetype=[('text files', '*.txt')])
        if file is not None:
            content = file.read()
        metin.insert(INSERT, content)
    
    link_frame = tk.Frame(main_frame)
    baslik = tk.Label(main_frame, text='// Dijital Linklerim', font=('Lucida Console', 14), fg='#6A5ACD')
    baslik.pack(anchor=tk.W, padx=10)

    note_image_lb = tk.Label(link_frame, image=buyuknote)
    note_image_lb.pack(padx=200, pady=20)

    metin = tk.Text(main_frame, height='15', width='32', wrap=WORD, bg="#C4CCF5", fg='#192140', padx=10, pady=8, font=('Lucida Console', 12))
    metin.place(x=80, y=200)
    

    buton1 = tk.Button(main_frame, width='17', height='2', bg='#5672DE',fg='#E6E6FA',font=('Lucida Console', 11), relief='groove', text='Link Kaydet', command=save_file).place(x=50, y=510)
    buton2 = tk.Button(main_frame, width='17', height='2', bg='#5672DE',fg='#E6E6FA',font=('Lucida Console', 11), relief='groove', text='Link Aç', command=open_file).place(x=290, y=510)


    link_frame.pack(anchor=tk.W, pady=10)

liste_resim = tk.PhotoImage(file='bosliste.png')
buyukliste = liste_resim.subsample(1,1)
def liste_sayfa():
    def save_file():
        open_file = filedialog.asksaveasfile(mode='w', defaultextension='.txt')
        if open_file is None:
            return
        text = str(metin.get(1.0, END))
        open_file.write(text)
        open_file.close()

    def open_file():
        file=filedialog.askopenfile(mode='r', filetype=[('text files', '*.txt')])
        if file is not None:
            content = file.read()
        metin.insert(INSERT, content)

    liste_frame = tk.Frame(main_frame)
    baslik = tk.Label(main_frame, text=' // Dijital Listem', font=('Lucida Console', 14), fg='#6A5ACD')
    baslik.pack(anchor=tk.W, padx=1)
    baslik.place(y=5)

    liste_resim_lb = tk.Label(liste_frame, image=buyukliste)
    liste_resim_lb.pack()

    liste_frame.pack(anchor=tk.W, pady=10)

    buton1 = tk.Button(main_frame, width='20', height='2', bg='#5672DE',fg='#E6E6FA',font=('Lucida Console', 10), relief='groove', text='Listemi Kaydet', command=save_file).place(x=30, y=530)
    buton2 = tk.Button(main_frame, width='20', height='2', bg='#5672DE',fg='#E6E6FA',font=('Lucida Console', 10), relief='groove', text='Listemi Aç', command=open_file).place(x=298, y=530)

    metin = tk.Text(main_frame, height='21', width='25', wrap=WORD, bg="#C4CCF5", fg='#192140', padx=10, pady=8, font=('Lucida Console', 11))
    metin.place(x=128, y=139)

k = tk.PhotoImage(file='conclusion.png')
def gunluk_sayfa():
    def save_file():
        open_file = filedialog.asksaveasfile(mode='w', defaultextension='.txt')
        if open_file is None:
            return
        text = str(metin.get(1.0, END))
        open_file.write(text)
        open_file.close()

    def open_file():
        file=filedialog.askopenfile(mode='r', filetype=[('text files', '*.txt')])
        if file is not None:
            content = file.read()
        metin.insert(INSERT, content)

    gunluk_frame = tk.Frame(main_frame)
    baslik = tk.Label(main_frame, text=' // Dijital Günlüğüm', font=('Lucida Console', 14), fg='#4C96F5')
    baslik.pack(anchor=tk.W)

    kagit = tk.Label(gunluk_frame, image=k)
    kagit.pack()

    gunluk_frame.pack(anchor=tk.W, pady=10)

    b1 = tk.Button(main_frame, width='17', height='2', bg='#5672DE',fg='#E6E6FA',font=('Lucida Console', 10),relief='groove', text='Günlüğümü Kaydet', command=save_file).place(x=150, y=548)
    b2 = tk.Button(main_frame, width='15', height='2', bg='#5672DE',fg='#E6E6FA',font=('Lucida Console', 10),relief='groove', text='Günlüğümü Aç',command=open_file).place(x=305, y=548)

    metin = tk.Text(main_frame, height='26', width='26', wrap=WORD, bg="#4C96F5", fg='#192140',padx=10, pady=8, font=('Lucida Console', 11))
    metin.place(x=127, y=104)

def hide_indicators(): # butonlara basıldıkça gri renkten çıkaran, diğerleri gri yapan
    bildirim_indicate.config(bg='#6A5ACD')
    link_indicate.config(bg='#6A5ACD')
    liste_indicate.config(bg='#6A5ACD')
    gunluk_indicate.config(bg='#6A5ACD')

def delete_pages():
    for frame in main_frame.winfo_children():
        frame.destroy()

def indicate(lb, page): # yan şeritleri gri yapmıştık tekrar rengine dönmesini sağlayan fonksiyon
    hide_indicators()
    lb.config(bg="#E6E6FA")
    delete_pages()
    page()

options_frame = tk.Frame(root, bg='#6A5ACD')    # mor şerit oluşturuldu

resim = tk.PhotoImage(file='takvim.png')
kucukresim = resim.subsample(10,10)

resim_image_lb = tk.Label(options_frame, image=kucukresim)
resim_image_lb.pack(padx=10)
resim_image_lb.place(x=20, y=260)

resim2 = tk.PhotoImage(file='link.png')
kucukresim2 = resim2.subsample(10,10)

resim2_image_lb2 = tk.Label(options_frame, image=kucukresim2)
resim2_image_lb2.pack(padx=10)
resim2_image_lb2.place(x=21, y=340)

resim3 = tk.PhotoImage(file='gunluk.png')
kucukresim3 = resim3.subsample(10,10)

resim3_image_lb3 = tk.Label(options_frame, image=kucukresim3)
resim3_image_lb3.pack(padx=10)
resim3_image_lb3.place(x=21, y=420)

resim4 = tk.PhotoImage(file='listem.png')
kucukresim4 = resim4.subsample(10,10)

resim4_image_lb4 = tk.Label(options_frame, image=kucukresim4)
resim4_image_lb4.pack(padx=10)
resim4_image_lb4.place(x=21, y=500)

# ilk ekranın butonu oluşturuldu
bildirim_btn = tk.Button (options_frame, text='Bildirim', font=('Modern No. 20', 15), 
                      fg='#E6E6FA', bd=0, bg='#6A5ACD',
                      command=lambda: indicate(bildirim_indicate, bildirim_sayfa)) # yukarıdaki fonksiyonu oluşturduk ve butona basıldığı anda yan tarafında mavi dikey şerit belli oldu

bildirim_btn.place(x=10, y=50) # x ve y koordinat düzleminde yerlerini belirliyor

bildirim_indicate = tk.Label(options_frame, text='', bg='#6A5ACD')   # dikey çizgi eklendi
bildirim_indicate.place(x=3, y=50, width=5, height=40) # dikey çizgi boyutlandırıldı

# ikinci ekranın butonu oluşturuldu
link_btn = tk.Button (options_frame, text='Link', font=('Modern No. 20', 15), 
                      fg='#E6E6FA', bd=0, bg='#6A5ACD',
                      command=lambda: indicate(link_indicate, link_sayfa)) 

link_btn.place(x=10, y=100)

link_indicate = tk.Label(options_frame, text='', bg='#6A5ACD')   # dikey çizgi eklendi
link_indicate.place(x=3, y=100, width=5, height=40) # dikey çizgi boyutlandırıldı

# üçüncü ekranın utonu oluşturuldu
liste_btn = tk.Button (options_frame, text='Liste', font=('Modern No. 20', 15), 
                      fg='#E6E6FA', bd=0, bg='#6A5ACD',
                      command=lambda: indicate(liste_indicate, liste_sayfa))

liste_btn.place(x=10, y=150) # x ve y koordinat düzleminde yerlerini belirliyor

liste_indicate = tk.Label(options_frame, text='', bg='#6A5ACD')   # dikey çizgi eklendi
liste_indicate.place(x=3, y=150, width=5, height=40) # dikey çizgi boyutlandırıldı

# döndüncü ekranın utonu oluşturuldu
gunluk_btn = tk.Button (options_frame, text='Günlük', font=('Modern No. 20', 15), 
                      fg='#E6E6FA', bd=0, bg='#6A5ACD',
                      command=lambda: indicate(gunluk_indicate, gunluk_sayfa))

gunluk_btn.place(x=10, y=200) # x ve y koordinat düzleminde yerlerini belirliyor

gunluk_indicate = tk.Label(options_frame, text='', bg='#6A5ACD')   # dikey çizgi eklendi
gunluk_indicate.place(x=3, y=200, width=5, height=40) # dikey çizgi boyutlandırıldı

options_frame.pack(side=tk.LEFT) #oluşturduğumuz paneli sağa doğru oturttuk
options_frame.pack_propagate(False)
options_frame.configure(width=100, height=600) # panelin boyutunu ayarladık

main_frame = tk.Frame(root, highlightbackground='#6A5ACD',
                      highlightthickness=2)

main_frame = tk.Frame(root)
baslik = tk.Label(main_frame, text=' // Dijital Ajandam', font=('Lucida Console', 20), fg='white')
baslik.pack(anchor=tk.W, padx=1)
baslik.place(y=5)

baslik2 = tk.Label(main_frame, text=' Hoş Geldin', font=('Lucida Console', 28), fg='#6A5ACD')
baslik2.pack(anchor=tk.W, padx=1)
baslik2.place(x=110, y=80)

girisekran1 = tk.PhotoImage(file='girisekran.png')
buyukgirisekran1 = girisekran1.subsample(2,2)

girisekran1_lb = tk.Label(main_frame, image=buyukgirisekran1)
girisekran1_lb.pack()
girisekran1_lb.place(y=180)

main_frame.pack(side=tk.LEFT)
main_frame.pack_propagate(False)
main_frame.configure(height=600, width=500)

root.mainloop()