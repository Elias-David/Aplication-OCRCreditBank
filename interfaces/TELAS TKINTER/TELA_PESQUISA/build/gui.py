
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\david\Desktop\TI\EDTECH\DESAFIO_CICLO1\TKDESIGNER\testes\tela_pesquisa\build\assets\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("1030x520")
window.configure(bg = "#FFFFFF")


canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 520,
    width = 1030,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
canvas.create_rectangle(
    0.0,
    0.0,
    1030.0,
    85.0,
    fill="#2E5266",
    outline="")

canvas.create_rectangle(
    739.0,
    85.0,
    1030.0,
    520.0,
    fill="#D3D0CB",
    outline="")

canvas.create_text(
    94.0,
    21.0,
    anchor="nw",
    text="OCRCreditBank",
    fill="#FEFEFE",
    font=("Poppins Regular", 32 * -1)
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_1 clicked"),
    relief="flat"
)
button_1.place(
    x=17.0,
    y=100.0,
    width=155.0,
    height=24.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_2 clicked"),
    relief="flat"
)
button_2.place(
    x=17.0,
    y=138.0,
    width=124.0,
    height=24.0
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_3 clicked"),
    relief="flat"
)
button_3.place(
    x=17.0,
    y=176.0,
    width=162.0,
    height=24.0
)

image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    45.0,
    43.0,
    image=image_image_1
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    796.0,
    108.0,
    image=image_image_2
)

button_image_4 = PhotoImage(
    file=relative_to_assets("button_4.png"))
button_4 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_4 clicked"),
    relief="flat"
)
button_4.place(
    x=895.0,
    y=431.0,
    width=93.0,
    height=29.0
)

button_image_5 = PhotoImage(
    file=relative_to_assets("button_5.png"))
button_5 = Button(
    image=button_image_5,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_5 clicked"),
    relief="flat"
)
button_5.place(
    x=772.0,
    y=431.0,
    width=93.0,
    height=29.0
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    873.0,
    168.0,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#FEFEFE",
    fg="#000716",
    highlightthickness=0
)
entry_1.place(
    x=774.0,
    y=152.0,
    width=198.0,
    height=30.0
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    873.0,
    219.0,
    image=entry_image_2
)
entry_2 = Entry(
    bd=0,
    bg="#FEFEFE",
    fg="#000716",
    highlightthickness=0
)
entry_2.place(
    x=774.0,
    y=203.0,
    width=198.0,
    height=30.0
)

entry_image_3 = PhotoImage(
    file=relative_to_assets("entry_3.png"))
entry_bg_3 = canvas.create_image(
    873.0,
    270.0,
    image=entry_image_3
)
entry_3 = Entry(
    bd=0,
    bg="#FEFEFE",
    fg="#000716",
    highlightthickness=0
)
entry_3.place(
    x=774.0,
    y=254.0,
    width=198.0,
    height=30.0
)

entry_image_4 = PhotoImage(
    file=relative_to_assets("entry_4.png"))
entry_bg_4 = canvas.create_image(
    822.5,
    330.0,
    image=entry_image_4
)
entry_4 = Entry(
    bd=0,
    bg="#FEFEFE",
    fg="#000716",
    highlightthickness=0
)
entry_4.place(
    x=798.0,
    y=314.0,
    width=49.0,
    height=30.0
)

entry_image_5 = PhotoImage(
    file=relative_to_assets("entry_5.png"))
entry_bg_5 = canvas.create_image(
    822.5,
    399.0,
    image=entry_image_5
)
entry_5 = Entry(
    bd=0,
    bg="#FEFEFE",
    fg="#000716",
    highlightthickness=0
)
entry_5.place(
    x=798.0,
    y=383.0,
    width=49.0,
    height=30.0
)

entry_image_6 = PhotoImage(
    file=relative_to_assets("entry_6.png"))
entry_bg_6 = canvas.create_image(
    932.5,
    330.0,
    image=entry_image_6
)
entry_6 = Entry(
    bd=0,
    bg="#FEFEFE",
    fg="#000716",
    highlightthickness=0
)
entry_6.place(
    x=908.0,
    y=314.0,
    width=49.0,
    height=30.0
)

entry_image_7 = PhotoImage(
    file=relative_to_assets("entry_7.png"))
entry_bg_7 = canvas.create_image(
    932.5,
    399.0,
    image=entry_image_7
)
entry_7 = Entry(
    bd=0,
    bg="#FEFEFE",
    fg="#000716",
    highlightthickness=0
)
entry_7.place(
    x=908.0,
    y=383.0,
    width=49.0,
    height=30.0
)

canvas.create_text(
    772.0,
    132.0,
    anchor="nw",
    text="N° CÉDULA",
    fill="#000000",
    font=("Poppins Light", 13 * -1)
)

canvas.create_text(
    772.0,
    183.0,
    anchor="nw",
    text="TITULAR",
    fill="#000000",
    font=("Poppins Light", 13 * -1)
)

canvas.create_text(
    772.0,
    235.0,
    anchor="nw",
    text="AGENTE",
    fill="#000000",
    font=("Poppins Light", 13 * -1)
)

canvas.create_text(
    842.0,
    289.0,
    anchor="nw",
    text="VALORES(R$)",
    fill="#000000",
    font=("Poppins Light", 13 * -1)
)

canvas.create_text(
    817.0,
    353.0,
    anchor="nw",
    text="DATA (DD/MM/AAAA)",
    fill="#000000",
    font=("Poppins Light", 13 * -1)
)
window.resizable(False, False)
window.mainloop()