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

velrem2 = re.findall(r'.*DCS.*\n',logop) #problem (NameError: name 'valrem2' is not defined)
print(valrem2)
print(logfin)


