#need to do
class PhoneEntry(hours,minutes,seconds,phonenumber,totalseconds,billAmount):
    def __init__(self,hours,minutes,seconds,phonenumber,billAmount,totalseconds):
        "contructor called"#doc string
        self.hours=hours
        self.minutes=minutes
        self.seconds=seconds
        self.phonenumber=phonenumber
        self.billAmount=billAmount
        self.totalseconds=totalseconds
    def setBillAmount(self,billAmount):
        self.billAmount=billAmount
    def setTotalsecs(self,totalseconds):
        self.totalseconds=totalseconds
    def getBillAmount(self):
        return self.billAmount
    def getTotalseconds(self):
        return self.totalseconds



hm=dict(phonenumber,phoneentry_tempobj)
totalseconds=0
input_log="00:01:01,400-234-090 00:05:01,701-080-080 00:05:00,400-234-090".strip()
logs=input_log.split(" ")
for i in range(len(logs)):
    log=logs[i].strip()#string type
    part1=log.split(",")[0]#getting the duaration(list type)
    part2=log.split(",")[1]#getting the phonenumber(list type)
    hours=int(log[0:2])#by slicing
    minutes=int(log[3:5])
    seconds=int(log[6:8])
    phonenumber=log[9::].replace('-','')
    print(hours,minutes,seconds,"==>",phonenumber)
    totalseconds=(hours*60*60)+(minutes*60)+seconds
    if totalseconds<300:
        billAmount=totalseconds*3
    else:
        totalMinutes=(hours*60)+minutes
        if seconds>0:
            totalMinutes+=1
        billAmount=totalMinutes*150
    phoneentry_tempobj=PhoneEntry(hours,minutes,seconds,phonenumber,billAmount,totalseconds)

    if PhoneEntry not in hashmap.keys():
        hashmap[phonenumber]=phoneentry
    else:
        currentobj=phoneEntry(hashmap.get(phonenumber))
        updatedBillAmount=currentobj.getBillAmount()+billAmount
        updatedTotalSecs=currentobj.getTotalseconds+totalseconds
        currentobj.setBillAmount(updatedBillAmount)
        currentobj.setTotalsecs(updatedTotalSecs)
        #hashmap.remove(phonenumber)
        #hashmap[phonenumber]=currentobj
        hashmap.replace(phonenumber,currentobj)
