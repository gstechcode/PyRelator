import json, os, time
import psutil
from tkinter import *
from tkinter import ttk
from threading import Thread
from Views import FormMain
from Libs import Capture
from Libs import Report14
from Libs import Report12
from Libs import IPR
from Libs import ConvGIF
from Libs import ConvertSTLs

class PyRelator:
	def __init__(self):
		while True:
			if(not self.MonitorIsRunning()):
				self.MonitorConnection()
			else:
				formulario= FormMain.Execute()
				banco= self.getBanco()
				if(banco["relatorios1214"]):
					report14= Report14.Report14(banco)
					report12= Report12.Report12(banco)
					report12= Report12.Report12(banco)
				if(banco["capturas"]):
					capturas= Capture.CaptureView(banco)
				if(banco["relatorioipr"]):
					ipr= IPR.Report(banco)
				if(banco["otimizargifs"]):
					gifot= ConvGIF.ConvGIF(banco)
				if(banco["otimizarstls"]):
					stGabriellot= ConvertSTLs.ConvertSTLs(banco)
				break
	def getBanco(self):
		db= open(os.environ["USERPROFILE"] + "\\Documents\\PyRelator\\Cache\\FormMain.cache","r")
		return json.loads(db.readlines()[0])
	def MonitorIsRunning(self):
		return "PyMonitor.exe" in (i.name() for i in psutil.process_iter())
	def MonitorConnection(self):
		self.display= Tk()
		self.display.title("PyMonitor Control")
		self.display.config(bg="orange", padx="10px", pady="10px")
		self.label= Label(self.display, bg="orange", fg="white", text="Conectando ao Monitor...", font="Arial 22")
		self.label.pack(pady="10px")
		self.progress= ttk.Progressbar(self.display, mode="determinate", length= 300, maximum= 100)
		self.progress.pack(pady="10px")
		self.MonitorConnecting()
		self.display.mainloop()
	def MonitorConnecting(self):
		while(not self.MonitorIsRunning()):
			self.display.update()
		self.label["text"]= "Sincronizando..."
		self.progress.start()
		while(self.progress["value"] != 99.0):
			self.display.update()
		self.display.destroy()
x= PyRelator()