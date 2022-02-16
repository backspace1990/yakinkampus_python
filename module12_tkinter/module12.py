from tkinter import *
from tkcalendar import DateEntry

master = Tk()

canvas = Canvas(master, height=500, width=800)
canvas.pack()

frame_top = Frame(master, bg='#add8e6')
frame_top.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.1)

frame_under_left = Frame(master, bg='#add8e6')
frame_under_left.place(relx=0.1, rely=0.21, relwidth=0.23, relheight=0.5)

frame_under_right = Frame(master, bg='#add8e6')
frame_under_right.place(relx=0.339, rely=0.21, relwidth=0.56, relheight=0.5)

hatirlatma_tipi_etiketi = Label(frame_top, bg='#add8e6', text='Hatirlatma tipi :', font='Verdana 12 bold')
hatirlatma_tipi_etiketi.pack(padx=10, pady=10, side=LEFT)

hatirlatma_tipi_opsion = StringVar(frame_top)
hatirlatma_tipi_opsion.set("\t")

hatirlatma_tipi_drop_menu = OptionMenu(frame_top,
                                       hatirlatma_tipi_opsion,
                                       "Dogum Gunu",
                                       "Alis-veris",
                                       "Odeme")
hatirlatma_tipi_drop_menu.pack(padx=10, pady=10, side=LEFT)

hatirlatma_tarih_secici = DateEntry(frame_top, width=12, background='orange', foreground='black', borderwidth=1,
                                    locale='ru_RU')
hatirlatma_tarih_secici.top_cal.overrideredirect(False)
hatirlatma_tarih_secici.pack(padx=10, pady=10, side=RIGHT)

hatirlatma_tarihi_etiketi2 = Label(frame_top, bg='#add8e6', text='Hatirlatma tarihi :', font='Verdana 12 bold')
hatirlatma_tarihi_etiketi2.pack(padx=10, pady=10, side=LEFT)
# pack
# place
# grid

# ---
Label(frame_under_left, bg='#add8e6', text='Hatirlatma Yontemi :', font='Verdana 12 bold').pack(padx=10,
                                                                                                pady=10, anchor=NW)

var = IntVar()

R1 = Radiobutton(frame_under_left, text="Sisteme kaydet", variable=var, value=1, font='Verdana 12 bold', bg='#add8e6')
R1.pack(anchor=NW, pady=5, padx=15)

R2 = Radiobutton(frame_under_left, text="E-posta gonder", variable=var, value=2, font='Verdana 12 bold', bg='#add8e6')
R2.pack(anchor=NW, pady=5, padx=15)

var1 = IntVar()
C1 = Checkbutton(frame_under_left, text="Ayni gun", variable=var1, onvalue=1, offvalue=0, font='Verdana 12 bold',
                 bg='#add8e6')
C1.pack(anchor=NW, pady=5, padx=25)
var2 = IntVar()
C2 = Checkbutton(frame_under_left, text="Bir gun once", variable=var2, onvalue=1, offvalue=0, font='Verdana 12 bold',
                 bg='#add8e6')
C2.pack(anchor=NW, pady=5, padx=25)
var3 = IntVar()
C3 = Checkbutton(frame_under_left, text="Bir hafta once", variable=var3, onvalue=1, offvalue=0, font='Verdana 12 bold',
                 bg='#add8e6')
C3.pack(anchor=NW, pady=5, padx=25)

# ----
"""
def e_posta_send():
    users = '<users_mail>'
    users_passw = '<users_pasww>'
    receiver_user = '<reciver_users>'
    users_Msg = text_aria.get("1.0", 'end')
    context = ssl.create_default_context()
    port = 465
    hosts_smtp = 'smtp.gmail.com'
    e_posta_server = smtplib.SMTP_SSL(host=hosts_smtp, port=port, context=context)
    e_posta_server.login(users, users_passw)
    e_posta_server.sendmail(users, receiver_user, users_Msg)
    return 'E-posts is sending'
"""
from tkinter import messagebox


def gonder():
    son_msj = ''
    try:
        if var.get():
            if var.get() == 1:
                son_msj += 'Veriniz basriyla sisteme kaydedildi'

                tip = hatirlatma_tipi_opsion.get() if hatirlatma_tipi_opsion.get() == '' else 'Genel'
                tarih = hatirlatma_tarih_secici.get()
                mesaj = text_aria.get("1.0", 'end')

                with open('hatirlatmalar.txt', "w") as dosya:
                    dosya.write(f"{tip} kategorisinde, {tarih} tarihinde ve --'{mesaj}'notuyla hatirlatma")
                    dosya.close()
            else:
                son_msj += 'Veriniz e-posta yoluyla size ulasacaktir'
            messagebox.showinfo("Basarili islem", son_msj)
        else:
            son_msj += 'Gerekli alanlarin dolduruldugundan emin olun!'
            messagebox.showwarning("Eksik islem", son_msj)
    except:
        son_msj += "basarisiz islem"
        messagebox.showerror('basarisiz islem', son_msj)
    finally:
        master.destroy()
    return


Label(frame_under_right, bg='#add8e6', text='Hatirlatma Mesaji :', font='Verdana 12 bold').pack(padx=10, pady=10,
                                                                                                anchor=NW)
text_aria = Text(frame_under_right, height=9, width=60)
text_aria.tag_configure('style', foreground='#bfbfbf', font=('Verdana', 7, 'bold'))
text_aria.pack(padx=4, pady=3, anchor=NW)

karsilama_text = 'Metnini buraya gir...'
text_aria.insert(END, karsilama_text, 'style')

send_buton = Button(frame_under_right, text='Gonder', command=gonder)
send_buton.pack(anchor=S, pady=10)

master.mainloop()
