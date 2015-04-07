#!/usr/bin/env python
#-*- coding:utf-8 -*-
import sys
import urllib2
import urllib
import json
import time
import socket
import os
import ConfigParser

public_dic={}
public_dic["login_email"]="" #replace your email 替换你的dnspod账号email
public_dic["login_password"]="" #replace your password 替换你的密码
domain="" #replace your domain  你的域名
record="" #replace your record 你的二级域名
autosave=1 ## auto save info
cfgpath='./ddns.cfg'
cf = ConfigParser.ConfigParser()
public_dic["format"]="json"
headers={}
headers["User-Agent"]="lixinDDNS/1(lixin@lixin.me)"

isCron=True ##是否作为定时任务执行，isCron==True 的话，则不会进入循环
ip=''
sleepTime=3000

def readcfg():
    cf.read(cfgpath)
    o = cf.options("ddns")
    global domain
    global record
    public_dic["login_email"]=cf.get('ddns',"email")
    public_dic["login_password"]=cf.get('ddns',"password")
    domain=cf.get('ddns',"domain")
    record=cf.get('ddns',"record")

def saveIP(ip):
    f=open('./ddnsip.txt','w')
    f.write(ip)
    f.close()
def readIP():
    if not os.path.isfile('./ddnsip.txt'):
        return ""
    f=open('./ddnsip.txt','r')
    myip=f.read()
    f.close()
    return myip

def WriteLog(msg):
    f=open('./ddns.log','a')
    f.write(time.strftime("%Y/%m/%d %H:%M:%S",time.localtime())+"    "+msg+"\n")
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
    
def run(email=None,password=None,Domain=domain,Record=record):
    public_dic["login_email"]=email or public_dic["login_email"]
    public_dic["login_password"]=password or public_dic["login_password"]
    domain=Domain
    record=Record
    try:
        newIP=getMyIp()
        oldIP=readIP()
        if oldIP==newIP:
            return
        domainID=getDomainID()
        if domainID==0:
            return
        recordID=getRecordID(domainID)
        if recordID==0:
            return
        setDDNS(domainID,recordID)
        saveIP(newIP)
        WriteLog("new ip="+newIP)
    except Exception, e:
        WriteLog("has a ERROR:"+e.strerror)
if __name__ == '__main__':
    if len(sys.argv)==2:
        public_dic["login_code"]=sys.argv[1]
        print 'reading cfg...'
        readcfg()
    if len(sys.argv) >=5:
        if len(sys.argv) ==6:
            public_dic["login_code"]=sys.argv[5]
        public_dic["login_email"]=sys.argv[1]
        public_dic["login_password"]=sys.argv[2]
        domain=sys.argv[3]
        record=sys.argv[4]
    if isCron:
        run()
        exit()
    while True:
        try:
            newIP=getMyIp()
            if ip !=newIP:
                domainID=getDomainID()
                if domainID!=0:
                    recordID=getRecordID(domainID)
                    if recordID !=0:
                        setDDNS(domainID,recordID)
                        ip=newIP
                        WriteLog("new ip="+ip)
                        pass
        except Exception, e:
            WriteLog("has a ERROR:"+e.strerror)
        time.sleep(sleepTime)
    pass
    
