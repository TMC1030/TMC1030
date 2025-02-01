class SmartPlug:
    def __init__(self,initialConsumptionRate):
        self.switchedOn = False
        self.setConsumptionRate(initialConsumptionRate)

    def toggleSwitch(self):
        self.switchedOn = not self.switchedOn

    def getSwitchedOn(self):
        return self.switchedOn

    def getConsumptionRate(self):
        return self.consumptionRate

    def setConsumptionRate(self,newConsumptionRate):
        if 0<= newConsumptionRate <= 150:
            self.consumptionRate = newConsumptionRate
        else:
            print("Invalid consumption rate. Please provide a value between 0 & 150")

    def __str__(self):
        return f"Status: {self.switchedOn}, Consumption Rate: {self.consumptionRate}"

class SmartAirFryer:
    def __init__(self):
        self.switchedOn = False
        self.option = "Healthy"

    def toggleSwitch(self):
        self.switchedOn = not self.switchedOn

    def getSwitchedOn(self):
        return self.switchedOn

    def getOption(self):
        return self.option

    def setOption(self,newOption):
        options = ["Healthy","Defrost","Crispy"]
        if newOption in options:
            self.option = newOption
        else:
            print("Invalid option. Please choose from: ",options)

    def __str__(self):
        statusDisplay = "On" if self.switchedOn else "Off"
        return f"SmartAirFryer: {statusDisplay}, Option: {self.option}"

class SmartHome:
    def __init__(self):
        self.devices = []

    def getDevices(self):
        return self.devices

    def getDeviceAt(self,index):
        return self.devices[index]

    def addDevice(self,device):
        self.devices.append(device)

    def removeDeviceAt(self,index):
        del self.devices[index]

    def toggleSwitch(self,index):
        self.devices[index].toggleSwitch()

    def turnOnAll(self):
        for device in self.devices:
            if not device.getSwitchedOn():
                device.toggleSwitch()

    def turnOffAll(self):
        for device in self.devices:
            if device.getSwitchedOn():
                device.toggleSwitch()

    def __str__(self):
        output = f"You have {len(self.devices)} devices \n"
        for index in range(len(self.devices)):
            output += f"Device{index}: {self.devices[index]} \n"
        return output

def testSmartPlug():
    plug = SmartPlug(45)
    plug.toggleSwitch()
    print("Status:",plug.getSwitchedOn())
    print("Consumption Rate:",plug.getConsumptionRate())
    plug.setConsumptionRate(75)
    print("New Consumption Rate:",plug.getConsumptionRate())
    print(plug)

#testSmartPlug()

def testDevice():
    device = SmartAirFryer()
    device.toggleSwitch()
    print("Switch status: ", device.getSwitchedOn())
    print("Current option: ", device.getOption())
    device.setOption("Crispy")
    print("Updated option: ", device.getOption())
    print(device)

#testDevice()

def testSmartHome():
    smartHomeTest = SmartHome()
    plug1 = SmartPlug(45)
    plug2 = SmartPlug(45)
    airFryer = SmartAirFryer()
    smartHomeTest.addDevice(plug1)
    smartHomeTest.addDevice(plug2)
    smartHomeTest.addDevice(airFryer)
    print(smartHomeTest)
    plug1.toggleSwitch()
    plug1.setConsumptionRate(150)
    plug2.setConsumptionRate(25)
    airFryer.toggleSwitch()
    smartHomeTest.toggleSwitch(0)
    print(smartHomeTest)
    smartHomeTest.turnOnAll()
    print(smartHomeTest)
    smartHomeTest.removeDeviceAt(0)
    print(smartHomeTest)

testSmartHome()
