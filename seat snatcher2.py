#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 12 14:28:52 2018

@author: connorvhennen
"""

#Disclaimer: Set up this at like 2 am for a freind so it's not the cleanest, 
#but it works

#Depencies: Python 2.7, twilio, apscheduler, internet, a twilio account,
#registered numbers on that account

#pip install twilio
from twilio.rest import Client 
import urllib2
import re
import copy
#conda install -c conda-forge apscheduler 
from apscheduler.schedulers.blocking import BlockingScheduler

#Create a Twilio Account and set SID and Token to the values assigned to your account

accountSID = 'AC8fed5af1cc7XXXXXXXXXXXXXXXXX'
authToken = '948c845624585XXXXXXXXXXXXXXXXX'
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
        clas = clas[0].split("Spring 2018")
        #classTitle= re.sub(r'/','',clas[1])
        #print clas[1]
        classTitle= re.sub(r'<.+?>','',clas[1])
        #print classTitle
        classTitle= re.sub(r'  ',' ',classTitle)
        return "There are " + spots[0] + " of " + spots[1] + " spots remaining in: " +  classTitle[:-1]

    else:
        clas = copy.deepcopy(page)
        
        clas = re.sub("real-time","",clas)
        clas = re.sub("\s+"," ",clas)
        clas = clas.split("Lecture")
        clas = clas[0].split("Spring 2018")
        #classTitle= re.sub(r'/','',clas[1])
        #print clas[1]
        classTitle= re.sub(r'<.+?>','',clas[1])
        #print classTitle
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




#seth = "+15104149301"
#jack = "+14084728462"
#tanner = "+7074786389"
#sami = "+7074788486"
me = "+17073277984"
musk = "+13109136851"
mom = "+17074902362"
rios = "+16194149537"
jackie = "+14084728462"
mom = "+17074902362"

#DEFINING SETH's 16 LECTURES TO BE MONITORED
class1 = 'https://sa.ucla.edu/ro/Public/SOC/Results/ClassDetail?term_cd=18S&subj_area_cd=ECON%20%20%20&crs_catlg_no=0106G%20%20%20&class_id=180420201&class_no=%20002%20%20'
class2 = 'https://sa.ucla.edu/ro/Public/SOC/Results/ClassDetail?term_cd=18S&subj_area_cd=ECON%20%20%20&crs_catlg_no=0106G%20%20%20&class_id=180420200&class_no=%20001%20%20'
class3 = 'https://sa.ucla.edu/ro/Public/SOC/Results/ClassDetail?term_cd=18S&subj_area_cd=ECON%20%20%20&crs_catlg_no=0122%20%20%20%20&class_id=180432200&class_no=%20001%20%20'
class4 = 'https://sa.ucla.edu/ro/Public/SOC/Results/ClassDetail?term_cd=18S&subj_area_cd=ECON%20%20%20&crs_catlg_no=0019%20%20%20%20&class_id=180057203&class_no=%20003%20%20'
class4 = 'https://sa.ucla.edu/ro/Public/SOC/Results/ClassDetail?term_cd=18S&subj_area_cd=BIOSTAT&crs_catlg_no=0100A%20%20%20&class_id=135300200&class_no=%20001%20%20'
#pic16_a
class5 = 'https://sa.ucla.edu/ro/Public/SOC/Results/ClassDetail?term_cd=18S&subj_area_cd=COMPTNG&crs_catlg_no=0016%20%20%20%20&class_id=157048200&class_no=%20001%20%20'
#pic16_b
class6 = 'https://sa.ucla.edu/ro/Public/SOC/Results/ClassDetail?term_cd=18S&subj_area_cd=COMPTNG&crs_catlg_no=0016%20%20%20%20&class_id=157048210&class_no=%20002%20%20'
#pic10c
class7 = 'https://sa.ucla.edu/ro/Public/SOC/Results/ClassDetail?term_cd=18S&subj_area_cd=COMPTNG&crs_catlg_no=0010C%20%20%20&class_id=157052200&class_no=%20001%20%20'
#pic10b (cuz I know it's openings)
class8 = 'https://sa.ucla.edu/ro/Public/SOC/Results/ClassDetail?term_cd=18S&subj_area_cd=COMPTNG&crs_catlg_no=0010B%20%20%20&class_id=157051200&class_no=%20001%20%20'
#pic20
class9 = 'https://sa.ucla.edu/ro/Public/SOC/Results/ClassDetail?term_cd=18S&subj_area_cd=COMPTNG&crs_catlg_no=0020A%20%20%20&class_id=157102200&class_no=%20001%20%20'
#pic40
class10 = 'https://sa.ucla.edu/ro/Public/SOC/Results/ClassDetail?term_cd=18S&subj_area_cd=COMPTNG&crs_catlg_no=0040A%20%20%20&class_id=157166200&class_no=%20001%20%20'
#cs32
class11 = 'https://sa.ucla.edu/ro/Public/SOC/Results/ClassDetail?term_cd=18S&subj_area_cd=COM%20SCI&crs_catlg_no=0032%20%20%20%20&class_id=187096200&class_no=%20001%20%20'
#open history upper div's no pre-reqs
class12 = 'https://sa.ucla.edu/ro/Public/SOC/Results/ClassDetail?term_cd=18S&subj_area_cd=HIST%20%20%20&crs_catlg_no=0105C%20%20%20&class_id=221315200&class_no=%20001%20%20'
class13 = 'https://sa.ucla.edu/ro/Public/SOC/Results/ClassDetail?term_cd=18S&subj_area_cd=HIST%20%20%20&crs_catlg_no=0109B%20%20%20&class_id=221343200&class_no=%20001%20%20'

#upper div rojas econ
class14 = 'https://sa.ucla.edu/ro/Public/SOC/Results/ClassDetail?term_cd=18S&subj_area_cd=ECON%20%20%20&crs_catlg_no=0144%20%20%20%20&class_id=180593200&class_no=%20001%20%20'

class15 = 'https://sa.ucla.edu/ro/Public/SOC/Results/ClassDetail?term_cd=18S&subj_area_cd=ECON%20%20%20&crs_catlg_no=0122%20%20%20%20&class_id=180432200&class_no=%20001%20%20'
class16 = 'https://sa.ucla.edu/ro/Public/SOC/Results/ClassDetail?term_cd=18S&subj_area_cd=ECON%20%20%20&crs_catlg_no=0112%20%20%20%20&class_id=180457200&class_no=%20001%20%20'



def sendMessage():
    '''
    Function that checks each given lecture URL and builds up a series of paragraphs
    (or just a super big string really)
    
    Returns: A string that contains the statuses of all classes that have room. It disregards those
    that do not, of course, because that would be a waste of a text.
    
    Note: You can use try and except statements so that it still works 
    with a number lower than 16
    '''

    check1 = checkEnrollment(class1)

    

    check2 = checkEnrollment(class2)

    
    
    check3 = checkEnrollment(class3)
    ##except:
        #check3 = 'Err'
        #print 'Error for class3'

    ##try:
    check4 = checkEnrollment(class4)
    ##except:
        #check4 = 'Err'
        #print 'Error for class4'
        
        
    ##try:
    check5 = checkEnrollment(class5)
    ##except:
        #check5 = 'Err'
        #print 'Error for class5'
        
    ##try:
    check6 = checkEnrollment(class6)
    ##except:
        #check6 = 'Err'
        #print 'Error for class6'
        
    
    check7 = checkEnrollment(class7)
    ##except:
        #check7 = 'Err'
        #print 'Error for class7'
        
    #try:
    check8 = checkEnrollment(class8)
    #except:
        #check8 = 'Err'
        #print 'Error for class8'
    #try:
    check9 = checkEnrollment(class9)
    #except:
        #check9 = 'Err'
        #print 'Error for class9'
    
    #try:
    check10 = checkEnrollment(class10)
    #except:
        #check10 = 'Err'
        #print 'Error for class10'
    
    #try:
    check11 = checkEnrollment(class11)
    #except:
        #check11 = 'Err'
        #print 'Error for class11'

    #try:
    check12 = checkEnrollment(class12)
    #except:
        #check12 = 'Err'
        #print 'Error for class12'
        
        
    ##try:
    check13 = checkEnrollment(class13)
    ##except:
        #check13 = 'Err'
        #print 'Error for class13'
        
    ##try:
    check14 = checkEnrollment(class14)
    ##except:
        #check14 = 'Err'
        #print 'Error for class14'
        
    ##try:
    check15 = checkEnrollment(class15)
    ##except:
        #check15 = 'Err'
        #print 'Error for class15'
        
    ##try:
    check16 = checkEnrollment(class16)
    ##except:
        #check16 = 'Err'
        #print 'Error for class16'
    
    
    checks = [check1,check2,check3,check4,check5,check6,check7,check8,check9,check10,check11,check12,check13,check14,check15,check16]
    
    #for i in range(0,len(checks)+1):
        #if checks[i] == 'Err':
            #checks[i] = 'Waitlist Full'
    
    result = ''
    
    for i in range(0,len(checks)):
        if 'Waitlist Full' in checks[i] or 'No Waitlist' in checks[i]:
            a = 1
        else: 
            if len(result) > 0:
                result += '\n\n' + checks[i]
            else:
                result = checks[i]
    return result
            

def shootIt():
    '''
    Input: Not really an input (see line 265), but where it says "to=rios" on
    line 264, that's where you can change ur input param. Which is a string 
    (a phone number with a + in front)
    
    Also this isn't actually a necessary function; I was just trouble
    shooting to all hell and it turned out to be a wi-fi issue.
    '''
    news = sendMessage()
    if len(news) == 0:
        return
    else:
        message = client.messages.create(
                to=mom,from_="+17073293214", body= news)
    
#There's a way to allow for input paramaters in apscheduling but it
#asn't worth it in this case.
scheduler = BlockingScheduler()
scheduler.add_job(shootIt, 'interval', seconds = 5)
scheduler.start()

#NOTE: Generally a student would scan for like 1 or just a few classes, 
#get alerted and then unsubscribe. This might seem spammy now, but 
#that's because I purposefully chose classes I knew to be open 
#so as to prove the concept



