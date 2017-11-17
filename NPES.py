__author__ = 'naperkins'
import random

createBool = False
primeFile = None
yourName = None
yourUser = None
yourPass = None
yourNameNum = None
yourUserNum = None
yourPassNum = None
passList = []
end = None

def getFactors(num):
    factors = ''
    num = int(num)
    for a in range(num):
        a += 1
        if int(str(num/float(a))[str(num/float(a)).find('.')+1:]) == 0:
            factors += '%s ' % str(a)
    return factors
def isPrime(num):
    if getFactors(num) == '1 %s ' % num:
        return True
    else:
        return False
try:
   with open("passFile.txt", 'r') as passFile:
    for i, x in enumerate(passFile):
        if 0 <= i <= 6:
            passList.append(x[:-1])
        elif i > 6:
            break
    nameIn = raw_input("Please enter your screename: ")
    userIn = raw_input("Please enter your username: ")
    passIn = raw_input("Please enter your password: ")
    if nameIn == passList[0]:
        pass
    if userIn == passList[2]:
        pass
    if passIn == passList[4]:
        pass
    else:
        print "One or more of the fields you entered were incorrect."
        end = True
    if (float(passList[1]) * float(passList[3]) * float(passList[5])) == float(passList[6]) and not end:
        print "Congratulation you have gained access!"
        end = True
except:
    if not end:
        try:
            primeFile = open("primeFile.txt", "r")
            createBool = True
        except:
            primeFile = open("primeFile.txt", "w")
        primeFile.close()

        if not createBool:
            for x in range(10000):
                if isPrime(x):
                    primeFile = open("primeFile.txt", "a")
                    primeFile.writelines(str(x) + "\n")
                x += 1
        else:
            pass
        primeFile.close()
        if not createBool:
            yourPrimes = None
        primeFile = open("primeFile.txt", "r")
        yourPrimes = primeFile.read().split("\n")
        yourPrimes.pop()
        yourName = raw_input("Please enter a screename: ")
        yourUser = raw_input("Please enter a username: ")
        yourPass = raw_input("Please enter a password: ")
        yourNameNum = random.choice(yourPrimes)
        yourPrimes.remove(yourNameNum)
        yourUserNum = random.choice(yourPrimes)
        yourPrimes.remove(yourUserNum)
        yourPassNum = random.choice(yourPrimes)
        yourPrimes.remove(yourPassNum)
        try:
            passFile = open("passFile.txt", "r")
        except:
            passFile = open("passFile.txt", "w")
        passFile.close()
        passFile = open("passFile.txt", "a")
        passFile.writelines(yourName + "\n")
        passFile.writelines(str(yourNameNum) + "\n")
        passFile.writelines(yourUser + "\n")
        passFile.writelines(str(yourUserNum) + "\n")
        passFile.writelines(yourPass + "\n")
        passFile.writelines(str(yourPassNum) + "\n")
        passFile.writelines(str(float(yourNameNum) * float(yourUserNum) * float(yourPassNum)) + "0")
    else:
        pass