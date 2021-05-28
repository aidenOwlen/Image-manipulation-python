# -*- coding:Utf-8 -*-

from tkinter import *
from tkinter import filedialog
import os
import sys
from PIL import Image,ImageTk,ImageFilter,ImageDraw,ImageFont,ImageOps, ImageEnhance
from PIL.ImageColor import getcolor, getrgb
from PIL.ImageOps import grayscale
import tkinter.ttk
import time
from threading import Thread,RLock

drawingg = 0
speed = 5
bakhh = 0
VarTPage = 0
class FullScreenApp(object):
    def __init__(self, master, **kwargs):
        self.master=master
        pad=3
        self._geom='200x200+0+0'
        master.geometry("{0}x{1}+0+0".format(
            master.winfo_screenwidth()-pad, master.winfo_screenheight()-pad))
LastVarFrame = 0
XX = 0
YY = 0
MoveX = 0
MoveY = 0
ShirtName =  "black.png"
ShirtNamed = "black.png"

CWD = os.getcwd()

COLORS = ["Color",'black', "white", "yellow", "orange", "blue", "grey", "green", "red"]

Ba3jj = False
The_Path = os.path.join(os.environ["HOMEPATH"],"desktop")
filename = ""
ROTATION = 0
D = 2
C = 2
jj3 = ""

def BackingShirt():
    global kouchi2, smk
    kouchi2 = kouchi.split(".")
    
    try:
        smk = Image.open("Back/"+kouchi2[0]+"BACK."+kouchi2[1])
        smk.save("Back/{}BACKC.png".format(kouchi2[0]))
    except:
        print("option not avalaible for this product")
    
def restart_program():
    """Restarts the current program.
    Note: this function does not return. Any cleanup action (like
    saving data) must be done before calling this function."""
    python = sys.executable
    os.execl(python, python, * sys.argv)
    
def BackProduct():
        global mkss

        try:
            mkss = PhotoImage(file = "Back/{}BACKC.png".format(kouchi2[0]))
            can2.itemconfig(ImageX2, image = mkss)
        except:
            print("option not avalaible for this product")
            
        BackProduct.config(bg="grey")
        FrontProduct.config(bg="dark grey")
    
        

def FrontProduct():
    FrontProduct.config(bg="grey")
    BackProduct.config(bg="dark grey")
    Combiner()
    
    

def DeleteColor():
    global Liste_Coul,CustomColorBox
    To_del = CustomColorBoxDeg.get()
    Liste_Coul.remove(To_del)
    CustomColorBox.config(values = Liste_Coul)
    ff = open("cou.txt", "w")
    for i in Liste_Coul:
        if i != "":
            ff.write("{}\n".format(i))
    ff.close()
    CustomColorBox.current(0)
        
    
    
def rgb2hex(r,g,b):
    hex = "#{:02x}{:02x}{:02x}".format(r,g,b)
    return hex

def hex2rgb(hexcode):
    rgb = tuple(map(ord,hexcode[1:].decode('hex')))
    return rgb

def CustomColor():
    global jj3 , Ba3jj
    The_Custom_Color = CustomColorBox.get()
    The_Custom_Color = The_Custom_Color.split(",")
    The_Custom_Color_Red = int(The_Custom_Color[0])
    The_Custom_Color_Green = int(The_Custom_Color[1])
    The_Custom_Color_Blue = int(The_Custom_Color[2])
    jj3 = rgb2hex(The_Custom_Color_Red, The_Custom_Color_Green, The_Custom_Color_Blue)
    Ba3jj = True
    ChangeColor(jj3)
    CustomColor.config(bg=jj3)
    

    
def AddColor():
    global The_Blue, The_Red, The_Green, kkk3
    try:
        BlueColorDeg.get() == int(BlueColorDeg.get())
        The_Blue = BlueColorDeg.get()
        if The_Blue > 255 or The_Blue < 0:
            raise TypeError
    except:
        The_Blue = 0

    try:
        GreenColorDeg.get() == int(GreenColorDeg.get())
        The_Green = GreenColorDeg.get()
        if The_Green > 255 or The_Green < 0:
            raise TypeError
    except:
            The_Green = 255

    try:
        RedColorDeg.get() == int(RedColorDeg.get())
        The_Red = RedColorDeg.get()
        if The_Red > 255 or The_Red <0:
            raise TypeError
    except:
        The_Red = 255

    ff = open("cou.txt","a")
    ff.write("{},{},{}\n".format(str(The_Red),str(The_Green),str(The_Blue)))
    ff.close()
    AddCustom()
    kkk3 = rgb2hex(The_Red, The_Green, The_Blue)
    AddColor.config(bg=kkk3)
    

def AddCustom():
    global Liste_Coul
    ff = open("cou.txt","r")
    Liste_Coul = ff.readlines()
    for i in Liste_Coul:
        if i == "" or i == "\n":
            Liste_Coul.remove(i)
    
    ff.close()
    CustomColorBox.config(values = Liste_Coul)
            
def ViewAll():
    LastFrame.grid_remove()
    AllFrame.grid(row=0,column=0)
    
def NextX():
    global LastVarFrame
    LastFrameHH()
    
    frame2.grid_remove()
    LastVarFrame = 1
      
def AllQuit(event):
    fenetre.destroy()
    fenetre.quit()

def AllBack(event):
    AllFrame.grid_remove()
    LastFrame.grid()
 
    
def LastBack():
    LastFrame.grid_remove()
    frame2.grid()

def Finish():
    mkkkk = Image.open(Combined)
    mkkkk.save("SavedProducts/{}".format(Combined))
    fenetre.destroy()
    fenetre.quit()
    
def DefaultFinal():
    global m333
    m333 = PhotoImage(file = Combined)
    LastCan.itemconfig(FinalImage, image = m333)
    
def SaveText2():
    global m3za, LastCan, FinalImage, drawingg
    if drawingg == 1:
        kbch3 = Combined.split(".")
        kbch3 = kbch3[0]
        m3izou = Image.open("TextAdded{}.png".format(kbch3))
        m3izou.save(Combined)
        m3za = PhotoImage(file = Combined)
        LastCan.itemconfig(FinalImage, image = m3za)
        drawingg = 0
    else:
        print("You have not drawed any text")
    

def CancelText2():
    global m3za
    m3za = PhotoImage(file = Combined)
    LastCan.itemconfig(FinalImage, image = m3za)

def FinalRotate():
    global m3iz, m3izou,LastCan,LastImg
    m3iz = Image.open(Combined)
    m3iz = m3iz.rotate(FinalComboDeg.get())
    m3iz.save("RotatedFinal.png")
    m3izou = PhotoImage(file="RotatedFinal.png")
    
    LastCan.itemconfig(FinalImage, image = m3izou)

def ZoomIn():
    global zoomed, LastCan, FinalImage, zoomed2,D, LastImg, ma33
    D += 1
    zoomed = ma33.zoom(D,D)
    zoomed2 = zoomed.subsample(2,2)
    LastCan.itemconfig(FinalImage, image = zoomed2)

def ZoomOut():
    global sampled, sampled2, FinalImage, LastCan, C,LastImg,ma33
    C += 1
    sampled = ma33.subsample(C,C)
    sampled2 = sampled.zoom(2,2)
    LastCan.itemconfig(FinalImage,image=sampled2)

def A3():
    global img2, Img22, CombinedImage, XX, YY
    XX = 297
    YY = 420
    img2 = Image.open(ShirtNamed2[0]+"X.png")
    img2 = img2.convert("RGBA")
    Img22 = Image.open(BaseImaged)
    Img22 = Img22.convert("RGBA")
    Img22 = Img22.resize((XSize + XX,YSize + YY))
    img2.paste(Img22, (XSize+MoveX,80+YSize+MoveY),Img22)
    img2.save(Combined)
    CombinedImage = PhotoImage(file = Combined)
    can2.itemconfig(ImageX2, image = CombinedImage)
    
def A4():
    global img2, Img22, CombinedImage, XX, YY
    XX = 210
    YY = 297
    img2 = Image.open(ShirtNamed2[0]+"X.png")
    img2 = img2.convert("RGBA")
    Img22 = Image.open(BaseImaged)
    Img22 = Img22.convert("RGBA")
    Img22 = Img22.resize((XSize+XX,YSize+YY))
    img2.paste(Img22, (XSize+MoveX,80+YSize+MoveY),Img22)
    img2.save(Combined)
    CombinedImage = PhotoImage(file = Combined)
    can2.itemconfig(ImageX2, image = CombinedImage)
                      
def Combiner():
    global img2, Img22, CombinedImage, XX, YY
    img2 = Image.open(ShirtNamed2[0]+"X.png")
    img2 = img2.convert("RGBA")

    Img22 = Image.open(BaseImaged)
    Img22 = Img22.convert("RGBA")
    Img22 = Img22.resize((XSize+XX,YSize+YY))

    img2.paste(Img22, (XSize+MoveX, 80+YSize+MoveY), Img22)
    img2.save(Combined)

    CombinedImage = PhotoImage(file = Combined)

    can2.itemconfig(ImageX2, image = CombinedImage)

def BackX():
  restart_program()
def Next1():
    
    frame.pack_forget()
    
    global BackProduct, FrontProduct,DeleteColor,Liste_Coul,A3,A4,SpeedDeg,ComboSpeed,GreenColorDeg,bakhh,BackX, CustomColorBox, CustomColorBoxDeg, AddColor,RedColorDeg,RedColor,ListeRGB1,CustomColor,ListeRGB2, ListeRGB3, GreebColorDeg, GreenColor, BlueColor,BlueColorDeg,ImageX2, NextX,Combined,CombinedImage,BaseImaged,frame2, img2,Img2, ShirtNamed2, can2, ImageX, XSize,YSize, Imgg22, img22,ImageX2, labelcol,listecolor,RotBut,RotBut2, ResetBut,LabelMove,MLeft,MUp,MRight,MDown,RLeft,RUp,RRight,RDown,LabelRes,TPage
        #FRAME 2
    if bakhh == 0:
        frame2 = Frame(fenetre)
        frame2.grid(row=0,column=0)
        img2 = Image.open(ShirtName)
        ShirtNamed2 = ShirtNamed.split(".png")
        img2.save(ShirtNamed2[0] + "X.png")
        can2 = Canvas(frame2, width = fenetre.winfo_screenwidth()-50, height = screen_height-100, bg = "dark grey")
        can2.grid(row=0,column=0)
        can2.create_window(2400,6000, anchor = NW, window=Label(frame2, text=""))
        
        Img2 = PhotoImage(file=ShirtNamed2[0]+"X.png")    


        XSize = int(img2.size[0]/3)
        YSize = int(img2.size[1]/3)

        
        Img22 = Image.open(filename)
        BaseImaged2 = BaseImage.split(".png")
        BaseImaged = BaseImaged2[0] +"Z.png"
        Img22.save(BaseImaged)
        Combined = BaseImaged2[0] + ShirtNamed2[0] + ".png"
        CombinedImage = PhotoImage(file = "")
        
        

        ImageX2 = can2.create_image(30,80,anchor=NW,image=CombinedImage)
        Combiner()
        

        



        labelcol = Label(frame2, text="Change product's color : ", fg = "red", bg="dark grey",font=("Times",12, "italic"))
        can2.create_window(img2.size[0]+100, 40, window = labelcol, anchor = NW)


        listecolor = {"White":"#FFFAFA","LightGrey":"#778899","DarkGrey":"#A9A9A9",\
                      "Black": "#191919","LightBlue":"#ADD8E6","DeepSkyBlue":"#00BFFF",\
                      "DodgerBlue":"#1E90FF","LawnGreen":"#7CFC00","Gold":"#FFD700",\
                      "Orange":"#FFA500","LightCoral":"#F08080","Orangered":"#FF4500",\
                      "MediumPurple":"#9370DB","SpringGreen":"#00FF7F","Aqua":"#00FFFF",\
                      "Brown":"#A52A2A","DimGrey":"#696969","SlateGrey":"#708090"}


        TPage = Button(frame2,text="Base image treatment", bg ="dark grey", fg ="dark blue", width = int(XSize/2),command=TPage)
        can2.create_window(10,10,window=TPage, anchor = NW)
        k = 40
        for i,j in listecolor.items():
            k+=25
            can2.create_window(img2.size[0]+100,k,window=Button(frame2,text=i, bg=j,command=lambda j=i:ChangeColor(j), width = 10),anchor=NW)

        CustomColor = Button(frame2, text = "Custom Color", bg ="dark grey", width = 10, command = CustomColor)
        can2.create_window(img2.size[0]+100,k+25, window=CustomColor, anchor = NW)

        DeleteColor = Button(frame2, text = "Delete Color", bg ="dark grey", width = 10, command = DeleteColor)
        can2.create_window(img2.size[0] + 333, k+25, window=DeleteColor, anchor =NW)
        
        CustomColorBoxDeg = StringVar()
        CustomColorBox = tkinter.ttk.Combobox(frame2, textvariable = CustomColorBoxDeg,values =[], state = "readonly")
        can2.create_window(img2.size[0]+185, k+27, window = CustomColorBox, anchor = NW)
        ff = open("cou.txt", "r")
        Liste_Coul = ff.readlines()
        for i in Liste_Coul:
            if i == "" or i == "\n" or i == " ":
                Liste_Coul.remove(i)
                
        Liste_Coul.insert(0,"125,0,0")
            
        CustomColorBox["value"] = Liste_Coul
        
        CustomColorBox.current(0)
        ff.close()

        AddColor = Button(frame2, text="Add Color", bg="dark grey", width = 10,command = AddColor)
        can2.create_window(img2.size[0]+100,k+50, window=AddColor, anchor = NW)

        RedColorDeg = IntVar()
        RedColor = tkinter.ttk.Combobox(frame2, textvariable=RedColorDeg, width = 4)
        ListeRGB1 = list(range(256))
        ListeRGB1.insert(0,"red")
        RedColor["value"] = ListeRGB1
        RedColor.current(0)
        can2.create_window(img2.size[0]+185,k+52,window=RedColor,anchor=NW)
        

        GreenColorDeg = IntVar()
        GreenColor = tkinter.ttk.Combobox(frame2,textvariable=GreenColorDeg, width = 4)
        can2.create_window(img2.size[0]+235, k+52,window =GreenColor,anchor=NW)

        BlueColorDeg = IntVar()
        BlueColor = tkinter.ttk.Combobox(frame2, textvariable = BlueColorDeg, width = 4)
        can2.create_window(img2.size[0]+285, k+52, window = BlueColor, anchor = NW)

        
        ListeRGB2 = list(range(256))
        ListeRGB2.insert(0, "green")
        GreenColor["value"] = ListeRGB2
        GreenColor.current(0)
        
        ListeRGB3 = list(range(256))
        ListeRGB3.insert(0,"blue")
        BlueColor["value"] = ListeRGB3
        BlueColor.current(0)
        
        

        
        
        

        


            
        RotBut = Button(frame2,text="Rotate product",bg="dark grey",command=Rotate, width = 15)
        can2.create_window(img2.size[0]+100, k+125,window=RotBut,anchor=NW)


        RotBut2 = Button(frame2,text="Rotate base image", bg="dark grey", command=Rotate2, width = 15)
        can2.create_window(img2.size[0]+100,k+155,window=RotBut2,anchor=NW)

        ResetBut = Button(frame2,text="Reset", bg="dark grey",fg="black",command=ResetBut1, width = 15)
        can2.create_window(img2.size[0]+100, k+185,window=ResetBut,anchor=NW)

        BackProduct = Button(frame2, text = "Back", bg ="dark grey", width = 13, height = 2,command = BackProduct)
        can2.create_window(img2.size[0]+ 220, k+125, window = BackProduct, anchor = NW)

        FrontProduct = Button(frame2, text = "Front", bg ="dark grey", width = 13, height = 2, command = FrontProduct)
                              
        can2.create_window(img2.size[0]+ 220, k+170, window = FrontProduct, anchor = NW)


        NextX = Button(frame2, text = "Next =>", bg = "dark grey", fg = "blue", width = 30,command = NextX)
        can2.create_window(img2.size[0] + 100, k + 225, window = NextX, anchor = NW)

        BackX = Button(frame2, text = "<= Back", bg ="dark grey", fg = "red", width = 30, command = BackX)
        can2.create_window(img2.size[0] + 100, k+250, window = BackX, anchor = NW)

        LabelMove = Label(frame2, text="Move base image", bg="dark grey",fg="black")
        can2.create_window(img2.size[0] +230,135, window=LabelMove,anchor=NW)
        MLeft = Button(frame2,text="⇐", bg="dark grey",command =MLeft)
        can2.create_window(img2.size[0] + 236,135+60,window=MLeft,anchor=NW)
        MUp = Button(frame2,text="⇑",bg="dark grey", command = MUp)
        can2.create_window(img2.size[0]+40+230,135+47,window=MUp)
        MRight = Button(frame2,text="⇒",bg="dark grey",command = MRight)
        can2.create_window(img2.size[0]+50+230,135+60, window=MRight,anchor=NW)
        MDown = Button(frame2, text="⇓", bg="dark grey", command =MDown)
        can2.create_window(img2.size[0]+40+230,135+99,window = MDown)
        
        SpeedDeg = IntVar()
        ComboSpeed = tkinter.ttk.Combobox(frame2, textvariable = SpeedDeg)
        can2.create_window(img2.size[0]+50+230+50, 135+60, window = ComboSpeed, anchor = NW)
        ListeSpeed = list(range(30))
        ListeSpeed.insert(0,"Speed mouvement")
        ComboSpeed["value"] = ListeSpeed
        ComboSpeed.current(0)
        

        LabelRes = Label(frame2, text="Resize base image", bg="dark grey",fg="black")
        can2.create_window(img2.size[0] +230,290, window=LabelRes,anchor=NW)
        RLeft = Button(frame2,text="-", bg="dark grey",command =RLeft)
        can2.create_window(img2.size[0]+240,135+60+145,window=RLeft,anchor=NW)
        RUp = Button(frame2,text="+",bg="dark grey", command = RUp)
        can2.create_window(img2.size[0]+40+230,135+47+145,window=RUp)
        RRight = Button(frame2,text="+",bg="dark grey",command = RRight)
        can2.create_window(img2.size[0]+50+230,135+60+145, window=RRight,anchor=NW)
        RDown = Button(frame2, text="-", bg="dark grey", command =RDown)
        can2.create_window(img2.size[0]+40+230,135+99+145,window = RDown)

        A4 = Button(frame2, text = "A4", bg = "dark grey", width =6, fg ="dark red", command = A4)
        can2.create_window(img2.size[0]+350, 135+47+150, window = A4, anchor = NW)

        A3 = Button(frame2, text = "A3", bg ="dark grey", width = 6, fg = "dark blue",command = A3)
        can2.create_window(img2.size[0]+350,135+99+125, window = A3,anchor = NW)
        
        ys = Scrollbar(frame2, orient='vertical', command=can2.yview)
        ys.grid(row=0, column=1, sticky = "ns")
        can2.configure(yscrollcommand=ys.set, scrollregion=can2.bbox('all'))
        can2.yview_moveto(0)

        xs = Scrollbar(frame2, orient='horizontal', command=can2.xview)
        xs.grid(row=1, column=0, sticky = "we")
        can2.configure(xscrollcommand=xs.set, scrollregion=can2.bbox('all'))
        can2.xview_moveto(0)
        bakhh = 1
        app=FullScreenApp(fenetre)
    else:
        frame2.grid()
        img = Image.open(ShirtName)
        ShirtNamed2 = ShirtNamed.split(".png")
        img.save(ShirtNamed2[0] + "X.png")
        Img2 = PhotoImage(file = ShirtNamed2[0]+"X.png")
        Img22 = Image.open(filename)
        BaseImaged2 = BaseImage.split(".png")
        BaseImaged = BaseImaged2[0] + "Z.png"
        Img22.save(BaseImaged)
        Combined = BaseImaged2[0] + ShirtNamed2[0] + ".png"
        CombinedImage = PhotoImage(file = "")
        Combiner()
        
        
        
        

def Pillows():
    global temp,kouchi,shirtmage,ShirtName,ShirtNamed,ResShirt,BACKSHIRT,ShirtNameB3,ShirtNamed11,ShirtNamedB3,ShirtNamed11B3,ResShirtB3
    ShirtName =  filedialog.askopenfilename(initialdir = "pillows/",title = "Choose image", filetypes = (("png files","*.png"),("jpg files", "*.jpg"),("gif files", "*.gif"),("Jpeg files","*.jpeg")) )
    ShirtNamed = ShirtName.split("/")
    ShirtNamed = ShirtNamed[len(ShirtNamed)-1]
    ShirtNamed11 = ShirtNamed.split(".")
    
    kouchi = ShirtNamed11[0] + "." + ShirtNamed11[1]
    ShirtNamed11 = ShirtNamed11[0]
    
   
        
       
    

    ResShirt = Image.open(ShirtName)
    ResShirt = ResShirt.resize((243,243))
    ResShirt.save("{}/shirts/Resize/{}.png".format(CWD, ShirtNamed11))
    shirtmage = PhotoImage(file = "{}/shirts/Resize/{}.png".format(CWD, ShirtNamed11))
    LabelImg2.configure(image = shirtmage)
    ShirtNameB3 = ShirtName
    ShirtNamedB3 = ShirtNamed
    ShirtNamed11B3 = ShirtNamed11
    ResShirtB3 = ResShirt
    BackingShirt()

def Phones():
    global temp,kouchi,shirtmage,ShirtName,ShirtNamed,ResShirt,BACKSHIRT,ShirtNameB3,ShirtNamed11,ShirtNamedB3,ShirtNamed11B3,ResShirtB3
    ShirtName =  filedialog.askopenfilename(initialdir = "phones/",title = "Choose image", filetypes = (("png files","*.png"),("jpg files", "*.jpg"),("gif files", "*.gif"),("Jpeg files","*.jpeg")) )
    ShirtNamed = ShirtName.split("/")
    ShirtNamed = ShirtNamed[len(ShirtNamed)-1]
    ShirtNamed11 = ShirtNamed.split(".")
    
    
    
    kouchi = ShirtNamed11[0] + "." + ShirtNamed11[1]
    ShirtNamed11 = ShirtNamed11[0]
    
    

    ResShirt = Image.open(ShirtName)
    ResShirt = ResShirt.resize((243,243))
    ResShirt.save("{}/shirts/Resize/{}.png".format(CWD, ShirtNamed11))
    shirtmage = PhotoImage(file = "{}/shirts/Resize/{}.png".format(CWD, ShirtNamed11))
    LabelImg2.configure(image = shirtmage)
    ShirtNameB3 = ShirtName
    ShirtNamedB3 = ShirtNamed
    ShirtNamed11B3 = ShirtNamed11
    ResShirtB3 = ResShirt
    BackingShirt()


def TShirts():
    global temp,kouchi,BACKSHIRT, shirtmage,ShirtName,ShirtNamed,ResShirt,ShirtNamed11,ShirtNamedB3,ShirtNamedB3,ShirtNamed11B3,ResShirtB3,ShirtNameB3
    ShirtName =  filedialog.askopenfilename(initialdir = "shirts/",title = "Choose image", filetypes = (("png files","*.png"),("jpg files", "*.jpg"),("gif files", "*.gif"),("Jpeg files","*.jpeg")) )
    ShirtNamed = ShirtName.split("/")
    ShirtNamed = ShirtNamed[len(ShirtNamed)-1]
    ShirtNamed11 = ShirtNamed.split(".")
    
    kouchi = ShirtNamed11[0] + "." + ShirtNamed11[1]
    ShirtNamed11 = ShirtNamed11[0]
    
    
    
    

    ResShirt = Image.open(ShirtName)
    ResShirt = ResShirt.resize((243,243))
    ResShirt.save("{}/shirts/Resize/{}.png".format(CWD, ShirtNamed11))
    shirtmage = PhotoImage(file = "{}/shirts/Resize/{}.png".format(CWD, ShirtNamed11))
    LabelImg2.configure(image = shirtmage)
    ShirtNameB3 = ShirtName
    ShirtNamedB3 = ShirtNamed
    ShirtNamed11B3 = ShirtNamed11
    ResShirtB3 = ResShirt
    BackingShirt()
    

    
def Other():
    global temp,kouchi,BACKSHIRT, shirtmage,ShirtName,ShirtNamed,ResShirt,ShirtNamed11,ShirtNamedB3,ShirtNamedB3,ShirtNamed11B3,ResShirtB3,ShirtNameB3
    ShirtName =  filedialog.askopenfilename(initialdir = "Other/",title = "Choose image", filetypes = (("png files","*.png"),("jpg files", "*.jpg"),("gif files", "*.gif"),("Jpeg files","*.jpeg")) )
    ShirtNamed = ShirtName.split("/")
    ShirtNamed = ShirtNamed[len(ShirtNamed)-1]
    ShirtNamed11 = ShirtNamed.split(".")
    
    kouchi = ShirtNamed11[0] + "." + ShirtNamed11[1]
    ShirtNamed11 = ShirtNamed11[0]
    
    
    
    

    ResShirt = Image.open(ShirtName)
    ResShirt = ResShirt.resize((243,243))
    ResShirt.save("{}/shirts/Resize/{}.png".format(CWD, ShirtNamed11))
    shirtmage = PhotoImage(file = "{}/shirts/Resize/{}.png".format(CWD, ShirtNamed11))
    LabelImg2.configure(image = shirtmage)
    ShirtNameB3 = ShirtName
    ShirtNamedB3 = ShirtNamed
    ShirtNamed11B3 = ShirtNamed11
    ResShirtB3 = ResShirt
    BackingShirt()
    
    
    

def Sharpness():
    global TImg
    maa = Image.open("kk.png")
    enhancer = ImageEnhance.Sharpness(maa)
    maa = enhancer.enhance(SharpnessDeg.get())
    maa.save("kktemp.png")

    TImg = PhotoImage(file = "kktemp.png")
    Tcan.itemconfigure(TImage, image = TImg)

def Brightness():
    global TImg
    maa = Image.open("kk.png")
    enhancer = ImageEnhance.Brightness(maa)
    maa = enhancer.enhance(BrightnessDeg.get())
    maa.save("kktemp.png")

    TImg = PhotoImage(file = "kktemp.png")
    Tcan.itemconfigure(TImage, image = TImg)

def Colors():
    global TImg
    maa = Image.open("kk.png")
    enhancer = ImageEnhance.Color(maa)
    maa = enhancer.enhance(ColorsDeg.get())
    maa.save("kktemp.png")

    TImg = PhotoImage(file = "kktemp.png")
    Tcan.itemconfigure(TImage, image = TImg)
def Contrast():
    global TImg
    maa = Image.open("kk.png")
    enhancer = ImageEnhance.Contrast(maa)
    maa = enhancer.enhance(ContrastDeg.get())
    maa.save("kktemp.png")

    TImg = PhotoImage(file = "kktemp.png")
    Tcan.itemconfigure(TImage, image = TImg)
    

def Invert():
    global TImg
    mg = Image.open("kk.png")
    mg = ImageOps.invert(mg)
    mg.save("kktemp.png")
    TImg = PhotoImage(file = "kktemp.png")
    Tcan.itemconfigure(TImage, image = TImg)
    
def Colorize():
    global TImg
    Color1 = Colorize1.get()
    Color2 = Colorize2.get()
    mg = Image.open("kk.png")
    mg = ImageOps.grayscale(mg)
    mg = ImageOps.colorize(mg, Color1, Color2)
    mg.save("kktemp.png")
    TImg = PhotoImage(file = "kktemp.png")
    Tcan.itemconfigure(TImage,image = TImg)


def Expand():
    global TImg
    try :
        value = ExpandDeg.get()
    except :
        value = 50

    try:
        col = ExpandColor.get()
    except:
        col = "black"

    mg = Image.open("kk.png")
    mg = ImageOps.expand(mg, value,col)
    mg.save("kktemp.png")
    TImg = PhotoImage(file = "kktemp.png")
    Tcan.itemconfigure(TImage, image = TImg)
    

def Flip():
    global TImg
    mg = Image.open("kk.png")
    mg = ImageOps.flip(mg)
    mg.save("kktemp.png")
    TImg = PhotoImage(file = "kktemp.png")
    Tcan.itemconfigure(TImage, image = TImg)

def Mirror():
    global TImg
    mg = Image.open("kk.png")
    mg = ImageOps.mirror(mg)
    mg.save("kktemp.png")
    TImg = PhotoImage(file = "kktemp.png")
    Tcan.itemconfigure(TImage, image = TImg)    
    

def Solarize():
    global TImg
    try :
        value = SolarizeDeg.get()
    except:
        value = 128
    
    mg = Image.open("kk.png")
    mg = ImageOps.solarize(mg,value)
    mg.save("kktemp.png")
    TImg = PhotoImage(file = "kktemp.png")
    Tcan.itemconfigure(TImage, image = TImg)  

def Crop():
    global TImg
    try :
        value = CropDeg.get()
    except:
        value = 10
    
    mg = Image.open("kk.png")
    mg = ImageOps.crop(mg,value)
    mg.save("kktemp.png")
    TImg = PhotoImage(file = "kktemp.png")
    Tcan.itemconfigure(TImage, image = TImg) 

def GrayScale():
    global TImg

    
    mg = Image.open("kk.png")
    mg = ImageOps.grayscale(mg)
    mg.save("kktemp.png")
    TImg = PhotoImage(file = "kktemp.png")
    Tcan.itemconfigure(TImage, image = TImg)




def Detail():
    global Timg
    mage = Image.open("kk.png")
    mage = mage.filter(ImageFilter.DETAIL)
    mage.save("kktemp.png")
    Timg = PhotoImage(file = "kktemp.png")
    Tcan.itemconfigure(TImage,image = Timg)
    mage.close()
    

def Enhance():
    global Timg
    mage = Image.open("kk.png")
    
    try:
        
        valuee = EnhanceDeg.get()
        
        if valuee == 1:
            
            mage = mage.filter(ImageFilter.EDGE_ENHANECE)
        else:
            
            mage = mage.filter(ImageFilter.EDGE_ENHANCE_MORE)
    except:
        
        mage = mage.filter(ImageFilter.EDGE_ENHANCE_MORE)
        
    
    
    mage.save("kktemp.png")
    Timg = PhotoImage(file = "kktemp.png")
    Tcan.itemconfigure(TImage,image = Timg)
    mage.close()

def Emboss():
    global Timg
    mage = Image.open("kk.png")
    mage = mage.filter(ImageFilter.EMBOSS)
    mage.save("kktemp.png")
    Timg = PhotoImage(file = "kktemp.png")
    Tcan.itemconfigure(TImage,image = Timg)
    mage.close()

def Smooth():
    global Timg
    mage = Image.open("kk.png")
    try:
        value = SmoothDeg.get()
        
        if value == 1:
            
            mage = mage.filter(ImageFilter.SMOOTH)
        else:
            
            mage = mage.filter(ImageFilter.SMOOTH_MORE)
    except:
        
        mage = mage.filter(ImageFilter.SMOOTH_MORE)
        
    
    
    mage.save("kktemp.png")
    Timg = PhotoImage(file = "kktemp.png")
    Tcan.itemconfigure(TImage,image = Timg)
    mage.close()

def Sharpen():
    global Timg
    mage = Image.open("kk.png")
    mage = mage.filter(ImageFilter.SHARPEN)
    mage.save("kktemp.png")
    Timg = PhotoImage(file = "kktemp.png")
    Tcan.itemconfigure(TImage,image = Timg)
    mage.close()

def FindEdges():
    global Timg
    mage = Image.open("kk.png")
    mage = mage.filter(ImageFilter.FIND_EDGES)
    mage.save("kktemp.png")
    Timg = PhotoImage(file = "kktemp.png")
    Tcan.itemconfigure(TImage,image = Timg)
    mage.close()

def DrawText2():
  
    global m3za,Couleur2, XC2, YC2, WT2, FT2
    try:
        Couleur2 = TColor2.get()
        if Couleur2 == "Color":
            raise NameError
    except:
        Couleur2 = "black"

    try:
        FT2 = Le_Font2.get()
        if FT2 == "Fonts":
            raise NameError
    except:
        FT2 = "arial.ttf"

    try:
        YC2 = Y_Texte2.get()
        YC2 = int(YC2)
    except:
        YC2 = len(Liste_Y2)/2
        YC2 = int(YC2)

    try:
        XC2 = X_Texte2.get()
        XC2 = int(XC2)
    except:
        XC2 = 20

    try:
        WT2 = Le_Texte_Width2.get()
        WT2 = int(WT2)
    except:
        WT2 = 40
        
    

    drawingg = 1
    base = Image.open(Combined).convert('RGBA')
    try:
        opp = OpVar.get()
    except:
        opp = 255
    

    # make a blank image for the text, initialized to transparent text color
    txt = Image.new('RGBA', base.size, (255,255,255,0))

    # get a font

    # get a drawing context
    d = ImageDraw.Draw(txt)
    te = Le_Texte2.get(1.0,"end-1c")
    
    

    font2 = ImageFont.truetype(FT2, WT2, encoding="unic")
    kbch3 = Combined.split(".")
    kbch3 = kbch3[0]


    # draw text, half opacity
    d.text((XC2, YC2), te, Couleur2, font2)
    out = Image.alpha_composite(base, txt)
    out.save("TextAdded{}.png".format(kbch3))
    base.close()
    m3za = PhotoImage(file = "TextAdded{}.png".format(kbch3))
    LastCan.itemconfigure(FinalImage,image=m3za)
    

def DrawText():
  
    global Timg,Couleur, XC, YC, WT, FT
    try:
        Couleur = TColor.get()
        if Couleur == "Color":
            raise NameError
    except:
        Couleur = "black"

    try:
        FT = Le_Font.get()
        if FT == "Fonts":
            raise NameError
    except:
        FT = "arial.ttf"

    try:
        YC = Y_Texte.get()
        YC = int(YC)
    except:
        YC = len(Liste_Y)/2
        YC = int(YC)

    try:
        XC = X_Texte.get()
        XC = int(XC)
    except:
        XC = 20

    try:
        WT = Le_Texte_Width.get()
        WT = int(WT)
    except:
        WT = 40
        
    

    
    base = Image.open('kk.png').convert('RGBA')
    try:
        opp = OpVar.get()
    except:
        opp = 255
    

    # make a blank image for the text, initialized to transparent text color
    txt = Image.new('RGBA', base.size, (255,255,255,0))

    # get a font

    # get a drawing context
    d = ImageDraw.Draw(txt)
    te = Le_Texte.get(1.0,"end-1c")
    
    

    font = ImageFont.truetype(FT, WT, encoding="unic")


    # draw text, half opacity
    d.text((XC, YC), te, Couleur, font)
    out = Image.alpha_composite(base, txt)
    out.save("kktemp.png")
    base.close()
    Timg = PhotoImage(file = "kktemp.png")
    Tcan.itemconfigure(TImage,image=Timg)
    
    
def DrawCross():
    global Timg
    im = Image.open("kk.png")

    draw = ImageDraw.Draw(im)
    
    draw.line((0, 0) + im.size, fill=128)
    draw.line((0, im.size[1], im.size[0], 0), fill=128)
    im.save("kktemp.png")
    Timg = PhotoImage(file="kktemp.png")
    Tcan.itemconfigure(TImage,image = Timg)

def ResBB():
    global Timg
    tim = Image.open(filename)
    tim.save("kk.png")
    Timg = PhotoImage(file ="kk.png")
    Tcan.itemconfigure(TImage,image =Timg)

def Blur():
    
    global Timg,Tcan,ImageBlur
    try:
        value = BlurVar.get()
    except:
        value = 10
    global Timg,ImageBlur
    ImageBlur = Image.open("kk.png")
    ImageBlur.filter(ImageFilter.GaussianBlur(value)).save("kktemp.png")
    ImageBlur.close()

    Timg = PhotoImage(file="kktemp.png")
    Tcan.itemconfigure(TImage,image=Timg)

def SaveB():
    global Img22, img22
    Img22 = Image.open("kktemp.png")
    
    Img22.save(BaseImaged)
    Img22.close()
    Tframe.grid_remove()
    frame2.grid()
    Combiner()
    

def CancelB():
    global ba3
    ba3 = Image.open(filename)
    ba3.save("kktemp.png")
    Tframe.grid_remove()
    frame2.grid()
    
    
def Save():
    global Timg
    Img = Image.open("kktemp.png")
    Img.save("kk.png")
    Img.close()

def Cancel():
    global Timg, Img
    Img = Image.open("kk.png")
    Img.save("kktemp.png")
    Img.close()

    Timg = PhotoImage(file="kk.png")
    Tcan.itemconfigure(TImage,image=Timg)
    
def TPage():
    global VarTPage
    if VarTPage == 0:
        
        global Brightness, ContrastDeg,Sharpness,Tframe,frame2, TImg, Timg, Tcan, TImage, Blur, BlurSave,BlurCancel, BlurVar, BlurCombo, BlurListe,The_Image3333, The_Image4444, ResBB, SaveBB, CancelBB, DrawCross, DrawCrossCancel, DrawCrossSave, DrawText, Le_Texte, VarWidth, Le_Texte_Width, ListeWidth, Var_X, Var_Y, Liste_Y, Tfont,Le_Font, X_Texte, Y_Texte,Liste_Font,TColor, The_Color, SaveText, COLORS, CancelText,BrightnessDeg, BrightnessC,ListeBrightness,SharpnessDeg, SharpnessC, ListeSharpness, Colors,ColorsDeg, ColorsC, ListeColorskk, Contrast, ConstrastDeg,ContrastC, CancelEnhance, SaveEnhance,Detail,Emboss,FindEdges,Sharpen,Enhance,ListeDeg,EnhanceDeg,EnhanceD,Smooth,SmoothDeg,SmoothD, EnhanceD,SmoothD,ListeDeg,GrayScale,Invert,Flip,Mirror,Solarize,SolarizeDeg,SolarizeD, Expand, ExpandDeg, ExpandD,ExpandColor,ExpandC,ListeSolarize, Crop, CropDeg, CropD,ListeCrop, ExpandD, SolarizeD, Colorize, Colorize1, ColorizeFC,Colorize2, ColorizeSC,ColorizeListe,SaveFilter,CancelFilter,Opacity, OpVar, ListeOp, Opacity, ys
        frame2.grid_remove()
        Tframe = Frame(fenetre, width = screen_width -50, height = screen_height-100, background="dark grey")
        Tframe.grid(row=0,column=0)



        TImg = Image.open(filename)
        TImg.save("kk.png")
        Timg = PhotoImage(file="kk.png")
        Tcan = Canvas(Tframe, width = screen_width-50, height = screen_height-100, bg = "dark grey")
        Tcan.grid(row=0,column=0)
        TImg.close()

        TImage = Tcan.create_image(10,10,image = Timg,anchor=NW)



        Blur = Button(Tframe, bg = "dark grey",text = "Blur", command = Blur)
        Tcan.create_window(TImg.size[0]+100, 10, window = Blur, anchor = NW)

        BlurSave = Button(Tframe, bg="dark grey", text ="Cancel", fg = "dark blue",command = Cancel)
        Tcan.create_window(TImg.size[0]+230, 10, window=BlurSave, anchor = NW)

        BlurCancel = Button(Tframe, bg ="dark grey", text="Save", fg = "dark red",command = Save)
        Tcan.create_window(TImg.size[0]+282,10, window = BlurCancel, anchor = NW)

        BlurVar = IntVar()
        BlurCombo = tkinter.ttk.Combobox(Tframe, textvariable=BlurVar, state = "readonly",width=10)
        Tcan.create_window(TImg.size[0]+140,10,window = BlurCombo, anchor=NW)
        BlurListe = list(range(50))
        BlurListe.insert(0,"Default = 10")
        BlurCombo["values"] = BlurListe
        BlurCombo.current(0)

        The_Image3333 = PhotoImage(file = "")
        The_Image4444 = PhotoImage(file = "")
                                   
        ResBB = Button(Tframe,bg="dark grey", text = "Reset", image = The_Image3333, width = TImg.size[0],height = 20, compound = CENTER,command = ResBB)
        Tcan.create_window(10, TImg.size[1]+30, window = ResBB, anchor=NW)

        SaveBB = Button(Tframe, bg="dark grey", text="Save and return", fg = "dark red",image = The_Image4444, width = TImg.size[0]/2-10, height = 20, compound = CENTER, command = SaveB)
        Tcan.create_window(10,TImg.size[1]+60, window = SaveBB, anchor = NW)

        CancelBB = Button(Tframe, bg="dark grey", text="Cancel and return", fg = "dark blue",image = The_Image4444, width = TImg.size[0]/2-10, height = 20, compound = CENTER, command = CancelB)
        Tcan.create_window(TImg.size[0]/2+20,TImg.size[1]+60, window = CancelBB, anchor = NW)

                                   
                                   

        DrawCross = Button(Tframe, bg="dark grey", text="Draw cross",command = DrawCross)
        Tcan.create_window(TImg.size[0]+100,41,window=DrawCross,anchor=NW)

        DrawCrossSave = Button(Tframe,bg="dark grey",fg = "dark blue", text="Cancel", command = Cancel)
        Tcan.create_window(TImg.size[0]+174, 41, window = DrawCrossSave, anchor = NW)

        DrawCrossCancel = Button(Tframe, bg="dark grey", text="Save",fg = "dark red", width = 12,command = Save)
        Tcan.create_window(TImg.size[0]+226, 41, window = DrawCrossCancel, anchor = NW)

        DrawText = Button(Tframe,bg="dark grey",text="Draw text",width=10,command = DrawText)
        Tcan.create_window(TImg.size[0]+100,83,window = DrawText, anchor=NW)

        Le_Texte = Text(Tframe,bg="dark grey",width=30, height = 5)
        Tcan.create_window(TImg.size[0]+100,120,window=Le_Texte,anchor=NW)

        VarWidth = IntVar()
        Le_Texte_Width = tkinter.ttk.Combobox(Tframe, textvariable = VarWidth, state="readonly",width =10)
        Tcan.create_window(TImg.size[0]+100,210,window=Le_Texte_Width,anchor =NW)
        ListeWidth = list(range(150))
        ListeWidth.insert(0, "Width=20")
        Le_Texte_Width["values"] = ListeWidth
        Le_Texte_Width.current(0)

        Var_X = IntVar()
        X_Texte = tkinter.ttk.Combobox(Tframe,textvariable = Var_X, state = "readonly", width = 8)
        Tcan.create_window(TImg.size[0]+190,210,window=X_Texte, anchor = NW)
        Liste_X  = list(range(int(TImg.size[0])))
        Liste_X.insert(0,"X coords")
        X_Texte["values"] = Liste_X
        X_Texte.current(0)

        Var_Y = IntVar()
        Y_Texte = tkinter.ttk.Combobox(Tframe,textvariable = Var_Y, state = "readonly", width = 8)
        Tcan.create_window(TImg.size[0]+268,210,window=Y_Texte, anchor = NW)

        Liste_Y  = list(range(int(TImg.size[1])))
        Liste_Y.insert(0,"Y coords")
        Y_Texte["values"] = Liste_Y
        Y_Texte.current(0)

        Tfont = StringVar()
        Le_Font = tkinter.ttk.Combobox(Tframe,textvariable = Tfont, state = "readonly",width=15)
        Tcan.create_window(TImg.size[0]+100,236,window = Le_Font, anchor =NW)
        Liste_Font = os.listdir("C://Windows/Fonts")
        Liste_Font.insert(0,"Fonts")
        Le_Font["values"] = Liste_Font
        Le_Font.current(0)

        TColor = StringVar()
        The_Color = tkinter.ttk.Combobox(Tframe,textvariable = TColor, state = "readonly",width = 16)
        Tcan.create_window(TImg.size[0]+220, 236, window = The_Color, anchor = NW)
        The_Color["values"] = COLORS
        The_Color.current(0)

        SaveText = Button(Tframe, text = "Save", command = Save, width = 15,bg = "dark grey", fg = "dark red")
        Tcan.create_window(TImg.size[0]+100, 263, window = SaveText, anchor = NW)

        CancelText = Button(Tframe, text = "Cancel", command = Cancel, width = 15, bg = "dark grey", fg = "dark blue")
        Tcan.create_window(TImg.size[0]+220, 263, window = CancelText, anchor = NW)






        Tcan.create_rectangle(TImg.size[0]+90,75,TImg.size[0]+360, 300)

        Tcan.create_rectangle(TImg.size[0]+90,314,TImg.size[0]+360, 635)

        Tcan.create_rectangle(TImg.size[0]+90, 659, TImg.size[0]+360, 800)

        Brightness = Button(Tframe, text = "Brightness", width = 15, bg ="dark grey", command = Brightness)
        Tcan.create_window(TImg.size[0] +100, 696, window = Brightness, anchor= NW)

        BrightnessDeg = DoubleVar()
        BrightnessC = tkinter.ttk.Combobox(Tframe, textvariable = BrightnessDeg, width = 15, state ="readonly")
        Tcan.create_window(TImg.size[0] +220, 698, window = BrightnessC, anchor = NW)
        ListeBrightness = [0.0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0]
        BrightnessC["value"] = ListeBrightness
        BrightnessC.current(5)

        Sharpness = Button(Tframe, text = "Sharpness", width = 15, bg ="dark grey", command = Sharpness)
        Tcan.create_window(TImg.size[0] +100, 666, window = Sharpness, anchor= NW)

        SharpnessDeg = DoubleVar()
        SharpnessC = tkinter.ttk.Combobox(Tframe, textvariable = SharpnessDeg, width = 15, state ="readonly")
        Tcan.create_window(TImg.size[0] +220, 668, window = SharpnessC, anchor = NW)
        ListeSharpness = [0.0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0,1.1,1.2,1.3,1.4,1.5,1.6,1.7,1.8,1.9,2.0]
        SharpnessC["value"] = ListeSharpness
        SharpnessC.current(5)


        Colors = Button(Tframe, text = "Colors", width = 15, bg ="dark grey", command = Colors)
        Tcan.create_window(TImg.size[0] +100, 728, window = Colors, anchor= NW)

        ColorsDeg = DoubleVar()
        ColorsC = tkinter.ttk.Combobox(Tframe, textvariable = ColorsDeg, width = 15, state ="readonly")
        Tcan.create_window(TImg.size[0] +220, 730, window = ColorsC, anchor = NW)
        ListeColorskk = [0.0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0]
        ColorsC["value"] = ListeColorskk
        ColorsC.current(5)

        Contrast = Button(Tframe, text = "Contrast", width = 15, bg ="dark grey", command = Contrast)
        Tcan.create_window(TImg.size[0] +100, 758, window = Contrast, anchor= NW)

        ContrastDeg = DoubleVar()
        ContrastC = tkinter.ttk.Combobox(Tframe, textvariable = ContrastDeg, width = 15, state ="readonly")
        Tcan.create_window(TImg.size[0] +220, 760, window = ContrastC, anchor = NW)
        ListeContrastkk = [0.0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0]
        ContrastC["value"] = ListeContrastkk
        ContrastC.current(5)

        CancelEnhance = Button(Tframe, text = "Cancel Enhance", bg = "dark grey", fg = "dark blue", width = 15,command = Cancel)
        Tcan.create_window(TImg.size[0]+100, 790, window = CancelEnhance, anchor = NW)

        SaveEnhance = Button(Tframe, text = "Save Enhance", bg = "dark grey", fg = "dark red", width = 15,command = Save)
        Tcan.create_window(TImg.size[0]+220, 790, window = SaveEnhance, anchor = NW)




        Detail = Button(Tframe , text = "Detail", width = 15, bg = "dark grey", command = Detail)
        Tcan.create_window(TImg.size[0]+ 100, 321, window = Detail, anchor = NW)

        Emboss = Button(Tframe, text = "Emboss", width = 15, bg = "dark grey", command = Emboss)
        Tcan.create_window(TImg.size[0] + 220, 321, window = Emboss, anchor = NW)


        FindEdges = Button(Tframe,text = "Find Edges", width = 15, bg = "dark grey",command = FindEdges)
        Tcan.create_window(TImg.size[0] + 100, 351, window = FindEdges, anchor = NW)

        Sharpen = Button(Tframe, text = "Sharpen", width = 15, bg = "dark grey", command = Sharpen)
        Tcan.create_window(TImg.size[0] + 220, 351, window = Sharpen, anchor = NW)

        Enhance = Button(Tframe, text = "Edge enhance", width = 15, bg = "dark grey", command = Enhance)
        Tcan.create_window(TImg.size[0] + 100, 381, window = Enhance, anchor = NW)

        ListeDeg = ["Degree","1","2"]

        EnhanceDeg = IntVar()
        EnhanceD = tkinter.ttk.Combobox(Tframe, textvariable = EnhanceDeg, width = 15,state="readonly")
        Tcan.create_window(TImg.size[0] + 220, 383, window = EnhanceD, anchor = NW)

        Smooth = Button(Tframe, text = "Smooth", width = 15, bg = "dark grey",command = Smooth)
        Tcan.create_window(TImg.size[0]+100, 411, window = Smooth, anchor = NW)

        SmoothDeg = IntVar()
        SmoothD = tkinter.ttk.Combobox(Tframe, textvariable = SmoothDeg, width = 15, state="readonly")
        Tcan.create_window(TImg.size[0] + 220, 413, window = SmoothD, anchor = NW)

        EnhanceD["value"] = ListeDeg
        EnhanceD.current(0)

        SmoothD["value"] = ListeDeg
        SmoothD.current(0)

        GrayScale = Button(Tframe, text = "GrayScale", width = 15, bg = "dark grey", command = GrayScale)
        Tcan.create_window(TImg.size[0]+100, 441, window = GrayScale, anchor = NW)

        Invert = Button(Tframe, text = "Invert colors", width = 15, bg = "dark grey", command = Invert)
        Tcan.create_window(TImg.size[0]+220, 441, window = Invert, anchor = NW)

        Flip = Button(Tframe, text = "Flip", width = 15, bg = "dark grey", command = Flip)
        Tcan.create_window(TImg.size[0]+100, 471, window = Flip, anchor = NW)

        Mirror = Button(Tframe, text = "Mirror", width = 15, bg = "dark grey", command = Mirror)
        Tcan.create_window(TImg.size[0] + 220, 471, window = Mirror, anchor = NW)

        Solarize = Button(Tframe, text = "Solarize", width = 15, bg = "dark grey",command = Solarize)
        Tcan.create_window(TImg.size[0] + 100, 501, window = Solarize, anchor = NW)

        SolarizeDeg = IntVar()
        SolarizeD = tkinter.ttk.Combobox(Tframe, textvariable = SolarizeDeg, width = 15,state="readonly")
        Tcan.create_window(TImg.size[0] + 220, 503, window = SolarizeD, anchor = NW)

        Expand = Button(Tframe, text = "Expand", width = 15, bg = "dark grey",command = Expand)
        Tcan.create_window(TImg.size[0] + 100, 531, window = Expand, anchor = NW)

        ExpandDeg = IntVar()
        ExpandD = tkinter.ttk.Combobox(Tframe, textvariable = ExpandDeg, width = 6,state="readonly")
        Tcan.create_window(TImg.size[0] + 220, 533, window=ExpandD, anchor = NW)

        ExpandColor = StringVar()
        ExpandC = tkinter.ttk.Combobox(Tframe,textvariable = ExpandColor, width = 5, state ="readonly")
        Tcan.create_window(TImg.size[0]+280, 533, window = ExpandC, anchor = NW)

        ListeSolarize = list(range(255))
        ListeExpand = list(range(200))
        ListeExpand.insert(0,"degree")
        ListeExpandColor = ["color","blue","red","white","yellow","black","orange","green","grey"]
        ExpandC["value"] = ListeExpandColor
        ExpandC.current(0)

        ListeSolarize.insert(0,"Threshold")

        Crop = Button(Tframe, text ="Crop", width = 15, bg = "dark grey", command = Crop)
        Tcan.create_window(TImg.size[0]+100, 561, window = Crop, anchor = NW)
        CropDeg = IntVar()
        CropD = tkinter.ttk.Combobox(Tframe, textvariable = CropDeg, width = 15)
        Tcan.create_window(TImg.size[0]+220, 563,window = CropD, anchor = NW)
        ListeCrop = list(range(200))
        ListeCrop.insert(0,"Crop degree")
        CropD["value"] = ListeCrop
        CropD.current(0)



        ExpandD["value"] = ListeExpand
        SolarizeD["value"] = ListeSolarize
        ExpandD.current(0)
        SolarizeD.current(0)

        Colorize = Button(Tframe,text = "Bi-Color", width = 15, bg = "dark grey", command = Colorize)
        Tcan.create_window(TImg.size[0] + 100, 591, window = Colorize, anchor = NW)

        Colorize1 = StringVar()
        ColorizeFC = tkinter.ttk.Combobox(Tframe, textvariable = Colorize1, width = 5, state = "readonly")
        Tcan.create_window(TImg.size[0]+220, 591, window = ColorizeFC, anchor = NW)

        Colorize2 = StringVar()
        ColorizeSC = tkinter.ttk.Combobox(Tframe, textvariable = Colorize2, width = 5, state = "readonly")
        Tcan.create_window(TImg.size[0]+280, 591, window= ColorizeSC, anchor = NW)

        ColorizeListe = ["blue","red","white","yellow","black","orange","green","grey"]
        ColorizeFC["value"] = ColorizeListe
        ColorizeFC.current(0)

        ColorizeSC["value"] = ColorizeListe
        ColorizeSC.current(1)


        SaveFilter = Button(Tframe , text = "Save filter", width = 15,bg = "dark grey", fg = "dark red",command = Save)
        CancelFilter = Button(Tframe, text = "Cancel filter",width = 15,bg = "dark grey",fg = "dark blue", command = Cancel)

        Tcan.create_window(TImg.size[0] + 100, 621, window = CancelFilter, anchor = NW)
        Tcan.create_window(TImg.size[0] + 220, 621, window = SaveFilter, anchor = NW)


        OpVar = IntVar()
        Opacity = tkinter.ttk.Combobox(Tframe, textvariable=OpVar,state = "readonly", width = 19)
        Tcan.create_window(TImg.size[0]+190, 84,window=Opacity,anchor=NW)
        ListOp = list(range(256))
        ListOp.insert(0,"Opacity (default=255)")
        Opacity["values"] = ListOp
        Opacity.current(0)

        ys = Scrollbar(Tframe, orient='vertical', command=Tcan.yview)
        ys.grid(row=0, column=1, sticky = "ns")
        Tcan.configure(yscrollcommand=ys.set, scrollregion=Tcan.bbox('all'))
        Tcan.yview_moveto(0)

        xs = Scrollbar(Tframe, orient='horizontal', command=Tcan.xview)
        xs.grid(row=1, column=0, sticky = "we")
        Tcan.configure(xscrollcommand=xs.set, scrollregion=Tcan.bbox('all'))
        Tcan.xview_moveto(0)
        app=FullScreenApp(fenetre)
        VarTPage = 1 
    else:
        frame2.grid_remove()
        Tframe.grid()


    

def ResetBut1():
    global img2,Img2,img22, Img22, ImageX2,XX,YY,MoveX,MoveY
    MoveX = 0
    MoveY = 0
    XX = 0
    YY = 0
    
    img2 = Image.open(ShirtName)
    img2.save(ShirtNamed2[0]+"X.png")


    XSize = int(img2.size[0]/3)
    YSize = int(img2.size[1]/3)
    
    Img22 = Image.open(filename)
    Img22.save(BaseImaged)

    Combiner()
    



def Rotate():
    global img2,img22,Img2,Img22,ROTATION
    ROTATION += 90
    RotImg = Image.open(Combined)
    RotImg.rotate(ROTATION).save(Combined)
    img22 = PhotoImage(file = Combined)
    
   
    can2.itemconfig(ImageX2,image=img22)

def Rotate2():
    global Img22, img22,ROTATION
    ROTATION += 90
    Img22 = Image.open(BaseImaged)
    Img22 = Img22.rotate(ROTATION)
    
    Img22.save(BaseImaged)
    Combiner()

def MLeft():
    global MoveX,ComboSpeed, SpeedDeg
    try:
        SpeedDeg.get() == int(SpeedDeg.get())
        speed = SpeedDeg.get()
    except:
        speed = 5
        
    MoveX -= speed
    Combiner()
    
    

def MRight():
    global MoveX
    try:
        SpeedDeg.get() == int(SpeedDeg.get())
        speed = SpeedDeg.get()
    except:
        speed = 5
    MoveX += speed
    Combiner()

def MUp():
    global MoveY
    try:
        SpeedDeg.get() == int(SpeedDeg.get())
        speed = SpeedDeg.get()
    except:
        speed = 5
    MoveY -= speed
    Combiner()

def MDown():
    global MoveY
    try:
        SpeedDeg.get() == int(SpeedDeg.get())
        speed = SpeedDeg.get()
    except:
        speed = 5
    MoveY +=speed
    Combiner()

def RLeft():
    global img22,Img22,XSize,YSize,XX
    XX -=10
    Combiner()

def RRight():
    global img22,Img22,XSize,YSize, XX
    XX +=10
    Combiner()

def RUp():
    global img22,Img22,XSize,YSize, YY
    YY += 10
    Combiner()


def RDown():
    
    global img22,Img22,XSize,YSize, YY
    YY -= 10
    Combiner()

    

def image_tint(src, tint='#ffffff'):
    if Image.isStringType(src):  # file path?
        src = Image.open(src)
    if src.mode not in ['RGB', 'RGBA']:
        src = src.convert("RGBA", palette=Image.ADAPTIVE, colors=256)
    
    src.load()

    tr, tg, tb = getrgb(tint)
    tl = getcolor(tint, "L")  # tint color's overall luminosity
    if not tl: tl = 1  # avoid division by zero
    tl = float(tl)  # compute luminosity preserving tint factors
    sr, sg, sb = map(lambda tv: tv/tl, (tr, tg, tb))  # per component
                                                      # adjustments
    # create look-up tables to map luminosity to adjusted tint
    # (using floating-point math only to compute table)
    luts = (tuple(map(lambda lr: int(lr*sr + 0.5), range(256))) +
            tuple(map(lambda lg: int(lg*sg + 0.5), range(256))) +
            tuple(map(lambda lb: int(lb*sb + 0.5), range(256))))
    l = grayscale(src)  # 8-bit luminosity version of whole image
    if Image.getmodebands(src.mode) < 4:
        merge_args = (src.mode, (l, l, l))  # for RGB verion of grayscale
    else:  # include copy of src image's alpha layer
        a = Image.new("L", src.size)
        a.putdata(src.getdata(3))
        merge_args = (src.mode, (l, l, l, a))  # for RGBA verion of grayscale
        luts += tuple(range(256))  # for 1:1 mapping of copied alpha values

    return Image.merge(*merge_args).point(luts)      

def SelectFile():
    global filename,BaseImage,BaseImage1, filename3, Ba3eImage1,Ba3eImage
    filename = filedialog.askopenfilename(initialdir = "background",title = "Choose image", filetypes = (("png files","*.png"),("jpg files", "*.jpg"),("gif files", "*.gif"),("Jpeg files","*.jpeg")) )
    LabelDir.configure(text = "Directory : {}".format(filename))
    BaseImage = filename.split("/")
    BaseImage = BaseImage[len(BaseImage)-1]
    BaseImage1 = BaseImage.split(".")
    BaseImage1 = BaseImage1[0]

    filename3 = filename
    Ba3eImage1 = BaseImage1
    Ba3eImage = BaseImage
    
    
    

def Upload():
    
    global TheImage,img
    img = Image.open(filename)
    img = img.resize((243,243))
    img.save("{}/ResizedImage/{}.png".format(CWD, BaseImage1))
    TheImage = "{}/ResizedImage/{}.png".format(CWD, BaseImage1)
    img = PhotoImage(file=TheImage)
    LabelImg.config(image=img)
    
    bou1.configure(text = "Change image")

def ChangeColor(jj):
    global can2, Img2,ShirtNamed2,Ba3jj
    if Ba3jj == True:
        The_Color_Here = jj3
    else:
        The_Color_Here = listecolor[jj]
    input_image_path = ShirtNamed2[0]+"X.png"
    print('tinting "{}"'.format(input_image_path))

    root, ext = os.path.splitext(input_image_path)
    suffix = '_result_py{}'.format(sys.version_info[0])
    result_image_path = ShirtNamed2[0]+"X.png"

    print('creating "{}"'.format(result_image_path))
    result = image_tint(input_image_path,jj)
    if os.path.exists(result_image_path):  # delete any previous result file
        os.remove(result_image_path)
    result.save(result_image_path)  # file name's extension determines format
    
    Combiner()


    
    if Ba3jj == True:
        The_Color_Here = jj3
    else:
        The_Color_Here = listecolor[jj]
    input_image_path = "Back/{}BACKC.png".format(kouchi2[0])
    print('tinting "{}"'.format(input_image_path))

    root, ext = os.path.splitext(input_image_path)
    suffix = '_result_py{}'.format(sys.version_info[0])
    result_image_path = "Back/{}BACKC.png".format(kouchi2[0])

    print('creating "{}"'.format(result_image_path))
    result = image_tint(input_image_path,jj)
    if os.path.exists(result_image_path):  # delete any previous result file
        os.remove(result_image_path)
    result.save(result_image_path)  # file name's extension determines format
    Ba33jj = False
    
    
    
def ChangeColorBack(jj):
    global can2, Img2,Ba3jj, mkk3
    if Ba3jj == True:
        The_Color_Here = jj3
    else:
        The_Color_Here = listecolor[jj]
    input_image_path = "Back/{}BACKC.png".format(kouchi2[0])
    print('tinting "{}"'.format(input_image_path))

    root, ext = os.path.splitext(input_image_path)
    suffix = '_result_py{}'.format(sys.version_info[0])
    result_image_path = "Back/{}BACKC.png".format(kouchi2[0])

    print('creating "{}"'.format(result_image_path))
    result = image_tint(input_image_path,jj)
    if os.path.exists(result_image_path):  # delete any previous result file
        os.remove(result_image_path)
    result.save(result_image_path)  # file name's extension determines format
    Ba33jj = False
    mkk3 = PhotoImage(file = "Back/{}BACKC.png".format(kouchi2[0]))
    can2.itemconfig(ImageX2, image = mkk3)
    


fenetre = Tk()
screen_height = fenetre.winfo_screenheight()
screen_width = fenetre.winfo_screenwidth()
fenetre.configure(width = screen_width -50, height = screen_height-100, background="dark grey")

frame = Frame(fenetre, width = 600, height = 500)
frame.grid(row = 0, column = 0)

can = Canvas(frame, width = 600, height = 500, bg = "dark grey")
can.grid(row=1, column=1)

baseL = Label(frame, text = "Base image",bg = "dark grey", fg = "red")
can.create_window(110,60,window = baseL, anchor = NW)

baseP = Label(frame, text = "Product",bg = "dark grey", fg = "blue")
can.create_window(410,60,window = baseP, anchor = NW)

can.create_rectangle(30,120,280,370)
can.create_rectangle(330,120,580,370)

bou1 = Button(frame, text = "Select img to upload", width = 20,bg = "dark grey",command = SelectFile)
can.create_window(30,390, anchor = NW, window = bou1)

bou2 = Button(frame, text = "Upload", bg = "dark grey", width = 11, command = Upload)
can.create_window(190,390, anchor = NW, window = bou2)

#ListeDesProduits = Label(frame,text = "List of products : ", fg = "blue", bg = "dark grey")
#can.create_window(340,30,anchor = NW, window = ListeDesProduits)

LabelDir = Label(frame, text= "Directory : ", fg = "red", bg = "dark grey")
can.create_window(32,440, window = LabelDir,anchor=W)


Phones = Button(frame, text = "Phones", bg = "dark grey", command = Phones,width =10)
can.create_window(330, 390, anchor=NW,window = Phones)

TShirts = Button(frame, text = "T-Shirts", bg = "dark grey", command = TShirts,width =10)
can.create_window(415, 390, anchor = NW, window = TShirts)

Pillows = Button(frame, text = "Pillows", bg ="dark grey", width = 10, command = Pillows)
can.create_window(500, 390, anchor = NW, window = Pillows)

Other = Button(frame, text = "Other", bg = "dark grey", width = 22, command = Other)
can.create_window(330, 420, anchor = NW, window = Other)
                        
Next = Button(frame,text="Next =>", bg="dark grey", fg ="blue",width = 10,command = Next1)
can.create_window(500,450,window = Next, anchor = NW)

img = PhotoImage(file="")

img2 = PhotoImage(file = "")

LabelImg = Label(frame, image = img,width = 243, height=243)
can.create_window(32,122,anchor =NW, window = LabelImg)

LabelImg2 = Label(frame, image = img2,width = 243, height=243)
can.create_window(332,122,anchor =NW, window = LabelImg2)



def LastFrameHH():
    global LastFrame,LastVarFrame, LastCan2, FinalRotate,FinalComboDeg,FinalCombo,FinalListe,FinalCombo,ZoomIn,ZoomOut,DefaultFinal,\
           ma3ouz,ma33,Liste_Y2,DrawText2,Le_Texte2,VarWidth2,Le_Texte_Width2, ListeWidth2,Var_X2,X_Texte2,Liste_X2,Var_Y2,Y_Texte2,Tfont2,Le_Font2,Liste_Font2,TColor2,The_Color2,CancelText2, SaveText2, ViewAll,LastBack,Finish,Combined,FinalImage,LastCan
    if LastVarFrame == 0:
        LastFrame = Frame(fenetre, background ="dark grey")
        LastFrame.grid(row=0,column=0)


        LastCan2 = Canvas(LastFrame, width = 400, height = int(fenetre.winfo_screenheight()-100), bg = "dark grey")
        LastCan2.grid(row=0, column = 0) #Can 2 (buttons)

        FinalRotate = Button(LastFrame, text = "Rotate", width = 15, bg = "dark grey", command = FinalRotate)
        LastCan2.create_window(10,10, anchor = NW, window = FinalRotate)

        FinalComboDeg = IntVar()
        FinalCombo = tkinter.ttk.Combobox(LastFrame, textvariable = FinalComboDeg, width = 15)
        LastCan2.create_window(135,12, anchor = NW, window = FinalCombo)
        FinalListe = list(range(360))              #Rotate 
        FinalCombo["value"] = FinalListe
        FinalCombo.current(90)

        ZoomIn = Button(LastFrame, text = "Zoom in ( + )", width = 15, bg = "dark grey", fg ="green",command = ZoomIn)
        LastCan2.create_window(10, 40, anchor = NW, window = ZoomIn)

        ZoomOut = Button(LastFrame, text = "Zoom Out ( - )", width = 15, bg ="dark grey", fg ="red",command = ZoomOut)
        LastCan2.create_window(135, 40, anchor = NW, window = ZoomOut)

        DefaultFinal = Button(LastFrame, text = "Default", width = 33, bg = "dark grey",command = DefaultFinal)
        LastCan2.create_window(10, 70, anchor = NW, window = DefaultFinal)
        ma3ouz = Image.open(Combined)
        
        ################ DRAWING TEXT ####################################
        LastCan2.create_rectangle(6, 129, 270, 323)

        DrawText2 = Button(LastFrame,bg="dark grey",text="Draw text",width=35,command = DrawText2)
        LastCan2.create_window(10,116,window = DrawText2, anchor=NW)

        Le_Texte2 = Text(LastFrame,bg="dark grey",width=31, height = 6)
        LastCan2.create_window(10,150,window=Le_Texte2,anchor=NW)

        VarWidth2 = IntVar()
        Le_Texte_Width2 = tkinter.ttk.Combobox(LastCan2, textvariable = VarWidth2, state="readonly",width =10)
        LastCan2.create_window(10,250,window=Le_Texte_Width2,anchor =NW)
        ListeWidth2 = list(range(150))
        ListeWidth2.insert(0, "Width=20")
        Le_Texte_Width2["values"] = ListeWidth2
        Le_Texte_Width2.current(0)

        Var_X2 = IntVar()
        X_Texte2 = tkinter.ttk.Combobox(LastCan2,textvariable = Var_X2, state = "readonly", width = 10)
        LastCan2.create_window(95,250,window=X_Texte2, anchor = NW)
        Liste_X2  = list(range(int(ma3ouz.size[0])))
        Liste_X2.insert(0,"X coords")
        X_Texte2["values"] = Liste_X2
        X_Texte2.current(0)

        Var_Y2 = IntVar()
        Y_Texte2 = tkinter.ttk.Combobox(LastCan2,textvariable = Var_Y2, state = "readonly", width = 10)
        LastCan2.create_window(181,250,window=Y_Texte2, anchor = NW)

        Liste_Y2  = list(range(int(ma3ouz.size[1])))
        Liste_Y2.insert(0,"Y coords")
        Y_Texte2["values"] = Liste_Y2
        Y_Texte2.current(0)

        Tfont2 = StringVar()
        Le_Font2 = tkinter.ttk.Combobox(LastCan2,textvariable = Tfont2, state = "readonly",width=17)
        LastCan2.create_window(10,280,window = Le_Font2, anchor =NW)
        Liste_Font2 = os.listdir("C://Windows/Fonts")
        Liste_Font2.insert(0,"Fonts")
        Le_Font2["values"] = Liste_Font2
        Le_Font2.current(0)

        TColor2 = StringVar()
        The_Color2 = tkinter.ttk.Combobox(LastCan2,textvariable = TColor2, state = "readonly",width = 17)
        LastCan2.create_window(138, 280, window = The_Color2, anchor = NW)

        The_Color2["values"] = COLORS
        The_Color2.current(0)

        CancelText2 = Button(LastCan2, text = "Cancel text", fg = "blue", bg ="dark grey", width = 16,command=CancelText2)
        LastCan2.create_window(10, 310, anchor = NW, window = CancelText2)

        SaveText2 = Button(LastCan2, text = "Save text", fg = "red", bg ="dark grey", width = 16,command = SaveText2)
        LastCan2.create_window(138, 310, anchor = NW, window = SaveText2)

        ViewAll = Button(LastCan2, text = "View All saved products", fg = "dark blue", bg="dark grey", width = 33,command = ViewAll)
        LastCan2.create_window(10, 400, anchor = NW, window = ViewAll)

        LastBack = Button(LastCan2, text = "Back", fg = "dark green", bg = "dark grey", width = 25,command = LastBack)
        LastCan2.create_window(10, fenetre.winfo_screenheight()-140, anchor = NW, window = LastBack)

        Finish = Button(LastCan2, text ="Finish", fg = "dark red", bg= "dark grey", width = 25, command = Finish)
        LastCan2.create_window(210, fenetre.winfo_screenheight()-140, anchor = NW, window=Finish)




        ################ DRAWING TEXT ####################################

        ma3ouz = Image.open(Combined)
        ma33 = PhotoImage(file =Combined)

        if ma3ouz.size[0] >= int(fenetre.winfo_screenwidth()/2):
            ww = int(fenetre.winfo_screenwidth()/2)
        else:
            ww = ma3ouz.size[0]

        if ma3ouz.size[1] >= int(fenetre.winfo_screenheight()-100):
            hh = int(fenetre.winfo_screenheight()-100)
        else:
            hh = ma3ouz.size[1]

        LastCan = Canvas(LastFrame, bg = "dark grey", width = ww, height = hh)
        LastCan.grid(row = 0, column = 2) #Can 1 ( img )

        FinalImage = LastCan.create_image(0,0, anchor = NW, image = ma33)

        LastCan.create_window(2400,2400, anchor = NW, window = Label(LastFrame,text="",bg="dark grey"))



        ys = Scrollbar(LastFrame, orient='vertical', command=LastCan.yview)
        ys.grid(row=0, column=3, sticky = "ns")
        LastCan.configure(yscrollcommand=ys.set, scrollregion=LastCan.bbox('all'))
        LastCan.yview_moveto(0)

        xs = Scrollbar(LastFrame, orient='horizontal', command=LastCan.xview)
        xs.grid(row=1, column=2, sticky = "we")
        LastCan.configure(xscrollcommand=xs.set, scrollregion=LastCan.bbox('all'))
        LastCan.xview_moveto(0)
        app=FullScreenApp(fenetre)
    else:
        LastFrame.grid(row=0,column=0)
        
        ma33 = PhotoImage(file = Combined)
        LastCan.itemconfig(FinalImage, image = ma33)
        
        



AllFrame = Frame(fenetre, background = "dark grey")

AllCan = Canvas(AllFrame, width = fenetre.winfo_screenwidth()/2, height = fenetre.winfo_screenheight()-100, bg="dark grey")
AllCan.grid(row=0, column =1)
AllCan.create_window(5000,60500, anchor = NW, window=Label(AllFrame, text="", bg="dark grey"))



AllBackk = Label(AllFrame, text = "BACK", font=("Courrier",50),fg ="dark green",bg = "grey", width =10, height=10)
AllBackk.grid(row=0,column=0)
AllBackk.bind("<Button-1>",AllBack)



AllQuitt = Label(AllFrame, text = "QUIT" ,font=("Courrier",50),fg="dark red", bg = "grey", width = 10, height =10)
AllQuitt.grid(row=0,column=3)
AllQuitt.bind("<Button-1>", AllQuit)




terms = {}
cc = 0
yba3 = 0
for i in os.listdir("SavedProducts"):
    try:
        terms["T{}".format(cc)] = PhotoImage(file = "SavedProducts\{}".format(i))
        AllCan.create_image(100,yba3, anchor = NW, image = terms["T{}".format(cc)])
        cc += 1
        grb3 = Image.open("SavedProducts\{}".format(i))
        yba3 += grb3.size[1]+150
        AllCan.create_line(0,yba3 - 75, 5000, yba3 - 75)
    except:
        pass
    
    

    
    

ys = Scrollbar(AllFrame, orient='vertical', command=AllCan.yview)
ys.grid(row=0, column=2, sticky = "ns")
AllCan.configure(yscrollcommand=ys.set, scrollregion=AllCan.bbox('all'))
AllCan.yview_moveto(0)

xs = Scrollbar(AllFrame, orient='horizontal', command=AllCan.xview)
xs.grid(row=1, column=1, sticky = "we")
AllCan.configure(xscrollcommand=xs.set, scrollregion=AllCan.bbox('all'))
AllCan.xview_moveto(0)
app=FullScreenApp(fenetre)





#app=FullScreenApp(fenetre)
fenetre.mainloop()
os.system("pause")












