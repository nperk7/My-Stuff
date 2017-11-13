__author__ = 'naperkins'
#This is the emotion subsystem and is meant to determine the emotions of Alpha through a subprocess

class Love():
    def __init__(self):
        self.Emotions = [self.affection, self.lust, self.longing]
        self.curEmotions = []
        self.choice = None

    def affection(self):
        self.affectionEmotion = [self.adoration, self.subAffection, self.love, self.fondness, self.liking, self.attraction,
                             self.caring, self.tenderness, self.compassion, self.sentimentality]
    def lust(self):
        self.lustEmotions = [self.arousal, self.desire, self.subLust, self.passion, self.infatuation]
    def longing(self):
        self.longingEmotion = [self.subLonging]

    def log(self):
        Log(self.choice).log()

class Joy():
    def __init__(self):
        self.Emotions = [self.cheerfulness, self.zest, self.contentment, self.pride, self.optimism, self.enthrallment,
                         self.relief]
        self.choice = None

    def cheerfulness(self):
        self.cheerEmotions = [self.amusement, self.bliss, self.subSheerfulness, self.gaiety, self.glee, self.jolliness,
                              self.joviality, self.joy, self.delight, self.enjoyment, self.gladness, self.happiness,
                              self.jubilation, self.elation, self.satisfaction, self.ecstasy, self.euphoria]
    def zest(self):
        self.zestEmotions = [self.enthusiasm, self.zeal, self.subZest, self.excitment, self.thrill, self.exhilaration]
    def contentment(self):
        self.contentmentEmotions = [self.subContentment, self.pleasure]
    def pride(self):
        self.prideEmotions = [self.subPride, self.triumph]
    def optimism(self):
        self.optimismEmotions = [self.eagerness, self.hope, self.optimism]
    def enthrallment(self):
        self.entrallmentEmotions = [self.subEntrallment, self.rapture]
    def relief(self):
        self.reliefEmotions = [self.subRelief]

    def log(self):
        Log(self.choice).log()

class Suprise():
    def __init__(self):
        self.Emotions = [self.amazement, self.subSuprise, self.astonishment]
        self.choice = None

    def suprise(self):
        self.supriseEmotions = [self.amazement, self.subSuprise, self.astonishment]

    def log(self):
        Log(self.choice).log()

class Anger():
    def __init__(self):
        self.Emotions = [self.irritation,self.exasperation, self.rage, self.disgust, self.envy, self.torment]
        self.choice = None

    def irritation(self):
        self.irritationEmotions = [self.aggravation, self.subIrritation, self.agitation, self.annoyance, self.grouchiness,
                             self.grumpiness]
    def exasperation(self):
        self.exasperationEmotions = [self.subExasperation, self.frustration]
    def rage(self):
        self.rageEmotions = [self.subAnger, self.subRage, self.outrage, self.fury, self.wrath, self.hostility,
                             self.ferocity, self.ferocity, self.bitterness, self.hate, self.loathing, self.scorn,
                             self.spite, self.vengefulness, self.dislike, self.resentment]
    def disgust(self):
        self.disgustEmotions = [self.subDisgust, self.revulsion, self.contempt]
    def envy(self):
        self.envyEmotions = [self.subEnvy, self.jealousy]
    def torment(self):
        self.tormentEmotions = [self.subTorment]

    def log(self):
        Log(self.choice).log()

class Sadness():
    def __init__(self):
        self.Emotions = [self.suffering, self.sadness, self.disappointment, self.shame, self.neglect, self.sympath]
        self.choice = None

    def suffering(self):
        self.sufferingEmotions = [self.agony, self.subSuffering, self.hurt, self.anguish]
    def sadness(self):
        self.sadnessEmotions = [self.depression, self.despair, self.hoplessness, self.gloom, self.glumness,
                                self.subSadness, self.unhappiness, self.grief, self.sorrow, self.woe, self. misery,
                                self.melancholy]
    def disappointment(self):
        self.disappointmentEmotions = [self.dismay, self.subDisappointment, self.displeasure]
    def shame(self):
        self.shameEmotions = [self.guilt, self.subShame, self.regret, self.remorse]
    def neglect(self):
        self.neglectEmotions = [self.alienation, self.isolation, self.subNeglect, self.lonliness, self.rejection,
                                self.homesickness, self.defeat, self.dejection, self.insecurity, self.embarassment,
                                self.humiliation, self.insult]
    def sympathy(self):
        self.sympathyEmotions = [self.pity, self.subSympathy]

    def log(self):
        Log(self.choice).log()

class Fear():
    def __init__(self):
        self.Emotions = [self.horror, self.nervousness]
        self.choice = None

    def horror(self):
        self.horrorEmotions = [self.alarm, self.shock, self.fear, self.fright, self.subHorror, self.terror, self.panic,
                               self.hysteria, self.mortification]

    def nervousness(self):
        self.nervousnessEmotions = [self.anxiety, self.nervousness, self.tensenss, self.uneasiness, self.apprehension,
                                    self.worry, self.distress, self.dread]

    def log(self):
        Log(self.choice).log()

class Log():
    def __init__(self, choice):
        self.choice = choice

    def log(self):
        self.logFile = open("emotionLog.txt", "a")
        if self.choice != None:
            self.logFile.writeline("%s\n" % self.choice)
        self.logFile.close()
        self.choice = None

Love = Love()
Joy = Joy()
Suprise = Suprise()
Anger = Anger()
Sadness = Sadness()
Fear = Fear()
