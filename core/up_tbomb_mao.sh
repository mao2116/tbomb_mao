##########################################################
# DEV : MAO2116
# Github : https://github.com/mao2116
# IF YOU WANNA TAKE CREADITS FOR THIS TOOL,,,LOOK YOUR SELF AGAIN AND AGAIN,,

# THANKS TO ALLAH
# WELCOME HOME
# 
#####################৳৳৳৳৳৳৳৳৳৳৳৳৳৳৳৳৳৳৳৳৳################









a='\033[1;30m'
rc='\033[1;31m'
g='\033[1;32m' 
y='\033[1;33m'
b='\033[1;34m'
p='\033[1;35m'
c='\033[1;36m' 
w='\033[1;37m'
m='\033[1;94m'
n='\033[0;00m' 

logo(){
  clear
  echo -e "${y} _____ _   _ ${c} ____  ____  ${g}   ____   ___  __  __ ${g}THBD${n}  "
  echo -e "${y}|_   _| | | |${c}| __ )|  _ \ ${g}  | __ ) / _ \|  \/  | __ ) "
  echo -e "${y}  | | | |_| |${c}|  _ \| | | | ${g} |  _ \| | | | |\/| |  _ \ "
  echo -e "${y}  | | |  _  |${c}| |_) | |_| |${g}  | |_) | |_| | |  | | |_) |"
  echo -e "${y}  |_| |_| |_|${c}|____/|____/${g}___|____/ \___/|_|  |_|____/ "
  echo -e "                      |_${p}MAO${g}_|                        "
echo 
echo 
echo


echo -e "                  \033[1;30m[ \033[1;34mAUTHER \033[1;30m] \033[1;32mTERMUX \033[1;32mHACKER\033[1;31m BD"
echo -e "                  \033[1;30m[\033[1;34m GITHUB\033[1;30m ] \033[1;34mMAO2116"
echo -e "                  \033[1;30m[ \033[1;34mCODER \033[1;30m ] \033[1;30mMAO2116 "

}
logo
update(){
  echo -e "${p} A UPDATE AVAILABLE"
  sleep 0.1
  echo -e "${m} TBOMB_MAO IS UPDATING"
  sleep 1
  xdg-open https://www.facebook.com/mao2116/
  echo -e "${b} PLEASE WAIT..." 
  cd ; 
  rm -rf tbomb_mao ; 
  apt update ; 
  apt install python -y ; 
  apt install curl -y ; 
  pip install requests ; 
  curl https://codeload.github.com/mao2116/tbomb_mao/zip/refs/heads/main --output mao.zip ; 
  unzip mao.zip ; 
  rm -rf mao.zip ; 
  mv tbomb_mao-main tbomb_mao

  echo
  echo -e "${g} NOW YOUR TOOL UPDATED."
  echo
  echo -e "${y} THANKS FOR UPDATE ME."
  echo
  echo -e "${g}<==> NOW TYPE <==>"
  echo
  echo -e "${b} cd ; cd tbomb_mao ; python tbomb_mao.py${n}" ;
  sleep 3


}
update
echo 
echo
exit





##########################################################
# DEV : MAO2116
# Github : https://github.com/mao2116
# IF YOU WANNA TAKE CREADITS FOR THIS TOOL,,,LOOK YOUR SELF AGAIN AND AGAIN,,
# THANKS TO ALLAH
# WELCOME HOME
# MAO2116
#####################৳৳৳৳৳৳৳৳৳৳৳৳৳৳৳৳৳৳৳৳৳################
