__author__ = 'naperkins'
from Tkinter import *

class Choice():
    def __init__(self, master):
        root = Tk()
        self.budget = Budget(root)
        self.sandbox = Sandbox(root)
        self.master = master
        self.choiceLab = Label(self.master, text='Choose either "Sandbox Mode" which will let you experiement with different\n'
                                               ' budgets that you would like to consider but these budgets will not save\n'
                                               'or "Budget Mode" which is where you actually make a budget and it will\n'
                                               'be saved')
        self.butFrame = Frame(self.master)
        self.butFrame.pack(side=BOTTOM)
        self.testing = Button(self.butFrame, text="Sandbox Mode", command=self.sandboxMode)
        self.real = Button(self.master, text="Budget Mode", command=self.budgetMode)
        self.choiceLab.pack(side=TOP)
        self.real.pack()
        self.testing.pack()



    def sandboxMode(self):
        self.master.destroy()
        self.sandbox.preMain()
        self.sandbox.refresh()
    def budgetMode(self):
        self.master.destroy()
        self.budget.master.destroy()
        #self.budget.refresh()


    def refresh(self):
        self.master.mainloop()


class Budget():
    def __init__(self, master):
        #Eating at home: 275, Electricity: 120, Public Transportation: 62, Car Payment: 300, Phone: 100, Gas: 50, Savings: %10, Water: 100
        #Electricity, transportation, phone, cable, internet, entertainment, gas, savings
        self.master = master
        self.master.configure(background="white")
        self.master.title("budgetYou")
        self.customize = Menu(self.master)
        self.filemenu = Menu(self.customize, tearoff=0)
        self.customize.add_cascade(label="Customize", menu=self.filemenu)
        self.filemenu.add_command(label="Red", command=self.red)
        self.filemenu.add_command(label="Green", command=self.green)
        self.filemenu.add_command(label="Blue", command=self.blue)
        self.filemenu.add_command(label="Purple", command=self.purple)
        self.filemenu.add_command(label="Pink", command=self.pink)
        self.filemenu.add_command(label="White", command=self.white)
        self.filemenu.add_command(label="Black", command=self.black)
        self.color = "white"
        self.debt = False
        self.textColor = "black"
        self.salary = 0
        self.housing = 0
        self.water = 0
        self.food = 0
        self.whatTranspo = ""
        self.whichTranspo = ""
        self.transpo = 0
        self.phonePln = 0
        self.electricity = 120
        self.gas = 50
        self.monthSalary = 0
        self.savings = 0


    def preMain(self):
        self.anSalary()


    def main(self):
        self.frame = Frame(self.master)
        self.frame.pack(side=TOP)
        if self.leftSpending() < 0:
            self.debtLabel = Label(self.master, text="Your budget has been ajusted to keep you leftover money at or above zero.")
            self.debtLabel.pack(side=BOTTOM)
            self.debtLabel.configure(background=self.color)
            self.debt = True
            self.debtAccountEnter()
            if self.leftSpending() < 0:
                self.debtAccountSavings()
                if self.leftSpending() < 0:
                    self.debtAccountTranspo()
        self.savings = self.monthSalary * 0.1
        self.leftBox = Listbox(self.frame, activestyle='dotbox', height=15, width=30)
        self.leftBox.bind('<<ListboxSelect>>', self.noAct)
        self.rightBox = Listbox(self.frame, activestyle='dotbox', height=15, width=30)
        self.rightBox.bind('<<ListboxSelect>>', self.change)
        self.leftBoxItems()
        self.rightBoxItems()
        self.leftBox.pack(side=LEFT)
        self.rightBox.pack(side=RIGHT)
        self.leftBox["bg"] = self.color
        self.leftBox["fg"] = self.textColor
        self.rightBox["bg"] = self.color
        self.rightBox["fg"] = self.textColor
        self.outlookLabel = Label(self.master, text="With your current spending habits you will have $%s in your savings account in 6 months." % format(self.savings * 6, ".2f"))
        self.outlookLabel.pack()
        self.outlookLabel.configure(background=self.color)


    def noAct(self, event):
        pass


    def change(self, event):
        self.outlookLabel.destroy()
        try:
            self.debtLabel.destroy()
        except:
            pass
        widget = event.widget
        self.selection = widget.curselection()
        self.frame.destroy()
        if self.selection == (1,):
            self.SuHousing()
        if self.selection == (2,):
            self.SuWater()
        if self.selection == (3,):
            self.SuFamily()
        if self.selection == (4,):
            self.StransCar()
        if self.selection == (6,):
            self.SuPhone()
        if self.selection == (5,):
            self.SGas()
        if self.selection == (7,):
            self.SuEntertainment()
        if self.selection == (8,):
            self.SuElectricity()
        if self.selection == (9,):
            self.main()
        if self.selection == (0,):
            self.main()


    def leftBoxItems(self):
        for item in ["Left to spend:", "Housing:", "Water:", "Food:", "%s" % self.whichTranspo.capitalize(), "Gas", "Phone Plan:", "Entertainment:", "Electricity:", "Savings:"]:
            self.leftBox.insert(END, item)
    def rightBoxItems(self):
        for item in ["$%s" % format(self.leftSpending(), ".2f"), "$%s" % format(self.housing, ".2f"),
                     "$%s" % format(self.water, ".2f"), "$%s" % format(self.food, ".2f"), "$%s" % format(self.transpo, ".2f"),
                     "$%s" % format(self.gas, ".2f"), "$%s" % format(self.phonePln, ".2f"), "$%s" % format(self.enter, ".2f"),
                     "$%s" % format(self.elec, ".2f"), "$%s" % format(self.savings, ".2f")]:
            self.rightBox.insert(END, item)


    def red(self):
        self.master.configure(background='red')
        self.color = 'red'
        try:
            self.salaryLabel.configure(background=self.color)
        except:
            pass
        try:
            self.housingLabel.configure(background=self.color)
        except:
            pass
        try:
            self.waterLabel.configure(background=self.color)
        except:
            pass
        try:
            self.familyLabel.configure(background=self.color)
        except:
            pass
        try:
            self.transpoLabel.configure(background=self.color)
        except:
            pass
        try:
            self.transLabel.configure(background=self.color)
        except:
            pass
        try:
            self.phoneLabel.configure(background=self.color)
        except:
            pass
        try:
            self.enterLabel.configure(background=self.color)
        except:
            pass
        try:
            self.debtLabel.configure(background=self.color)
        except:
            pass
        try:
            self.elecLabel.configure(background=self.color)
        except:
            pass
        try:
            self.outlookLabel.configure(background=self.color)
        except:
            pass
        try:
            self.leftBox["bg"] = self.color
        except:
            pass
        try:
            self.rightBox["bg"] = self.color
        except:
            pass
    def blue(self):
        self.master.configure(background='blue')
        self.color = 'blue'
        try:
            self.salaryLabel.configure(background=self.color)
        except:
            pass
        try:
            self.housingLabel.configure(background=self.color)
        except:
            pass
        try:
            self.waterLabel.configure(background=self.color)
        except:
            pass
        try:
            self.familyLabel.configure(background=self.color)
        except:
            pass
        try:
            self.transpoLabel.configure(background=self.color)
        except:
            pass
        try:
            self.transLabel.configure(background=self.color)
        except:
            pass
        try:
            self.phoneLabel.configure(background=self.color)
        except:
            pass
        try:
            self.enterLabel.configure(background=self.color)
        except:
            pass
        try:
            self.debtLabel.configure(background=self.color)
        except:
            pass
        try:
            self.elecLabel.configure(background=self.color)
        except:
            pass
        try:
            self.outlookLabel.configure(background=self.color)
        except:
            pass
        try:
            self.leftBox["bg"] = self.color
        except:
            pass
        try:
            self.rightBox["bg"] = self.color
        except:
            pass
    def green(self):
        self.master.configure(background='green')
        self.color = 'green'
        try:
            self.salaryLabel.configure(background=self.color)
        except:
            pass
        try:
            self.housingLabel.configure(background=self.color)
        except:
            pass
        try:
            self.waterLabel.configure(background=self.color)
        except:
            pass
        try:
            self.familyLabel.configure(background=self.color)
        except:
            pass
        try:
            self.transpoLabel.configure(background=self.color)
        except:
            pass
        try:
            self.transLabel.configure(background=self.color)
        except:
            pass
        try:
            self.phoneLabel.configure(background=self.color)
        except:
            pass
        try:
            self.enterLabel.configure(background=self.color)
        except:
            pass
        try:
            self.elecLabel.configure(background=self.color)
        except:
            pass
        try:
            self.outlookLabel.configure(background=self.color)
        except:
            pass
        try:
            self.leftBox["bg"] = self.color
        except:
            pass
        try:
            self.rightBox["bg"] = self.color
        except:
            pass
        try:
            self.debtLabel.configure(background=self.color)
        except:
            pass
    def purple(self):
        self.master.configure(background='purple')
        self.color = 'purple'
        try:
            self.salaryLabel.configure(background=self.color)
        except:
            pass
        try:
            self.housingLabel.configure(background=self.color)
        except:
            pass
        try:
            self.waterLabel.configure(background=self.color)
        except:
            pass
        try:
            self.familyLabel.configure(background=self.color)
        except:
            pass
        try:
            self.transpoLabel.configure(background=self.color)
        except:
            pass
        try:
            self.transLabel.configure(background=self.color)
        except:
            pass
        try:
            self.phoneLabel.configure(background=self.color)
        except:
            pass
        try:
            self.enterLabel.configure(background=self.color)
        except:
            pass
        try:
            self.debtLabel.configure(background=self.color)
        except:
            pass
        try:
            self.elecLabel.configure(background=self.color)
        except:
            pass
        try:
            self.outlookLabel.configure(background=self.color)
        except:
            pass
        try:
            self.leftBox["bg"] = self.color
        except:
            pass
        try:
            self.rightBox["bg"] = self.color
        except:
            pass
    def pink(self):
        self.master.configure(background='pink')
        self.color = 'pink'
        try:
            self.salaryLabel.configure(background=self.color)
        except:
            pass
        try:
            self.housingLabel.configure(background=self.color)
        except:
            pass
        try:
            self.waterLabel.configure(background=self.color)
        except:
            pass
        try:
            self.familyLabel.configure(background=self.color)
        except:
            pass
        try:
            self.transpoLabel.configure(background=self.color)
        except:
            pass
        try:
            self.transLabel.configure(background=self.color)
        except:
            pass
        try:
            self.phoneLabel.configure(background=self.color)
        except:
            pass
        try:
            self.enterLabel.configure(background=self.color)
        except:
            pass
        try:
            self.debtLabel.configure(background=self.color)
        except:
            pass
        try:
            self.elecLabel.configure(background=self.color)
        except:
            pass
        try:
            self.outlookLabel.configure(background=self.color)
        except:
            pass
        try:
            self.leftBox["bg"] = self.color
        except:
            pass
        try:
            self.rightBox["bg"] = self.color
        except:
            pass
    def white(self):
        self.master.configure(background='white')
        self.color = 'white'
        try:
            self.salaryLabel.configure(background=self.color)
        except:
            pass
        try:
            self.housingLabel.configure(background=self.color)
        except:
            pass
        try:
            self.waterLabel.configure(background=self.color)
        except:
            pass
        try:
            self.familyLabel.configure(background=self.color)
        except:
            pass
        try:
            self.transpoLabel.configure(background=self.color)
        except:
            pass
        try:
            self.transLabel.configure(background=self.color)
        except:
            pass
        try:
            self.phoneLabel.configure(background=self.color)
        except:
            pass
        try:
            self.enterLabel.configure(background=self.color)
        except:
            pass
        try:
            self.debtLabel.configure(background=self.color)
        except:
            pass
        try:
            self.elecLabel.configure(background=self.color)
        except:
            pass
        try:
            self.outlookLabel.configure(background=self.color)
        except:
            pass
        try:
            self.leftBox["bg"] = self.color
        except:
            pass
        try:
            self.rightBox["bg"] = self.color
        except:
            pass
    def black(self):
        self.master.configure(background='black')
        self.color = 'black'
        try:
            self.salaryLabel.configure(background=self.color)
        except:
            pass
        try:
            self.housingLabel.configure(background=self.color)
        except:
            pass
        try:
            self.waterLabel.configure(background=self.color)
        except:
            pass
        try:
            self.familyLabel.configure(background=self.color)
        except:
            pass
        try:
            self.transpoLabel.configure(background=self.color)
        except:
            pass
        try:
            self.transLabel.configure(background=self.color)
        except:
            pass
        try:
            self.phoneLabel.configure(background=self.color)
        except:
            pass
        try:
            self.enterLabel.configure(background=self.color)
        except:
            pass
        try:
            self.debtLabel.configure(background=self.color)
        except:
            pass
        try:
            self.elecLabel.configure(background=self.color)
        except:
            pass
        try:
            self.outlookLabel.configure(background=self.color)
        except:
            pass
        try:
            self.leftBox["bg"] = self.color
        except:
            pass
        try:
            self.rightBox["bg"] = self.color
        except:
            pass


    def whiteText(self):
        self.textColor = "white"
        try:
            self.salaryLabel.configure(foreground=self.textColor)
        except:
            pass
        try:
            self.housingLabel.configure(foreground=self.textColor)
        except:
            pass
        try:
            self.waterLabel.configure(foreground=self.textColor)
        except:
            pass
        try:
            self.familyLabel.configure(foreground=self.textColor)
        except:
            pass
        try:
            self.transpoLabel.configure(foreground=self.textColor)
        except:
            pass
        try:
            self.transLabel.configure(foreground=self.textColor)
        except:
            pass
        try:
            self.phoneLabel.configure(foreground=self.textColor)
        except:
            pass
        try:
            self.enterLabel.configure(background=self.textColor)
        except:
            pass
        try:
            self.debtLabel.configure(background=self.textColor)
        except:
            pass
        try:
            self.elecLabel.configure(background=self.textColor)
        except:
            pass
        try:
            self.outlookLabel.configure(background=self.textColor)
        except:
            pass
        try:
            self.leftBox["bg"] = self.textColor
        except:
            pass
        try:
            self.rightBox["bg"] = self.textColor
        except:
            pass
    def blackText(self):
        self.textColor = "black"
        try:
            self.salaryLabel.configure(foreground=self.textColor)
        except:
            pass
        try:
            self.housingLabel.configure(foreground=self.textColor)
        except:
            pass
        try:
            self.waterLabel.configure(foreground=self.textColor)
        except:
            pass
        try:
            self.familyLabel.configure(foreground=self.textColor)
        except:
            pass
        try:
            self.transpoLabel.configure(foreground=self.textColor)
        except:
            pass
        try:
            self.transLabel.configure(foreground=self.textColor)
        except:
            pass
        try:
            self.phoneLabel.configure(foreground=self.textColor)
        except:
            pass
        try:
            self.enterLabel.configure(background=self.textColor)
        except:
            pass
        try:
            self.debtLabel.configure(background=self.textColor)
        except:
            pass
        try:
            self.elecLabel.configure(background=self.textColor)
        except:
            pass
        try:
            self.outlookLabel.configure(background=self.textColor)
        except:
            pass
        try:
            self.leftBox["bg"] = self.textColor
        except:
            pass
        try:
            self.rightBox["bg"] = self.textColor
        except:
            pass


    def toInt(self, stringFor):
        self.intString = ""
        for x in stringFor:
            try:
                self.intString += str(int(x))
            except:
                pass
        return int(self.intString)


    def anSalary(self):
        if self.color == "black":
            self.whiteText()
        else:
            self.blackText()
        self.salaryVar = StringVar()
        self.salaryLabel = Label(self.master, text="Please enter your annual salary after taxes.", fg=self.textColor)
        self.salaryLabel.pack()
        self.salaryLabel.configure(background=self.color)
        self.salaryEntry = Entry(self.master, text=self.salaryVar)
        self.salaryEntry.pack()
        self.salaryEntry.focus_set()
        self.salaryBut = Button(self.master, text="Next", command=self.anSalaryDel, justify=RIGHT)
        self.salaryBut.pack()
        self.master.bind("<Return>", self.callbackSalary)
    def anSalaryDel(self):
        self.salary = self.toInt(str(self.salaryEntry.get()))
        self.monthSalary = self.salary/12
        self.salaryLabel.destroy()
        self.salaryEntry.destroy()
        self.salaryBut.destroy()
        self.uHousing()
    def callbackSalary(self, event):
        self.salary = self.toInt(str(self.salaryEntry.get()))
        self.monthSalary = self.salary/12
        self.salaryLabel.destroy()
        self.salaryEntry.destroy()
        self.salaryBut.destroy()
        self.uHousing()


    def uHousing(self):
        if self.color == "black":
            self.whiteText()
        else:
            self.blackText()
        self.housingVar = StringVar()
        self.housingLabel = Label(self.master, text="Please enter your mortgage/rent per month.", fg=self.textColor)
        self.housingLabel.pack()
        self.housingLabel.configure(background=self.color)
        self.housingEntry = Entry(self.master, textvariable=self.housingVar)
        self.housingEntry.pack()
        self.housingEntry.focus_set()
        self.housingBut = Button(self.master, text="Next", command=self.uHousingDel, justify=RIGHT)
        self.housingBut.pack()
        self.master.bind("<Return>", self.callbackHousing)
    def uHousingDel(self):
        self.housing = self.toInt(str(self.housingEntry.get()))
        self.housingLabel.destroy()
        self.housingEntry.destroy()
        self.housingBut.destroy()
        self.uWater()
    def callbackHousing(self, event):
        self.housing = self.toInt(str(self.housingEntry.get()))
        self.housingLabel.destroy()
        self.housingEntry.destroy()
        self.housingBut.destroy()
        self.uWater()

    def SuHousing(self):
        if self.color == "black":
            self.whiteText()
        else:
            self.blackText()
        self.housingVar = StringVar()
        self.housingLabel = Label(self.master, text="Please enter your mortgage/rent per month.", fg=self.textColor)
        self.housingLabel.pack()
        self.housingLabel.configure(background=self.color)
        self.housingEntry = Entry(self.master, textvariable=self.housingVar)
        self.housingEntry.pack()
        self.housingEntry.focus_set()
        self.housingBut = Button(self.master, text="Next", command=self.SuHousingDel, justify=RIGHT)
        self.housingBut.pack()
        self.master.bind("<Return>", self.ScallbackHousing)
    def SuHousingDel(self):
        self.housing = self.toInt(str(self.housingEntry.get()))
        self.housingLabel.destroy()
        self.housingEntry.destroy()
        self.housingBut.destroy()
        self.main()
    def ScallbackHousing(self, event):
        self.housing = self.toInt(str(self.housingEntry.get()))
        self.housingLabel.destroy()
        self.housingEntry.destroy()
        self.housingBut.destroy()
        self.main()


    def uWater(self):
        if self.color == "black":
            self.whiteText()
        else:
            self.blackText()
        self.waterVar = StringVar()
        self.waterLabel = Label(self.master, text="Please enter your monthly water bill.", fg=self.textColor)
        self.waterLabel.pack()
        self.waterLabel.configure(background=self.color)
        self.waterEntry = Entry(self.master, textvariable=self.waterVar)
        self.waterEntry.pack()
        self.waterEntry.focus_set()
        self.waterBut = Button(self.master, text="Next", command=self.uWaterDel, justify=RIGHT)
        self.waterBut.pack()
        self.master.bind("<Return>", self.callbackWater)
    def uWaterDel(self):
        self.water = self.toInt(str(self.waterEntry.get()))
        self.waterLabel.destroy()
        self.waterEntry.destroy()
        self.waterBut.destroy()
        self.uFamily()
    def callbackWater(self, event):
        self.water = self.toInt(str(self.waterEntry.get()))
        self.waterLabel.destroy()
        self.waterEntry.destroy()
        self.waterBut.destroy()
        self.uFamily()

    def SuWater(self):
        if self.color == "black":
            self.whiteText()
        else:
            self.blackText()
        self.waterVar = StringVar()
        self.waterLabel = Label(self.master, text="Please enter your monthly water bill.", fg=self.textColor)
        self.waterLabel.pack()
        self.waterLabel.configure(background=self.color)
        self.waterEntry = Entry(self.master, textvariable=self.waterVar)
        self.waterEntry.pack()
        self.waterEntry.focus_set()
        self.waterBut = Button(self.master, text="Next", command=self.SuWaterDel, justify=RIGHT)
        self.waterBut.pack()
        self.master.bind("<Return>", self.ScallbackWater)
    def SuWaterDel(self):
        self.water = self.toInt(str(self.waterEntry.get()))
        self.waterLabel.destroy()
        self.waterEntry.destroy()
        self.waterBut.destroy()
        self.main()
    def ScallbackWater(self, event):
        self.water = self.toInt(str(self.waterEntry.get()))
        self.waterLabel.destroy()
        self.waterEntry.destroy()
        self.waterBut.destroy()
        self.main()


    def uFamily(self):
        if self.color == "black":
            self.whiteText()
        else:
            self.blackText()
        self.foodVar = StringVar()
        self.familyLabel = Label(self.master, text="Please enter the size of your family.", fg=self.textColor)
        self.familyLabel.pack()
        self.familyLabel.configure(background=self.color)
        self.familyEntry = Entry(self.master, textvariable=self.foodVar)
        self.familyEntry.pack()
        self.familyEntry.focus_set()
        self.familyBut = Button(self.master, text="Next", command=self.uFamilyDel, justify=RIGHT)
        self.familyBut.pack()
        self.master.bind("<Return>", self.callbackFam)
    def uFamilyDel(self):
        self.food = self.toInt(str(self.familyEntry.get())) * 275
        self.familyLabel.destroy()
        self.familyEntry.destroy()
        self.familyBut.destroy()
        self.uTranspo()
        self.trans()
    def callbackFam(self, event):
        self.food = self.toInt(str(self.familyEntry.get())) * 275
        self.familyLabel.destroy()
        self.familyEntry.destroy()
        self.familyBut.destroy()
        self.uTranspo()
        self.trans()

    def SuFamily(self):
        if self.color == "black":
            self.whiteText()
        else:
            self.blackText()
        self.foodVar = StringVar()
        self.familyLabel = Label(self.master, text="Please enter how much you pay for food in your family per month.", fg=self.textColor)
        self.familyLabel.pack()
        self.familyLabel.configure(background=self.color)
        self.familyEntry = Entry(self.master, textvariable=self.foodVar)
        self.familyEntry.pack()
        self.familyEntry.focus_set()
        self.familyBut = Button(self.master, text="Next", command=self.SuFamilyDel, justify=RIGHT)
        self.familyBut.pack()
        self.master.bind("<Return>", self.ScallbackFam)
    def SuFamilyDel(self):
        self.food = self.toInt(str(self.familyEntry.get()))
        self.familyLabel.destroy()
        self.familyEntry.destroy()
        self.familyBut.destroy()
        self.main()
    def ScallbackFam(self, event):
        self.food = self.toInt(str(self.familyEntry.get()))
        self.familyLabel.destroy()
        self.familyEntry.destroy()
        self.familyBut.destroy()
        self.main()


    def uTranspo(self):
        if self.color == "black":
            self.whiteText()
        else:
            self.blackText()
        self.whatTranspoVar = StringVar()
        self.transpoLabel = Label(self.master, text="Do you take public transportation\n or do you have your own car?", fg=self.textColor)
        self.transpoLabel.pack()
        self.transpoLabel.configure(background=self.color)
        self.transpoLabel.configure(background=self.color)
        self.transpoEntry = Entry(self.master, textvariable=self.whatTranspoVar)
        self.transpoEntry.pack()
        self.transpoEntry.focus_set()
        self.transpoBut = Button(self.master, text="Next", command=self.uTranspoDel, justify=RIGHT)
        self.transpoBut.pack()
        self.master.bind("<Return>", self.callbackTrans)
    def uTranspoDel(self):
        self.whatTranspo = str(self.transpoEntry.get()).lower()
        self.transpoLabel.destroy()
        self.transpoEntry.destroy()
        self.transpoBut.destroy()
        self.trans()
    def callbackTrans(self, event):
        self.whatTranspo = str(self.transpoEntry.get()).lower()
        self.transpoLabel.destroy()
        self.transpoEntry.destroy()
        self.transpoBut.destroy()
        self.trans()


    def trans(self):
        try:
            if self.whatTranspo.find("not") != -1:
                if self.whatTranspo.find("pub") and self.whatTranspo.find("transpo") != -1:
                    self.transCar()
                if self.whatTranspo.find("car") or self.whatTranspo.find("own") != -1:
                    self.transpo = 62
                    self.whichTranspo = "public transportation"
                    self.uPhone()
            if self.whatTranspo.find("not") or self.whatTranspo.find("don") == -1:
                if self.whatTranspo.find("pub") != -1:
                    self.transpo = 62
                    self.whichTranspo = "public transportation"
                    self.uPhone()
                if self.whatTranspo.find("car") != -1:
                    self.transCar()
        except:
            pass


    def transCar(self):
        if self.color == "black":
            self.whiteText()
        else:
            self.blackText()
        self.transpo = StringVar()
        self.transLabel = Label(self.master, text="Please enter your car payment per month", fg=self.textColor)
        self.transLabel.pack()
        self.transLabel.configure(background=self.color)
        self.transEntry = Entry(self.master, textvariable=self.transpo)
        self.transEntry.pack()
        self.transEntry.focus_set()
        self.transBut = Button(self.master, text="Next", command=self.transCarDel)
        self.transBut.pack()
        self.master.bind("<Return>", self.callbackTransCar)
    def transCarDel(self):
        self.transpo = self.toInt(str(self.transEntry.get()))
        self.transLabel.destroy()
        self.transEntry.destroy()
        self.transBut.destroy()
        self.whichTranspo = "car payments"
        self.uPhone()
    def callbackTransCar(self, event):
        self.transpo = self.toInt(str(self.transEntry.get()))
        self.transLabel.destroy()
        self.transEntry.destroy()
        self.transBut.destroy()
        self.whichTranspo = "car payments"
        self.uPhone()

    def StransCar(self):
        if self.color == "black":
            self.whiteText()
        else:
            self.blackText()
        self.transpo = StringVar()
        self.transLabel = Label(self.master, text="Please enter your transportations payment per month", fg=self.textColor)
        self.transLabel.pack()
        self.transLabel.configure(background=self.color)
        self.transEntry = Entry(self.master, textvariable=self.transpo)
        self.transEntry.pack()
        self.transEntry.focus_set()
        self.transBut = Button(self.master, text="Next", command=self.StransCarDel)
        self.transBut.pack()
        self.master.bind("<Return>", self.ScallbackTransCar)
    def StransCarDel(self):
        self.transpo = self.toInt(str(self.transEntry.get()))
        self.transLabel.destroy()
        self.transEntry.destroy()
        self.transBut.destroy()
        self.main()
    def ScallbackTransCar(self, event):
        self.transpo = self.toInt(str(self.transEntry.get()))
        self.transLabel.destroy()
        self.transEntry.destroy()
        self.transBut.destroy()
        self.main()


    def uPhone(self):
        if self.color == "black":
            self.whiteText()
        else:
            self.blackText()
        self.phonePlnVar = StringVar()
        self.phoneLabel = Label(self.master, text="How much do you/your family pay\n monthly for your phone plan(s)?", fg=self.textColor)
        self.phoneLabel.pack()
        self.phoneLabel.configure(background=self.color)
        self.phoneEntry = Entry(self.master, textvariable=self.phonePlnVar)
        self.phoneEntry.pack()
        self.phoneEntry.focus_set()
        self.phoneBut = Button(self.master, text="Next", command=self.SuPhoneDel, justify=RIGHT)
        self.phoneBut.pack()
        self.master.bind("<Return>", self.callbackPhone)
    def uPhoneDel(self):
        self.phonePln = self.toInt(str(self.phoneEntry.get()))
        self.phoneLabel.destroy()
        self.phoneEntry.destroy()
        self.phoneBut.destroy()
        self.uEntertainment()
    def callbackPhone(self, event):
        self.phonePln = self.toInt(str(self.phoneEntry.get()))
        self.phoneLabel.destroy()
        self.phoneEntry.destroy()
        self.phoneBut.destroy()
        self.uEntertainment()

    def SuPhone(self):
        if self.color == "black":
            self.whiteText()
        else:
            self.blackText()
        self.phonePlnVar = StringVar()
        self.phoneLabel = Label(self.master, text="How much do you/your family pay\n monthly for your phone plan(s)?", fg=self.textColor)
        self.phoneLabel.pack()
        self.phoneLabel.configure(background=self.color)
        self.phoneEntry = Entry(self.master, textvariable=self.phonePlnVar)
        self.phoneEntry.pack()
        self.phoneEntry.focus_set()
        self.phoneBut = Button(self.master, text="Next", command=self.SuPhoneDel, justify=RIGHT)
        self.phoneBut.pack()
        self.master.bind("<Return>", self.ScallbackPhone)
    def SuPhoneDel(self):
        self.phonePln = self.toInt(str(self.phoneEntry.get()))
        self.phoneLabel.destroy()
        self.phoneEntry.destroy()
        self.phoneBut.destroy()
        self.main()
    def ScallbackPhone(self, event):
        self.phonePln = self.toInt(str(self.phoneEntry.get()))
        self.phoneLabel.destroy()
        self.phoneEntry.destroy()
        self.phoneBut.destroy()
        self.main()


    def SGas(self):
        if self.color == "black":
            self.whiteText()
        else:
            self.blackText()
        self.gasVar = StringVar()
        self.gasLabel = Label(self.master, text="How much do you pay for gasoline monthly?", fg=self.textColor)
        self.gasLabel.pack()
        self.gasLabel.configure(background=self.color)
        self.gasEntry = Entry(self.master, textvariable=self.phonePlnVar)
        self.gasEntry.pack()
        self.gasEntry.focus_set()
        self.gasBut = Button(self.master, text="Next", command=self.SuGas, justify=RIGHT)
        self.gasBut.pack()
        self.master.bind("<Return>", self.ScallbackGas)
    def SuGas(self):
        self.gas = self.toInt(str(self.gasEntry.get()))
        self.gasLabel.destroy()
        self.gasEntry.destroy()
        self.gasBut.destroy()
        self.main()
    def ScallbackGas(self, event):
        self.gas = self.toInt(str(self.gasEntry.get()))
        self.gasLabel.destroy()
        self.gasEntry.destroy()
        self.gasBut.destroy()
        self.main()


    def uEntertainment(self):
        if self.color == "black":
            self.whiteText()
        else:
            self.blackText()
        self.enterVar = StringVar()
        self.enterLabel = Label(self.master, text="How much do you pay for entertainment per month?", fg=self.textColor)
        self.enterLabel.pack()
        self.enterLabel.configure(background=self.color)
        self.enterEntry = Entry(self.master, textvariable=self.waterVar)
        self.enterEntry.pack()
        self.enterEntry.focus_set()
        self.enterBut = Button(self.master, text="Next", command=self.uEntertainmentDel, justify=RIGHT)
        self.enterBut.pack()
        self.master.bind("<Return>", self.callbackEntertainment)
    def uEntertainmentDel(self):
        self.enter = self.toInt(str(self.enterEntry.get()))
        self.enterLabel.destroy()
        self.enterEntry.destroy()
        self.enterBut.destroy()
        self.uElectricity()
    def callbackEntertainment(self, event):
        self.enter = self.toInt(str(self.enterEntry.get()))
        self.enterLabel.destroy()
        self.enterEntry.destroy()
        self.enterBut.destroy()
        self.uElectricity()

    def SuEntertainment(self):
        if self.color == "black":
            self.whiteText()
        else:
            self.blackText()
        self.enterVar = StringVar()
        self.enterLabel = Label(self.master, text="How much do you pay for entertainment per month?", fg=self.textColor)
        self.enterLabel.pack()
        self.enterLabel.configure(background=self.color)
        self.enterEntry = Entry(self.master, textvariable=self.waterVar)
        self.enterEntry.pack()
        self.enterEntry.focus_set()
        self.enterBut = Button(self.master, text="Next", command=self.SuEntertainmentDel, justify=RIGHT)
        self.enterBut.pack()
        self.master.bind("<Return>", self.ScallbackEntertainment)
    def SuEntertainmentDel(self):
        self.enter = self.toInt(str(self.enterEntry.get()))
        self.enterLabel.destroy()
        self.enterEntry.destroy()
        self.enterBut.destroy()
        self.main()
    def ScallbackEntertainment(self, event):
        self.enter = self.toInt(str(self.enterEntry.get()))
        self.enterLabel.destroy()
        self.enterEntry.destroy()
        self.enterBut.destroy()
        self.main()


    def uElectricity(self):
        if self.color == "black":
            self.whiteText()
        else:
            self.blackText()
        self.elecVar = StringVar()
        self.elecLabel = Label(self.master, text="How much do you pay for electricity monthly?", fg=self.textColor)
        self.elecLabel.pack()
        self.elecLabel.configure(background=self.color)
        self.elecEntry = Entry(self.master, textvariable=self.waterVar)
        self.elecEntry.pack()
        self.elecEntry.focus_set()
        self.elecBut = Button(self.master, text="Next", command=self.uElectricityDel, justify=RIGHT)
        self.elecBut.pack()
        self.master.bind("<Return>", self.callbackElectricity)
    def uElectricityDel(self):
        self.elec = self.toInt(str(self.elecEntry.get()))
        self.elecLabel.destroy()
        self.elecEntry.destroy()
        self.elecBut.destroy()
        self.main()
    def callbackElectricity(self, event):
        self.elec = self.toInt(str(self.elecEntry.get()))
        self.elecLabel.destroy()
        self.elecEntry.destroy()
        self.elecBut.destroy()
        self.main()

    def SuElectricity(self):
        if self.color == "black":
            self.whiteText()
        else:
            self.blackText()
        self.elecVar = StringVar()
        self.elecLabel = Label(self.master, text="How much do you pay for electricity monthly?", fg=self.textColor)
        self.elecLabel.pack()
        self.elecLabel.configure(background=self.color)
        self.elecEntry = Entry(self.master, textvariable=self.waterVar)
        self.elecEntry.pack()
        self.elecEntry.focus_set()
        self.elecBut = Button(self.master, text="Next", command=self.SuElectricityDel, justify=RIGHT)
        self.elecBut.pack()
        self.master.bind("<Return>", self.ScallbackElectricity)
    def SuElectricityDel(self):
        self.elec = self.toInt(str(self.elecEntry.get()))
        self.elecLabel.destroy()
        self.elecEntry.destroy()
        self.elecBut.destroy()
        self.main()
    def ScallbackElectricity(self, event):
        self.elec = self.toInt(str(self.elecEntry.get()))
        self.elecLabel.destroy()
        self.elecEntry.destroy()
        self.elecBut.destroy()
        self.main()


    def debtAccountEnter(self):
        if self.enter > 50:
            self.enter = 30
    def debtAccountSavings(self):
        self.savings = self.monthSalary * 0.05
    def debtAccountTranspo(self):
        self.transpo = 62
        self.whichTranspo = "public transportation"


    def leftSpending(self):
        self.left = self.monthSalary - (self.housing + self.water + self.food + self.transpo + self.electricity
                                        + self.gas + self.savings + self.phonePln + self.enter + self.elec)
        return self.left


    def refresh(self):
        self.master.config(menu=self.customize)
        self.master.mainloop()


class Sandbox():
    def __init__(self, master):
        self.master = master


    def preMain(self):
        pass


    def refresh(self):
        self.master.mainloop()


root = Tk()
budget = Budget(root)
budget.preMain()
budget.refresh()