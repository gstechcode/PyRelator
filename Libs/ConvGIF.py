#CONVERTE GIFS

import cv2
import time
from tkinter import *
import tkinter as tt
from tkinter import ttk
from PIL import Image
import subprocess
import imageio
import os

class ConvGIF:
        def __init__(self, master):
                self.master= master
                self.translateVars()
                self.temp= Tk()
                self.temp.title("Todos os vídeos estão na pasta?")
                self.temp.config(bg="orange", padx="100px", pady="30px")
                btn= Button(self.temp, text="Sim", command= self.go, bg="green", fg="white", relief="flat", font="Arial 18")
                btn.pack(pady="10px")
                self.temp.mainloop()
                self.display= Tk()
                self.display.title("PyReport")
                self.lbl= tt.Label(self.display, text="Verificando vídeos... 0%", fg="white", bg="orange", font="Arial 18")
                self.lbl.pack(pady="10px")
                self.progress= ttk.Progressbar(self.display, mode="determinate", orient="horizontal", length= 100)
                self.progress.pack(pady="10px")
                self.display.config(bg="orange", padx= "30px", pady="30px")
                self.infff= 0
                self.setup= self.path.split("\\")
                self.setup= self.setup[len(self.setup) - 1]
                self.VerifyFiles()
                self.display.mainloop()
        def translateVars(self):
                self.path= self.master["path"]
                self.sup= self.master["sup"]
                self.inf= self.master["inf"]
                self.diagnostico= self.master["diagnostico"]
        def go(self):
                self.temp.destroy()
        def StatusBar(self, text, value):
                self.display.update()
                self.lbl["text"]= text
                self.progress["value"] = value
                self.display.update()
        def VerifyFiles(self):
                self.display.update()
                main= self.path + "/"
                file1,file2, file3, file4, file8= main + "1.avi", main + "2.avi", main + "3.avi", main + "4.avi", main + "8.avi"
                if(self.sup != "0" and self.inf != "0"):
                        print(1)
                        while True:
                                if(os.path.isfile(file1) and os.path.isfile(file2) and os.path.isfile(file3) and os.path.isfile(file4) and os.path.isfile(file8)):
                                        break
                                else:
                                        self.display.update()
                                        time.sleep(2)
                elif(self.sup == "0" or self.sup == "-"):
                        print(2)
                        while True:
                                if(os.path.isfile(file1) and os.path.isfile(file2) and os.path.isfile(file3) and os.path.isfile(file8)):
                                        break
                                else:
                                        self.display.update()
                                        time.sleep(2)
                elif(self.inf == "0" or self.inf == "-"):
                        print(3)
                        while True:
                                if(os.path.isfile(file1) and os.path.isfile(file2) and os.path.isfile(file3) and os.path.isfile(file4)):
                                        break
                                else:
                                        self.display.update()
                                        time.sleep(2)
                self.StatusBar("Convertendo vídeos... 40%", 30) 
                self.CFiles("1","Video Vista Lateral Direita")
                self.StatusBar("Convertendo vídeos... 60%", 40)
                self.CFiles("2","Video Vista Frontal")
                self.StatusBar("Convertendo vídeos... 80%", 80)
                self.CFiles("3","Video Vista Lateral Esquerda")
                if(self.diagnostico):
                        self.CFiles("4","Video Vista Oclusal Superior")
                        self.CFiles("8","Video Vista Oclusal Inferior")
                        self.StatusBar("Convertendo vídeos... 100%", 100)
                        self.display.destroy()
                        return 0;       
                if(self.sup != "0"):
                        if(int(self.sup) > int(self.inf)):
                                self.CFiles("4","Video Vista Oclusal Superior")
                        else:
                                self.SubFiles("4","Video Vista Oclusal Superior",self.sup)
                if(self.inf != "0"):
                        if(int(self.inf) > int(self.sup)):
                                self.CFiles("8","Video Vista Oclusal Inferior")
                        else:
                                self.SubFiles("8","Video Vista Oclusal Inferior",self.inf)
                self.StatusBar("Convertendo vídeos... 100%", 100)
                self.display.destroy()
        def CFiles(self,video,name):
                print(f"{self.path}\\{video}.avi", f"{self.path}\\0{video} - {name} - {self.setup}.gif")
                self.video1= CoreMovie(f"{self.path}\\{video}.avi", f"{self.path}\\0{video} - {name} - {self.setup}.gif", pgs=self.lbl, update= self.display.update)
                os.rename(f"{self.path}\\{video}.avi",f"{self.path}\\0{video} - {name} - {self.setup}.avi")
        def SubFiles(self,video,name, endx):
                self.video1= CoreMovie(f"{self.path}\\{video}.avi", f"{self.path}\\0{video} - {name} - {self.setup}.gif", end= endx, pgs= self.lbl, update= self.display.update)
                os.rename(f"{self.path}\\{video}.avi",f"{self.path}\\0{video} - {name} - {self.setup}.avi")


class CoreMovie:
        def __init__(self,video,name, pgs, update, end= 1000000000000000000000000000):
                frames = []
                progress= pgs
                self.progress= pgs
                self.name= name
                self.update= update
                self.video= video
                if(int(end) < 10000):
                    end = int(end) * 15
                cap= cv2.VideoCapture(self.video)
                image_count = 0
                progress["text"]= "Processando video..."
                update()
                while True:
                    ret, frame = cap.read()
                    if(ret == 1):
                        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                        image_count += 1
                        frames.append(rgb_frame)
                        update()
                        if(image_count == int(end) + 8):
                            break
                    else:
                        break
                cap.release()
                cv2.destroyAllWindows()
                progress["text"]= "Salvando GIF..."
                update()
                with imageio.get_writer(self.name, mode="I", fps=30) as writer:
                    for idx, frame in enumerate(frames):
                        writer.append_data(frame)
                        update()
                self.Optimize()
        def Optimize(self):
                self.progress["text"]= "Otimizando GIF..."
                self.update()
                gifsicle= os.environ["USERPROFILE"] + "\\Documents\\PyRelator\\Tools\\gifsicle.exe"
                DETACHED_PROCESS = 0x00000008
                subprocess.call(f'"{gifsicle}" -i "{self.name}" -O3 --colors 256 -o "{self.name}"')
