from tkinter import *
k= Tk()
width= k.winfo_screenwidth()
height= k.winfo_screenheight()
k.destroy()
if(width == 1600 and height == 900):
    from Resources import Res1600X900 as f
import pyautogui as p
import sys, shutil, os

class CaptureView(f.functions):
    def __init__(self,master):
        self.path= master["path"]
        super().__init__()
        self.master= master
        self.capture()
    def capture(self):
        while True:
            self.captFront()
            self.captBack()
            self.captLeft90()
            self.captLeft45()
            self.captRight90()
            self.captRight45()
            op= p.confirm(title="Deu tudo certo?", text="", buttons=["Sim","Não"])
            if(op == "Sim"):
                break
        if(self.master["sup"] != "0"):
            self.captOclSup("sup")
            self.captOclSup("sob")
            self.captOclSup("ipr")
        if(self.master["inf"] != "0"):
            self.captOclInf("inf")
            self.captOclInf("sob")
            self.captOclInf("ipr")
        p.confirm(title="Pronto para o estagiamento?", text="", buttons=["Pronto"])
        while 1:
            if(self.master["sup"] == "0" and self.master["inf"] != "0"):
                self.estCapt("SIM","Inferior")
            elif(self.master["sup"] != "0" and self.master["inf"] == "0"):
                self.estCapt("SIM","Superior")
            elif(self.master["sup"] != "0" and self.master["inf"] != "0"):
                self.estCapt("SIM","Ambas")
            else:
                self.estCapt("SIM","Tabela")
            repeatEst= p.confirm(title="Quer repetir o estagiamento?", text="", buttons=["SIM","NAO"])
            if(repeatEst == "NAO"):
                break
            else:
                p.click(1134,14)
        shutil.copy(os.environ["USERPROFILE"] + "\\Documents\\PyRelator\\Images\\tmp\\5.png", self.master["path"] + "\\05 - Sobreposicao " + self.master["setup"] + " Superior - " + self.master["paciente"] + ".png")
        shutil.copy(os.environ["USERPROFILE"] + "\\Documents\\PyRelator\\Images\\tmp\\6.png", self.master["path"] + "\\06 - Sobreposicao " + self.master["setup"] + " Inferior - " + self.master["paciente"] + ".png")

