__author__ = 'naperkins'
#This is an updated and more useful version of CAS_MRK_1
#This is meant to be more like J.A.R.V.I.S. than CleverBot
#CAS stands for CompletelyAutomatedSystem
from datetime import datetime
#from os import system
import pickle
import urllib2
import time
import audioop
import imaplib
import webbrowser
import subprocess
import re
import email
import pywapi
from math import *
import smtplib
import urllib


def recognize(lower):
    '''hmdir = "/usr/share/pocketsphinx/model/hmm/wsj1&quot;"
    lmd   = "/usr/share/pocketsphinx/model/lm/wsj/wlist5o.3e-7.vp.tg.lm.DMP&quot;"
    dictd = "/usr/share/pocketsphinx/model/lm/wsj/wlist5o.dic&quot;"
    wavfile = "test.wav"

    def decodeSpeech(hmmd,lmdir,dictp,wavfile):

        import pocketsphinx as ps

        speechRec = ps.Decoder(hmm = hmmd, lm = lmdir, dict = dictp)
        wavFile = file(wavfile,'rb')
        wavFile.seek(44)
        speechRec.decode_raw(wavFile)
        result = speechRec.get_hyp()
        return result[0]

    recognised = decodeSpeech(hmdir, lmd, dictd, wavfile)
    print recognised'''
    pass


def encrypt(plain):
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']
    plain = plain.lower()
    encrypted = ''
    for a in plain:
        alpha = make_word(alphabet)
        c = alpha.find(a) + 1
        b = plain.find(a)
        if plain[b] == ' ' or plain[b] == '@' or plain[b] == '.' or plain[b] == '7' or plain[b] == '1':
            encrypted += a
        if a in alphabet:
            a = 26 - c
            encrypted += alphabet[a]
    return encrypted


def make_word(words):
    result = ""
    for i in words:
        result += i
    return result


def my_email(recipient):
    try:
        try:
            user = open("User_email.txt", 'r')
        except IOError:
            user = open("User_email.txt", 'w')
            print("say What is your email?")
            email = encrypt(raw_input())
            print('say What is your password?')
            password = encrypt(raw_input())
            pickle.dump(email, user)
            pickle.dump(password, user)
            user.close()
            user = open("User_email.txt", 'r')
        email = encrypt(pickle.load(user))
        password = encrypt(pickle.load(user))
        contacts = open("Contacts.txt", 'r')
        emails = []
        people = []
        hi = True
        times = 1
        a = True
        while a:
            x = contacts.readlines()
            new_lst = []
            for a in x:
                if '\n' in a:
                    new_lst.append(a.replace('\n', ''))
                else:
                    new_lst.append(a)
            for x in new_lst:
                if x == 'end':
                    a = False
                if times == 1 and hi:
                    times = 2
                    emails.append(x)
                if times == 2 and not hi:
                    times = 1
                    people.append(x)
                if hi:
                    hi = False
                elif not hi:
                    hi = True
        contacts.close()
        if recipient in people:
            ask = 'yes'
        if recipient not in people:
            ask = 'no'
        if ask == 'yes':
            start = False
            while True:
                attempt = recipient
                times = 0
                attempt.lower()
                for i in people:
                    if i == attempt:
                        recipient = emails.pop(times)
                        start = True
                    else:
                        times += 1
                if start:
                    break
        else:
            pass
        print('say What would you like to email them?')
        text = raw_input()
        smtpserver = smtplib.SMTP("smtp.gmail.com",587)
        smtpserver.starttls()
        smtpserver.login(email, password)
        smtpserver.sendmail(email, recipient, text)
        print('say E mail Sent!')
        smtpserver.close()
    except smtplib.socket.gaierror:
        print('say Sir I can not email because there is no internet.')


def text(recipient):
    contacts = open("text_contacts.txt", 'r')
    emails = []
    people = []
    hi = True
    times = 1
    a = True
    while a:
        x = contacts.readlines()
        new_lst = []
        for a in x:
            if '\n' in a:
                new_lst.append(a.replace('\n', ''))
            else:
                new_lst.append(a)
        for x in new_lst:
            if x == 'end':
                a = False
            if times == 1 and hi:
                times = 2
                emails.append(x)
            if times == 2 and not hi:
                times = 1
                people.append(x)
            if hi:
                hi = False
            elif not hi:
                hi = True
    contacts.close()
    if recipient in people:
        ask = 'yes'
    if recipient not in people:
        ask = 'no'
    if ask == 'yes':
        start = False
        while True:
            attempt = recipient
            times = 0
            attempt.lower()
            for i in people:
                if i == attempt:
                    recipient = emails.pop(times)
                    start = True
                else:
                    times += 1
            if start:
                break
    else:
        pass
    message = raw_input()
    args = [1, 3]

    p = subprocess.Popen(
            ['/usr/bin/osascript', '-'] + [str(arg) for arg in args],
            stdout=subprocess.PIPE, stderr=subprocess.PIPE,
            stdin=subprocess.PIPE)

    scpt = '''
    tell application "Messages"

        set targetBuddy to "+1%s"
        set targetService to id of 1st service whose service type = iMessage


        set textMessage to "%s"

        set theBuddy to buddy targetBuddy of service id targetService
        send textMessage to theBuddy



    end tell
    ''' % (recipient, message)
    out, err = p.communicate(scpt)

    if p.returncode:
        return 'ERROR:', err
    else:
        return out # 4


def multiple_lines(string):
    return re.sub(('(?<!Dr)(?<!Esq)\. +(?=[A-Z])'),'.\n',string)


def re_format(string):
    string = string.title()
    for a in string:
        if a == ' ':
            string = string.replace(a, '')
    string = re.sub(r'\.([a-zA-Z])', r'. \1', re.sub(r"(?<=\w)([A-Z])", r" \1", string))
    string = re.sub(r'[,]+(?![0-9])', r', ', string)
    alpha = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x', 'c', 'v', 'b', 'n', 'm', 'Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', 'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'Z', 'X', 'C', 'V', 'B', 'N', 'M']
    num = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    for a in string:
        if a in num:
            if string[string.find(a)-1] in alpha:
                string = string.replace(a, ' %s'%a)
    return string


def dict_take_out(word):
    no_odds = [',', '.', 'Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', 'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'Z', 'X', 'C', 'V', 'B', 'N', 'M', ' ', 'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x', 'c', 'v', 'b', 'n', 'm', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    for a in word:
        if a not in no_odds:
            word = word.replace(a, '')
    return word


def take_out_less_odds(string):
    no_odds = ['-', "'", ',', '.', 'Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', 'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'Z', 'X', 'C', 'V', 'B', 'N', 'M', ' ', 'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x', 'c', 'v', 'b', 'n', 'm', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    for a in string:
        if a not in no_odds:
            string = string.replace(a, '')
    return string


def make_able_to_speak(string):
    nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    for a in string:
        if string[string.find(a)+1] in nums and a == ',' and string.find(a) != 0:
            lst = list(string)
            del lst[string.find(a)+1]
            string = ''.join(lst)
    return string.replace('-', ' ')


def take_out_odds(string):
    no_odds = ['-', ',',  '.', 'Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', 'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'Z', 'X', 'C', 'V', 'B', 'N', 'M', ' ', 'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x', 'c', 'v', 'b', 'n', 'm', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    for a in string:
        if a not in no_odds:
            string = string.replace(a, '')
    return string


def take_out_parenthesis(st):
    string = list(st)
    for a in string:
        if a == '(':
            del string[st.find(a)]
        if a == ')':
            del string[st.find(a) - 1]
    return ''.join(string)


def take_out_tags(string):
    lts = list(string)
    z = 0
    for x in string:
        if x == '>':
            lts.insert(z+1, ' ')
            z += 1
        z += 1
    string = ''.join(lts)
    st = list(string)
    odd = ['<', '>']
    times = 0
    for a in string:
        if a in odd:
            times += 1
    times /= 2
    for b in range(times):
        start = string.find('<') - 1
        end = string.find('>')
        bet = end - start + 1
        for a in range(bet):
            del st[start]
        string = ''.join(st)
    return string


def take_out_brackets(string):
    st = list(string)
    odd = ['[', ']']
    times = 0
    for a in string:
        if a in odd:
            times += 1
    times /= 2
    for b in range(times):
        start = string.find('[') - 1
        end = string.find(']')
        bet = end - start + 1
        for a in range(bet):
            del st[start]
        string = ''.join(st)
    return string


def get_info_from_web_page(text):
    try:
        n = 0
        text = text.title()
        url = text.replace(" ", "_").replace('.', '._')
        search = "http://en.wikipedia.org/wiki/%s" % url
        page = urllib2.urlopen(search).read()
        start = page.find('</span></h2>') + 12
        end = page.find('<sup id="cite_ref-135" class="reference">', start)
        new_page = "%s" % (page[start:end])
        for a in new_page:
            if a == '<':
                if new_page[n - 1] != ' ':
                    lst = list(new_page)
                    lst.insert(n, ' ')
                    new_page = ''.join(lst)
                    n += 1
            n += 1
        return multiple_lines(re_format(take_out_less_odds(take_out_parenthesis(take_out_brackets(take_out_tags(new_page))))))
    except urllib2.HTTPError:
        return('Sorry sir the internet is not available right now.')


def take_from_web_page(text):
    try:
        string = take_out_odds(take_out_parenthesis(take_out_brackets(take_out_tags(get_info_from_web_page(text)))))
        start = string.find('.') + 1
        end = string.find('.', start)
        return string[:end]
    except urllib2.HTTPError:
        return('Sorry sir the internet is not available right now.')


def prev_track():
    cmd = '''osascript<<END
    tell application "iTunes"
    previous track
    end tell
    END'''
    print(cmd)


def play_song(sng):
    prev_track()
    cmd = """osascript<<END
    tell application "iTunes"
    play track "%s"
    end tell
    END""" % (sng)
    print(cmd)


def playlist(ply_lst):
    cmd = """osascript<<END
    tell application "iTunes"
    play playlist "%s"
    end tell
    END""" % (ply_lst)
    print(cmd)


def pause():
    cmd = """osascript<<END
    tell application "iTunes"
    pause
    end tell
    END"""
    print(cmd)


def play():
    cmd = """osascript<<END
    tell application "iTunes"
    play
    end tell
    END"""
    print(cmd)


def mute():
    cmd = """osascript<<END
    set curVol to (get (output volume of (get volume settings)))
    if curVol > 0 then
        set volume output volume 0
    else
        set volume output volume 50
    end if
    END"""
    print(cmd)


def morning():
    try:
        result = pywapi.get_weather_from_yahoo('43026')
        temp = str(eval('%s * 1.8000 + 32.00' % result['condition']['temp'])).replace('-', 'negative')
        feels_like = str(eval('%s * 1.8000 + 32.00' % result['wind']['chill'])).replace('-', 'negative')
        condition = result['forecasts'][0]['text']
        high = result['forecasts'][0]['high'].replace('-', 'negative')
        low = result['forecasts'][0]['low'].replace('-', 'negative')
        date = result['forecasts'][0]['date']
        day = result['forecasts'][0]['day']
        sun_rise = result['astronomy']['sunrise']
        sun_set = result['astronomy']['sunset']
        print('say Good morning Sir, today is %s the %s the temperature is %s degrees fahrenheit and the condition is %s but it actually feels like %s degrees fahrenheit, the sun rose at %s and the sun will set at %s, the low is %s and the high is %s' % (day, date, temp, condition, feels_like, sun_rise, sun_set, low, high))
    except KeyError:
        print('say Sorry sir the weather is not available right now.')


def weather():
    try:
        result = pywapi.get_weather_from_yahoo('43026')
        temp = str(eval('%s * 1.8000 + 32.00' % result['condition']['temp'])).replace('-', 'negative')
        feels_like = str(eval('%s * 1.8000 + 32.00' % result['wind']['chill'])).replace('-', 'negative')
        condition = result['forecasts'][0]['text']
        print('say Sir, the temperature is %s degrees but, it actually feels like %s degrees, the condition is %s' % (temp, feels_like, condition))
    except KeyError:
        print('say Sorry sir the weather is not available right now.')


def vol_up():
    cmd = '''osascript<<END
    set theOutput to output volume of (get volume settings)
    set volume output volume (theOutput + 10)
    END'''
    print(cmd)


def vol_down():
    cmd = '''osascript<<END
    set theOutput to output volume of (get volume settings)
    set volume output volume (theOutput - 10)
    END'''
    print(cmd)


def next_track():
    cmd = '''osascript<<END
    tell application "iTunes"
    next track
    end tell
    END'''
    print(cmd)


def start_vol():
    cmd = '''osascript<<END
    set volume output volume (50)
    END'''
    print(cmd)


def morning_vol():
    cmd = '''osascript<<END
    set volume output volume (100)
    END'''
    print(cmd)


def day_of_week():
    day = datetime.now().isoweekday()
    if day == 1:
        return 'Monday'
    if day == 2:
        return 'Tuesday'
    if day == 3:
        return 'Wednesday'
    if day == 4:
        return 'Thursday'
    if day == 5:
        return 'Friday'
    if day == 6:
        return 'Saturday'
    if day == 7:
        return 'Sunday'


def correct_day_ending(day):
    if (len(str(day)) - 1) == '1':
        return 'st'
    elif (len(str(day)) - 1) == '2':
        return 'nd'
    elif (len(str(day)) - 1) == '3':
        return 'rd'
    else:
        return 'th'


def geoip(a):
    try:
        capitals = {'Alabama': 'Montgomery',
                    'Alaska': 'Juneau',
                    'Arizona': 'Phoenix',
                    'Arkansas': 'Little Rock',
                    'California': 'Sacramento',
                    'Colorado': 'Denver',
                    'Connecticut': 'Hartford',
                    'Delaware': 'Dover',
                    'Florida': 'Tallahassee',
                    'Georgia': 'Atlanta',
                    'Hawaii': 'Honolulu',
                    'Idaho': 'Boise',
                    'Illinois': 'Springfield',
                    'Indiana': 'Indianapolis',
                    'Iowa': 'Des Moines',
                    'Kansas': 'Topeka',
                    'Kentucky': 'Frankfort',
                    'Louisiana': 'Baton Rouge',
                    'Maine': 'Augusta',
                    'Maryland': 'Annapolis',
                    'Massachusetts': 'Boston',
                    'Michigan': 'Lansing',
                    'Minnesota': 'St. Paul',
                    'Mississippi': 'Jackson',
                    'Missouri': 'Jefferson City',
                    'Montana': 'Helena',
                    'Nebraska': 'Lincoln',
                    'Nevada': 'Carson City',
                    'New Hampshire': 'Concord',
                    'New Jersey': 'Trenton',
                    'New Mexico': 'Santa Fe',
                    'New York': 'Albany',
                    'North Carolina': 'Raleigh',
                    'North Dakota': 'Bismark',
                    'Ohio': 'Columbus',
                    'Oklahoma': 'Oklahoma City',
                    'Oregon': 'Salem',
                    'Pennsylvania': 'Harrisburg',
                    'Rhode Island': 'Providence',
                    'South Carolina': 'Columbia',
                    'South Dakota': 'Pierre',
                    'Tennessee': 'Nashville',
                    'Texas': 'Austin',
                    'Utah': 'Salt Lake City',
                    'Vermont': 'Montpelier',
                    'Virgina': 'Richmond',
                    'Washington': 'Olympia',
                    'West Virgina': 'Charleston',
                    'Wisconsin': 'Madison',
                    'Wyoming': 'Cheyenne'}

        states = ['Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California', 'Colorado', 'Connecticut', 'Delaware',
                  'Florida', 'Georgia', 'Hawaii', 'Idaho', 'Illinois', 'Indiana', 'Iowa', 'Kansas', 'Kentucky', 'Louisiana',
                  'Maine', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota', 'Mississippi', 'Missouri', 'Montana',
                  'Nebraska', 'Nevada', 'New Hampshire', 'New Jersey', 'New Mexico', 'New York', 'North Carolina',
                  'North Dakota', 'Ohio','Oklahoma', 'Oregon', 'Pennsylvania', 'Rhode Island', 'South Carolina',
                  'South Dakota', 'Tennessee', 'Texas','Utah', 'Vermont', 'Virgina', 'Washington','West Virgina',
                  'Wisconsin', 'Wyoming']


        while 1:
            a = a.lower()
            a = a.title()
            num = 0
            cap = 0

            for key in capitals:
                if key == a:
                    page = urllib2.urlopen('http://woeid.rosselliot.co.nz/lookup/%s' % capitals[key]).read()
                    cap = capitals[key]
                num += 1
            if a in states:
                f = page.find(cap)
                if f != -1:
                    start = page.find('data-center_long="', f) + 18
                    end = page.find('"', start)
                    start1 = page.find('data-center_lat="', end) + 17
                    end1 = page.find('"', start1)
                    return '%s Latitude: %s Longitude: %s' % (a, page[start1:end1], page[start:end])
            else:
                for b in states:
                    f = a.find(b)
                    if f != -1:
                        f = len(a[f:])
                        f = len(a) - f
                        x = a[:f - 1]
                        le = len(x)
                        g = a[le + 1:]
                        x = x.replace(' ', '%20')
                        page = urllib2.urlopen('http://woeid.rosselliot.co.nz/lookup/%s' % x).read()
                        f = page.find(g)
                        start = page.find('data-center_long="', f - 136) + 18
                        end = page.find('"', start)
                        start1 = page.find('data-center_lat="', end) + 17
                        end1 = page.find('"', start1)
                        return '%s Latitude: %s Longitude: %s' % (a, page[start1:end1], page[start:end])
    except urllib2.HTTPError:
        return('say Sorry sir the weather is not available right now.')


def play_dvd():
    cmd = """osascript<<END
    tell application "DVD Player"
    activate
    play dvd
    end tell
    END"""
    print(cmd)


def pause_dvd():
    cmd = """osascript<<END
    tell application "DVD Player"
    activate
    pause dvd
    end tell
    END"""
    print(cmd)


def my_quit(app):
    cmd = """osascript<<END
    tell application "%s"
    quit
    end tell
    END""" % app
    print(cmd)


def my_replace(s, r, n_r, n):
    p = 0
    z = 0
    for a in s:
        if a == r:
            p += 1
            if p == n:
                lst = list(s)
                del lst[z]
                lst.insert(z, n_r)
                s = ''.join(lst)
                p = 0
        z += 1
    return s


def read_email1():
    global server
    try:
        mail = imaplib.IMAP4_SSL('imap.gmail.com')
        user = open("User_email.txt", 'r')
        username = encrypt(user.readline().replace("\n", ""))
        password = encrypt(user.readline())
        user.close()
        mail.login(username, password)
        mail.list()
        mail.select('inbox')
        result, data = mail.uid('search', None, "UNSEEN")
        i = len(data[0].split())
        for x in range(i):
            latest_email_uid = data[0].split()[x]
            result, email_data = mail.uid('fetch', latest_email_uid, '(RFC822)')
            a = '%s\n\n' % email_data[0][1]
            b = email.message_from_string(a)
            if b.is_multipart():
                for payload in b.get_payload():
                    # if payload.is_multipart(): ...
                    body = payload.get_payload()
                    break
            else:
                body = b.get_payload()
            '''s = [x.start() for x in re.finditer('<div>', body[:body.find("</div><div c")+1])]
            h = [x.start() for x in re.finditer('<br>', body[:body.find("</div><div c")+1])]
            print s
            print h
            idk = 5
            for g in s:
                for k in h:
                    if int(k) <= int(g)+5:
                        pass
                    else:
                        print body[int(g)+idk:int(k)]
            print "\n\n\n\n"'''
            try:
                if b['From'].find("<") != -1 and b['From'].find(">") != -1:
                    #print body
                    return [((b['From'])[(b['From']).find("<") + 1:(b['From']).find(">")],
                             b['Subject'].replace('&#39;', "'").replace('"', '&quot;'),
                             body[body.find('>')+1:body.find('<', body.find('>')+1)].replace('&#39;', "'").replace('"', '&quot;')), b['From']]
                else:
                    #print body
                    return body[body.find('>')+1:body.find('<', body.find('>')+1)].replace('&#39;', "'").replace('"', '&quot;'), b['From']
                #return ['You have an E mail from %s. The subject is %s, and The message is %s.' % (b['From'].replace('>', '').replace('<', '').replace('.', ' dot ').replace('@', ' at '), b['Subject'].replace('&#39;', "'").replace('"', '&quot;'), body[body.find('>')+1:body.find('<', body.find('>')+1)].replace('&#39;', "'").replace('"', '&quot;')), b['From']]
            except AttributeError:
                return ['You have no emails.', '']
    except imaplib.socket.gaierror:
        return ['Sir I can not check your email because there is no internet.', '']


def read_email():
    emails = []
    reply = []
    while 1:
        new = read_email1()
        if new is None:
            break
        else:
            emails.append(new[0])
            reply.append(new[1])
    #bod = str(emails[:])
    nw_msg = []
    nw_rep = []
    for a in emails:
        msg = a[2]
        nw_msg.append(msg.replace('\r', "").replace('\n', " "))
    for a in reply:
        pers = a[:a.find("<")-1]
        nw_rep.append(pers.replace('"', "").replace("-", " "))
    #print 'dfsbakfasd'
    #print bod
    return nw_msg, nw_rep


def check_song():
    args = [1, 3]

    p = subprocess.Popen(
            ['/usr/bin/osascript', '-'] + [str(arg) for arg in args],
            stdout=subprocess.PIPE, stderr=subprocess.PIPE,
            stdin=subprocess.PIPE)

    scpt = '''
    tell application "iTunes"
        set what to get name of current track
    end tell
    '''

    out, err = p.communicate(scpt)

    if p.returncode:
        return 'ERROR:', err
    else:
        return out # 4


def check_playlist():
    args = [1, 3]

    p = subprocess.Popen(
            ['/usr/bin/osascript', '-'] + [str(arg) for arg in args],
            stdout=subprocess.PIPE, stderr=subprocess.PIPE,
            stdin=subprocess.PIPE)

    scpt = '''
    tell application "iTunes"
        set what to get name of current playlist
    end tell
    '''

    out, err = p.communicate(scpt)

    if p.returncode:
        return 'ERROR:', err
    else:
        return out # 4


def what_part_of_speech(word):
    page = urllib2.urlopen('http://www.merriam-webster.com/dictionary/%s' % word).read()
    start = page.find('<meta name="twitter:description" content="') + 42
    end = page.find('|', start)
    return dict_take_out(page[start:end])


def search_dictionary(word):
    page = urllib2.urlopen('http://www.merriam-webster.com/dictionary/%s' % word).read()
    start = page.find('<meta name="Description" content="Define %s' % word) + (43+len('%s' % word))
    end = page.find(',', start)
    defin = page[start:end].replace('-', ' ').replace('(', ' ').replace(')', ' ').replace('"', ' ').replace("'", ' ')
    return defin[:-6]


def go_to(a):
    page = urllib2.urlopen('https://search.yahoo.com/search;_ylt=AqYVYuEKFOdyPSRYJI1H8oebvZx4?p=%s&toggle=1&cop=mss&ei'
                       '=UTF-8&fr=yfp-t-250&fp=1' % a).read()
    start = page.find('<a id="link-1" class="yschttl spt" href="') + 41
    end = page.find('"', start)
    webbrowser.open_new(page[start:end])


def check_month(month_num):
    months = {
        "January": 1,
        "February": 2,
        "March": 3,
        "April": 4,
        "May": 5,
        "June": 6,
        "July": 7,
        "August": 8,
        "September": 9,
        "October": 10,
        "November": 11,
        "December": 12,
    }
    for key in months:
        if months[key] == month_num:
            return key


def close_window(name):
    cmd = """
    osascript<<END
    tell application "%s"
    close every window
    end tell
    END
    """ % name
    print(cmd)


def x_out_tab(name):
    cmd = """osascript<<END
    try
    tell application "Firefox"
    set winlist to count of every window
    repeat with i from 1 to winlist
    close (every tab of window i whose name contains "%s")
    end repeat
    end tell
    end try
    END""" % name
    print(cmd)


def calculator(lower):
    f = 0
    for a in lower:
        try:
            d = int(a)
            break
        except ValueError:
            if a == '(' or a == ')':
                break
        f += 1
    try:
        ans = eval(lower[f:])
        print('say %s' % ans)
    except SyntaxError:
        pass


def get_factors(num):
    factors = ''
    num = int(num)
    for a in range(num):
        a += 1
        if int(str(num/float(a))[str(num/float(a)).find('.')+1:]) == 0:
            factors += '%s ' % str(a)
    return factors


def isprime(num):
    if get_factors(num) == '1 %s ' % num:
        return '%s is prime.' % num
    else:
        return '%s is not prime.' % num


def factor(equat):
    n = 0
    indexes = []
    reas = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '+', '-', '^']
    for a in equat:
        if a not in reas:
            equat = equat.replace(a, '')
    start = equat.find('^')
    equat = equat.replace(equat[start:start+2], '')
    for a in equat:
        if a == '-' or a == '+':
            indexes.append(str(n))
        n += 1
    a = equat[:int(indexes[0])]
    if a == '':
        a = '1'
    if a == '-':
        a == '-1'
    if "+" in a:
        a = a.replace('+', '')
    b = equat[int(indexes[0]):int(indexes[1])]
    if "+" in b:
        b = b.replace('+', '')
    c = equat[int(indexes[1]):]
    if "+" in c:
        c = c.replace('+', '')
    rad = eval('%s*%s-(4*%s*%s)' % (b, b, a, c))
    try:
        rt = str(sqrt(int(rad)))
        return "The x-intercepts are %s, and %s" % (eval('(%s+%s)/2*%s' % (str(int(b)*-1), rt, a)) * -1, eval('(%s-%s)/2*%s' % (str(int(b)*-1), rt, a)) * -1)
    except ValueError:
        rt = str(sqrt(int(rad)*-1))
        return "The x-intercepts are %si, and %si" % (eval('(%s+%s)/2*%s' % (str(int(b)*-1), rt, a)) * -1, eval('(%s-%s)/2*%s' % (str(int(b)*-1), rt, a)) * -1)


def eject_disc():
    cmd = """osascript<<END
    tell application "DVD Player"
    activate
    eject dvd
    end tell
    END"""
    print(cmd)


def add_contacts():
    print('say For texting or email')
    type = raw_input()
    if type == 'email':
        contacts = open("Contacts.txt", 'a')
        a = True
        while a:
            with open('Contacts.txt', 'rb+') as f:
                f.seek(0,2)
                size=f.tell()
                f.truncate(size-4)
            print("say What is a persons email that you would like to put in your contacts")
            person = raw_input()
            print("say What would you like the tag for their email to be")
            person_short = raw_input()
            person.lower()
            person_short.lower()
            contacts.write('%s\n' % person)
            contacts.write('%s\n' % person_short)
            contacts.write('end\n')
            contacts.close()
            a = False
    if type == 'texting':
        contacts = open("text_contacts.txt", 'a')
        a = True
        while a:
            with open('Contacts.txt', 'rb+') as f:
                f.seek(0,2)
                size=f.tell()
                f.truncate(size-4)
            print("say What is a persons number that you would like to put in your contacts")
            person = raw_input()
            print("say What would you like the tag for their number to be")
            person_short = raw_input()
            person.lower()
            person_short.lower()
            contacts.write('%s\n' % person)
            contacts.write('%s\n' % person_short)
            contacts.write('end\n')
            contacts.close()
            a = False


def get_news():
    try:
        pg = urllib2.urlopen('http://www.cnn.com/').read()
        start1 = pg.find('<span class="cd__headline-text">') + 32
        end1 = pg.find('</span>', start1)
        start2 = pg.find('<span class="cd__headline-text">', end1) + 32
        end2 = pg.find('</span>', start2)
        start3 = pg.find('<span class="cd__headline-text">', end2) + 32
        end3 = pg.find('</span>', start3)
        start4 = pg.find('<span class="cd__headline-text">', end3) + 32
        end4 = pg.find('</span>', start4)
        start5 = pg.find('<span class="cd__headline-text">', end4) + 32
        end5 = pg.find('</span>', start5)
        return [pg[start1:end1].replace('(', ' ').replace(')', ' ').replace('-', ' ').replace(':', '').replace('.', ' ').replace(';', ' ').replace("'", ''), pg[start2:end2].replace('(', ' ').replace(')', ' ').replace('-', ' ').replace(':', '').replace('.', ' ').replace(';', ' ').replace("'", ''), pg[start3:end3].replace('(', ' ').replace(')', ' ').replace('-', ' ').replace(':', '').replace('.', ' ').replace(';', ' ').replace("'", ''), pg[start4:end4].replace('(', ' ').replace(')', ' ').replace('-', ' ').replace(':', '').replace('.', ' ').replace(';', ' ').replace("'", ''), pg[start5:end5].replace('(', ' ').replace(')', ' ').replace('-', ' ').replace(':', '').replace('.', ' ').replace(';', ' ').replace("'", '')]
    except urllib2.HTTPError:
        return('Sorry sir the internet is not available right now.')


def call(recipient):
    contacts = open("Contacts.txt", 'r')
    a = True
    while a:
        x = contacts.readlines()
        new_lst = []
        for a in x:
            if '\n' in a:
                new_lst.append(a.replace('\n', ''))
            else:
                new_lst.append(a)
        tag = []
        number = []
        num = 1
        for x in new_lst:
            if x == 'end':
                a = False
            if num == 1:
                number.append(x)
                num = 2
            elif num == 2:
                tag.append(x)
                num = 1
    contacts.close()
    number.pop()
    name = recipient
    name.lower()
    while True:
        times = 0
        for i in tag:
            if name == i:
                start = True
                break
            else:
                times += 1
        if start:
            break
    number_recip = number[times]
    cmd = """osascript<<END
    do shell script "open facetime://%s?audio=yes"
    tell application "FaceTime"
        activate
    end tell
    delay 1
    tell application "System Events"
        tell process "FaceTime"
            keystroke return
        end tell
    end tell
    END""" % number_recip
    print(cmd)


states = ['Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California', 'Colorado', 'Connecticut', 'Delaware', 'Florida',
              'Georgia', 'Hawaii', 'Idaho', 'Illinois', 'Indiana', 'Iowa', 'Kansas', 'Kentucky', 'Louisiana', 'Maine',
              'Maryland', 'Massachusetts', 'Michigan', 'Minnesota', 'Mississippi', 'Missouri', 'Montana', 'Nebraska',
              'Nevada', 'New Hampshire', 'New Jersey', 'New Mexico', 'New York', 'North Carolina', 'North Dakota',
              'Ohio','Oklahoma', 'Oregon', 'Pennsylvania', 'Rhode Island', 'South Carolina', 'South Dakota',
              'Tennessee', 'Texas','Utah', 'Vermont', 'Virgina', 'Washington','West Virgina', 'Wisconsin', 'Wyoming']
now = datetime.now()
read = '0'
day = now.day
p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paInt16, channels=1, rate=44100, input=True, frames_per_buffer=1024)
while 1:
    reading = ''
    by = open("bye.txt", 'r')
    reading += by.read()
    by.close()
    #if reading == 'True':
    if True == True:
        by = open("bye.txt", 'w')
        by.write('False')
        by.close()
        while 1:
            new_lst = []
            rem = []
            ti = []
            hi = True
            times = 1
            a = True
            while a:
                user = open('reminders.txt', 'r')
                x = user.readlines()
                new_lst = []
                for a in x:
                    if '\n' in a:
                        new_lst.append(a.replace('\n', ''))
                    else:
                        new_lst.append(a)
                for x in new_lst:
                    if x in rem:
                        a = False
                        rem.pop()
                        ti.pop()
                    if times == 1 and hi:
                        times = 2
                        rem.append(x)
                    if times == 2 and not hi:
                        times = 1
                        ti.append(x)
                    if hi:
                        hi = False
                    elif not hi:
                        hi = True
                user.close()
            data = stream.read(1024)
            rmsTemp = audioop.rms(data, 2)
            clp = rmsTemp
            if clp >= 2500 and recognize(data) != "":
            #if clp >= 500:
                stream.stop_stream()
                stream.close()
                p.terminate()
                prev_track()
                play_song("Should I Stay Or Should I Go")
                start_vol()
                time.sleep(5)
                print('say Welcome back sir')
                while 1:
                    now = datetime.now()
                    q = raw_input()
                    lowers = q.lower()
                    lower = lowers
                    lower.replace('information', 'info')
                    if lower ==  'previous':
                        user = open('previous.txt', 'r')
                        lower =  user.readlines()[0]
                        user.close()
                    user = open('previous.txt', 'w')
                    user.write(lower)
                    user.close()
                    if "time" in lower and 'play' not in lower:
                        n = datetime.now()
                        if n.hour > 12:
                            a = 'pm'
                            b =  n.hour - 12
                            if len(str(n.minute)) == 1:
                                nm = 'o %s' % n.minute
                                print("say Sir, the time is %s %s PM" % (b, nm))
                            else:
                                print("say Sir, the time is %s %s PM" % (b, n.minute))
                        else:
                            a = 'am'
                            if len(str(n.minute)) == 1:
                                nm = 'o %s' % n.minute
                                print("say Sir, the time is %s %s PM" % (b, nm))
                            else:
                                print("say Sir, the time is %s %s PM" % (b, n.minute))
                    if "date" in lower:
                        n = datetime.now()
                        print("say Sir, the date is %s/%s/%s" % (n.month, n.day, n.year))
                    if (" day" in lower or 'day ' in lower or 'today' in lower) and 'date' not in lower:
                        n = datetime.now()
                        print("say Sir, today is %s the %s%s" % (day_of_week(), n.day, correct_day_ending(n.day)))
                    if lower.find("search") != -1 or ((lower.find('what is ') != -1 or lower.find('whats') != -1) and lower.find('definiton') == -1):
                        if lower.find('what is ') != -1:
                            search = lower[lower.find('what is ') + 8:]
                            search = search.replace(' ', '+')
                            page = urllib2.urlopen('https://search.yahoo.com/search;_ylt=A0LEVzKnad5UfNMAjlVXNyoA;_ylc=X1MDMjc2NjY3OQRfcgMyBGZyA3lmcC10LTI1MARncHJpZANVb1RuRl9rZVRKbWRVU1VsTDVpSC5BBG5fcnNsdAMwBG5fc3VnZwM5BG9yaWdpbgNzZWFyY2gueWFob28uY29tBHBvcwMwBHBxc3RyAwRwcXN0cmwDBHFzdHJsAzIwBHF1ZXJ5A3RvcCB0ZW4gZmFzdGVzdCBjYXJzBHRfc3RtcAMxNDIzODYyMjA4?p=%s&fr2=sb-top-search&fr=yfp-t-250&fp=1' % search).read()
                            start = page.find('ac-algo ac-21th" href="') + 23
                            end = page.find('"', start)
                            webbrowser.open_new(page[start:end])
                        if lower.find('what is a ') != -1:
                            search = lower[lower.find('what is a ') + 10:]
                            search = search.replace(' ', '+')
                            page = urllib2.urlopen('https://search.yahoo.com/search;_ylt=A0LEVzKnad5UfNMAjlVXNyoA;_ylc=X1MDMjc2NjY3OQRfcgMyBGZyA3lmcC10LTI1MARncHJpZANVb1RuRl9rZVRKbWRVU1VsTDVpSC5BBG5fcnNsdAMwBG5fc3VnZwM5BG9yaWdpbgNzZWFyY2gueWFob28uY29tBHBvcwMwBHBxc3RyAwRwcXN0cmwDBHFzdHJsAzIwBHF1ZXJ5A3RvcCB0ZW4gZmFzdGVzdCBjYXJzBHRfc3RtcAMxNDIzODYyMjA4?p=%s&fr2=sb-top-search&fr=yfp-t-250&fp=1' % search).read()
                            start = page.find('ac-algo ac-21th" href="') + 23
                            end = page.find('"', start)
                            webbrowser.open_new(page[start:end])
                        if lower.find('whats ') != -1:
                            search = lower[lower.find('whats ') + 6:]
                            search = search.replace(' ', '+')
                            page = urllib2.urlopen('https://search.yahoo.com/search;_ylt=A0LEVzKnad5UfNMAjlVXNyoA;_ylc=X1MDMjc2NjY3OQRfcgMyBGZyA3lmcC10LTI1MARncHJpZANVb1RuRl9rZVRKbWRVU1VsTDVpSC5BBG5fcnNsdAMwBG5fc3VnZwM5BG9yaWdpbgNzZWFyY2gueWFob28uY29tBHBvcwMwBHBxc3RyAwRwcXN0cmwDBHFzdHJsAzIwBHF1ZXJ5A3RvcCB0ZW4gZmFzdGVzdCBjYXJzBHRfc3RtcAMxNDIzODYyMjA4?p=%s&fr2=sb-top-search&fr=yfp-t-250&fp=1' % search).read()
                            start = page.find('ac-algo ac-21th" href="') + 23
                            end = page.find('"', start)
                            webbrowser.open_new(page[start:end])
                        if lower.find('whats a ') != -1:
                            search = lower[lower.find('whats a ') + 8:]
                            search = search.replace(' ', '+')
                            page = urllib2.urlopen('https://search.yahoo.com/search;_ylt=A0LEVzKnad5UfNMAjlVXNyoA;_ylc=X1MDMjc2NjY3OQRfcgMyBGZyA3lmcC10LTI1MARncHJpZANVb1RuRl9rZVRKbWRVU1VsTDVpSC5BBG5fcnNsdAMwBG5fc3VnZwM5BG9yaWdpbgNzZWFyY2gueWFob28uY29tBHBvcwMwBHBxc3RyAwRwcXN0cmwDBHFzdHJsAzIwBHF1ZXJ5A3RvcCB0ZW4gZmFzdGVzdCBjYXJzBHRfc3RtcAMxNDIzODYyMjA4?p=%s&fr2=sb-top-search&fr=yfp-t-250&fp=1' % search).read()
                            start = page.find('ac-algo ac-21th" href="') + 23
                            end = page.find('"', start)
                            webbrowser.open_new(page[start:end])
                        else:
                            search = lower[lower.find(' ')+1:]
                            search = search.replace(' ', '+')
                            page = urllib2.urlopen('https://search.yahoo.com/search;_ylt=A0LEVzKnad5UfNMAjlVXNyoA;_ylc=X1MDMjc2NjY3OQRfcgMyBGZyA3lmcC10LTI1MARncHJpZANVb1RuRl9rZVRKbWRVU1VsTDVpSC5BBG5fcnNsdAMwBG5fc3VnZwM5BG9yaWdpbgNzZWFyY2gueWFob28uY29tBHBvcwMwBHBxc3RyAwRwcXN0cmwDBHFzdHJsAzIwBHF1ZXJ5A3RvcCB0ZW4gZmFzdGVzdCBjYXJzBHRfc3RtcAMxNDIzODYyMjA4?p=%s&fr2=sb-top-search&fr=yfp-t-250&fp=1' % search).read()
                            start = page.find('ac-algo ac-21th" href="') + 23
                            end = page.find('"', start)
                            webbrowser.open_new(page[start:end])
                    if lower.find('get info on') != -1:
                        start = lower.find('on') + 2
                        word = lower[start+1:]
                        try:
                            print('say Gathering data, please wait a few seconds.')
                            print('say %s' % take_from_web_page(word))
                            print('say For more info on %s look at the %s.txt file' % (word, word.title().replace(' ', '_')))
                            user = open('%s.txt' % word.title().replace(' ', '_'), 'w')
                            user.write(get_info_from_web_page(word))
                            user.close()
                        except urllib2.HTTPError:
                            webbrowser.open("https://www.google.com/#q=%s" % word.replace(' ', '+'))
                    if "open" in lower:
                        a = lower.replace("open ", "")
                        a = "'" + a + "'"
                        a = "open -a " + a
                        print(a)
                    if "weather" in lower:
                        weather()
                    if "email" in lower and ('check' not in lower and 'read' not in lower):
                        try:
                            if lower.find('email') - 1 == -1:
                                start = lower.find(' ') + 1
                                my_email(lower[start:])
                        except IndexError:
                            pass
                    if 'text' in lower:
                        start = lower.find(' ') + 1
                        text(lower[start:])
                        print('say Text sent!')
                    if lower.find('your') != -1 and lower.find('name') != -1:
                        print("say I'm Arsi")
                    if lower.find('dont') and lower.find('wait'):
                        pass
                    if lower.find('goodnight') != -1 or lower.find('sleep') != -1 or lower.find('bye') != -1:
                        print("say Goodbye Sir")
                        pause()
                        b = open("bye.txt", 'w')
                        b.write('True')
                        b.close()
                        p = pyaudio.PyAudio()
                        stream = p.open(format=pyaudio.paInt16, channels=1, rate=44100, input=True, frames_per_buffer=1024)
                        break
                    if lower.find('play') != -1 and lower.find(' ') != -1 and 'dvd' not in lower:
                        try:
                            ply_lst = lower[lower.find(' ') + 1:]
                            ply_lst = ply_lst.lower().title()
                            playlist(ply_lst)
                            time.sleep(.5)
                            if ply_lst not in check_playlist():
                                pause()
                                play_song(ply_lst)
                            if ply_lst not in check_song() and ply_lst not in check_playlist():
                                pause()
                                sng = ply_lst.replace(' ', '+')
                                page = urllib2.urlopen('https://www.youtube.com/results?search_query=%s' % sng).read()
                                page = page[page.find('</div><div class="yt-lockup-content">'):]
                                title_start = page.find('title="') + 7
                                title_end = page.find('"', title_start)
                                title = page[title_start:title_end]
                                start = page.find('<a href="') + 9
                                duration_start = page.find('Duration: ', start) + 10
                                duration_end = page.find('.', duration_start)
                                duration = page[duration_start:duration_end]
                                end = page.find('"', start)
                                webbrowser.open_new("https://www.youtube.com/%s" % page[start:end])
                                colon = duration.find(':')
                                minute = duration[:colon]
                                new_min = int(minute) * 60
                                duration = new_min + int(duration[colon+1:])
                                duration += 3
                                #time.sleep(duration)
                                #x_out_tab(title)
                        except urllib2.HTTPError:
                            print('say Sorry sir the internet is not available right now.')
                    if lower.find('play') != -1 and lower.find(' ') == -1 and 'dvd' not in lower:
                        play()
                    if lower.find('play') != -1 and 'dvd' in lower:
                        play_dvd()
                    if lower.find('pause') != -1 and 'dvd' not in lower:
                        pause()
                    if lower.find('pause') != -1 and 'dvd' in lower:
                        pause_dvd()
                    if lower.find('mute') != -1:
                        mute()
                    if lower.find('up') != -1:
                        vol_up()
                    if lower.find('down') != -1:
                        vol_down()
                    if lower.find('reminder') != -1 and lower.find('reminders') == -1:
                        numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', ':']
                        times = []
                        for a in lower:
                            if a in numbers:
                                times.append(a)
                        l = len(times)
                        if l == 3:
                            times.insert(1, ' ')
                        if l == 4:
                            times.insert(2, ' ')
                        print('say Sir, what day should this be')
                        da = raw_input()
                        da = da.lower()
                        if da == 'today':
                            da = datetime.now().day
                        if da == 'tomorrow':
                            da = datetime.now().day + 1
                        try:
                            if len(da) == 1:
                                da = ''.join((' ', da))
                        except TypeError:
                            pass
                        times.insert(0, '%s ' % da)
                        times = make_word(times)
                        print('say Sir, what should this reminder be for.')
                        rem = raw_input()
                        rem = rem.lower()
                        print('say Sir, should this be AM or PM.')
                        ap = raw_input()
                        ap = ap.upper()
                        times += ' %s' % ap
                        if times.find(' ') == 2:
                            print('say Your reminder for %s has been set for %s on the %s%s.' % (rem, times[2:], times[:2], correct_day_ending(times[:2])))
                        if times.find(' ') == 3:
                            print('say Your reminder for %s has been set for %s on the %s%s.' % (rem, times[3:], times[:3], correct_day_ending(times[:3])))
                        user = open('reminders.txt', 'a')
                        user.write('%s\n' % rem)
                        user.write('%s\n' % times)
                        user.close()
                    if lower.find('next') != -1:
                        next_track()
                    if lower.find('back') != -1 and 'go' in lower:
                        prev_track()
                    if 'other Arsi' == 'activated':
                        b = open("bye.txt", 'r+')
                        b.write('True')
                        b.close()
                    if 'arsi' in lower:
                        read = ''
                        by = open("bye.txt", 'r')
                        read += by.read()
                        by.close()
                        if read == 'False':
                            print('say Yes Sir.')
                        if read == 'True':
                            print('say Welcome Back Sir.')
                            by = open("bye.txt", 'w')
                            by.write('False')
                    if lower.find('flight') != -1 and lower.find('plan') != -1:
                        place = lower.find('for')
                        for a in states:
                            if a.lower() in lower:
                                if lower.find('city') >= lower.find(a):
                                    print('say Setting flight plan for %s' % a)
                        user = open('flights.txt', 'w')
                        user.write(geoip(lower[place + 4:]))
                    if 'render' in lower:
                        print('open -a "Sketch Up"')
                    if lower == 'iron man 3':
                        play_song('Iron Man 3')
                    if 'quit' in lower:
                        start = lower.find(' ') + 1
                        my_quit(lower[start:])
                    if (lower.find('read') != -1 or lower.find('check') != -1) and lower.find('email') != -1 and lower.find('email ') == -1 and lower.find('mail') != -1 and lower.find('mail ') != -1:
                        a = read_email()
                        rvar = 0
                        print('say You have %s emails,' % str(len(a[0])))
                        for hj in a[1]:
                            if rvar != 0:
                                print("say and %s," % hj)
                            else:
                                print("say from %s," % hj)
                            rvar += 1
                        print("say Would you like me to read any of them")
                        """if a[1] != '':
                            print('say Would you like to email %s back?' % a[1])
                            ans = raw_input()
                            if ans.find('yes') != -1 or ans.find('yeah') != -1:
                                my_email(a[1])"""
                    if lower.find('define') != -1 or lower.find('definition') != -1:
                        if lower.find('definition') != -1:
                            start = lower.find('of ') + 3
                            word = lower[start:]
                        else:
                            start = lower.find(' ') + 1
                            word = lower[start:]
                        print('say %s' % search_dictionary(word))
                    if lower.find('go') != -1 and lower.find('to') != -1:
                        search = lower.find('to ') + 3
                        search = lower[search:]
                        go_to(search)
                    if 'close' in lower:
                        start = lower.find(' ') + 1
                        close_window(lower[start:])
                    if lower.find('prime') != -1:
                        start = lower.find('is') + 3
                        end = lower.find(' ', start)
                        print('say %s' % isprime(lower[start:end]))
                    if lower.find('^2') != -1:
                        startnum = 0
                        theindex = 0
                        for a in lower:
                            if str(type(a)).find('int') != -1:
                                theindex = startnum
                            startnum += 1
                        factor(lower[theindex:])
                    if 'eject' and ('disc' or 'dvd') in lower:
                        eject_disc()
                    if lower.find('add') != -1 and lower.find('contact') != -1:
                        add_contacts()
                    if lower.find('reminders') != -1:
                        today_remind = []
                        for a in ti:
                            le = len(a)
                            if le == 10:
                                if int(a[:3]) == datetime.now().day:
                                    today_remind += '%s, ' % a
                        today_remind = today_remind[:len(today_remind)-2]
                        print('say %s' % today_remind)
                    if lower.find('news') != -1:
                        for a in get_news():
                            print('say %s' % a)
                    if lower.find('call') != -1:
                        start = lower.find('call') + 5
                        call(lower[start:])
                now = datetime.now()
                if read == '0' and day == now.day:
                    if now.hour == 7 and now.minute == 0:
                        morning_vol()
                        morning()
                        today_remind = []
                        for a in ti:
                            le = len(a)
                            if le == 10:
                                if int(a[:3]) == datetime.now().day:
                                    today_remind += '%s, ' % a
                        today_remind = today_remind[:len(today_remind)-2]
                        print('say %s' % today_remind)
                        print('say %s' % get_news())
                        read = '1'
                        day = now.day
                if day == now.day - 1:
                    day = now.day
                    read = '0'
                for a in ti:
                    le = len(a)
                    if le == 10:
                        if int(a[:3]) == datetime.now().day:
                            if a[8:] == 'PM':
                                if int(a[3:5]) == (datetime.now().hour - 12):
                                    if int(a[5:7]) >= datetime.now().minute and int(a[5:7]) <= (datetime.now().minute + 1):
                                        b = str(a)
                                        find = ti.index(b)
                                        for x in rem:
                                            r = rem.index(x)
                                            if find == r:
                                                print('say Sir, %s, is ready' % x)
                                                dele = []
                                                with open('reminders.txt') as myFile:
                                                    for num, line in enumerate(myFile, 1):
                                                        if x + '\n' == line:
                                                            dele.append(num)
                                                with open('reminders.txt') as myFile:
                                                    for num, line in enumerate(myFile, 1):
                                                        if a + '\n' == line:
                                                            dele.append(num)
                                                f = open('reminders.txt', 'r+')
                                                s = [y for x, y in enumerate(f) if x not in [line-1 for line in dele]]
                                                f.seek(0)
                                                f.write(''.join(s))
                                                f.truncate(f.tell())
                                                f.close()
                                                p = pyaudio.PyAudio()
                                                stream = p.open(format=pyaudio.paInt16, channels=1, rate=44100, input=True, frames_per_buffer=1024)
                    if le == 10:
                        if int(a[:3]) == datetime.now().day:
                            if a[8:] == 'AM':
                                if int(a[3:5]) == datetime.now().hour:
                                    if int(a[5:7]) >= datetime.now().minute and int(a[5:7]) <= (datetime.now().minute + 1):
                                        b = str(a)
                                        find = ti.index(b)
                                        for x in rem:
                                            r = rem.index(x)
                                            if find == r:
                                                print('say Sir, %s, is ready' % x)
                                                dele = []
                                                with open('reminders.txt') as myFile:
                                                    for num, line in enumerate(myFile, 1):
                                                        if x + '\n' == line:
                                                            dele.append(num)
                                                with open('reminders.txt') as myFile:
                                                    for num, line in enumerate(myFile, 1):
                                                        if a + '\n' == line:
                                                            dele.append(num)
                                                f = open('reminders.txt', 'r+')
                                                s = [y for x, y in enumerate(f) if x not in [line-1 for line in dele]]
                                                f.seek(0)
                                                f.write(''.join(s))
                                                f.truncate(f.tell())
                                                f.close()
                                                p = pyaudio.PyAudio()
                                                stream = p.open(format=pyaudio.paInt16, channels=1, rate=44100, input=True, frames_per_buffer=1024)
                    if le == 11:
                        if int(a[:3]) == datetime.now().day:
                            if a[9:] == 'PM':
                                if int(a[3:6]) == (datetime.now().hour - 12):
                                    if int(a[6:8]) >= datetime.now().minute and int(a[6:8]) <= (datetime.now().minute + 1):
                                        b = str(a)
                                        find = ti.index(b)
                                        for x in rem:
                                            r = rem.index(x)
                                            if find == r:
                                                print('say Sir, %s, is ready' % x)
                                                dele = []
                                                with open('reminders.txt') as myFile:
                                                    for num, line in enumerate(myFile, 1):
                                                        if x + '\n' == line:
                                                            dele.append(num)
                                                with open('reminders.txt') as myFile:
                                                    for num, line in enumerate(myFile, 1):
                                                        if a + '\n' == line:
                                                            dele.append(num)
                                                f = open('reminders.txt', 'r+')
                                                s = [y for x, y in enumerate(f) if x not in [line-1 for line in dele]]
                                                f.seek(0)
                                                f.write(''.join(s))
                                                f.truncate(f.tell())
                                                f.close()
                                                p = pyaudio.PyAudio()
                                                stream = p.open(format=pyaudio.paInt16, channels=1, rate=44100, input=True, frames_per_buffer=1024)
                    if le == 11:
                        if int(a[:3]) == datetime.now().day:
                            if a[9:] == 'AM':
                                if int(a[3:6]) == datetime.now().hour:
                                    if int(a[6:8]) >= datetime.now().minute and int(a[6:8]) <= (datetime.now().minute + 1):
                                        b = str(a)
                                        find = ti.index(b)
                                        for x in rem:
                                            r = rem.index(x)
                                            if find == r:
                                                print('say Sir, %s, is ready' % x)
                                                dele = []
                                                with open('reminders.txt') as myFile:
                                                    for num, line in enumerate(myFile, 1):
                                                        if x + '\n' == line:
                                                            dele.append(num)
                                                with open('reminders.txt') as myFile:
                                                    for num, line in enumerate(myFile, 1):
                                                        if a + '\n' == line:
                                                            dele.append(num)
                                                f = open('reminders.txt', 'r+')
                                                s = [y for x, y in enumerate(f) if x not in [line-1 for line in dele]]
                                                f.seek(0)
                                                f.write(''.join(s))
                                                f.truncate(f.tell())
                                                f.close()
                                                p = pyaudio.PyAudio()
                                                stream = p.open(format=pyaudio.paInt16, channels=1, rate=44100, input=True, frames_per_buffer=1024)
