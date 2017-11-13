__author__ = 'naperkins'
#This is the the memory subsystem which is meant to keep all long term memories
from shortMemory import *

def createMemory():
    memList = []
    memory = ""
    longevity = None
    triggers = []
    triggerType = []
    initialImpact = None
    initialTime = None
    longImpact = None
    shortChoice(memList)

def shortChoice(memList):
    if memList[1] <= 14:
        superShort.add(superShort, memList)
