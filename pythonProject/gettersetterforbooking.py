class makebooking():
    def __init__(self,mid,pickupaddress,pickuptime,dropoffaddress,status):
        self.mid = mid
        self.pickupaddress = pickupaddress
        self.pickuptime = pickuptime
        self.dropoffaddress = dropoffaddress
        self.status = status

    def getMID(self):
        return self.mid
    def getPICKUPADDRESS(self):
        return self.pickupaddress
    def getPICKUPTME(self):
        return self.pickuptime
    def getDROPOFFADDRESS(self):
        return self.dropoffaddress
    def getSTATUS(self):
        return self.status


    def setMID(self,mid):
        self.mid = mid
    def setPICKUPADDRESS(self,pickupaddress):
        self.pickupaddress = pickupaddress
    def setPICKUPTIME(self,pickuptime):
        self.pickuptime = pickuptime
    def setDROPOFFADDRESS(self,dropoffaddress):
        self.dropoffaddress = dropoffaddress
    def setSTATUS(self,status):
        self.status = status


    def str(self):
        return ("{}, {}".format(self.mid,self.pickupaddress, self.pickuptime,self.dropoffaddress,self.status))
