import re

def remlist(plist, valrem):
   return [value for value in plist if value not in valrem]
print("MoarCores log parser. Logs are read from logs.txt\nAuthored By VenAAX")

log = open("logs.txt")
logfin = log.readlines()
log.close()
log = open("logs.txt")
logop = log.read()
log.close()

valrem = re.findall(r'.*is offline.\n',logop) #remove online/offline messages
logfin = remlist(logfin,valrem)
print (valrem)

valrem = re.findall(r'.*is online.\n',logop) #Continued
logfin = remlist(logfin,valrem)
print(valrem)

valrem = re.findall('\[\S+\s+DCS.*\n',logop) #remove DCS messages. Level up and OOC chat
logfin = remlist(logfin,valrem)
print(valrem)

valrem = re.findall(' Total Xp: .*\n',logop) #Remove total XP after XP add
logfin = remlist(logfin,valrem)
print(valrem)

valrem = re.findall('\[\S+\s+ Second Life:.*\n',logop) #Remove music change, SL messages
logfin = remlist(logfin,valrem)
print(valrem)
#leaving timestamps in chat
print(logfin)

logw = open("cleanlog.txt","w")
logw.write (' '.join(logfin))
logw.close()



