from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys

import datetime
import requests
import smtplib
import subprocess
import time
import traceback

def setDriverOptions():
    options = Options()
    options.binary_location =  "/usr/bin/chromium-browser"
    options.add_argument("--headless")
    return webdriver.Chrome(options=options)
def getCreds():
    f=open("creds","r")
    creds=[]
    for i in f:
        creds.append(i[:-1])
    uname1=str(creds[0])
    gocode1="".join(str(creds[1])[::-1].split("m"))
    uname2=str(creds[2])
    gocode2=int(str(creds[3]),2)
    return uname1,gocode1,uname2,gocode2
def getReceivers():
    f=open("receivers","r")
    receivers=[]
    for i in f:
        receivers.append(i[:-1])
    return receivers
def refreshSession():
    driver=setDriverOptions()
    driver.get("http://placement.iitk.ac.in")
    username = driver.find_element_by_id("id_username")
    password = driver.find_element_by_id("id_password")
    uname1,gocode1,uname2,gocode2=getCreds()
    username.send_keys(uname1)
    password.send_keys(gocode1)
    enter_attempt = driver.find_element_by_xpath("//*[@type='Submit']")
    enter_attempt.submit()
    return driver,uname2,gocode2
def sendMailToAll(msg,sender,code,receivers):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    server.login(sender,code)
    #print(msg)
    for receiver in receivers:
        try:
            print ("sending mail to "+receiver)
            server.sendmail(sender,receiver,msg)
            print("mail sent")
            time.sleep(11)
        except:
            print(traceback.format_exc())
            print('Error sendnig mail to '+receiver)
    server.quit()
def DashUpdates(dashList,dashMsgList,prevUpdate):
    k=0
    msg="\n\n**UPDATE**\n\n"
    while k<len(dashList) and dashList[k].text.strip()!=prevUpdate:
        subprocess.Popen(['notify-send',"UPDATE",dashList[k].text.strip()+"\n"+dashMsgList[k].text.strip()])
        msg=msg+"\n\nUPDATE #"+str(k)+"\n\n"+dashList[k].text.strip()+"\n"+dashMsgList[k].text.strip()
        k+=1
    return msg.encode('utf-8')
def main():
    driver,uname2,gocode2=refreshSession()
    url="http://placement.iitk.ac.in/dashboard/"
    prevUpdate="HarnessIo : Test"
    i=0
    receivers=getReceivers()
    s=datetime.datetime.now()
    while True:
        try:
            driver.get(url)
            page_source=driver.page_source
            soup=BeautifulSoup(page_source,'html.parser')
            dashList=soup.findAll("div",{"class":"col-sm-9"})
            dashMsgList=soup.findAll("div",{"class","panel-body news"})
            presUpdate=(dashList[0].text).strip()
            if prevUpdate!=presUpdate and i!=0:
                msg=DashUpdates(dashList,dashMsgList,prevUpdate)
                sendMailToAll(msg,uname2,gocode2,receivers)
            else:
                print("No new updates!!!")
                i=1
            prevUpdate=presUpdate
            print("Time elapsed : ",datetime.datetime.now()-s,"Time now : ",datetime.datetime.now())
            time.sleep(60)
        except:
            print(traceback.format_exc())
			while True:
				try:
					i=0
					print("Connection  Failed !!!")
            		driver,uname2,gocode2=refreshSession()
					break
				except:
					print(traceback.format_exc())
					pass
if __name__=="__main__":
    main()
