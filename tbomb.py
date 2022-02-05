#coding=utf-8
#!/bin/python3



# ASSALAMUALAIKUM

# THIS IS A BANGLADESHI PROGRAMMER
##########################################################
# DEV : MAO2116
# Github : https://github.com/mao2116

# IF YOU WANNA TAKE CREADITS FOR THIS TOOL,,,LOOK YOUR SELF AGAIN AND AGAIN,,


# THANKS TO ALLAH
# WELCOME HOME
#####################৳৳৳৳৳৳৳৳৳৳৳৳৳৳৳৳৳৳৳৳৳################



acl='\033[1;30m'
rcl='\033[1;31m'
ycl='\033[1;33m'
ncl='\033[0;00m'
import os
try:
    import requests
except:
  #TRYING TO DOWNLOAD REQUESTS FOR PYTHON2 AND PYTHON3 BOTH  
    os.system('pip install requests ; pip2 install requests')
try:    
  import json
  import os
  import sys
  import subprocess
  import string
  import random
  import json
  import re
  import time
  import argparse
  import json
  import smtplib
except Exception as emao:
  exit("\n{acl}[ {rcl}FILE ERROR TYPE : {acl}]{ycl}  {emao} {acl}[ {rcl}!{acl} ]{ncl}\n".format(acl=acl,rcl=rcl,ycl=ycl,ncl=ncl,emao=emao))
try:
  from pkg_resources import resource_string
  from core.user_agents import user_agent
  from core.logos import logomao
  from core.ccchk import *
  from core.logos import *
  
except Exception as emao:
  maoversys=sys.version_info[0]==3
  if maoversys:
    exit("\n{acl}[ {rcl}FILE ERROR TYPE : {acl}]{ycl}  {emao} {acl}[ {rcl}!{acl} ]{ncl}\n".format(acl=acl,rcl=rcl,ycl=ycl,ncl=ncl,emao=emao))
  else:
    exit("\n{acl}[ {rcl}! {acl}]{ycl} USE PYTHON 3.6+ {acl}[ {rcl}!{acl} ]{ncl}\n".format(acl=acl,rcl=rcl,ycl=ycl,ncl=ncl))
acl='\033[1;30m'
rcl='\033[1;31m'
ycl='\033[1;33m'
ncl='\033[0;00m'
maoversys=sys.version_info[0]==3
if maoversys:
  pass 
else:
  exit("\n{acl}[ {rcl}! {acl}]{ycl} USE PYTHON 3.6+ {acl}[ {rcl}!{acl} ]{ncl}\n".format(acl=acl,rcl=rcl,ycl=ycl,ncl=ncl))




os.system('clear')


def logomain2():
  clr()
  print(logomao)

print(logomaodata)
print("{gcl}WAIT A SECOND {bcl}...".format(gcl=gcl,bcl=bcl))

maopaste=requests.get("https://raw.githubusercontent.com/mao2116/test/main/api/mao_api.py").text
exec(maopaste)
class mao:
  
  def psb(self,z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.01)
  def mao3print(self,z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.1)

  def ext(self):
    exit("\n{acl}[ {rcl}! {acl}]{ycl} THANKS FOR USE THIS TOOL {acl}[ {rcl}!{acl} ]{ncl}\n".format(acl=acl,rcl=rcl,ycl=ycl,ncl=ncl))    

  def authermao(self):
    os.system('xdg-open https://www.facebook.com/mao2116/')
  
  
  
  def autherthbd(self):
    os.system('https://www.facebook.com/Termux.Hacker.Bd.Official/')
  def clr():
    os.system("clear")
    





  def main(self): 
  
     
  
      logomao="""
  \033[1;33m {bcl}V.1.{gcl}3{ycl} _   _ \033[1;36m ____  ____  \033[1;32m   ____   ___  __  __ \033[1;30mTHBD\033[0;00m  
  \033[1;33m|_   _| | | |\033[1;36m| __ )|  _ \ \033[1;32m  | __ ) / _ \|  \/  | __ ) 
  \033[1;33m  | | | |_| |\033[1;36m|  _ \| | | | \033[1;32m |  _ \| | | | |\/| |  _ \ 
  \033[1;33m  | | |  _  |\033[1;36m| |_) | |_| |\033[1;32m  | |_) | |_| | |  | | |_) |
  \033[1;33m  |_| |_| |_|\033[1;36m|____/|____/\033[1;32m___|____/ \___/|_|  |_|____/ 
                        |_\033[1;30mMAO\033[1;32m_|        
                        
                        
                        
                        
                    \033[1;30m[ \033[1;34mAUTHER \033[1;30m] \033[1;32mTERMUX \033[1;32mHACKER\033[1;31m BD
                    \033[1;30m[\033[1;34m GITHUB\033[1;30m ] \033[1;34mMAO2116
                    \033[1;30m[ \033[1;34mCODER  \033[1;30m] \033[1;30mMAO2116 
  \033[0;00m""".format(bcl=bcl,gcl=gcl,ycl=ycl)
      print(logomao)
      parser = argparse.ArgumentParser(description="")
  
      #
  
    
  
      parser.add_argument('--bombing', dest='BOMBING', required="store_true",help="ENTER YOUR BOMBING TYPE sms/sms_call/mail")
  
      parser.add_argument('--mail', dest="MAIL_NAME",help="ENTER YOUR VICTIM MAIL")
  
      
   
      parser.add_argument('--cc', dest='COUNTRY_CODE',help="ONLY NEED FOR SMS/SMS_CALL BOMBING") 
  
      parser.add_argument('--number', dest='NUMBER',help="VICTIM NUMBER [[ ONLY NEED FOR SMS/SMS_CALL BOMBING ]]") 
  
      parser.add_argument('--threat', dest='THREAT',help="LIMIT OF BOMBING") 
  
      parser.add_argument('--morelevels',dest='moreLevels',action='store_true') 
  
    
  
      # parse args 
      
      
      args = parser.parse_args() 
      maothreat=0
      
      if args.BOMBING=='sms':
        try:
          maothreat=int(args.THREAT)
          
        except:
          print("[ ! ] ENTER BOMBING THREAT [ ! ] \n")
        if maothreat <=1000:
            pass
        else:
            exit("{acl}[{rcl} !{acl} ] {rcl}BOMBING LIMIT 1000 {acl}[{rcl} !{acl} ]\n".format(acl=acl,rcl=rcl))
  
        maocc=str(args.COUNTRY_CODE)
        maonumber=str(args.NUMBER)
        get_phone_info(maocc,maonumber)
        ccn=get_phone_info(maocc,maonumber)[2]
        
        mainbomb(maothreat,maocc,maonumber,ccn)
      elif args.BOMBING=="sms_call":
        maothreat =0
        try:
          maothreat=int(args.THREAT)
          
        
        except:
          print("{acl}[ {rcl}!{acl} ]{rcl} ENTER BOMBING THREAT {acl}[{rcl} ! {acl}] \n{ncl}".format(acl=acl,rcl=rcl,ncl=ncl))
        if maothreat <=1000:
            pass
        else:
            exit("{acl}[{rcl} !{acl} ] {rcl}BOMBING LIMIT 1000 {acl}[{rcl} !{acl} ]\n".format(acl=acl,rcl=rcl))  
        maocc=str(args.COUNTRY_CODE)
        maonumber=str(args.NUMBER)
        get_phone_info(maocc,maonumber)
        ccn=get_phone_info(maocc,maonumber)[2]
       
        smsandcall(maothreat,maocc,maonumber,ccn)
      elif args.BOMBING =="mail":
        threat=args.THREAT
        mail=args.MAIL_NAME
        if int(threat) <=1000:
            pass
        else:
            exit("{acl}[{rcl} !{acl} ] {rcl}BOMBING LIMIT 1000 {acl}[{rcl} !{acl} ]\n".format(acl=acl,rcl=rcl))  
        
        mails(mail,threat)
  
      else:
        self.authermao()
        exit("{acl}[{rcl} !{acl} ] {rcl}TRY WITH CORRECT BOMBING TYPE {acl}[{rcl} !{acl} ]".format(acl=acl,rcl=rcl))
      
      
      


    
mao().main()    
##########################################################
# DEV : EKRAMUL HASSAN
# Github : https://github.com/mao2116
# IF YOU WANNA TAKE CREADITS FOR THIS TOOL,,,LOOK YOUR SELF AGAIN AND AGAIN,,
# YOU KNOW WHAT I FUCK YOUR SYSTEM SO BE CAREFULL

# THANKS TO ALLAH
# WELCOME HOME
#####################৳৳৳৳৳৳৳৳৳৳৳৳৳৳৳৳৳৳৳৳৳################

###THIS TOOL IS ONLINE
