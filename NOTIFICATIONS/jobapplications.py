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


def setDriverOptions():
    options = Options()
    options.binary_location="/usr/bin/chromium-browser"
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
    for receiver in receivers:
        try:
            print ("sending mail to "+receiver)
            server.sendmail(sender,receiver,msg)
            print("mail sent")
            time.sleep(11)
        except:
            print('Error sendnig mail to '+receiver)
    server.quit()
def showNewJobs(newComp):
    for new in newComp:
        subprocess.Popen(['notify-send',"New companies to APPLY",new])
def main():
    driver,uname2,gocode2=refreshSession()
    url="http://placement.iitk.ac.in/jobapplications/"
    prev="nothing"
    prevComp=[]
    i=0
    receivers=getReceivers()
    prevComp=[]
    s=datetime.datetime.now()
    while True:
        try:
            driver.get(url)
            page_source=driver.page_source
            soup=BeautifulSoup(page_source,'html.parser')
            updates=soup.findAll("tr")
            newComp=[]
            for rows in updates[1:]:
                if str(rows.find("td"))[4:-5] not in prevComp:
                    newComp.append(str(rows.find("td"))[4:-5])
            if len(newComp)>0 and i!=0:
                print (newComp)
                msg="\n".join(newComp)
                msg="\n\n New companies to APPLY\n\n"+msg
                showNewJobs(newComp)
                sendMailToAll(msg,uname2,gocode2,receivers)
            else:
                print("No new Jobs.")
                i=1
            prevComp=prevComp+newComp
            print("Time elapsed : ",datetime.datetime.now()-s,"Time now : ",datetime.datetime.now())
            time.sleep(60)
        except:
            i=0
            print("Connection  Failed !!!")
            driver,uname2,gocode2=refreshSession()
if __name__=="__main__":
    main()
