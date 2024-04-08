from pathlib import Path

from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, Label


def menu_awal():
    global window
    OUTPUT_PATH = Path(__file__).parent
    ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\Surya Baaskara\OneDrive\Documents\build\assets\frame0")


    def relative_to_assets(path: str) -> Path:
        return ASSETS_PATH / Path(path)


    window = Tk()

    window.geometry("450x773")
    window.configure(bg = "#FFFFFF")


    canvas = Canvas(
        window,
        bg = "#FFFFFF",
        height = 773,
        width = 450,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
    )

    canvas.place(x = 0, y = 0)
    image_image_1 = PhotoImage(
        file=relative_to_assets("image_1.png"))
    image_1 = canvas.create_image(
        235.0,
        397.0,
        image=image_image_1
    )

    button_image_1 = PhotoImage(
        file=relative_to_assets("button_1.png"))
    button_1 = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=kem,
        relief="flat"
    )
    button_1.place(
        x=240.0,
        y=615.0,
        width=149.0,
        height=55.0
    )

    button_image_2 = PhotoImage(
        file=relative_to_assets("button_2.png"))
    button_2 = Button(
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=uang_5k,
        relief="flat"
    )
    button_2.place(
        x=60.0,
        y=419.0,
        width=153.1475830078125,
        height=65.5909423828125
    )

    button_image_3 = PhotoImage(
        file=relative_to_assets("button_3.png"))
    button_3 = Button(
        image=button_image_3,
        borderwidth=0,
        highlightthickness=0,
        command= Uang_50k,
        relief="flat"
    )
    button_3.place(
        x=240.6136474609375,
        y=500.4091796875,
        width=153.14755249023438,
        height=65.5909423828125
    )

    button_image_4 = PhotoImage(
        file=relative_to_assets("button_4.png"))
    button_4 = Button(
        image=button_image_4,
        borderwidth=0,
        highlightthickness=0,
        command=uang_10k,
        relief="flat"
    )
    button_4.place(
        x=240.28329467773438,
        y=418.681884765625,
        width=153.14755249023438,
        height=65.5909423828125
    )

    button_image_5 = PhotoImage(
        file=relative_to_assets("button_5.png"))
    button_5 = Button(
        image=button_image_5,
        borderwidth=0,
        highlightthickness=0,
        command=uang_20k,
        relief="flat"
    )
    button_5.place(
        x=60.0,
        y=496.4091796875,
        width=153.1475830078125,
        height=65.5909423828125
    )
    window.resizable(False, False)
    window.mainloop()

def uang_5k():
    global window
    window.destroy() 
    
    OUTPUT_PATH = Path(__file__).parent
    ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\Surya Baaskara\OneDrive\Documents\build\assets\frame5")


    def relative_to_assets(path: str) -> Path:
        return ASSETS_PATH / Path(path)


    window = Tk()

    window.geometry("450x773")
    window.configure(bg = "#FFFFFF")


    canvas = Canvas(
        window,
        bg = "#FFFFFF",
        height = 773,
        width = 450,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
    )

    canvas.place(x = 0, y = 0)
    image_image_1 = PhotoImage(
        file=relative_to_assets("image_1.png"))
    image_1 = canvas.create_image(
        235.0,
        397.0,
        image=image_image_1
    )

    button_image_1 = PhotoImage(
        file=relative_to_assets("button_1.png"))
    button_1 = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=kem,
        relief="flat"
    )
    button_1.place(
        x=221.0,
        y=609.0,
        width=149.0,
        height=55.0
    )

    button_image_2 = PhotoImage(
        file=relative_to_assets("button_2.png"))
    button_2 = Button(
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=uang_10k,
        relief="flat"
    )
    button_2.place(
        x=41.0,
        y=414.0,
        width=153.14755249023438,
        height=65.5909423828125
    )

    button_image_3 = PhotoImage(
        file=relative_to_assets("button_3.png"))
    button_3 = Button(
        image=button_image_3,
        borderwidth=0,
        highlightthickness=0,
        command=Uang_15k,
        relief="flat"
    )
    button_3.place(
        x=224.28329467773438,
        y=415.681884765625,
        width=153.14755249023438,
        height=65.5909423828125
    )
    window.resizable(False, False)
    window.mainloop()

def uang_10k():
    global window
    window.destroy()    

    OUTPUT_PATH = Path(__file__).parent
    ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\Surya Baaskara\OneDrive\Documents\build\assets\frame4")


    def relative_to_assets(path: str) -> Path:
        return ASSETS_PATH / Path(path)


    window = Tk()

    window.geometry("450x773")
    window.configure(bg = "#FFFFFF")


    canvas = Canvas(
        window,
        bg = "#FFFFFF",
        height = 773,
        width = 450,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
    )

    canvas.place(x = 0, y = 0)
    image_image_1 = PhotoImage(
        file=relative_to_assets("image_1.png"))
    image_1 = canvas.create_image(
        235.0,
        397.0,
        image=image_image_1
    )

    button_image_1 = PhotoImage(
        file=relative_to_assets("button_1.png"))
    button_1 = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=kem,
        relief="flat"
    )
    button_1.place(
        x=221.0,
        y=609.0,
        width=149.0,
        height=55.0
    )

    button_image_2 = PhotoImage(
        file=relative_to_assets("button_2.png"))
    button_2 = Button(
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=Uang_15k,
        relief="flat"
    )
    button_2.place(
        x=41.0,
        y=414.0,
        width=153.1475830078125,
        height=65.5909423828125
    )

    button_image_3 = PhotoImage(
        file=relative_to_assets("button_3.png"))
    button_3 = Button(
        image=button_image_3,
        borderwidth=0,
        highlightthickness=0,
        command=uang_20k,
        relief="flat"
    )
    button_3.place(
        x=224.2833251953125,
        y=415.681884765625,
        width=153.1475830078125,
        height=65.5909423828125
    )
    window.resizable(False, False)
    window.mainloop()

def Uang_15k():
    global window
    window.destroy()
    
    OUTPUT_PATH = Path(__file__).parent
    ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\Surya Baaskara\OneDrive\Documents\build\assets\frame1")

    def relative_to_assets(path: str) -> Path:
        return ASSETS_PATH / Path(path)


    window = Tk()

    window.geometry("450x773")
    window.configure(bg = "#FFFFFF")


    canvas = Canvas(
        window,
        bg = "#FFFFFF",
        height = 773,
        width = 450,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
    )

    canvas.place(x = 0, y = 0)
    image_image_1 = PhotoImage(
        file=relative_to_assets("image_1.png"))
    image_1 = canvas.create_image(
        235.0,
        397.0,
        image=image_image_1
    )

    button_image_1 = PhotoImage(
        file=relative_to_assets("button_1.png"))
    button_1 = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=kem,
        relief="flat"
    )
    button_1.place(
        x=221.0,
        y=609.0,
        width=149.0,
        height=55.0
    )

    button_image_2 = PhotoImage(
        file=relative_to_assets("button_2.png"))
    button_2 = Button(
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=onigiri,
        relief="flat"
    )
    button_2.place(
        x=190.0,
        y=271.0,
        width=112.47945404052734,
        height=39.740234375
    )

    button_image_3 = PhotoImage(
        file=relative_to_assets("button_3.png"))
    button_3 = Button(
        image=button_image_3,
        borderwidth=0,
        highlightthickness=0,
        command=uang_20k,
        relief="flat"
    )
    button_3.place(
        x=42.0,
        y=415.0,
        width=153.14755249023438,
        height=65.5909423828125
    )

    button_image_4 = PhotoImage(
        file=relative_to_assets("button_4.png"))
    button_4 = Button(
        image=button_image_4,
        borderwidth=0,
        highlightthickness=0,
        command=burger,
        relief="flat"
    )
    button_4.place(
        x=290.0,
        y=280.0,
        width=112.47946166992188,
        height=39.740234375
    )
    window.resizable(False, False)
    window.mainloop()

def uang_20k():
    global window
    window.destroy()
    
    OUTPUT_PATH = Path(__file__).parent
    ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\Surya Baaskara\OneDrive\Documents\build\assets\frame3")


    def relative_to_assets(path: str) -> Path:
        return ASSETS_PATH / Path(path)


    window = Tk()

    window.geometry("450x773")
    window.configure(bg = "#FFFFFF")


    canvas = Canvas(
        window,
        bg = "#FFFFFF",
        height = 773,
        width = 450,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
    )

    canvas.place(x = 0, y = 0)
    image_image_1 = PhotoImage(
        file=relative_to_assets("image_1.png"))
    image_1 = canvas.create_image(
        235.0,
        397.0,
        image=image_image_1
    )

    button_image_1 = PhotoImage(
        file=relative_to_assets("button_1.png"))
    button_1 = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=kem,
        relief="flat"
    )
    button_1.place(
        x=221.0,
        y=609.0,
        width=149.0,
        height=55.0
    )

    button_image_2 = PhotoImage(
        file=relative_to_assets("button_2.png"))
    button_2 = Button(
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=nasi,
        relief="flat"
    )
    button_2.place(
        x=32.0,
        y=273.0,
        width=112.4794921875,
        height=39.740234375
    )

    button_image_3 = PhotoImage(
        file=relative_to_assets("button_3.png"))
    button_3 = Button(
        image=button_image_3,
        borderwidth=0,
        highlightthickness=0,
        command=kem_5k,
        relief="flat"
    )
    button_3.place(
        x=156.0,
        y=273.0,
        width=112.4794921875,
        height=39.740234375
    )

    button_image_4 = PhotoImage(
        file=relative_to_assets("button_4.png"))
    button_4 = Button(
        image=button_image_4,
        borderwidth=0,
        highlightthickness=0,
        command=kem_5k,
        relief="flat"
    )
    button_4.place(
        x=280.0,
        y=273.0,
        width=112.4794921875,
        height=39.740234375
    )
    window.resizable(False, False)
    window.mainloop()

def Uang_50k ():
    global window
    window.destroy()
    
    OUTPUT_PATH = Path(__file__).parent
    ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\Surya Baaskara\OneDrive\Documents\build\assets\frame2")


    def relative_to_assets(path: str) -> Path:
        return ASSETS_PATH / Path(path)


    window = Tk()

    window.geometry("450x773")
    window.configure(bg = "#FFFFFF")


    canvas = Canvas(
        window,
        bg = "#FFFFFF",
        height = 773,
        width = 450,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
    )

    canvas.place(x = 0, y = 0)
    image_image_1 = PhotoImage(
        file=relative_to_assets("image_1.png"))
    image_1 = canvas.create_image(
        235.0,
        397.0,
        image=image_image_1
    )

    button_image_1 = PhotoImage(
        file=relative_to_assets("button_1.png"))
    button_1 = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=kem,
        relief="flat"
    )
    button_1.place(
        x=221.0,
        y=609.0,
        width=149.0,
        height=55.0
    )

    button_image_2 = PhotoImage(
        file=relative_to_assets("button_2.png"))
    button_2 = Button(
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=kem_30k,
        relief="flat"
    )
    button_2.place(
        x=32.0,
        y=273.0,
        width=112.4794921875,
        height=39.740234375
    )

    button_image_3 = PhotoImage(
        file=relative_to_assets("button_3.png"))
    button_3 = Button(
        image=button_image_3,
        borderwidth=0,
        highlightthickness=0,
        command=kem_35k,
        relief="flat"
    )
    button_3.place(
        x=156.0,
        y=273.0,
        width=112.4794921875,
        height=39.740234375
    )

    button_image_4 = PhotoImage(
        file=relative_to_assets("button_4.png"))
    button_4 = Button(
        image=button_image_4,
        borderwidth=0,
        highlightthickness=0,
        command=kem_35k,
        relief="flat"
    )
    button_4.place(
        x=280.0,
        y=273.0,
        width=112.4794921875,
        height=39.740234375
    )
    window.resizable(False, False)
    window.mainloop()

def kem():
    global window
    window.destroy()
    
    OUTPUT_PATH = Path(__file__).parent
    ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\Surya Baaskara\OneDrive\Documents\build\assets\frame10")


    def relative_to_assets(path: str) -> Path:
        return ASSETS_PATH / Path(path)


    window = Tk()

    window.geometry("450x772")
    window.configure(bg = "#604747")


    canvas = Canvas(
        window,
        bg = "#604747",
        height = 772,
        width = 450,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
    )

    canvas.place(x = 0, y = 0)
    button_image_1 = PhotoImage(
        file=relative_to_assets("button_1.png"))
    button_1 = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=terimakasih,
        relief="flat"
    )
    button_1.place(
        x=29.0,
        y=582.0,
        width=399.0,
        height=78.0
    )

    image_image_1 = PhotoImage(
        file=relative_to_assets("image_1.png"))
    image_1 = canvas.create_image(
        229.0,
        271.0,
        image=image_image_1
    )
    window.resizable(False, False)
    window.mainloop()

def kem_5k ():
    global window
    window.destroy()
    
    OUTPUT_PATH = Path(__file__).parent
    ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\Surya Baaskara\OneDrive\Documents\Semester 3\build\assets\frame0")


    def relative_to_assets(path: str) -> Path:
        return ASSETS_PATH / Path(path)


    window = Tk()

    window.geometry("450x772")
    window.configure(bg = "#604747")


    canvas = Canvas(
        window,
        bg = "#604747",
        height = 772,
        width = 450,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
    )

    canvas.place(x = 0, y = 0)
    image_image_1 = PhotoImage(
        file=relative_to_assets("image_1.png"))
    image_1 = canvas.create_image(
        229.0,
        367.0,
        image=image_image_1
    )

    button_image_1 = PhotoImage(
        file=relative_to_assets("button_1.png"))
    button_1 = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=burger,
        relief="flat"
    )
    button_1.place(
        x=234.46990966796875,
        y=464.0,
        width=146.53009033203125,
        height=147.110107421875
    )

    button_image_2 = PhotoImage(
        file=relative_to_assets("button_2.png"))
    button_2 = Button(
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=onigiri,
        relief="flat"
    )
    button_2.place(
        x=69.0,
        y=464.0,
        width=146.53009033203125,
        height=147.110107421875
    )
    window.resizable(False, False)
    window.mainloop()

def kem_30k():
    global window
    window.destroy()
    
    OUTPUT_PATH = Path(__file__).parent
    ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\Surya Baaskara\OneDrive\Documents\Semester 3\build\assets\frame1")


    def relative_to_assets(path: str) -> Path:
        return ASSETS_PATH / Path(path)


    window = Tk()

    window.geometry("450x772")
    window.configure(bg = "#604747")


    canvas = Canvas(
        window,
        bg = "#604747",
        height = 772,
        width = 450,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
    )

    canvas.place(x = 0, y = 0)
    image_image_1 = PhotoImage(
        file=relative_to_assets("image_1.png"))
    image_1 = canvas.create_image(
        229.0,
        360.0,
        image=image_image_1
    )

    button_image_1 = PhotoImage(
        file=relative_to_assets("button_1.png"))
    button_1 = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=nasi,
        relief="flat"
    )
    button_1.place(
        x=140.0,
        y=459.0,
        width=161.0,
        height=150.0
    )
    window.resizable(False, False)
    window.mainloop()

def kem_35k():
    global window
    window.destroy()
    
    OUTPUT_PATH = Path(__file__).parent
    ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\Surya Baaskara\OneDrive\Documents\Semester 3\build\assets\frame3")


    def relative_to_assets(path: str) -> Path:
        return ASSETS_PATH / Path(path)


    window = Tk()

    window.geometry("450x772")
    window.configure(bg = "#604747")


    canvas = Canvas(
        window,
        bg = "#604747",
        height = 772,
        width = 450,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
    )

    canvas.place(x = 0, y = 0)
    image_image_1 = PhotoImage(
        file=relative_to_assets("image_1.png"))
    image_1 = canvas.create_image(
        229.0,
        363.0,
        image=image_image_1
    )

    button_image_1 = PhotoImage(
        file=relative_to_assets("button_1.png"))
    button_1 = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=onigiri,
        relief="flat"
    )
    button_1.place(
        x=234.46990966796875,
        y=464.0,
        width=146.5300750732422,
        height=147.110107421875
    )

    button_image_2 = PhotoImage(
        file=relative_to_assets("button_2.png"))
    button_2 = Button(
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=burger,
        relief="flat"
    )
    button_2.place(
        x=69.0,
        y=464.0,
        width=146.5300750732422,
        height=147.110107421875
    )
    window.resizable(False, False)
    window.mainloop()

def nasi():
    global window
    window.destroy()
    
    OUTPUT_PATH = Path(__file__).parent
    ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\Surya Baaskara\OneDrive\Documents\build\assets\frame6")


    def relative_to_assets(path: str) -> Path:
        return ASSETS_PATH / Path(path)


    window = Tk()

    window.geometry("450x772")
    window.configure(bg = "#FFFFFF")


    canvas = Canvas(
        window,
        bg = "#FFFFFF",
        height = 772,
        width = 450,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
    )

    canvas.place(x = 0, y = 0)
    image_image_1 = PhotoImage(
        file=relative_to_assets("image_1.png"))
    image_1 = canvas.create_image(
        225.0,
        386.0,
        image=image_image_1
    )

    button_image_1 = PhotoImage(
        file=relative_to_assets("button_1.png"))
    button_1 = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=hangat,
        relief="flat"
    )
    button_1.place(
        x=194.0,
        y=130.0,
        width=189.0,
        height=73.95651245117188
    )

    button_image_2 = PhotoImage(
        file=relative_to_assets("button_2.png"))
    button_2 = Button(
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=hangat,
        relief="flat"
    )
    button_2.place(
        x=194.0,
        y=300.0,
        width=189.0,
        height=73.9565200805664
    )

    button_image_3 = PhotoImage(
        file=relative_to_assets("button_3.png"))
    button_3 = Button(
        image=button_image_3,
        borderwidth=0,
        highlightthickness=0,
        command=hangat,
        relief="flat"
    )
    button_3.place(
        x=194.0,
        y=470.0,
        width=189.0,
        height=73.9565200805664
    )
    window.resizable(False, False)
    window.mainloop()

def onigiri():
    global window
    window.destroy()
    
    OUTPUT_PATH = Path(__file__).parent
    ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\Surya Baaskara\OneDrive\Documents\build\assets\frame7")


    def relative_to_assets(path: str) -> Path:
        return ASSETS_PATH / Path(path)


    window = Tk()

    window.geometry("450x772")
    window.configure(bg = "#FFFFFF")


    canvas = Canvas(
        window,
        bg = "#FFFFFF",
        height = 772,
        width = 450,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
    )

    canvas.place(x = 0, y = 0)
    image_image_1 = PhotoImage(
        file=relative_to_assets("image_1.png"))
    image_1 = canvas.create_image(
        300.0,
        515.0,
        image=image_image_1
    )

    button_image_1 = PhotoImage(
        file=relative_to_assets("button_1.png"))
    button_1 = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=hangat,
        relief="flat"
    )
    button_1.place(
        x=195.0,
        y=327.0,
        width=189.0,
        height=73.95654296875
    )

    button_image_2 = PhotoImage(
        file=relative_to_assets("button_2.png"))
    button_2 = Button(
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=hangat,
        relief="flat"
    )
    button_2.place(
        x=195.0,
        y=165.0,
        width=189.0,
        height=73.95654296875
    )
    window.resizable(False, False)
    window.mainloop()

def burger():
    global window
    window.destroy()
    
    OUTPUT_PATH = Path(__file__).parent
    ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\Surya Baaskara\OneDrive\Documents\build\assets\frame8")


    def relative_to_assets(path: str) -> Path:
        return ASSETS_PATH / Path(path)


    window = Tk()

    window.geometry("450x772")
    window.configure(bg = "#FFFFFF")


    canvas = Canvas(
        window,
        bg = "#FFFFFF",
        height = 772,
        width = 450,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
    )

    canvas.place(x = 0, y = 0)
    image_image_1 = PhotoImage(
        file=relative_to_assets("image_1.png"))
    image_1 = canvas.create_image(
        225.0,
        386.0,
        image=image_image_1
    )

    button_image_1 = PhotoImage(
        file=relative_to_assets("button_1.png"))
    button_1 = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=hangat,
        relief="flat"
    )
    button_1.place(
        x=205.0,
        y=130.0,
        width=189.0,
        height=73.95654296875
    )

    button_image_2 = PhotoImage(
        file=relative_to_assets("button_2.png"))
    button_2 = Button(
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=hangat,
        relief="flat"
    )
    button_2.place(
        x=205.0,
        y=459.0,
        width=189.0,
        height=73.95654296875
    )

    button_image_3 = PhotoImage(
        file=relative_to_assets("button_3.png"))
    button_3 = Button(
        image=button_image_3,
        borderwidth=0,
        highlightthickness=0,
        command=hangat,
        relief="flat"
    )
    button_3.place(
        x=205.0,
        y=297.0,
        width=189.0,
        height=73.95654296875
    )
    window.resizable(False, False)
    window.mainloop()

def hangat():
    global window
    window.destroy()

    OUTPUT_PATH = Path(__file__).parent
    ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\Surya Baaskara\OneDrive\Documents\build\assets\frame15")


    def relative_to_assets(path: str) -> Path:
        return ASSETS_PATH / Path(path)


    window = Tk()

    window.geometry("450x772")
    window.configure(bg = "#604747")


    canvas = Canvas(
        window,
        bg = "#604747",
        height = 772,
        width = 450,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
    )

    canvas.place(x = 0, y = 0)
    image_image_1 = PhotoImage(
        file=relative_to_assets("image_1.png"))
    image_1 = canvas.create_image(
        225.0,
        370.0,
        image=image_image_1
    )

    button_image_1 = PhotoImage(
        file=relative_to_assets("button_1.png"))
    button_1 = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=hangatin,
        relief="flat"
    )
    button_1.place(
        x=47.0,
        y=423.0,
        width=358.0,
        height=108.0
    )

    button_image_2 = PhotoImage(
        file=relative_to_assets("button_2.png"))
    button_2 = Button(
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=jadi,
        relief="flat"
    )
    button_2.place(
        x=46.0,
        y=545.0,
        width=358.0,
        height=108.0
    )
    window.resizable(False, False)
    window.mainloop()

def hangatin():
    global window
    window.destroy()

    OUTPUT_PATH = Path(__file__).parent
    ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\Surya Baaskara\OneDrive\Documents\Semester 3\build\assets\frame2")


    def relative_to_assets(path: str) -> Path:
        return ASSETS_PATH / Path(path)


    window = Tk()

    window.geometry("450x772")
    window.configure(bg = "#604747")


    canvas = Canvas(
        window,
        bg = "#604747",
        height = 772,
        width = 450,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
    )

    canvas.place(x = 0, y = 0)
    button_image_1 = PhotoImage(
        file=relative_to_assets("button_1.png"))
    button_1 = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=jadi,
        relief="flat"
    )
    button_1.place(
        x=29.0,
        y=471.0,
        width=399.0,
        height=78.0
    )

    image_image_1 = PhotoImage(
        file=relative_to_assets("image_1.png"))
    image_1 = canvas.create_image(
        229.0,
        227.0,
        image=image_image_1
    )
    window.resizable(False, False)
    window.mainloop()

def jadi():
    global window
    window.destroy()

    OUTPUT_PATH = Path(__file__).parent
    ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\Surya Baaskara\OneDrive\Documents\build\assets\frame13")


    def relative_to_assets(path: str) -> Path:
        return ASSETS_PATH / Path(path)


    window = Tk()

    window.geometry("450x772")
    window.configure(bg = "#604747")


    canvas = Canvas(
        window,
        bg = "#604747",
        height = 772,
        width = 450,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
    )

    canvas.place(x = 0, y = 0)
    button_image_1 = PhotoImage(
        file=relative_to_assets("button_1.png"))
    button_1 = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=terimakasih,
        relief="flat"
    )
    button_1.place(
        x=38.0,
        y=590.0,
        width=375.0,
        height=94.0
    )

    image_image_1 = PhotoImage(
        file=relative_to_assets("image_1.png"))
    image_1 = canvas.create_image(
        228.0,
        292.0,
        image=image_image_1
    )
    window.resizable(False, False)
    window.mainloop()

def terimakasih():
    global window
    window.destroy()
    
    OUTPUT_PATH = Path(__file__).parent
    ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\Surya Baaskara\OneDrive\Documents\build\assets\frame14")


    def relative_to_assets(path: str) -> Path:
        return ASSETS_PATH / Path(path)


    window = Tk()

    window.geometry("450x772")
    window.configure(bg = "#604747")


    canvas = Canvas(
        window,
        bg = "#604747",
        height = 772,
        width = 450,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
    )

    canvas.place(x = 0, y = 0)
    image_image_1 = PhotoImage(
        file=relative_to_assets("image_1.png"))
    image_1 = canvas.create_image(
        225.0,
        299.0,
        image=image_image_1
    )

    button_image_1 = PhotoImage(
        file=relative_to_assets("button_1.png"))
    button_1 = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("Selesai"),
        relief="flat"
    )
    button_1.place(
        x=38.0,
        y=603.0,
        width=375.0,
        height=94.0
    )
    window.resizable(False, False)
    window.mainloop()

menu_awal()