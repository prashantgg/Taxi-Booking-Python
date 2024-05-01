class admin():
    def __init__(self,email,password):
        self.email = email
        self.password = password


    def getEMAIL(self):
        return self.email
    def getPASSWORD(self):
        return self.password

    def setEMAIL(self,email):
        self.email = email
    def setPASSWORD(self, password):
        self.password = password

    def str(self):
        return ("{}, {}".format(self.email, self.password))
