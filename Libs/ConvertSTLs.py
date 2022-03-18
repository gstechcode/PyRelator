#OTIMIZA STLS E RENOMEIA ARQUIVOS

from tkinter import *
import zipfile, time, os, shutil
from tkinter import ttk
from datetime import date
import subprocess

class ConvertSTLs:
        def __init__(self, master):
                self.master= master
                self.translateVars()
                self.temp= Tk()
                self.temp.title("PyRelator - Conversor de STLs")
                self.temp.config(bg="orange", padx="100px", pady="30px")
                self.label= Label(self.temp, text="Pronto para otimizar os STLs?",bg="orange", fg="white", font="Arial 15")
                self.btn= Button(self.temp, text="Sim", command= self.rename, bg="green", fg="white", relief="flat", font="Arial 18")
                self.btn.pack(pady="10px")
                self.temp.mainloop()
        def translateVars(self):
                self.path= self.master["path"]
                self.paciente= self.master["paciente"]
                self.setup= self.master["setup"]
        def rename(self):
                self.btn.pack_forget()
                self.label.pack_forget()
                self.lbl= Label(self.temp, text="Renomeando e convertendo STLs... 0%", bg="orange", fg="white", font="Arial 15")
                self.lbl.pack(pady="10px")
                self.progress= ttk.Progressbar(self.temp, mode="determinate", orient="horizontal", length= 100)
                self.progress.pack(pady="10px")
                try:
                        os.rename(self.path + "\\5.png",self.path + f"\\05 - Sobreposicao {self.setup} Superior - {self.paciente}.jpg")
                except Exception:
                        pass
                try:
                        os.rename(self.path + "\\6.png",self.path + f"\\06 - Sobreposicao {self.setup} Inferior - {self.paciente}.jpg")
                except Exception:
                        pass
                try:
                        os.rename(self.path + "\\13.pdf",self.path + f"\\13 - Relatorio de {self.setup} - {self.paciente}.pdf")
                except Exception:
                        pass
                self.renamePart2()
        def renamePart2(self):
                self.lbl["text"]= "Renomeando e convertendo STLs... 20%"
                self.progress["value"]= 20
                self.temp.update()
                time.sleep(2)
                self.processSTL()
        def getSTL(self, model):
                if(not(os.path.exists(f"{os.environ['USERPROFILE']}\\Documents\\PyRelator\\Convert"))):
                        os.mkdir(f"{os.environ['USERPROFILE']}\\Documents\\PyRelator\\Convert")
                self.localdoc= f"{os.environ['USERPROFILE']}\\Documents\\PyRelator\\Convert"
                shutil.move(f"{self.path}\\{model}",f"{self.localdoc}\\{model}")
                return f'"C:\Program Files\VCG\MeshLab\meshlabserver.exe" -i "{self.localdoc}\{model}" -o "{self.localdoc}\{model}" -s C:\multimeshscripting\scripts\simple_script.mlx -om vc fq wn'
        def processSTL(self):
                DETACHED_PROCESS = 0x00000008
                script= self.getSTL("15.stl")
                try:
                        subprocess.call(script, creationflags=DETACHED_PROCESS)
                        shutil.move(self.localdoc + "\\15.stl", self.path + f"\\15 - Modelo Original Superior - {self.paciente}.stl")
                except Exception:
                        pass
                script= self.getSTL("16.stl")
                try:
                        subprocess.call(script, creationflags=DETACHED_PROCESS)
                        shutil.move(self.localdoc + "\\16.stl", self.path + f"\\16 - Modelo Original Inferior - {self.paciente}.stl")
                except Exception:
                        pass
                script= self.getSTL("17.stl")
                try:
                        subprocess.call(script, creationflags=DETACHED_PROCESS)
                        shutil.move(self.localdoc + "\\17.stl", self.path + f"\\17 - Modelo {self.setup} Superior - {self.paciente}.stl")
                except Exception:
                        pass
                script= self.getSTL("18.stl")
                try:
                        subprocess.call(script, creationflags=DETACHED_PROCESS)
                        shutil.move(self.localdoc + "\\18.stl", self.path + f"\\18 - Modelo {self.setup} Inferior - {self.paciente}.stl")
                except Exception:
                        pass
                filestozip= []
                self.lbl["text"]= "Renomeando e convertendo STLs... 70%"
                self.progress["value"]= 70
                self.temp.update()
                time.sleep(1)
                
                self.lbl["text"]= "Compactando arquivos... 90%"
                self.progress["value"]= 90
                self.temp.update()
                time.sleep(1)
                for i in os.listdir(self.path):
                        if(".avi" in i):
                                continue
                        else:
                                filestozip.append(self.path + "\\" + i)

                dtsetup= date.today()
                self.ttsetup= self.setup.replace(" ","_")
                dtsetup= self.ttsetup + f"_{dtsetup.day}_{dtsetup.month}_{dtsetup.year}"
                
                filezip= zipfile.ZipFile(self.path + f"\\{dtsetup}.zip", 'w')

                for f in filestozip:
                        k= f.split("\\")
                        fname= k[len(k) - 1]
                        filezip.write(f,fname, compress_type = zipfile.ZIP_DEFLATED)
                filezip.close()
                self.temp.destroy()