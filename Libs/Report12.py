import textwrap
import os
from PIL import ImageDraw, Image, ImageFont
import shutil
from datetime import date
import time
import datetime
import re
import subprocess
import tkinter as tt
from tkinter import ttk
from tkinter import Tk, Text, Button, END, Label
import sys

class Report12:
        def __init__(self, db):
                self.calc= 1
                height= 1600
                width= 1104
                bg= (255,255,255)
                padx= 40
                self.database= db
                self.translateVars()
                auxv= 0
                self.width= 1104
                self.Y= 400
                self.tam= 35
                self.fonte= ImageFont.truetype(os.environ["USERPROFILE"] + "\\Documents\\PyRelator\\Fonts\\Arial.ttf",self.tam)
                self.padx= padx
                self.height= 1600
                auxdent= self.dentista.split(" ")
                try:
                        dentista= auxdent[0] + " " + auxdent[1]
                except Exception:
                        dentista= self.dentista
                if("a" in self.comment):
                		self.comment= self.comment.replace("\n"," <break> <break> ")
                		self.comment= "Prezado(a) " + dentista + " <break> " + self.comment
                for k in self.comment.split(" "):
                        auxv += 1
                        if(k == "<break>"):
                                self.calc += 1
                        if(auxv % 7 == 0):
                                self.calc += 1
                height= height + (self.calc * 40) - 200
                self.book= Image.new("RGB",(width,height),bg)
                self.draw= ImageDraw.Draw(self.book)
                self.cRect((0,0,self.width,int(340)),(31,91,141))
                self.Textc("Resumo Setup Virtual",(255,255,255),["c",230], 60)
                self.img(os.environ["USERPROFILE"] + "\\Documents\\PyRelator\\Images\\OrthoAligner.png",-7,center= ["c",-60])
                texto= "O Setup Virtual para < {paciente} > foi planejado conforme suas instruções."
                if("a" in self.comment):
                	texto += " <break> <break> " + self.comment + " <break> "
                texto += " <break> <break> Para realizar a etapa do presente planejamento, serão necessários: "
                texto += "<break> <break> Alinhadores Superiores: < {sup} > "
                texto += "<break> Alinhadores Inferiores: < {inf} > "
                texto += "<break> <break> Total de Alinhadores: < {total}({extenso}) > <break> <break>"
                if("Fase" in self.pacote or "Refino" in self.pacote):
                		texto += " < "
                if(self.pacote == "Fase II"):
                		texto += "Tratado anteriormente com OrthoAligner Fase I"
                elif(self.pacote == "Fase III"):
                		texto += "Tratado anteriormente com OrthoAligner Fase I, II"
                elif(self.pacote == "Fase IV"):
                		texto += "Tratado anteriormente com OrthoAligner Fase I, II, III"
                elif(self.pacote == "Fase V"):
                		texto += "Tratado anteriormente com OrthoAligner Fase I, II, III, IV"
                elif(self.pacote == "Fase VI"):
                		texto += "Tratado anteriormente com OrthoAligner Fase I, II, III, IV, V"
                if(self.pacote == "Refino II"):
                		texto += "Tratado anteriormente com OrthoAligner Refino I"
                elif(self.pacote == "Refino III"):
                		texto += "Tratado anteriormente com OrthoAligner Refino I, II"
                elif(self.pacote == "Refino IV"):
                		texto += "Tratado anteriormente com OrthoAligner Refino I, II, III"
                elif(self.pacote == "Refino V"):
                		texto += "Tratado anteriormente com OrthoAligner Refino I, II, III, IV"
                elif(self.pacote == "Refino VI"):
                		texto += "Tratado anteriormente com OrthoAligner Refino I, II, III, IV, V"
                texto += " > <break> O caso será tratado com um < OrthoAligner {pacote} > <break>"
                if("Fase" in self.pacote or "Refino" in self.pacote):
                		texto += " < " + self.validade + " > "
                texto= texto.replace("|"," <break> ")
                sup= self.sup
                inf= self.inf
                if(self.sup == "0"):
                        sup= "-"
                if(self.inf == "0"):
                        inf= "-"
                self.supp= sup
                self.inff= inf
                self.att= 0
                if(self.supatt != ""):
                        self.att += 1
                if(self.infatt != ""):
                        self.att += 1
                texto= texto.format(paciente=self.paciente,sup=str(sup) + self.supatt,inf=str(inf) + self.infatt,total=int(self.sup) + int(self.inf) + int(self.att), extenso=self.extenso(str(int(self.sup) + int(self.inf) + int(self.att))),pacote= self.pacote)
                self.Paragraph(texto)
                self.cRect((0,height-100,width,height),bg=(31,91,141))
                self.Textc("Consulte as informações completas na Ficha de Instruções",(255,255,255),["c",height-70], 40)
                self.book.save(self.path + f"\\12 - Resumo de {self.tsetup} - {self.paciente}.png")
        def cRect(self,coords,bg):
                self.draw.rectangle(coords,fill=bg)
        def translateVars(self):
                self.tsetup= self.database["setup"]
                try:
                        self.supatt= self.database["supatt"]
                except KeyError:
                        self.supatt= ""
                try:
                        self.infatt= self.database["infatt"]
                except KeyError:
                        self.infatt= ""
                self.paciente= self.database["paciente"]
                self.dentista= self.database["dentista"]
                self.sup= self.database["sup"]
                self.inf= self.database["inf"]
                self.vest= self.database["vestibular"]
                self.lin= self.database["lingual"]
                self.ocl= self.database["oclusal"]
                self.pacote= self.database["pacote"]
                self.ortodont= self.database["ortodontista"]
                self.validade= self.database["prazo"]
                self.path= self.database["path"]
                self.comment= self.database["comentario"]
        def Reg(self,text):
                self.log.write(self.data + " - " + text)
        def Paragraph(self,txt):
        		temp= " "
        		cont= 40
        		txt= re.split(" ",txt)
        		print(txt)
        		cursor= self.padx
        		for i in txt:
        				try:
        						cursor= self.get_text_dimensions(i, self.fonte)
        				except Exception:
        						pass
        				if(cont >= self.width - (self.padx * 2) - 130):
        						cont= self.padx
        						self.Y += 37
        				if(i == "<break>" or i == "\n"):
        						print("entrei")
        						cont= self.padx
        						self.Y += 37
        						i = i.replace("<break>","")
        						print(i)
        				elif(i == "<"):
        						self.fonte= ImageFont.truetype("C:\\Program Files\\PyReport-1600X900\\build\\exe.win-amd64-3.9\\fonts\\Arial-Bold.ttf",self.tam)
        				elif(i == ">"):
        						self.fonte= ImageFont.truetype("C:\\Program Files\\PyReport-1600X900\\build\\exe.win-amd64-3.9\\fonts\\Arial.ttf",self.tam)
        				else:
        						self.draw.text((cont, self.Y),i,fill= (0,0,0),font= self.fonte)
        						print(cont, cursor)
        						cont= cont + cursor[0] + 10
        def Textc(self,txt,color,c,tam):
                fonte= ImageFont.truetype("C:\\Program Files\\PyReport-1600X900\\build\\exe.win-amd64-3.9\\fonts\\Arial.ttf",tam)
                if("c" in c):
                	x= self.draw.textlength(txt, font= fonte)
                	self.draw.text((int((self.width-x)/2),c[1]),txt,fill=color,font=fonte)
        def get_text_dimensions(self,text_string, font):
        		ascent, descent = font.getmetrics()
        		text_width = font.getmask(text_string).getbbox()[2]
        		text_height = font.getmask(text_string).getbbox()[3] + descent
        		return [text_width, text_height]
        def img(self,fp,scale,center):
                img= Image.open(fp)
                if(scale >= 1):
                        img= img.resize((img.size[0]*scale,img.size[1]*scale))
                else:
                        scale *= -1
                        img= img.resize((int(img.size[0]/scale),int(img.size[1]/scale)))
                if("c" in center):
                        self.book.paste(img,(int((self.width - img.size[0])/2),center[1]),mask=img)
                else:
                        self.book.paste(img,center[0],center[1],mask=img)
        def extenso(self,num):
                listadef= {}
                n= [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,30,40,50,60,70,80,90,100]
                nums= ["um","dois","Três","Quatro","Cinco","Seis","Sete","Oito","Nove","Dez","Onze",
                       "Doze","Treze","Quatorze","Quinze","Dezesseis","Dezessete","Dezoito","Dezenove",
                       "Vinte","Trinta","Quarenta","Cinquenta","Sessenta","Setenta","Oitenta","Noventa",
                       "Cem"]
                if(int(num) == 0):
                    if(num == self.sup or num == self.inf):
                        return "-"
                    else:
                        return "zero"
                for pp in range(0,len(n)):
                        listadef[n[pp]]= nums[pp]
                if(int(num) in n):
                        return listadef[int(num)]
                kk= ""
                x=0
                numstr= str(num)
                total = int(self.sup) + int(self.inf)
                if(int(num) > 100):
                        kk += "Cento e "
                        numstr= numstr[1] + numstr[2]
                if(int(num) > 10 and int(num) < 100 or total > 100):
                        numstr= int(numstr)
                        if(numstr in n):
                            kk = kk + listadef[int(numstr)]
                        else:
                            numstr= str(numstr)
                            dez= int(numstr[0] + "0")
                            un= int(numstr[1])
                            kk= kk + listadef[dez] + " e " + listadef[un]
                #kk = kk + listadef[int(str(str(num[x]) + "0"))] + " e " + listadef[int(str(num[x+1]))]
                return kk



