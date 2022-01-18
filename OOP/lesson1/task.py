class InsurancePolicy():

    nextPolicyNumber = 1

    def __init__(self, insuredName) -> None:
        self.insuredName = [insuredName]
        self.policyNumber = InsurancePolicy.nextPolicyNumber
        InsurancePolicy.nextPolicyNumber += 1
    
    def __str__(self) -> str:
        return f'<Insurance Policy {self.policyNumber}: {self.insuredName[-1]}>'
    
    def setInsuredName(self, insuredName):
        self.insuredName.append(insuredName)

    def getInsuredName(self):
        return self.insuredName[-1]

class ContentsPolicy(InsurancePolicy):
    def __init__(self, insuredName, address, jewelleryExcess) -> None:
        super().__init__(insuredName)
        self.address = address
        self.jewelleryExcess = jewelleryExcess
    
    def __str__(self) -> str:
        return f'<Contents Policy {self.policyNumber}: {self.insuredName[-1]}, {self.address}, {self.jewelleryExcess}>'
    
    def getAddress(self):
        return self.address
    
    def setJewelleryExcess(self, amount):
        self.jewelleryExcess = amount
    
    def getJewelleryExcess(self):
        return self.jewelleryExcess

class MotorPolicy(InsurancePolicy):
    def __init__(self, insuredName, registration, make) -> None:
        super().__init__(insuredName)
        self.registration = registration
        self.make = make
    
    def __str__(self) -> str:
        return f'<Motor Policy {self.policyNumber}: {self.insuredName[-1]}, {self.registration}, {self.make}>'
    
    def getRegistration(self):
        return self.registration
    
    def getMake(self):
        return self.make

