class driver():
    def __init__(self,did,name,address,email,licenseplate,password):
        self.did = did
        self.name = name
        self.address = address
        self.email = email
        self.licenseplate = licenseplate
        self.password = password

    def getDID(self):
        return self.did
    def getNAME(self):
        return self.name
    def getADDRESS(self):
        return self.address
    def getEMAIL(self):
        return self.email
    def getLICENSEPLATE(self):
        return self.licenseplate
    def getPASSWORD(self):
        return self.password

    def setDID(self, did):
        self.did = did
    def setNAME(self,name):
        self.name = name
    def setADRESS(self,address):
        self.address = address
    def setEMAIL(self,email):
        self.email = email
    def setEMAIL(self,licenseplate):
        self.licenseplate = licenseplate
    def setPASSWORD(self, password):
        self.password = password

    def str(self):
        return ("{}, {}".format(self.did,self.name, self.address,self.email,self.licenseplate, self.password))
