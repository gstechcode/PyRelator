#modulo responsável por verificar a versão atual do software e atualizar
from urllib.request import urlopen as readURL
from urllib import request
import shutil
from bs4 import BeautifulSoup as Processor
from zipfile import ZipFile
import os
from tkinter import *
import json
import ctypes

class Manager:
	def __init__(self):
		self.dest= os.environ["USERPROFILE"] + "\\Documents"
		self.UPDATED= 0
		update= { "updated": False}
		stateChange= open(self.dest + "\\PyRelator\\settings.config","w")
		stateChange.write(json.dumps(update))
		stateChange.close()
		self.run()
	def readVersaoL(self): #pega a versão local
		try:
			file= open(self.dest + "\\PyRelator\\version.version","r")
			content= file.readlines()[0]
			file.close()

			return content
		except FileNotFoundError:
			return "Not installed"
	def Mbox(self,title, text, style):
		return ctypes.windll.user32.MessageBoxW(0, text, title, style)
	def readUpdates(self): #pega os textos de update
		info= readURL("https://github.com/gstechcode/PyRelator/blob/master/README.md")
		info= Processor(info.read(),"html.parser")
		return info.find(id="user-content-appatualizacao").contents
	def readVersionR(self): #pega versão remota
		info= readURL("https://github.com/gstechcode/PyRelator/blob/master/README.md")
		info= Processor(info.read(),"html.parser")
		return info.find(id="user-content-appversao").contents[1]
	def verififyState(self): #essa função deverá identificar o que será update, install or run
		versaoremota= self.readVersionR()
		textoatualizacao= self.readUpdates()
		versaolocal= self.readVersaoL()
		if(versaolocal == "Not installed"):
			return versaolocal
		return versaoremota != versaolocal
	def atualizar(self):
		x= self.Mbox('Atualização do PyRelator', 'Há uma nova atualização disponível! Atualizar agora?', 1)
		if(x == 1):
			self.getFile()
			update= { "updated": True}
			stateChange= open(self.dest + "\\PyRelator\\settings.config","w")
			stateChange.write(json.dumps(update))
			stateChange.close()
			self.MessageUpdate()
	def MessageUpdate(self):
		x= ""
		for i in self.readUpdates():
			x += str(i)
		x= x.replace("\n  ","")
		x= x.split("<br/>")
		i= Tk()
		i.title("PyRelator - Nova versão" + str(self.readVersaoL()))
		i.config(padx="10px", pady="10px", bg="white")
		lbl= Label(i,text="Novidades da versão " + str(self.readVersaoL()), fg="orange", bg="white", font="Arial 20 bold")
		lbl.pack(pady="40px")
		for p in x:
			lbl2= Label(i,text="Novidades da versão " + p, fg="black", bg="white", font="Arial 13 bold")
			lbl2.pack()
		btn= Button(i, text="Entendi", bg="green", fg="white", font="Arial 14", relief=FLAT, command= i.destroy)
		btn.pack()
		i.mainloop()
	def instalar(self):
		self.getFile()
		os.system(self.dest + "\\PyRelator\\Tools\\inkscape.exe")
	def removeFolder(self):
		try:
			shutil.rmtree(self.dest + "\\PyRelator")
		except Exception:
			pass
	def getFile(self):
		request.urlretrieve("https://github.com/gstechcode/PyRelator/archive/refs/heads/master.zip",self.dest + "\\PyReport.zip")
		self.removeFolder()
		folderzipped= ZipFile(self.dest + "\\PyReport.zip","r")
		folderzipped.extractall(self.dest + "\\PyReportdeszip")
		folderzipped.close()
		shutil.copytree(self.dest + "\\PyReportdeszip\\PyRelator-master", self.dest + "\\PyRelator")
		shutil.rmtree(self.dest + "\\PyReportdeszip")
		os.remove(self.dest + "\\PyReport.zip")
	def refresh(self, op):
		if(op == True):
			self.atualizar()
		elif(op == "Not installed"):
			self.instalar()
		os.system(self.dest + "\\PyRelator\\PyRelator.py")
	def run(self): #ação de acordo com o estado
		self.refresh(self.verififyState())

x= Manager()