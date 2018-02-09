#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 13 00:37:14 2018

@author: connorvhennen
"""

from twilio.rest import Client
import urllib2
import re
import copy
from apscheduler.schedulers.blocking import BlockingScheduler

#Create a Twilio Account and set SID and Token to the values assigned to your account
#accountSID = 'AC0a40d144a0dxxxxxxxxxxxxxxxxx'
#authToken = 'c25c212d82a8017xxxxxxxxxxxxxxxxx'
client = Client(accountSID, authToken)

def checkEnrollment(url):
    page=urllib2.urlopen(url).read()
    page = str(page)
    if re.search(r'Open',page):
        page1 = page.split('Open:')
        page2 = page1[1].split(' Left')
        page2[0] = re.sub(" ","",page2[0])

        #spots = re.findall(r'(\d+)?(\s)?(of)?(\d+)(?<= Left)',page1[1])
        spots = page2[0].split('of')
    
        clas = copy.deepcopy(page)
        
        clas = re.sub("real-time","",clas)
        clas = re.sub("\s+"," ",clas)
        clas = clas.split("Lecture")
        clas = clas[0].split("Winter 2018")
        #classTitle= re.sub(r'/','',clas[1])
        classTitle= re.sub(r'<.+?>','',clas[1])
        classTitle= re.sub(r'  ',' ',classTitle)
        return "There are " + spots[0] + " of " + spots[1] + " spots remaining in: " +  classTitle[:-1]

    else:
        clas = copy.deepcopy(page)
        
        clas = re.sub("real-time","",clas)
        clas = re.sub("\s+"," ",clas)
        clas = clas.split("Lecture")
        clas = clas[0].split("Winter 2018")
        #classTitle= re.sub(r'/','',clas[1])
        classTitle= re.sub(r'<.+?>','',clas[1])
        classTitle= re.sub(r'  ',' ',classTitle)
        if re.search('Closed',page):
            page1 = page.split('Closed')[1]
            page2 = page1.split(' span3')[0]
            #page2 = re.sub(" ","",page2)
            waitlistSec = re.findall(r'<div.+?</div>',page2)[0]
            waitlist = re.findall(r'(?=<p>).+?(?<=</p>)',waitlistSec)[0]
            waitlist = re.sub(r'<.+?>','',waitlist)
        elif re.search('Waitlist',page):
            page1 = page.split('Class Full')[1]
            page2 = page1.split(' span3')[0]
            #page2 = re.sub(" ","",page2)
            waitlistSec = re.findall(r'<div.+?</div>',page2)[0]
            waitlist = re.findall(r'(?=<p>).+?(?<=</p>)',waitlistSec)[0]
            waitlist = re.sub(r'<.+?>','',waitlist)
        return 'The waitlist for ' +  classTitle[:-1] + ' is: ' + waitlist




me = "+17073277984"
jack = "+14084728462"
tanner = "+7074786389"
sami = "+7074788486"

pic16 = "https://sa.ucla.edu/ro/Public/SOC/Results/ClassDetail?term_cd=18W&subj_area_cd=COMPTNG&crs_catlg_no=0016%20%20%20%20&class_id=157048210&class_no=%20002%20%20"
pic10b= "https://sa.ucla.edu/ro/Public/SOC/Results/ClassDetail?term_cd=18W&subj_area_cd=COMPTNG&crs_catlg_no=0010B%20%20%20&class_id=157051200&class_no=%20001%20%20"

def sendMessage():
    news = checkEnrollment(pic10b)
    if 'Waitlist Full' in news or 'No Waitlist' in news:
        return
    else:
        message = client.messages.create(
                to=me,
                #from_="+14158952xxx", Enter the number assigned to your Twilio account
                body= news)
   
scheduler = BlockingScheduler()
scheduler.add_job(sendMessage, 'interval', seconds = 1)
scheduler.start()

    
