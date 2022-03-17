from Resources import settings as s
import pyautogui as p
import time as t
from tkinter import *
import os
import win32api
import win32gui

class functions(s.settings):
    def __init__(self):
        super().__init__()
        p.PAUSE= 0.05
    def Sobrepos(self,btn):
        if(btn == "on"):
            p.click(1536,224)
        else:
            p.click(1460,224)
    def Transp(self,btn):
        t.sleep(1)
        if(btn == "on"):
            p.click(1534,143)
        else:
            p.click(1460,225)
    def IPR(self, btn):
        self.DownMenu()
        if(btn == "on"):
            p.PAUSE=0.5
            p.click(37,373, clicks=4)
            p.click(235,486)
            t.sleep(3)
            self.Transp("on")
            self.Dist("on")
        else:
            p.PAUSE=0.5
            p.click(38,431, clicks=4)
            p.click(236,540)
            t.sleep(3)
            self.Dist("off")
            
    def Dist(self,btn):
        if(btn == "off"):
            p.click(39,474)
            p.click(61,559)
        else:
            p.click(36,414)
            p.click(203,560)
    def DownMenu(self):
        p.moveTo(255,735)
        p.click(255,735, clicks=2)
    def Photo(self,text):
        p.click(1567,640)
        p.write(text)
        p.press(["tab","tab","tab"])
        p.press("enter")
    def SobreposPhoto(self,op):
        if(op == "sup"):
            p.alert(title="Atenção", text="Você tem 5 segundos para marcar sobreposição")
            t.sleep(5)
            self.Photo("Vista Oclusal Superior com Sobreposicao")
        else:
            p.alert(title="Atenção", text="Você tem 5 segundos para marcar sobreposição")
            t.sleep(5)
            self.Photo("Vista Oclusal Inferior com Sobreposicao")
    def question(self):
        x= p.confirm(title="Tem IPR?",text="",buttons=["SIM","NAO"])
        return x
    def IPRPhoto(self,op):
        p.PAUSE= 0.2
        if(op == "sup"):
            p.alert(title="Atenção", text="Marcou o IPR?")
            x= self.question()
            if(x == "SIM"):
                self.Photo("Vista Oclusal Superior com indicacao IPR")
            else:
                self.Photo("Vista Oclusal Superior sem indicacao IPR")
        else:
            p.alert(title="Atenção", text="Marcou o IPR?")
            x= self.question()
            if(x == "SIM"):
                self.Photo("Vista Oclusal Inferior com indicacao IPR")
            else:
                self.Photo("Vista Oclusal Inferior sem indicacao IPR")
    def Menu(self,btn):
        if(btn == "Otop"):
            p.click(1570,345)
        elif(btn == "Oinf"):
            p.click(1570,311)
        elif(btn == "Right"):
            p.click(1570,238)
        elif(btn == "Left"):
            p.click(1570,275)
        elif(btn == "Front"):
            p.click(1570,166)
        elif(btn == "Post"):
            p.click(1570,202)
        
    def Mand(self,btn):
        if(btn == "off"):
            p.click(1460,118)
        else:
            p.click(1530,115)
    def Max(self,btn):
        if(btn == "off"):
            p.click(1463,92)
        else:
            p.click(1536,88)
    def captFront(self):
        aux= 0
        dc = win32gui.GetDC(0)
        win32gui.MoveToEx(dc,0,0)
        win32gui.LineTo(dc,0,1600)
        p.click(1569,417)
        
        p.alert(title="Atenção", text="Ajuste a posição inicial, alinhe com a linha desenhada na tela")
        #Pega o contexto gráfico para o Desktop
        dc = win32gui.GetDC(0)
        #Desenha uma linha do ponto (0,0) até (1366,768)
        while True:
            win32gui.MoveToEx(dc,0,391)
            win32gui.LineTo(dc,1600,391)
            win32gui.MoveToEx(dc,300,0)
            win32gui.LineTo(dc,300,900)
            win32gui.MoveToEx(dc,0,84)
            win32gui.LineTo(dc,1600,84)
            win32gui.MoveToEx(dc,1371,0)
            win32gui.LineTo(dc,1371,900)
            win32gui.MoveToEx(dc,0,710)
            win32gui.LineTo(dc,1600,710)
            aux += 1
            print(aux)
            if(aux == 120):
                break
        t.sleep(3)
        self.Photo("Vista Oclusao Anterior")
        t.sleep(2)
        p.screenshot(region=(300,84,1070,626)).save(os.environ["USERPROFILE"] + "\\Documents\\PyRelator\\Images\\tmp\\7F.png")
        t.sleep(1)
        #captura essa foto
    def captBack(self):
        p.moveTo(700,391)
        p.moveTo(700,391)
        p.moveTo(700,391)
        p.mouseDown(button="RIGHT")
        p.moveTo(1067,391)
        p.mouseUp(button="LEFT")
        self.Photo("Vista Oclusao Posterior")
    def captLeft90(self):
        p.moveTo(700,391)
        p.mouseDown(button="RIGHT")
        p.moveTo(511,391)
        p.mouseUp(button="RIGHT")
        self.Photo("Vista Lateral Direita 90°")
    def captLeft45(self):
        p.moveTo(700,391)
        p.mouseDown(button="RIGHT")
        p.moveTo(593,391)
        p.mouseUp(button="RIGHT")
        self.Photo("Vista Lateral Direita 45°")
    def captRight90(self):
        p.moveTo(700,391)
        p.mouseDown(button="RIGHT")
        p.moveTo(480,391)
        p.mouseUp(button="RIGHT")
        self.Photo("Vista Lateral Esquerda 90°")
    def captRight45(self):
        p.moveTo(700,391)
        p.mouseDown(button="RIGHT")
        p.moveTo(795,391)
        p.mouseUp(button="RIGHT")
        self.Photo("Vista Lateral Esquerda 45°")
    def captOclSup(self,op):
        p.PAUSE= 0.2
        dc = win32gui.GetDC(0)
        if(op == "sup"):
            self.Menu("Otop")
            self.Mand("off")
            p.alert(title="Atenção", text="Ajuste a posição superior")
            aux= 0
            while True:
                win32gui.MoveToEx(dc,0,80)
                win32gui.LineTo(dc,1600,80)
                win32gui.MoveToEx(dc,300,0)
                win32gui.LineTo(dc,300,900)
                win32gui.MoveToEx(dc,0,800)
                win32gui.LineTo(dc,1600,800)
                win32gui.MoveToEx(dc,1280,0)
                win32gui.LineTo(dc,1280,900)
                aux += 1
                print(aux)
                if(aux == 120):
                    break
            t.sleep(4)
            self.Photo("Vista Oclusal Superior")
        elif(op == "sob"):
            self.Sobrepos("on")
            self.SobreposPhoto("sup") 
            self.Selfie("5")           
        else:
            self.Sobrepos("off")
            self.Transp("on")
            self.IPR("on")
            self.IPRPhoto("sup")
            self.Selfie("S")
    def Selfie(self, name):
        p.screenshot(region=(300,80,980,720)).save(os.environ["USERPROFILE"] + "\\Documents\\PyRelator\\Images\\tmp\\" + name + ".png")
    def captOclInf(self,op):
        if(op == "inf"):
            t.sleep(3)
            self.IPR("off")
            self.Menu("Oinf")
            self.Max("off")
            self.Mand("on")
            p.alert(title="Atenção", text="Ajuste a posição inferior")
            aux= 0
            dc = win32gui.GetDC(0)
            while True:
                win32gui.MoveToEx(dc,0,80)
                win32gui.LineTo(dc,1600,80)
                win32gui.MoveToEx(dc,300,0)
                win32gui.LineTo(dc,300,900)
                win32gui.MoveToEx(dc,0,800)
                win32gui.LineTo(dc,1600,800)
                win32gui.MoveToEx(dc,1280,0)
                win32gui.LineTo(dc,1280,900)
                aux += 1
                print(aux)
                if(aux == 120):
                    break
            t.sleep(4)
            self.Photo("Vista Oclusal Inferior")
        elif(op == "sob"):
            self.Sobrepos("on")
            self.SobreposPhoto("inf")
            self.Selfie("6")
        else:
            self.Sobrepos("off")
            p.click(39,434)
            p.click(256,156)
            self.DownMenu()
            self.IPR("on")
            self.IPRPhoto("inf")
            self.Selfie("I")
    
        
