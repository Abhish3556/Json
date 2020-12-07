import urllib.request
from datetime import *
def getlatestrates():
    url=urllib.request.urlopen("https://api.exchangeratesapi.io/latest")
    data=url.read()
    print(data)
    return data
getlatestrates()
def change(amount,currency,desirecurrency,date):
    url=urllib.request.urlopen("https://api.exchangeratesapi.io/"+date+"?base="+currency+"&"+"symbols="+desirecurrency)
    data=url.read()
    print(data)
    data=str(data)
    a=data.index(desirecurrency)
    b=data.index(',',a+1)
    c=data[a+5:b-1]
    c=float(c)
    d=c*amount
    print(d)
    print(date)

print("enter the amount to change")
k=int(input())
print("enter the name of currency to be change")
chg=input()
print("enter the name of currency to which currency to be change")
des=input()
print("enter the date of exchange")
dateofinput=input()
change(k,chg,des,dateofinput)

def printAcesding():
    url=urllib.request.urlopen("https://api.exchangeratesapi.io/latest")
    data=url.read()
    data=str(data)
    data=data[data.find("{",data.find("{")+1)+1:data.find("}")]
    data=data.split(",")
    l=[]
    for i in data:
        a=i.index('"')
        b=i.index('"',a+1)
        c=i[a+1:b]
        d=b+2
        e=i[d:]
        l.append([e,c])
    def sort(s):
        l = len(s)
        for i in range(0, l):
            for j in range(0, l-i-1):
                if (float(s[j][0])>float(s[j + 1][0])):
                    tempo = s[j]
                    s[j]= s[j + 1]
                    s[j + 1]= tempo
        for cc in range(0,l):
            print("1 Euro = " + s[cc][0] + " " + s[cc][1])
    sort(l)
printAcesding()
def extremeday(startDate,endDate,currency):
    url=urllib.request.urlopen("https://api.exchangeratesapi.io/history?start_at="+startDate+"&end_at="+endDate)
    data=url.read()
    data=str(data)
    a=data.index("{")
    curr=[]
    f=data.index("}}")
    b=data.index("{",a+1)
    c=data[b:f+2]
    x = c.index("{")
    y = c.index(":{")
    f=c.count(":{")
    f=f-1
    xy=c[x+1:y]
    y = -1
    v = -1
    p = -1
    z = -1
    temp = 0
    i = xy.index('"')
    j = xy.index("-")
    k = xy[i + 1:j]
    l = xy.index("-", j + 1)
    m = xy[j + 1:l]
    p = xy.index('"', i + 1)
    n = xy[l + 1:p]
    k = int(k)
    m = int(m)
    n = int(n)
    date1 = date(k, m, n)
    if date1.weekday() == 4:
        bc=c.index("}")
        cd=c[0:bc+1]
        if currency in cd:
            x=cd.index(currency)
            val=float(cd[x+5:cd.index(',',x+1)])
            print (currency, val)
            curr.append(val)
            curr.append(xy)
    for i in range(f):
        y = c.index(":{", y+1)
        v = c.index("},",v+1)
        p=c.index(":{",y+1)
        z = c[v+2:p]
        i = z.index('"')
        j = z.index("-")
        k = z[i + 1:j]
        l = z.index("-", j + 1)
        m = z[j + 1:l]
        pp = z.index('"', i + 1)
        n = z[l + 1:pp]
        k = int(k)
        m = int(m)
        n = int(n)
        date2 = date(k, m, n)
        if date2.weekday() == 4:
            vc=c.index("}",v+1)
            cv=c[p:vc]
            if currency in cv:
                x=cv.index(currency)
                val=float(cv[x+5:cv.index(',',x+1)])
                curr.append(val)
                curr.append(z)
    print (str(currency)+" was strongest on"+str(curr[curr.index(max(curr[::2]))+1]),".1 Euro was="+str(max(curr[::2])))
    print(str(currency)+" was weakest on"+ str(curr[curr.index(min(curr[::2]))+1]),".1 Euro was="+str(min(curr[::2])))
startDat =input("Enter the startDate ")
endDat =input("Enter the endDate ")
am=input("Enter the currency ")
extremeday(startDat, endDat,am)
def findMissingDates (startDate, endDate):
    url=urllib.request.urlopen("https://api.exchangeratesapi.io/history?start_at="+startDate+"&end_at="+endDate)
    data=url.read()
    data=str(data)
    def mac(staDate):
        j = staDate.index("-")
        k = staDate[:j]
        l = staDate.index("-", j + 1)
        m = staDate[j + 1:l]
        n = staDate[l + 1:]
        k = int(k)
        m = int(m)
        n = int(n)
        sa=date(k, m, n)
        return sa
    s=mac(startDate)
    e=mac(endDate)
    print(s,e)
    a=data.index("{")

    f=data.index("}}")

    b=data.index("{",a+1)
    c=data[b:f+2]
    c= str(c)
    delta = e - s       # as timedelta
    print("the following dates are not present")
    for i in range(delta.days + 1):
        day = s + timedelta(days=i)

        day= str(day)

        if (day) not in  c:
            print(day)
a="2019-08-29"
b="2019-09-29"
findMissingDates(a,b)