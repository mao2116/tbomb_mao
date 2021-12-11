acl='\033[1;30m'
rcl='\033[1;31m'
ycl='\033[1;33m'
ncl='\033[0;00m'
import json
def maocc1():
  try:
    
    mao=open("core/cc_codes_mao.json","r")
    mao=json.load(mao)
    mao=mao["MAOCC_CODES"]
    return mao
  except Exception as emao:
    exit("\n{acl}[ {rcl}FILE ERROR TYPE : {acl}]{ycl}  {emao} {acl}[ {rcl}!{acl} ]{ncl}\n".format(acl=acl,rcl=rcl,ycl=ycl,ncl=ncl,emao=emao))


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
   


def mailtypechk(mail):
  if "@gmail.com" in mail:
    return "GMAIL"
  elif "@yahoo.com" in mail :
    return "YAHOO MAIL"
  elif "@outlook.com" in mail :
    return "OUTLOOK MAIL"
  else:
    return "NONE"
    