import tkinter as tk
import webbrowser
r= tk.Tk()
r.title("Red Crescents For Palastine")
r.geometry("500x500+300+100")
r.configure(background="green")
def df():
    r.configure(background="red")
def dfc():
    r.configure(background="blue")
def dfcrt():
    r.configure(background="purple")
def dfqw():
    r.configure(background="orange")
def dfcqa():
    r.configure(background="black")
def dfcrtrty():
    r.configure(background="white")
def o_s():
    print("Egyptian Red Crescent")
def o_t():
    print("Turkey Red Crescent and IHH")
def o_w():
    print("Palastine Red Crescent")
def o_m():
    print("Cyrps Red Crescent")
menu_d = tk.Menu(r)
r.config(menu=menu_d)
file = tk.Menu(menu_d)
kay=tk.Menu(menu_d)
menu_d.add_cascade(label="Colors", menu=file)
menu_d.add_cascade(label="Information", menu=kay)
file.add_command(label="red", command=df)
file.add_command(label="blue", command=dfc)
file.add_command(label="purple", command=dfcrt)
file.add_command(label="orange", command=dfqw)
file.add_command(label="black", command=dfcqa)
file.add_command(label="white", command=dfcrtrty)
kay.add_command(label="Egypt", command=o_s)
kay.add_command(label="Turkey", command=o_t)
kay.add_command(label="Palastine", command=o_w)
kay.add_command(label="KKTC", command=o_m)
text=tk.Label(
    text="Red Crescents For Palastine",
    fg="red",
    bg="black",
    width=40,
    height=3,
    font="Tahoma"
)
text.pack()
def list_ok(event):
    secilen = liste.get(liste.curselection())
    if secilen == "İHH":
        url = "https://ihh.org.tr/filistin-gazze"
        webbrowser.open(url)
    elif secilen == "Turkey Red Crescent":
        url = "https://bagis.kizilay.org.tr/tr/bagis/bagisyap/32/filistin-genel-bagisi"
        webbrowser.open(url)
    elif secilen == "Cyrps Red Crescent":
        url = "https://www.kktkizilayi.org/bagis-online/gazzede-insanlik-olmesin"
        webbrowser.open(url)
    elif secilen == "Palastine Red Crescent":
        url = "https://www.palestinercs.org/ar"
        webbrowser.open(url)
    elif secilen == "Egyptian Red Crescent":
        url = "https://www.egyptianrc.org/Arabic/ERC-Activities/Activities/ActivityDetails/84"
        webbrowser.open(url)
liste=tk.Listbox(r)
liste.pack()
liste.insert(tk.END,"İHH")
liste.insert(tk.END,"Turkey Red Crescent")
liste.insert(tk.END,"Cyrps Red Crescent")
liste.insert(tk.END,"Palastine Red Crescent")
liste.insert(tk.END,"Egyptian Red Crescent")
liste.insert(tk.END,"")
liste.insert(tk.END,"")
liste.insert(tk.END,"")
liste.bind("<ButtonRelease-1>", list_ok)
r.mainloop()
###Free_Palastine###
###Love_Palastine###
#I'm from Turkey.#
"""
There is a massacre in Palestine.
I prepared this program so that
this massacre would not be forgotten.
Do not remain silent while there is a massacre!
Thank you for reviewing the program.
"""








