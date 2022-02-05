#coding=utf-8
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



import sys, os
acl='\033[1;30m'
rcl='\033[1;31m'
ycl='\033[1;33m'
ncl='\033[0;00m'
maoversys=sys.version_info[0]==3
if maoversys:
  pass
else:
  exit("\n{acl}[ {rcl}! {acl}]{ycl} USE PYTHON 3.6+ {acl}[ {rcl}!{acl} ]{ncl}\n".format(acl=acl,rcl=rcl,ycl=ycl,ncl=ncl))
try:
  import os,time
except Exception as emao:
  exit("\n{acl}[ {rcl}FILE ERROR TYPE : {acl}]{ycl}  {emao} {acl}[ {rcl}!{acl} ]{ncl}\n".format(acl=acl,rcl=rcl,ycl=ycl,ncl=ncl,emao=emao))
try:
  from core.logos import *
  from core.ccchk import *
except Exception as emao:
  exit("\n{acl}[ {rcl}FILE ERROR TYPE : {acl}]{ycl}  {emao} {acl}[ {rcl}!{acl} ]{ncl}\n".format(acl=acl,rcl=rcl,ycl=ycl,ncl=ncl,emao=emao))
  
manu="""
{acl}[ {ycl}1. {acl}] {gcl}SMS_BOMBING
{acl}[ {ycl}2. {acl}] {gcl}CALL AND SMS_BOMBING
{acl}[ {ycl}3. {acl}] {gcl}EMAIL BOMBING
{acl}[ {ycl}4. {acl}] {gcl}MAO_VIRUS (FB PAGE)
{acl}[ {ycl}5. {acl}] {gcl}THBD (FB GROUP)
{acl}[ {rcl}0. {acl}] {rcl}EXIT
""".format(acl=acl,gcl=gcl,ncl=ncl,rcl=rcl,ycl=ycl)
try:
  while True:
    
    os.system("clear")
    print(logomao)
    
    print(manu)
    mao=input('{ccl} ====>>{ycl} '.format(ccl=ccl,ycl=ycl))
    if mao=="1":
      os.system('clear')
      print(logomao)
      cc=input('{acl}>{mcl}>{acl}> {gcl}ENTER COUNTRY CODE {acl}:{ycl}'.format(acl=acl,mcl=mcl,gcl=gcl,ycl=ycl))
      if cc.startswith("+"):
        cc=cc.replace("+","")
      else:
        pass
  
      number=input('{acl}>{mcl}>{acl}>{gcl} ENTER NUMBER {acl}:{ycl}'.format(acl=acl,mcl=mcl,gcl=gcl,ycl=ycl))
      get_phone_info(cc,number)
      threat=input('{acl}>{mcl}>{acl}>{gcl} ENTER BOMBING LIMIT{acl}({pcl}MAX{acl}={gcl}1000{acl}) {acl}:{ycl}'.format(acl=acl,gcl=gcl,pcl=pcl,ycl=ycl,mcl=mcl))
      if int(threat) <=1000:
          pass
      else:
          exit("{acl}[{rcl} !{acl} ] {rcl}BOMBING LIMIT 1000 {acl}[{rcl} !{acl} ]\n".format(acl=acl,rcl=rcl))
      os.system('python tbomb.py --bombing sms --cc {cc} --number {number} --threat {threat}'.format(cc=cc,number=number,threat=threat))
      
      break
    elif mao=="2":
      os.system('clear')
      print(logomao)
      cc=input('{acl}>{mcl}>{acl}> {gcl}ENTER COUNTRY CODE {acl}:{ycl}'.format(acl=acl,mcl=mcl,gcl=gcl,ycl=ycl))
      if cc.startswith("+"):
        cc=cc.replace("+","")
      else:
        pass
  
      number=input('{acl}>{mcl}>{acl}>{gcl} ENTER NUMBER {acl}:{ycl}'.format(acl=acl,mcl=mcl,gcl=gcl,ycl=ycl))
      get_phone_info(cc,number)
      threat=input('{acl}>{mcl}>{acl}>{gcl} ENTER BOMBING LIMIT{acl}({pcl}MAX{acl}={gcl}1000{acl}) {acl}:{ycl}'.format(acl=acl,gcl=gcl,pcl=pcl,ycl=ycl,mcl=mcl))
      if int(threat) <=1000:
          pass
      else:
          exit("{acl}[{rcl} !{acl} ] {rcl}BOMBING LIMIT 1000 {acl}[{rcl} !{acl} ]\n".format(acl=acl,rcl=rcl))
      os.system('python tbomb.py --bombing sms_call --cc {cc} --number {number} --threat {threat}'.format(cc=cc,number=number,threat=threat))
      break
    elif mao =="3":
      os.system('clear')
      print(logomao)
      mails=input('{acl}>{mcl}>{acl}>{gcl} ENTER MAIL {acl}:{ycl}'.format(acl=acl,mcl=mcl,gcl=gcl,ycl=ycl))
      threat=input('{acl}>{mcl}>{acl}>{gcl} ENTER BOMBING LIMIT{acl}({pcl}MAX{acl}={gcl}1000{acl}) {acl}:{ycl}'.format(acl=acl,gcl=gcl,pcl=pcl,ycl=ycl,mcl=mcl))
      if int(threat) <=1000:
          pass
      else:
          exit("{acl}[{rcl} !{acl} ] {rcl}BOMBING LIMIT 1000 {acl}[{rcl} !{acl} ]\n".format(acl=acl,rcl=rcl))
            
      os.system('python tbomb.py --bombing mail --mail {mail} --threat {threat}'.format(mail=mails,threat=threat))
      break

    elif mao =="4":
      os.system('xdg-open https://www.facebook.com/mao2116/')
      break
    elif mao=="5":
      os.system('xdg-open https://www.facebook.com/groups/242589267650518/?ref=share')
      break
    elif mao=="0":
      exit('{acl}[{gcl} ! {acl}]{rcl} THANKS FOR USING THIS TOOL {acl}[ {gcl}!{acl} ]'.format(acl=acl,gcl=gcl,rcl=rcl))
    else:
      print('{acl}[{rcl} !{acl} ]{rcl} WRONG SELECTION {acl}[ {rcl}! {acl}]{ncl}'.format(acl=acl,rcl=rcl,ncl=ncl))
      time.sleep(1)
    
except KeyboardInterrupt:
  exit('\n{acl} [{rcl} !{acl} ]{rcl} ABORTING... {acl}[{rcl} !{acl} ]\n'.format(acl=acl,rcl=rcl))
except Exception as emao:
  exit("\n{acl}[ {rcl} ERROR TYPE : {acl}]{ycl}  {emao} {acl}[ {rcl}!{acl} ]{ncl}\n".format(acl=acl,rcl=rcl,ycl=ycl,ncl=ncl,emao=emao))
