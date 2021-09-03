import os,time

from core.logos import *

manu=f"""
{acl}[ {ycl}1. {acl}] {gcl}SMS_BOMBING
{acl}[ {ycl}2. {acl}] {gcl}CALL AND SMS_BOMBING
{acl}[ {ycl}3. {acl}] {gcl}EMAIL BOMBING
{acl}[ {ycl}4. {acl}] {gcl}OUTLOOKMAIL BOMBING
{acl}[ {ycl}5. {acl}] {gcl}MAO_VIRUS (FB PAGE)
{acl}[ {ycl}6. {acl}] {gcl}THBD (FB GROUP)
{acl}[ {rcl}0. {acl}] {rcl}EXIT
"""
try:
  while True:
    
    os.system("clear")
    print(logomao)
    
    print(manu)
    mao=input(f'{ccl} ====>>{ycl} ')
    if mao=="1":
      os.system('clear')
      print(logomao)
      cc=input('ENTER COUNTRY CODE (WITH OUT +):')
      number=input('ENTER NUMBER :')
      threat=input('ENTER BOMBING LIMIT(MAX=1000) :')
      os.system(f'python tbomb.py --cc {cc} --number {number} --threat {threat}')
      break
    elif mao=="2":
      os.system('clear')
      print(logomao)
      cc=input('ENTER COUNTRY CODE (WITH OUT +):')
      number=input('ENTER NUMBER :')
      threat=input('ENTER BOMBING LIMIT(MAX=1000) :')
      os.system(f'python tbomb.py --bombing sms_call --cc {cc} --number {number} --threat {threat}')
      break
    elif mao =="3":
      os.system('python tbomb.py --bombing email')
      break
    elif mao =="4":
      os.system('python tbomb.py --bombing email')
      break
    elif mao =="5":
      os.system('xdg-open https://www.facebook.com/mAoVirUs2116/')
      break
    elif mao=="6":
      os.system('xdg-open https://www.facebook.com/groups/242589267650518/?ref=share')
      break
    elif mao=="0":
      exit('[ ! ] THANKS FOR USING THIS TOOL [ ! ]')
    else:
      print(f'{rcl}WRONG INPUT{ncl}')
      time.sleep(1)
    
except KeyboardInterrupt:
  print('\nABORTING...\n')