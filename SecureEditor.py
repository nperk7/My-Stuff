# -*- coding: utf-8 -*-
__author__ = 'naperkins'
import os
import myEncrypt as en
from Tkinter import *
import tkFileDialog
import sys
import platform
import re
def upperfirst(x):
    return x[0].upper() + x[1:]
if platform.system().find('Darwin') != -1:
    class editFile():
        def __init__(self, roots):
            self.master = roots
            self.labelLog = Label(self.master, text='SimplEdit',bg='gray19', fg='green', font=("Times",20))
            self.labelLog.place(x=410,y=215)
            self.passWord = Entry(self.master, show="§", bd=5, relief=SUNKEN, bg='gray31', fg='white smoke')
            self.passWord.place(x=400,y=275)
            self.passWord.focus_set()
        def create(self):
            self.passWord.destroy()
            self.opnTxt = ""
            self.g = Button(self.master, text="Open File", command=self.get)
            self.g.place(x=0,y=0)
            self.s = Button(self.master, text="Save", command=self.sve)
            self.s.place(x=94,y=0)
            self.e = Button(self.master, text="Eject Drive", command=self.ejct)
            self.e.place(x=0,y=27)
            self.m = Button(self.master, text="Mount Drive", command=self.mount)
            self.m.place(x=94,y=27)
            self.title = Entry(self.master,bd=5,relief=GROOVE, bg='gray31', fg='white smoke')
            self.title.insert(0, "Document Name")
            self.title.place(x=196,y=27)
            self.scrollbar = Scrollbar(self.master)
            self.scrollbar.pack(side=RIGHT, fill=Y)
            self.t = Text(self.master, width=80, height= 30, bg='dim gray', font=("Times New Roman",14), fg="white smoke", relief=RIDGE, yscrollcommand=self.scrollbar.set)
            #self.t = Text(self.master, width=80, height= 30, bg='gray24', font=("Times New Roman",14), fg="gray76")
            self.t.insert(END, self.opnTxt)
            self.t.place(x=196,y=57)
            self.scrollbar.config(command=self.t.yview)
            self.t.focus_set()
        def sve(self):
            try:
                data = self.t.get(1.0, END)
                name = self.title.get()
                docName = os.path.expanduser("/Volumes/SURFACEPRO4/%s.txt" % name)
                fle = open(docName, "w")
                fle.write(en.encr(data))
                fle.close()
            except:
                self.befTxt = self.t.get(1.0, END)
                self.t.destroy()
                self.scrollbar.destroy()
                self.scrollbar = Scrollbar(self.master)
                self.scrollbar.pack(side=RIGHT, fill=Y)
                self.t = Text(self.master, width=80, height= 30, bg='dim gray', font=("Times New Roman",14), fg="white smoke", relief=RIDGE, yscrollcommand=self.scrollbar.set)
                #self.t = Text(self.master, width=80, height= 30, bg='gray24', font=("Times New Roman",14), fg="gray76")
                self.t.insert(END, self.opnTxt)
                self.t.place(x=196,y=57)
                self.scrollbar.config(command=self.t.yview)
                self.t.insert(END, "Please click mount drive and or insert a flash drive.")
        def get(self):
            self.flPath = tkFileDialog.askopenfilename(title="Choose A File")
            if self.flPath != '':
                docName = os.path.expanduser("%s" % self.flPath)
                fle = open(docName, "r")
                self.opnTxt = en.encr(fle.read())
                fle.close()
                try:
                    self.title.destroy()
                except:
                    pass
                self.title = Entry(self.master,bd=5,relief=GROOVE)
                self.title.insert(0, self.flPath[21:self.flPath.find(".")])
                self.title.place(x=196,y=27)
                try:
                    self.t.destroy()
                    self.scrollbar.destroy()
                except:
                    pass
                self.scrollbar = Scrollbar(self.master)
                self.scrollbar.pack(side=RIGHT, fill=Y)
                self.t = Text(self.master, width=80, height= 30, bg='dim gray', font=("Times New Roman",14), fg="white smoke", relief=RIDGE, yscrollcommand=self.scrollbar.set)
                #self.t = Text(self.master, width=80, height= 30, bg='gray24', font=("Times New Roman",14), fg="gray76")
                self.t.place(x=196,y=57)
                self.scrollbar.config(command=self.t.yview)
                self.t.insert(END, self.opnTxt)
            else:
                pass
        def updat(self):
            self.master.update()
            try:
                if self.passWord.get() == "Nperkins30":
                    self.create()
            except:
                pass
            self.master.bind("<Button-2>", self.autoCorrect)
        def ejct(self):
            os.system("diskutil unmount SURFACEPRO4")
        def mount(self):
            self.t.destroy()
            self.scrollbar.destroy()
            self.scrollbar = Scrollbar(self.master)
            self.scrollbar.pack(side=RIGHT, fill=Y)
            self.t = Text(self.master, width=80, height= 30, bg='dim gray', font=("Times New Roman",14), fg="white smoke", relief=RIDGE, yscrollcommand=self.scrollbar.set)
            #self.t = Text(self.master, width=80, height= 30, bg='gray24', font=("Times New Roman",14), fg="gray76")
            self.t.insert(END, self.opnTxt)
            self.t.place(x=196,y=57)
            self.scrollbar.config(command=self.t.yview)
            self.t.insert(END, self.befTxt)
            os.system("diskutil mount SURFACEPRO4")
            self.sve()
        def autoCorrect(self, *args):
            correctData = self.t.get(1.0, END)
            try:
                dictTion = {'helo': 'hello', 'helllo': 'hello', 'paladium': 'palladium', 'paladuim': 'palladium', 'palladuim': 'palladium',
                            'cnversation': 'conversation', 'conversatuon': 'conversation', 'whell': 'well', 'ad': 'and', 'theis': 'this ',
                            'knwo': 'know', 'kno': 'know', 'eill': 'will', 'i': 'I', 'si': 'is', 'burron': 'button', 'rhytym': 'rhythm',
                            'rhythym': 'rhythm', 'lekely': 'likely', 'likeley': 'likely', 'asure': 'assure', 'militry': 'military',
                            'statment': 'statement', 'rhytm': 'rhythm', 'futuer': 'future', 'futeur': 'future', 'teh': 'the', 'mispell': 'misspell',
                            'paralell': 'parallel', 'accidentaly': 'accidentally', 'acuire': 'acquire', 'aquire': 'acquire', 'accomodate': 'accommodate',
                            'accomodation': 'accommodation', 'acheive': 'achieve', 'accross': 'across', 'agressive': 'aggressive', 'agression': 'aggression',
                            'apparantly': 'apparently', 'appearence': 'appearance', 'arguement': 'argument', 'assasination': 'assassination',
                            'basicly': 'basically', 'begining': 'beginning', 'beleive': 'believe', 'belive': 'believe', 'bizzare': 'bizarre',
                            'buisness': 'business', 'calender': 'calendar', 'carribean': 'caribbean', 'cemetary': 'cemetery', 'chauffer': 'chauffeur',
                            'collegue': 'colleague', 'comming': 'coming', 'commitee': 'committee', 'completly': 'completely', 'concious': 'conscious'}
                for g in dictTion:
                    if correctData.find('%s ' % g) != -1:
                        correctData = correctData.replace('%s ' % g, '%s ' % dictTion[g])
                    if correctData.find(' %s' % g) != -1:
                        correctData = correctData.replace(' %s' % g, ' %s' % dictTion[g])
                    if correctData.find('%s,' % g) != -1:
                        correctData = correctData.replace('%s,' % g, '%s,' % dictTion[g])
                    if correctData.find('%s ' % g.title()) != -1:
                        correctData = correctData.replace('%s ' % g.title(), '%s ' % dictTion[g].title())
                    if correctData.find(' %s' % g.title()) != -1:
                        correctData = correctData.replace(' %s' % g.title(), ' %s' % dictTion[g].title())
                    if correctData.find('%s,' % g.title()) != -1:
                        correctData = correctData.replace('%s,' % g.title(), '%s,' % dictTion[g].title())
                #print correctData
                '''twPer = []
                onPer = []
                for m in re.finditer('. ', correctData):
                    onPer.append(m.start()+2)
                for k in re.finditer('.  ', correctData):
                    twPer.append(k.start()+3)
                for j in onPer:
                    correctData = correctData.replace(correctData[j], correctData[j].upper())
                for l in twPer:
                    correctData = correctData.replace(correctData[l], correctData[l].upper())
                correctData = upperfirst(correctData)'''
                self.t.destroy()
                self.scrollbar.destroy()
                self.scrollbar = Scrollbar(self.master)
                self.scrollbar.pack(side=RIGHT, fill=Y)
                self.t = Text(self.master, width=80, height= 30, bg='dim gray', font=("Times New Roman",14), fg="white smoke", relief=RIDGE, yscrollcommand=self.scrollbar.set)
                #self.t = Text(self.master, width=80, height= 30, bg='gray24', font=("Times New Roman",14), fg="gray76")
                self.t.insert(END, self.opnTxt)
                self.t.place(x=196,y=57)
                self.scrollbar.config(command=self.t.yview)
                self.t.insert(END, correctData[:-1])
            except:
                pass
if platform.system().find('Windows') != -1:
    class editFile():
        def __init__(self, roots):
            self.master = roots
            self.labelLog = Label(self.master, text='SimplEdit',bg='gray19', fg='green', font=("fixedsys",20))
            self.labelLog.place(x=395,y=195)
            self.entrPass = Label(self.master, text='Please enter your password',bg='gray19', fg='white smoke', font=("Helvetica",14))
            self.entrPass.place(x=355,y=240)
            self.passWord = Entry(self.master, show="§", bd=5, relief=SUNKEN, bg='gray31', fg='white smoke')
            self.passWord.place(x=400,y=275)
            self.passWord.focus_set()
        def create(self):
            self.passWord.destroy()
            self.opnTxt = ""
            self.g = Button(self.master, text="Open File", command=self.get)
            self.g.place(x=0,y=0)
            self.s = Button(self.master, text="Save", command=self.sve)
            self.s.place(x=94,y=0)
            self.e = Button(self.master, text="Eject Drive", command=self.ejct)
            self.e.place(x=0,y=27)
            self.m = Button(self.master, text="Mount Drive", command=self.mount)
            self.m.place(x=94,y=27)
            self.title = Entry(self.master,bd=5,relief=GROOVE, bg='gray31', fg='white smoke')
            self.title.insert(0, "Document Name")
            self.title.place(x=196,y=27)
            self.scrollbar = Scrollbar(self.master)
            self.scrollbar.pack(side=RIGHT, fill=Y)
            self.t = Text(self.master, width=80, height= 30, bg='dim gray', font=("Times New Roman",14), fg="white smoke", relief=RIDGE, yscrollcommand=self.scrollbar.set)
            #self.t = Text(self.master, width=80, height= 30, bg='gray24', font=("Times New Roman",14), fg="gray76")
            self.t.insert(END, self.opnTxt)
            self.t.place(x=196,y=57)
            self.scrollbar.config(command=self.t.yview)
            self.t.focus_set()
        def sve(self):
            try:
                data = self.t.get(1.0, END)
                name = self.title.get()
                docName = os.path.expanduser("C:/Users/naper/Desktop/SimplEdit Documents/%s.txt" % name)
                fle = open(docName, "w")
                fle.write(en.encr(data))
                fle.close()
            except:
                self.befTxt = self.t.get(1.0, END)
                self.t.destroy()
                self.scrollbar.destroy()
                self.scrollbar = Scrollbar(self.master)
                self.scrollbar.pack(side=RIGHT, fill=Y)
                self.t = Text(self.master, width=80, height= 30, bg='dim gray', font=("Times New Roman",14), fg="white smoke", relief=RIDGE, yscrollcommand=self.scrollbar.set)
                #self.t = Text(self.master, width=80, height= 30, bg='gray24', font=("Times New Roman",14), fg="gray76")
                self.t.insert(END, self.opnTxt)
                self.t.place(x=196,y=57)
                self.scrollbar.config(command=self.t.yview)
                self.t.insert(END, "Please click mount drive and or insert a flash drive.")
        def get(self):
            self.flPath = tkFileDialog.askopenfilename(title="Choose A File")
            if self.flPath != '':
                docName = os.path.expanduser("%s" % self.flPath)
                fle = open(docName, "r")
                self.opnTxt = en.encr(fle.read())
                fle.close()
                try:
                    self.title.destroy()
                except:
                    pass
                self.title = Entry(self.master,bd=5,relief=GROOVE, bg='gray31', fg='white smoke')
                self.title.insert(0, self.flPath[21:self.flPath.find(".")])
                self.title.place(x=196,y=27)
                try:
                    self.t.destroy()
                    self.scrollbar.destroy()
                except:
                    pass
                self.scrollbar = Scrollbar(self.master)
                self.scrollbar.pack(side=RIGHT, fill=Y)
                self.t = Text(self.master, width=80, height= 30, bg='dim gray', font=("Times New Roman",14), fg="white smoke", relief=RIDGE, yscrollcommand=self.scrollbar.set)
                #self.t = Text(self.master, width=80, height= 30, bg='gray24', font=("Times New Roman",14), fg="gray76")
                self.t.place(x=196,y=57)
                self.scrollbar.config(command=self.t.yview)
                self.t.insert(END, self.opnTxt[:] + ' ')
            else:
                pass
        def updat(self):
            self.master.update()
            try:
                if self.passWord.get() == "Nperkins30":
                    self.create()
            except:
                pass
            try:
                self.master.bind("<Button-3>", self.autoCorrect)
            except:
                pass
        def ejct(self):
            pass#os.system("diskutil unmount SURFACEPRO4")
        def mount(self):
            '''self.t.destroy()
            self.scrollbar.destroy()
            self.scrollbar = Scrollbar(self.master)
            self.scrollbar.pack(side=RIGHT, fill=Y)
            self.t = Text(self.master, width=80, height= 30, bg='dim gray', font=("Times New Roman",14), fg="white smoke", relief=RIDGE, yscrollcommand=self.scrollbar.set)
            #self.t = Text(self.master, width=80, height= 30, bg='gray24', font=("Times New Roman",14), fg="gray76")
            self.t.insert(END, self.opnTxt)
            self.t.place(x=196,y=57)
            self.scrollbar.config(command=self.t.yview)
            self.t.insert(END, self.befTxt)
            os.system("diskutil mount SURFACEPRO4")
            self.sve()'''
            pass
        def autoCorrect(self, *args):
            correctData = self.t.get(1.0, END)
            correctData = correctData[:-1]
            try:
                dictTion = {'helo': 'hello', 'helllo': 'hello', 'paladium': 'palladium', 'paladuim': 'palladium', 'palladuim': 'palladium',
                            'cnversation': 'conversation', 'conversatuon': 'conversation', 'whell': 'well', 'ad': 'and', 'theis': 'this ',
                            'knwo': 'know', 'kno': 'know', 'eill': 'will', 'i': 'I', 'si': 'is', 'burron': 'button', 'rhytym': 'rhythm',
                            'rhythym': 'rhythm', 'lekely': 'likely', 'likeley': 'likely', 'asure': 'assure', 'militry': 'military',
                            'statment': 'statement', 'rhytm': 'rhythm', 'futuer': 'future', 'futeur': 'future', 'teh': 'the', 'mispell': 'misspell',
                            'paralell': 'parallel', 'accidentaly': 'accidentally', 'acuire': 'acquire', 'aquire': 'acquire', 'accomodate': 'accommodate',
                            'accomodation': 'accommodation', 'acheive': 'achieve', 'accross': 'across', 'agressive': 'aggressive', 'agression': 'aggression',
                            'apparantly': 'apparently', 'appearence': 'appearance', 'arguement': 'argument', 'assasination': 'assassination',
                            'basicly': 'basically', 'begining': 'beginning', 'beleive': 'believe', 'belive': 'believe', 'bizzare': 'bizarre',
                            'buisness': 'business', 'calender': 'calendar', 'carribean': 'caribbean', 'cemetary': 'cemetery', 'chauffer': 'chauffeur',
                            'collegue': 'colleague', 'comming': 'coming', 'commitee': 'committee', 'completly': 'completely', 'concious': 'conscious',
                            'doingg': 'doing', 'namee': 'name'}
                #print correctData
                for g in dictTion:
                    if correctData.find('%s ' % g) != -1:
                        correctData = correctData.replace('%s ' % g, '%s ' % dictTion[g])
                    if correctData.find(' %s' % g) != -1:
                        correctData = correctData.replace(' %s' % g, ' %s' % dictTion[g])
                    if correctData.find('%s,' % g) != -1:
                        correctData = correctData.replace('%s,' % g, '%s,' % dictTion[g])
                    if correctData.find('%s ' % g.title()) != -1:
                        correctData = correctData.replace('%s ' % g.title(), '%s ' % dictTion[g].title())
                    if correctData.find(' %s' % g.title()) != -1:
                        correctData = correctData.replace(' %s' % g.title(), ' %s' % dictTion[g].title())
                    if correctData.find('%s,' % g.title()) != -1:
                        correctData = correctData.replace('%s,' % g.title(), '%s,' % dictTion[g].title())
                #print correctData
                '''twPer = []
                onPer = []
                for m in re.finditer('. ', correctData):
                    onPer.append(m.start()+2)
                for k in re.finditer('.  ', correctData):
                    twPer.append(k.start()+3)
                for j in onPer:
                    correctData = correctData.replace(correctData[j], correctData[j].upper())
                for l in twPer:
                    correctData = correctData.replace(correctData[l], correctData[l].upper())
                correctData = upperfirst(correctData)'''
                self.t.destroy()
                self.scrollbar.destroy()
                self.scrollbar = Scrollbar(self.master)
                self.scrollbar.pack(side=RIGHT, fill=Y)
                self.t = Text(self.master, width=80, height= 30, bg='dim gray', font=("Times New Roman",14), fg="white smoke", relief=RIDGE, yscrollcommand=self.scrollbar.set)
                #self.t = Text(self.master, width=80, height= 30, bg='gray24', font=("Times New Roman",14), fg="gray76")
                self.t.insert(END, self.opnTxt)
                self.t.place(x=196,y=57)
                self.scrollbar.config(command=self.t.yview)
                self.t.insert(END, correctData[:])
            except:
                pass
else:
    print 'SecureEditor should be available for you os soon.'


root = Tk()
root['bg'] = 'gray19'
w = 1000
h = 600
ws = 1280
hs = 750
x = (ws/2) - (w/2)
y = (hs/2) - (h/2)
root.geometry('%dx%d+%d+%d' % (w, h, x, y))
root.title("SecureEditor")
root.geometry('{}x{}'.format(1000, 600))
root.attributes('-alpha', 1)
#root.resizable(0, 0)
clsEdit = editFile(root)
while True:
    try:
        clsEdit.updat()
    except:
        sys.exit()