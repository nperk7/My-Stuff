__author__ = 'naperkins'
#This is the shortMemory subsystem which is meant to give memories to the Memory susbsytem and retain short term info

class superShort():
    def __init__(self):
        self.memory = ""
    def expire(self, memList):
        shortFile = open("shortMemory.txt", "r+")
        line = shortFile.readlines()
        shortFile.seek(0)
        for thing in line:
            if "%s\n" % thing != "%s" % (memList):
                shortFile.write(thing)
        shortFile.truncate()
        shortFile.close()
        self.switchLong(memList)
    def add(self, memList):
        shortFile = open("shortMemory.txt", "a")
        passInfo = "%s\n" % memList
        shortFile.write(passInfo)
        shortFile.truncate()
        shortFile.close()
    def switchLong(self, memList):
        longFile = open("longMemory.txt", "a")
        passInfo = "%s\n" % memList
        longFile.write(passInfo)
        longFile.truncate()
        longFile.close()
