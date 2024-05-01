class customer1():
    def __init__(self,cid,name,address,email,password,mobileno,creditcard):
        self.cid = cid
        self.name = name
        self.address = address
        self.email = email
        self.password = password
        self.mobileno = mobileno
        self.creditcard = creditcard

    def getCID(self):
        return self.cid
    def getNAME(self):
        return self.name
    def getADDRESS(self):
        return self.address
    def getEMAIL(self):
        return self.email
    def getPASSWORD(self):
        return self.password
    def getMOBILENO(self):
        return self.mobileno
    def getCREDITCARD(self):
        return self.creditcard


    def setCID(self, cid):
        self.cid = cid
    def setNAME(self,name):
        self.name = name
    def setADRESS(self,address):
        self.address = address
    def setEMAIL(self,email):
        self.email = email
    def setPASSWORD(self, password):
        self.password = password
    def setMOBILENO(self, mobileno):
            self.mobileno = mobileno
    def setCREDITCARD(self, creditcard):
            self.creditcard = creditcard

    def str(self):
        return ("{}, {}".format(self.cid,self.name, self.address,self.email, self.password,self.mobileno,self.creditcard))
