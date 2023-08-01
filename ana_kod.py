#ana kod
#hasan kaan kartal
import tkinter as tk
import subprocess
from PIL import Image, ImageTk
def button1_click():
    print("Button 1 clicked!")
    subprocess.run(["python", "C:/Users/hasan/PycharmProjects/kaan_ilk/exa_uygulaması.py"])

def button2_click():
    print("Button 2 clicked!")
    subprocess.run(["python", "C:/Users/hasan/PycharmProjects/kaan_ilk//exel_Deneme.py"])

if __name__ == "__main__":
    pencere = tk.Tk()
    pencere.title("Kartal Veteriner Klinigi Kullinici Paneli")
    pencere.geometry("700x700")
    image = Image.open("KARTAL.png")
    photo = ImageTk.PhotoImage(image)
    label = tk.Label(pencere, image=photo)
    label.pack()

    button1 = tk.Button(pencere,height=5,width=20,bg="black",fg="white",text="FİYAT DÜZENLEME", command=button1_click)
    button1.place(x=60,y=30)

    button2 = tk.Button(pencere,height=5,width=20,bg="black",fg="white", text="YENİ HASTA KAYDI", command=button2_click)
    button2.place(x=500,y=30)

    pencere.mainloop()

