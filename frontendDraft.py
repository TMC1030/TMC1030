from backend import *
from tkinter import *

class SmartHomeSystem:

    def __init__(self,smartHome):
        self.smartHome = smartHome

        self.win = Tk()
        self.win.title("Smart Home System")

        self.mainFrame = Frame(self.win)
        self.mainFrame.grid(
            row=0,
            column=0,
            padx=10,  # Optional padding to make the GUI look nicer
            pady=10,
        )

        self.addNewWidgets = StringVar()
        self.homeWidgets = []

    def deleteAllHomeWidgets(self):
        for widget in self.homeWidgets:
            widget.destroy()
        self.homeWidgets = []

    def run(self):
        self.createWidgets()
        self.win.mainloop()

    def createWidgets(self):
        self.deleteAllHomeWidgets()

        lblSAF = StringVar()
        lblSAF.set("Air Fryer:Off, Cooking Mode:Healthy")
        lP = StringVar()
        lP.set("Plug:Off, Consumption Rate:150")
        lblSAF1 = StringVar()
        lblSAF1.set("Air Fryer:Off, Cooking Mode:Defrost")
        lP1 = StringVar()
        lP1.set("Plug:Off, Consumption Rate:45")
        lblSAF2 = StringVar()
        lblSAF2.set("Air Fryer:Off, Cooking Mode:Crispy")

        labelSmartAirFryer = Label(self.mainFrame, textvariable=lblSAF)
        labelSmartAirFryer.grid(column=0, row=2)
        self.homeWidgets.append(labelSmartAirFryer)

        labelPlug = Label(self.mainFrame, textvariable=lP)
        labelPlug.grid(column=0, row=3)
        self.homeWidgets.append(labelPlug)

        labelSmartAirFryer1 = Label(self.mainFrame, textvariable=lblSAF1)
        labelSmartAirFryer1.grid(column=0, row=4)
        self.homeWidgets.append(labelSmartAirFryer1)

        labelPlug1 = Label(self.mainFrame, textvariable=lP1)
        labelPlug1.grid(column=0, row=5)
        self.homeWidgets.append(labelPlug1)

        labelSmartAirFryer2 = Label(self.mainFrame, textvariable=lblSAF2)
        labelSmartAirFryer2.grid(column=0, row=6)
        self.homeWidgets.append(labelSmartAirFryer2)

        btnDelete =Button(self.mainFrame, text="Delete",command=lambda index=0:self.removeDevice(index,labelSmartAirFryer,btnDelete,btnToggle,btnEdit))
        btnDelete.grid(column=3, row=2)
        self.homeWidgets.append(btnDelete)

        btnDelete = Button(self.mainFrame, text="Delete",command=lambda index=0:self.removeDevice(index,labelPlug,btnDelete,btnToggle,btnEdit))
        btnDelete.grid(column=3, row=3)
        self.homeWidgets.append(btnDelete)

        btnDelete = Button(self.mainFrame, text="Delete",command=lambda index=0:self.removeDevice(index,labelSmartAirFryer1,btnDelete,btnToggle,btnEdit))
        btnDelete.grid(column=3, row=4)
        self.homeWidgets.append(btnDelete)

        btnDelete = Button(self.mainFrame, text="Delete",command=lambda index=0:self.removeDevice(index,labelPlug1,btnDelete,btnToggle,btnEdit))
        btnDelete.grid(column=3, row=5)
        self.homeWidgets.append(btnDelete)

        btnDelete = Button(self.mainFrame, text="Delete",command=lambda index=0:self.removeDevice(index,labelSmartAirFryer2,btnDelete,btnToggle,btnEdit))
        btnDelete.grid(column=3, row=6)
        self.homeWidgets.append(btnDelete)

        btnToggle = Button(self.mainFrame, text="Toggle",command=lambda:self.toggle(2,lblSAF))
        btnToggle.grid(column=1, row=2)
        self.homeWidgets.append(btnToggle)

        btnToggle = Button(self.mainFrame, text="Toggle",command=lambda:self.toggle(0,lP))
        btnToggle.grid(column=1, row=3)
        self.homeWidgets.append(btnToggle)

        btnToggle = Button(self.mainFrame, text="Toggle",command=lambda:self.toggle(3,lblSAF1))
        btnToggle.grid(column=1, row=4)
        self.homeWidgets.append(btnToggle)

        btnToggle = Button(self.mainFrame, text="Toggle",command=lambda:self.toggle(1,lP1))
        btnToggle.grid(column=1, row=5)
        self.homeWidgets.append(btnToggle)

        btnToggle = Button(self.mainFrame, text="Toggle",command=lambda:self.toggle(4,lblSAF2))
        btnToggle.grid(column=1, row=6)
        self.homeWidgets.append(btnToggle)

        btnEdit = Button(self.mainFrame, text="Edit")
        btnEdit.grid(column=2, row=2)
        self.homeWidgets.append(btnEdit)

        btnEdit = Button(self.mainFrame, text="Edit")
        btnEdit.grid(column=2, row=3)
        self.homeWidgets.append(btnEdit)

        btnEdit = Button(self.mainFrame, text="Edit")
        btnEdit.grid(column=2, row=4)
        self.homeWidgets.append(btnEdit)

        btnEdit = Button(self.mainFrame, text="Edit")
        btnEdit.grid(column=2, row=5)
        self.homeWidgets.append(btnEdit)

        btnEdit = Button(self.mainFrame, text="Edit")
        btnEdit.grid(column=2, row=6)
        self.homeWidgets.append(btnEdit)

        turnOnAll = Button(self.mainFrame, text="Turn on all", command=lambda: self.turnOnAll(lblSAF,lP,lblSAF1,lP1,lblSAF2))
        turnOnAll.grid(column=0, row=0)
        self.homeWidgets.append(turnOnAll)

        turnOffAll = Button(self.mainFrame, text="Turn off all", command=lambda: self.turnOffAll(lblSAF,lP,lblSAF1,lP1,lblSAF2))
        turnOffAll.grid(column=1, row=0)
        self.homeWidgets.append(turnOffAll)

        addButton = Button(self.mainFrame, text="Add")
        addButton.grid(column=0, row=7)
        self.homeWidgets.append(addButton)

        labelSmartAirFryer = Label(self.mainFrame, textvariable=lblSAF)
        labelSmartAirFryer.grid(column=0, row=2)
        self.homeWidgets.append(labelSmartAirFryer)

        labelPlug = Label(self.mainFrame, textvariable=lP)
        labelPlug.grid(column=0,row=3)
        self.homeWidgets.append(labelPlug)

        labelSmartAirFryer = Label(self.mainFrame, textvariable=lblSAF1)
        labelSmartAirFryer.grid(column=0, row=4)
        self.homeWidgets.append(labelSmartAirFryer)

        labelPlug = Label(self.mainFrame, textvariable=lP1)
        labelPlug.grid(column=0, row=5)
        self.homeWidgets.append(labelPlug)

        labelSmartAirFryer = Label(self.mainFrame, textvariable=lblSAF2)
        labelSmartAirFryer.grid(column=0, row=6)
        self.homeWidgets.append(labelSmartAirFryer)

    def turnOnAll(self, lblSAF,lP,lblSAF1,lp1,lblSAF2):
        self.smartHome.turnOnAll()

        print(self.smartHome)

        lblSAF.set("Air Fryer:On, Cooking Mode:Healthy")
        lP.set("Plug:On, Consumption Rate:150")
        lblSAF1.set("Air Fryer:On, Cooking Mode:Defrost")
        lp1.set("Plug:On, Consumption Rate:45")
        lblSAF2.set("Air Fryer:On, Cooking Mode:Crispy")

    def turnOffAll(self, lblSAF,lP,lblSAF1,lp1,lblSAF2):
        self.smartHome.turnOffAll()

        print(self.smartHome)

        lblSAF.set("Air Fryer:Off, Cooking Mode:Healthy")
        lP.set("Plug:Off, Consumption Rate:150")
        lblSAF1.set("Air Fryer:Off, Cooking Mode:Defrost")
        lp1.set("Plug:Off, Consumption Rate:45")
        lblSAF2.set("Air Fryer:Off, Cooking Mode:Crispy")

    def toggle(self,index,label):
       device = self.smartHome.getDeviceAt(index)
       device.toggleSwitch()

       if isinstance(device,SmartPlug):
           status = "On" if device.switchedOn else "Off"
           name = "Plug"
           option = "Consumption Rate"
           optionValue = device.getConsumptionRate()
           label.set(f"{name}:{status},{option}:{optionValue}")

       elif isinstance(device,SmartAirFryer):
           status = "On" if device.switchedOn else "Off"
           name = "Air Fryer"
           option = "Cooking Mode"
           optionValue = device.getOption()
           label.set(f"{name}:{status}, {option}:{optionValue}")

    def removeDevice(self,index,label,btnDelete,btnToggle,btnEdit):
       label.destroy()
       btnDelete.destroy()
       btnToggle.destroy()
       btnEdit.destroy()
       self.smartHome.removeDeviceAt(index)
       del self.homeWidgets[index]

    def addNewWidgets(self):
        newWidget = self.addNewWidgets.get()
        self.smartHome.addDevice()


def main():
    smartHome = SmartHome()
    smartPlugOne = SmartPlug(150)
    smartPlugTwo = SmartPlug(45)
    smartAirFryer = SmartAirFryer()
    smartAirFryer1 = SmartAirFryer()
    smartAirFryer2 = SmartAirFryer()

    smartAirFryer.setOption("Healthy")
    smartAirFryer1.setOption("Defrost")
    smartAirFryer2.setOption("Crispy")

    smartHome.addDevice(smartPlugOne)
    smartHome.addDevice(smartPlugTwo)
    smartHome.addDevice(smartAirFryer)
    smartHome.addDevice(smartAirFryer1)
    smartHome.addDevice(smartAirFryer2)

    smartHomeSystem = SmartHomeSystem(smartHome)

    smartHomeSystem.run()

main()