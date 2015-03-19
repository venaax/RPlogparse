import re

def remlist(plist, valrem):
   return [value for value in plist if value not in valrem]
print("MoarCores log parser. Logs are read from logs.txt\nAuthored By VenAAX")

log = open("logs.txt")
logfin = log.readlines()
log.close()
log = open("logs.txt")
logop = log.read()

valrem = re.findall(r'.*is offline.\n',logop)
print (valrem)

logfin = remlist(logfin,valrem)

valrem = re.findall(r'.*is online.\n',logop)
logfin = remlist(logfin,valrem)
print(valrem)

valrem = re.findall(r'(\[\d\d:\d\d]) DCS.*\n',logop)
logfin = remlist(logfin,valrem)
print(valrem)
print(logfin)


