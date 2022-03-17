from tkinter import *
from datetime import datetime
import os
import pyautogui as p
import time
import shutil
import subprocess
import base64

class Report:
    def __init__(self, banco):
        self.database= banco
        self.option= x= p.confirm(title="Selecione as Arcadas para IPR",text="",buttons=["Superior","Inferior","Ambas","Não tem"])
        self.translateVars()
        if(self.option == "Não tem"):
            shutil.copy(os.environ["USERPROFILE"] + "\\Documents\\PyRelator\\Images\\tmp\\7F.png",f'{self.path}\\07 - Vista Frontal - {self.setup}.png')
        else:
            self.imgtemp= os.environ["USERPROFILE"] + "\\Documents\\PyRelator\\Images\\tmp"
            self.display= Tk()
            self.display.config(bg="orange",padx="20px",pady="20px")
            self.display.title("PyReport")
            self.__buildvars__()
            self.__buildBoxes__()
            self.display.mainloop()
    def __buildvars__(self,args=""):
        self.dtemp= os.environ["USERPROFILE"] + "\\Documents\\PyRelator\\Models\\tmp"
        self.pmain= os.environ["USERPROFILE"] + "\\Documents\\PyRelator"
        try:
            os.mkdir(self.dtemp)
        except Exception:
            pass
        self.total= {}
        self.TEETH= {}
        self.teeth, self.colors, self.iprs= {},{},{}
        self.desg= {}
        for ind in range(1,5):
            for subind in range(1,8):
                self.teeth[f"D{ind}{subind}"]= IntVar(self.display, value= 0)
        for ind in range(1,5):
            for subind in range(1,7):
                self.iprs[f"I{ind}{subind}{ind}{subind+1}"]= "0.0"
                self.colors[f"CI{ind}{subind}{ind}{subind+1}"]= "#000000"
        self.colors["CI1121"],self.iprs["I1121"]= "#000000", IntVar()
        self.colors["CI3141"],self.iprs["I3141"]= "#000000", IntVar()
    def translateVars(self):
        self.OS= self.database["os"]
        self.path= self.database["path"]
        self.setup= self.database["setup"]
        self.dentista= self.database["dentista"]
        self.paciente= self.database["paciente"]
    def __buildBoxes__(self):
        aux= 1
        self.fmain= Frame(self.display, bg="orange")
        self.fmain.grid(row=1,column=1, columnspan= 14)
        for ind in range(7,0,-1):
            box= self.Check(self.fmain, f"1{ind}",1,aux,self.teeth[f"D1{ind}"])
            box2= self.Check(self.fmain, f"4{ind}",2,aux,self.teeth[f"D4{ind}"])
            aux+= 1
        for ind in range(1,8):
            box= self.Check(self.fmain, f"2{ind}",1,aux,self.teeth[f"D2{ind}"])
            box2= self.Check(self.fmain, f"3{ind}",2,aux,self.teeth[f"D3{ind}"])
            aux += 1
        self.btn= Button(self.display, font="Arial 20", text="Pronto", bg="green", fg="white", relief="flat", command= self.__IPRs__)
        self.btn.grid(row=3,column=1, columnspan= 14, pady="20px")
    def __IPRs__(self):
        aux2= 1
        aux= 7
        self.fmain.grid_forget()
        self.fmain= Frame(self.display, bg="orange")
        self.fmain.grid(row=1,column=1, columnspan= 14)
        for ind in range(6,0,-1):
            self.iprs["I1" + str(aux-1) + "1" + str(aux)]= self.Entrys(self.fmain, "1" + str(aux-1) + "1" + str(aux),1,aux2)
            self.iprs["I4" + str(aux-1) + "4" + str(aux)]= self.Entrys(self.fmain, "4" + str(aux-1) + "4" + str(aux),2,aux2)
            aux2 += 1
            aux -= 1
        aux2 += 1
        self.iprs["I1121"]= self.Entrys(self.fmain, "1121",1,aux2)
        self.iprs["I3141"]= self.Entrys(self.fmain,"3141",2,aux2)
        aux2 += 1
        for ind in range(1,7):
            self.iprs["I2" + str(ind) + "2" + str(ind+1)]= self.Entrys(self.fmain, "2" + str(ind) + "2" + str(ind+1),1,aux2)
            self.iprs["I3" + str(ind) + "3" + str(ind+1)]= self.Entrys(self.fmain, "3" + str(ind) + "3" + str(ind+1),2,aux2)
            aux2 += 1
        self.btn["command"] = self.__Process__
    def __Process__(self):
        for i in self.teeth:
            self.TEETH[i]= self.teeth[i].get()
        for i in self.iprs:
            if(self.iprs[i].get() != "0.0"):
                self.colors[f"C{i}"]= "#FF0000"
            else:
                self.colors[f"C{i}"]= "#000000"
        for i in self.iprs:
            self.desg[i]= self.iprs[i].get()
        for i in self.TEETH:
            if(self.TEETH[i] == 1):
                pos= int(i[1] + i[2]) + 1
                ant= pos - 1
                self.desg["I" + str(ant) + str(pos)]= "0,0"
                self.colors["CI" + str(ant) + str(pos)]= "#000000"
            else:
                pass
        if(self.TEETH["D21"] == 1 and self.TEETH["D11"] == 1):
            self.desg["I1121"]= "0,0"
            self.colors["CI1121"]= "#000000"
        if(self.TEETH["D31"] == 1 and self.TEETH["D41"] == 1):
            self.desg["I3141"]= "0,0"
            self.colors["CI3141"]= "#000000"
        if(self.TEETH["D26"] == 1 and self.TEETH["D27"] == 0):
            self.desg["I2627"]= "0,0"
            self.colors["CI2627"]= "#000000"
        if(self.TEETH["D36"] == 1 and self.TEETH["D37"] == 0):
            self.desg["I3637"]= "0,0"
            self.colors["CI3637"]= "#000000"
        if(self.TEETH["D16"] == 1 and self.TEETH["D17"] == 0):
            self.desg["I1617"]= "0,0"
            self.colors["CI1617"]= "#000000"
        if(self.TEETH["D46"] == 1 and self.TEETH["D47"] == 0):
            self.desg["I4647"]= "0,0"
            self.colors["CI4647"]= "#000000"
        self.total.update(self.colors)
        self.total.update(self.desg)
        self.total.update(self.TEETH)
        self.__Generate__()
    def __Generate__(self):
        if(self.option == "Inferior"):
            with open(self.pmain + "\\Images\\IPR0.jpg", "rb") as image_file:
                sup = "data:image/png;base64," + base64.b64encode(image_file.read()).decode()
        elif(self.option == "Superior" or self.option == "Ambas"):
            with open(self.imgtemp + "\\S.png", "rb") as image_file:
                sup = "data:image/png;base64," + base64.b64encode(image_file.read()).decode()
        if(self.option == "Superior"):
            with open(self.pmain + "\\Images\\IPR0.jpg", "rb") as image_file:
                inf = "data:image/png;base64," + base64.b64encode(image_file.read()).decode()
        elif(self.option == "Inferior" or self.option == "Ambas"):
            with open(self.imgtemp + "\\I.png", "rb") as image_file:
                inf = "data:image/png;base64," + base64.b64encode(image_file.read()).decode()
        temp= {
            "OS": self.OS,
            "PACIENTE": self.paciente,
            "DENTISTA": self.dentista,
            "Superior": sup,
            "Inferior": inf
            }
        self.total.update(temp)
        file= open(os.environ["USERPROFILE"] + "\\Documents\\PyRelator\\Models\\Report.svg","r")
        xml= file.read()
        xml= xml.format(**self.total)
        file2= open(f"{self.dtemp}\\Model.svg","w")
        file2.write(xml)
        file2.close()
        file.close()
        subprocess.run([r"C:\Program Files\Inkscape\bin\inkscape.exe",f"{self.dtemp}\\Model.svg","--export-dpi=300", "--export-background-opacity=1","-o",f"{self.dtemp}\\7.png"])
        while not os.path.exists(f"{self.dtemp}\\7.png"):
            self.display.update()
        shutil.move(f"{self.dtemp}\\7.png",f'{self.path}\\07 - Relatorio de IPR {self.setup} - {self.paciente}.png')
        #os.remove(f"{self.imgtemp}\\S.jpg")
        #os.remove(f"{self.imgtemp}\\I.jpg")
        self.display.destroy()
    def Entrys(self,master,txt,x,y):
        frame= Frame(master,bg="orange")
        frame.grid(row= x, column= y, pady="10px")
        entrada= Entry(frame, width=10, justify="center", font="Arial 13")
        entrada.grid(row= 1, column= 1)
        label= Label(frame, bg="orange", text= txt, fg="white", font="Arial 14")
        label.grid(row= 2, column= 1)
        entrada.insert(0,"0.0")
        return entrada
    def Check(self,master,txt,x,y,var):
        frame= Frame(master,bg="orange")
        frame.grid(row= x, column= y)
        box= Checkbutton(frame, bg="orange", onvalue= 0, offvalue= 1, command= self.show, variable= var, activebackground= "orange", selectcolor="green", fg="white")
        box.grid(row= 1, column= 1)
        label= Label(frame, bg="orange", fg="white", text= txt, font="Arial 17")
        label.grid(row=2, column= 1)
        return box
    def show(self):
        for i in self.teeth:
            print(i," -> ",self.teeth[i].get())
