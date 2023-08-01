#yeni hasta kaydı
#hasan kaan kartal
import tkinter as tk
from PIL import Image, ImageTk
from openpyxl import Workbook, load_workbook
from datetime import datetime
pencere = tk.Tk()
pencere.title("Kartal Veteriner Klinigi Kullinici Paneli")
pencere.geometry("1000x700")

wb = load_workbook("C:/Users/hasan/Desktop/ilk_deneme.xlsx")
ws = wb.active
# ------------ Arka Plan-----------------
image = Image.open("KARTAL.png")
photo = ImageTk.PhotoImage(image)
label = tk.Label(pencere, image=photo)
label.pack()

# -----------------Buton----------------------
def butonBas():
    adsoyad = ent1.get()
    cins = ent2.get()
    yas = ent3.get()
    ucret = ent4.get()
    cinsiyet = ent5.get()
    tarih = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    if selected_option.get() == 1:
        ws.append([adsoyad, cins, cinsiyet, yas, "kedi", ucret, tarih])
    elif selected_option.get() == 2:
        ws.append([adsoyad, cins, cinsiyet, yas, "köpek", ucret,tarih])
    elif selected_option.get() == 3:
        ws.append([adsoyad, cins, cinsiyet, yas , "diğer",ucret,tarih])
    wb.save("C:/Users/hasan/Desktop/ilk_deneme.xlsx")
    print(adsoyad, cins, yas)
    ent1.delete(0, tk.END)
    ent2.delete(0, tk.END)
    ent3.delete(0, tk.END)
    ent4.delete(0, tk.END)
    ent5.delete(0, tk.END)

# -----------------------Yazılar-----------------------
e11 = tk.Label(text="KARTAL VETERİNER KLİNİĞİ HASTA KAYIT PLATFORMU", font="Arial 17 bold")
e11.place(x=0, y=0)

e1 = tk.Label(text="İSİM SOYİSİM", font="Arial 12 bold")
e1.place(x=10, y=50)
ent1 = tk.Entry(width=30)
ent1.place(x=120, y=50)

e2 = tk.Label(text="CİNS", font="Arial 12 bold")
e2.place(x=10, y=100)
ent2 = tk.Entry(width=30)
ent2.place(x=120, y=100)

e5 = tk.Label(text="CİNSİYET", font="Arial 12 bold")
e5.place(x=10, y=150)
ent5 = tk.Entry(width=30)
ent5.place(x=120, y=150)

e3 = tk.Label(text="YAŞ", font="Arial 12 bold")
e3.place(x=10, y=200)
ent3 = tk.Entry(width=30)
ent3.place(x=120, y=200)

e4 = tk.Label(text="ÜCRET", font="Arial 12 bold")
e4.place(x=10, y=250)
ent4 = tk.Entry(width=30)
ent4.place(x=120, y=250)

e4 = tk.Label(text="TÜR", font="Arial 12 bold")
e4.place(x=10, y=350)

# -------------------------Radio Button---------------------------
selected_option = tk.IntVar()

rb1 = tk.Radiobutton(pencere, text="kedi", font="Arial 12 bold", variable=selected_option, value=1)
rb1.place(x=120, y=300)

rb2 = tk.Radiobutton(pencere, text="köpek", font="Arial 12 bold", variable=selected_option, value=2)
rb2.place(x=120, y=350)

rb3 = tk.Radiobutton(pencere, text="diğer", font="Arial 12 bold", variable=selected_option, value=3)
rb3.place(x=120, y=400)

# --------------------------Buton----------------------------
giris_butonu = tk.Button(text=" Giriş ", bg="black", fg="white", font="Arial 12 bold", command=butonBas)
giris_butonu.place(x=400, y=50)

pencere.mainloop()