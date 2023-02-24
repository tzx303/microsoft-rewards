import requests
import random
import time

def random_str(length): 
    # 生成随机字符串 
    str = '' 
    chars = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789' 
    length = len(chars) - 1 
    random = Random() 
    for i in range(length): 
        str+=chars[random.randint(0, length)] 
    return str 
 
#打印随机字符串
print(random_str(8))
url = "https://bing.com/search?q="
headers = {
  ":authority":" cn.bing.com",
  ":method":" GET",
  ":path":" /?scope=web&FORM=QBLH",
  ":scheme":" https",
  "accept":" text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
  "accept-encoding":" gzip, deflate, br",
  "accept-language":" zh-CN,zh;q=0.9,en;q=0.8",
  "cache-control":" max-age=0",
  "cookie: MUID=035054D26EEA663138CF466F6AEA602A; MSCC=cid=t7pb6moz15syrs0qdzscrsgv-c1=2-c2=2-c3=2; SRCHD=AF=NOFORM; SRCHUID=V=2&GUID=E9514AE7A45C4A8E8FB0FE51BC70228A&dmnchg=1; ANON=A=ABE3FA32E2805DC26D5301AAFFFFFFFF&E=1c01&W=1; NAP=V=1.9&E=1ba7&C=g3nDTwDY8Q7EbQX8KH6FgryuhQTHu5kfqk0ZL1UYAA0MNo8gk6Sj6Q&W=1; PPLState=1; KievRPSSecAuth=FABqBBRaTOJILtFsMkpLVWSG6AN6C/svRwNmAAAEgAAACGVs76jV+N5RKAR9APyliSkqlO4PwIXhoexWicf9FWiYWZFEsOph64npQiLU3jOTV9SB9Apjz7anKucQ5x2CD7SBqI4Kjst7p1A1E1JC3bhPLWCJCONokl9eMcemnGKizeG49OBHP4tCJiO2AMM26BmByZ/FBjQAm/3YW/byhi4blXnGsax/nppNd73jv/mxb5fnItmqxbEWuSYF3iC8Bsvu2GQNKLhDj87rcoS+zykAeSNHF0OIlVspzoVM/1+z+W+0AxtpwAbKYJj8FMeNFequp+9WotsFZBGMon1JWtv8F6/tAt9VqrTllgT8FK5uVV6FF8pzeIR5aTQeHpHns1Od7m6Kl2noqsdW1nGOsvM4hpOn5AQMD2pVIJbrS3WP2gk9j76GfZ8VqVZNlc3DU4wMKI2Vyh0k8uFMOhn/FuJ//uJbng5PWKE+KkQqPmMvP6P6Ge4guIy5Dx4WHJ4Y9GN3UQ9RlAqaVzeOU0sQfsvEKiSf45WSCqiZRXDFFiIyE00KMuQy351M6RMxPzGxkpX3x3jTvP5LzjZcAvQaJUV1fYvP8DGWSRoaib5tmB53a1JMcaPgs1piLTUymgwpnMtwl8z4Y5ywNKKfrXSb9jIA/iDDqU2vpQfmRSRuVWpkocgdcSCaGiOu6woUiZ2wsEuwB8spWV+HScK5KSGGcmFFvt5RL3Gz4AJujnKb5gzIb8nAHYvsXMpvCCoWNEWmIyfyFUzOTisViUalpd27V+IqSeMK5HQzJbOt7WM9aKV/JuFdeljSaavKhZqhmDOhMeIduyahkFryeOIGVLo/ecAsNc3ZIvUxpb2b0rfIBYd2mkv5YJSA04JveRFHkxS0vom6GpjLujD0I4n0W1Osd/LjHe2ilLThFrEO7+6oXRS+/W2AMOzRWr8ILBYJ1osgzcs0wD40xIl/Wqe/Q/meCDwXHyAZAOTZpO8+GvGbqAftI1YtCjoWiYhPYQ/CR4XrmbPR1qWNjvv6x+A0oUHxGf1jgqfEucbm8I7D5uiLwS2dEcFNcjh1mcb75yiVwnKdtqrNwUvyRp6t4SSipweKNUmWWC4wV9LtjxvbSj/PB9DQl3Yg0Pg3uGomuuVZZcmsRLIV2KX2GP+mfzJzFcrBPYj9N+2slnZr6iGMcazqOVu8BEnpKrrYQM9JHLima5Xh8PUfW4+WgjYngdDWOoFQWshkcd1HBlpkPRnYxFx6N2B+ABaw4MqMATerTERx9Q7lKoZfnB9VZ6W9+5Bf9luIWo+5V5VUcP9sk6j3Y5Iv0p+W7HIYUwwHG/c5yMMXRWfZMFBVC4Psiakf45SNJOvN6vLnRRxgb5w6vg6NkJxfiyhSPdIotdMBETmLS1Mhjl6vqwMUFQ0vKqGC294UKfa3d4KyRwytJ/zSEaPYHXSzaCDbH8P4xVla757u7wqDXVsLPWWlKBQAG7kNR/Rw++RdeAkBqFdO2j+eYoc=; _U=1tn8CkP_pnjQH3CjJovHaTXuo9oPx42vd4db88kBTZAv7_DeVBjdqXzkhij5FlqBKZc3EI0YsU8aCcTtc45OTfHVlvvKdEmqDtYE0ZxHyGHjJ7asKvvZH6bnPs5ub2aCw2O9o4OunWoYcK9bPgt7sgIefhsgShBY5_wRAeELDKh7vJ3rGhKVJnBqyonrMMkBXZOu5gCwQCGrZLcFb_-kkgA; WLS=C=fda18e21fb883bb5&N=tzx; WLID=5jVZfeI/PfBgmLL2uTboMSMjcPEOoS4yFbzOWdS3hT3+08bODvwU8bJn73ssKu8MOUg1beEELu9S2OSzL41c+t67geGjiEJdkXoX+ifLVI8=; SUID=A; BFBUSR=BAWAS=1&BAWFS=1; BFB=AhCu0Mu_QK1bZ--Jb6as8QpGCt2fDvixu_6rW1meD2P9edzk2cBLZVS7nKVM87kX8pMsR73tPj_tBK7aLaPc75eZ1JdhJPmlUaKX2dKiHm2xXLhsBBt2jchFH8aARchbsyoOISh__NHreCgwlJHDHpSGw_uChu4CUdXXt7XFhlcgug; _UR=QS=0&TQS=0; SRCHUSR=DOB=20230219&T=1676803986000&POEX=W&TPC=1676804003000; _clck=1l0bhrf|1|f99|1; MUIDB=035054D26EEA663138CF466F6AEA602A; ZHCHATSTRONGATTRACT=TRUE; ANIMIA=FRE=1; _uetsid=a45b0e50b04311edba21c1829fb6c22f; _uetvid=a45b3f60b04311ed8f2c3f0974c2a6ee; _EDGE_S=SID=0D2BF664A2906B15245EE4D9A3FA6A08&mkt=EN-US&ui=en-us; _clsk=1thxdlp|1676807818274|7|0|m.clarity.ms/collect; MicrosoftApplicationsTelemetryDeviceId=1c1b1669-e9da-4531-8d37-a16d0970eb53; ZHCHATWEAKATTRACT=TRUE; SnrOvr=X=rebateson; SNRHOP=I=&TS=; ABDEF=V=13&ABDV=11&MRNB=1676817048588&MRB=0; _SS=SID=0D2BF664A2906B15245EE4D9A3FA6A08&R=282&RB=282&GB=0&RG=1000&RP=282&OCID=ML2AHZ&BTQID=-&BTSTKey=-&RA=-&BTOID=-&BTQN=-&BTEC=-&BTMC=-&BTCQC=-&BTIOM=-&BTCO=-&BTRACI=-&BTTC=-; _HPVN=CS=eyJQbiI6eyJDbiI6MSwiU3QiOjAsIlFzIjowLCJQcm9kIjoiUCJ9LCJTYyI6eyJDbiI6MSwiU3QiOjAsIlFzIjowLCJQcm9kIjoiSCJ9LCJReiI6eyJDbiI6MSwiU3QiOjAsIlFzIjowLCJQcm9kIjoiVCJ9LCJBcCI6dHJ1ZSwiTXV0ZSI6dHJ1ZSwiTGFkIjoiMjAyMy0wMi0xOVQwMDowMDowMFoiLCJJb3RkIjowLCJHd2IiOjAsIkRmdCI6bnVsbCwiTXZzIjowLCJGbHQiOjAsIkltcCI6MTR9; ai_session=SqEbB7482aQqOPfPHxsxov|1676817054349|1676817054349; ipv6=hit=1676820654369&t=4; OID=AhCic4QiIzsxg-iLg8O0jdnHTXYolprYT78ByheT_CVjV8fdYfHBB7HA5B6y6W1jYBieSlLehzvfGPgjHAX1DJuD; OIDI=AhAEFlK-MKOxtRjaHvpZoqYlkTSu5qlZc0WKqYLGLjORLA; _RwBf=ilt=1&ihpd=0&ispd=0&rc=282&rb=282&gb=0&rg=1000&pc=282&mtu=0&rbb=0.0&g=0&cid=&clo=0&v=102&l=2023-02-19T08:00:00.0000000Z&lft=0001-01-01T00:00:00.0000000&aof=0&o=0&p=WINDOWSBARACQ201902&c=M5001O&t=361&s=2023-02-19T10:50:51.6781062+00:00&ts=2023-02-19T14:30:54.9483560+00":"00&rwred=0&wls=0&lka=0&lkt=0&TH=&r=1&mta=0&e=61mtn1rOEeGwi-9JVrI6HsZP5uWc5M5v2AYkPIQBra5ZP70EUkj0TsVJWWrcJM4CCB-JS_brbr13O8oY8m6M4b-vqJOc5fwkEIvQwaxqVE0&A=; SRCHHPGUSR=SRCHLANG=zh-Hans&PV=15.0.0&WTS=63812400786&BRW=W&BRH=S&CW=1440&CH=280&SCW=1423&SCH=280&DPR=1.5&UTC=480&DM=0&HV=1676817054&PRVCW=1440&PRVCH=809&BZA=0",
  "referer: https":"//cn.bing.com/?toWww=1&redig=0CA6BA91D5324B76A765BE5B8DBEE693",
  "sec-ch-ua":" "Chromium";v="110", "Not A(Brand";v="24", "Google Chrome";v="110"",
  "sec-ch-ua-arch":" "x86"",
  "sec-ch-ua-bitness":" "64"",
  "sec-ch-ua-full-version":" "110.0.5481.104"",
  "sec-ch-ua-full-version-list":" "Chromium";v="110.0.5481.104", "Not A(Brand";v="24.0.0.0", "Google Chrome";v="110.0.5481.104"",
  "sec-ch-ua-mobile":" ?0",
  "sec-ch-ua-model":" """,
  "sec-ch-ua-platform":" "Windows"",
  "sec-ch-ua-platform-version":" "15.0.0"",
  "sec-fetch-dest":" document",
  "sec-fetch-mode":" navigate",
  "sec-fetch-site":" same-origin",
  "sec-fetch-user":" ?1",
  "upgrade-insecure-requests":" 1",
  "user-agent":" Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36"
  }
while True:                                                                        
  req = requests.get(url=url+random_str(random.randint(3,16)),headers=headers).text
  time.sleep(random.uniform(3, 15))
