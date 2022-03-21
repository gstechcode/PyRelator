import pyautogui as p
import time as t

class settings:
    def __init__(self):
        try:
            self.ortho= p.getWindowsWithTitle("OrthoAnalyzer")
            self.ortho[0].activate()
            self.ortho[0].maximize()
            self.chrome= p.getWindowsWithTitle("Google Chrome")
        except Exception:
            pass
    def setupActive(self):
        p.click(26,237)
    def estCapt(self, op, arcs):
        p.click(1400,34)
        t.sleep(2)
        path= self.path + "\\"
        p.click(254,154)
        t.sleep(3)
        p.click(226,239)
        t.sleep(1)
        if(op == "SIM"):
            p.click(1140,73)
            p.click(486,12)
            t.sleep(1)
            if(arcs == "Superior" or arcs == "Ambas"):
                p.click(1140,73)
                t.sleep(2)
                p.screenshot(region=(253,50,871,370)).save(path + "09 - Estagiamento " + str(self.master["sup"]) + " Superior - " + self.master["setup"] + ".png")
            if(arcs == "Inferior" or arcs == "Ambas"):
                p.click(1141,359)
                p.click(486,12)
                t.sleep(2)
                p.screenshot(region=(253,97,871,320)).save(path + "10 - Estagiamento " + str(self.master["inf"]) + " Inferior - " + self.master["setup"] + ".png")
        p.click(1134,12)
        p.click(354,71)
        t.sleep(4)
        p.screenshot(region=(3,32,1129,596)).save(path + "11 - Tabela de Movimentacao - " + self.master["setup"] + ".png")
        p.alert(title="Sucesso!", text="Capturas realizadas com sucesso!")
    def modelAc(self):
        p.press("pagedown")
        p.press("enter", presses=3)
    def btnBack(self):
        p.click(67,55)
    def modelDefault(self):
        p.click(70,264, clicks=3)
    def report(self):
        t.sleep(3)
        self.ortho[0].activate()
        self.PAUSE= 2
        self.btnBack()
        p.click(185,304)
        p.click(102,274)
        p.click(900,275)
        t.sleep(5)
        p.press("tab")
        p.press("enter")                 
        self.chrome[0].activate()
        self.chrome[0].maximize()
        t.sleep(10)
        p.hotkey("ctrl","p")
        t.sleep(2)
        p.press("enter")
        t.sleep(6)
        p.write(self.path)
        p.press("enter")
        p.write("13")
        p.press("tab", presses=3)
        p.press("enter")
        p.PAUSE= 1
        self.ortho[0].activate()
        self.ortho[0].maximize()
        t.sleep(5)
        self.btnBack()
        self.btnMV()
        self.modelDefault()
        p.PAUSE= 2
        self.modelAc()
        self.setupActive()
        p.PAUSE= 1
    def btnMV(self):
        p.click(33,414)
        
