#FSlogparse.py with a GUI to make it a little less shit to use.
import re
import easygui as w
import string

def remlist(plist, valrem):
   return [value for value in plist if value not in valrem]


def logdecode(logop):

    logfin = logop
    logfin = logfin.splitlines(0)
    logfin = [value + "\n" for value in logfin]
    valrem = re.findall(r'.*is offline.\n',logop) #remove online/offline messages
    logfin = remlist(logfin,valrem)
    valrem = re.findall(r'.*is online.\n',logop) #Continued
    logfin = remlist(logfin,valrem)
    valrem = re.findall('\[\S+\s+DCS.*\n',logop) #remove DCS messages. Level up and OOC chat
    logfin = remlist(logfin,valrem)
    valrem = re.findall(' Total Xp: .*\n',logop) #Remove total XP after XP add
    logfin = remlist(logfin,valrem)
    valrem = re.findall('\[\S+\s+ Second Life:.*\n',logop) #Remove music change, SL messages
    logfin = remlist(logfin,valrem)
    return logfin

title = "Toxia Log NC helper"
msg = "Paste logs in here"
logop = w.enterbox(msg,title)
logfin = logdecode(logop)
w.codebox("logs below","Cleaned Logs",logfin)
