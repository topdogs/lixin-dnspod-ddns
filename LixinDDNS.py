<<<<<<< HEAD
﻿#!/usr/bin/env python
#-*- coding:utf-8 -*-
import urllib2
import urllib
import json
import time
import socket

public_dic={}
public_dic["format"]="json"
headers={}
headers["User-Agent"]="lixinDDNS/1(lixin@lixin.me)"

public_dic["login_email"]="admin@admin.com" #replace your email
public_dic["login_password"]="password" #replace your password
domain="lixin.me" #replace your domain
record="home" #replace your record



ip=''
sleepTime=3000

def WriteLog(msg):
    f=open('ddns.log','a')
    f.write(time.ctime()+"    "+msg+"\n")
    f.close()
def getDomainID():
    url="https://dnsapi.cn/Domain.Info"
    params=public_dic.copy()
    params["domain"]=domain
    req=urllib2.Request(url,headers=headers,data=urllib.urlencode(params))
    resp=urllib2.urlopen(req)
    formatJson=json.load(resp)
    if formatJson["status"]["code"]!="1":
        WriteLog("getDomainID has Error: ("+formatJson["status"]["code"]+")"+formatJson["status"]["message"])
        return 0
    else:
        return formatJson["domain"]["id"]
    pass

def getRecordID(domain_id):
    url="https://dnsapi.cn/Record.List"
    params=public_dic.copy()
    params["domain_id"]=domain_id
    params["sub_domain"]=record
    req=urllib2.Request(url,headers=headers,data=urllib.urlencode(params))
    resp=urllib2.urlopen(req)
    myJson=json.load(resp)
    if myJson["status"]["code"]!="1":
        WriteLog("getRecordID has Error: ("+formatJson["status"]["code"]+")"+formatJson["status"]["message"])
        return 0
    else:
        ip=myJson["records"][0]['value']
        return myJson["records"][0]['id']
    pass
def getMyIp():
    url="ns1.dnspod.net"
    port=6666
    mySocket=socket.socket(socket.AF_INET,socket.SOCK_STREAM) 
    mySocket.connect((url,port))
    recv=mySocket.recv(16) 
    mySocket.close()
    return recv

    pass
def setDDNS(domainID,recordID):
    url="https://dnsapi.cn/Record.Ddns"
    params=public_dic.copy()
    params["domain_id"]=domainID
    params["sub_domain"]=record
    params["record_id"]=recordID
    params["record_line"]="默认"
    req=urllib2.Request(url,headers=headers,data=urllib.urlencode(params))
    resp=urllib2.urlopen(req)
    myJson=json.load(resp)
    if myJson["status"]["code"]!="1":
        WriteLog("setDDNS has Error: ("+myJson["status"]["code"]+")"+myJson["status"]["message"])
    pass
if __name__ == '__main__':
    while True:
        newIP=getMyIp()
        if ip !=newIP:
            domainID=getDomainID()
            if domainID!=0:
                recordID=getRecordID(domainID)
                if recordID !=0:
                    setDDNS(domainID,recordID)
                    ip=newIP
                    WriteLog("new ip="+ip+"\n")
                    pass
        time.sleep(sleepTime)
    pass
=======
﻿#!/usr/bin/env python
#-*- coding:utf-8 -*-
import urllib2
import urllib
import json
import time
import socket

public_dic={}
public_dic["format"]="json"
headers={}
headers["User-Agent"]="lixinDDNS/1(lixin@lixin.me)"

public_dic["login_email"]="admin@admin.com" #replace your email
public_dic["login_password"]="password" #replace your password
domain="lixin.me" #replace your domain
record="home" #replace your record



ip=''
sleepTime=3000

def WriteLog(msg):
    f=open('ddns.log','a')
    f.write(time.ctime()+"    "+msg+"\n")
    f.close()
def getDomainID():
    url="https://dnsapi.cn/Domain.Info"
    params=public_dic.copy()
    params["domain"]=domain
    req=urllib2.Request(url,headers=headers,data=urllib.urlencode(params))
    resp=urllib2.urlopen(req)
    formatJson=json.load(resp)
    if formatJson["status"]["code"]!="1":
        WriteLog("getDomainID has Error: ("+formatJson["status"]["code"]+")"+formatJson["status"]["message"])
        return 0
    else:
        return formatJson["domain"]["id"]
    pass

def getRecordID(domain_id):
    url="https://dnsapi.cn/Record.List"
    params=public_dic.copy()
    params["domain_id"]=domain_id
    params["sub_domain"]=record
    req=urllib2.Request(url,headers=headers,data=urllib.urlencode(params))
    resp=urllib2.urlopen(req)
    myJson=json.load(resp)
    if myJson["status"]["code"]!="1":
        WriteLog("getRecordID has Error: ("+formatJson["status"]["code"]+")"+formatJson["status"]["message"])
        return 0
    else:
        ip=myJson["records"][0]['value']
        return myJson["records"][0]['id']
    pass
def getMyIp():
    url="ns1.dnspod.net"
    port=6666
    mySocket=socket.socket(socket.AF_INET,socket.SOCK_STREAM) 
    mySocket.connect((url,port))
    recv=mySocket.recv(16) 
    mySocket.close()
    return recv

    pass
def setDDNS(domainID,recordID):
    url="https://dnsapi.cn/Record.Ddns"
    params=public_dic.copy()
    params["domain_id"]=domainID
    params["sub_domain"]=record
    params["record_id"]=recordID
    params["record_line"]="默认"
    req=urllib2.Request(url,headers=headers,data=urllib.urlencode(params))
    resp=urllib2.urlopen(req)
    myJson=json.load(resp)
    if myJson["status"]["code"]!="1":
        WriteLog("setDDNS has Error: ("+myJson["status"]["code"]+")"+myJson["status"]["message"])
    pass
if __name__ == '__main__':
    while True:
        newIP=getMyIp()
        if ip !=newIP:
            domainID=getDomainID()
            if domainID!=0:
                recordID=getRecordID(domainID)
                if recordID !=0:
                    setDDNS(domainID,recordID)
                    ip=newIP
                    WriteLog("new ip="+ip+"\n")
                    pass
        time.sleep(sleepTime)
    pass
    
