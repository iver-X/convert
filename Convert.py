#!/usr/bin/env python3
import requests, json, time, re, os

# Warna
KUNING = ('\x1b[1;93m')
MERAH = ('\x1b[1;91m')
HIJAU = ('\x1b[1;92m')
PUTIH = ('\x1b[1;97m')
BIRU  = ('\x1b[1;94m')
# Banner
banner = (f"""     {KUNING}{KUNING}[SELAMAT DATANG KAWAN]{KUNING}{KUNING}
{HIJAU}╔═╗┌─┐┌┐┌┬  ┬┌─┐┬─┐┌┬┐
{HIJAU}║  │ ││││└┐┌┘├┤ ├┬┘ │
{HIJAU}╚═╝└─┘┘└┘ └┘ └─┘┴└─ ┴
""")
#tanggal
def __init__(self):
		self.uid = []
	def main(self):
		os.system('clear')
		try:
banner()
IP = requests.get('https://api.ipify.org').text
jalan('[ selamat Datang Om  ]')
print('[•] Alamat IP kamu saat ini : 'IP)
print('[•] Kamu masuk pada         : 'waktu)
print()
# Convert Cookie Ke Token
class convert:

  def __init__(self):
    os.system('clear')
    print(f"""{banner}
{HIJAU}1.{BIRU} Mendapatkan token EAAI
{HIJAU}2.{BIRU} Dapatkan token EAAB
{HIJAU}3.{BIRU} Dapatkan token EAAA
{HIJAU}4.{BIRU} Cara menggunakan
{HIJAU}5.{BIRU} Keluar {HIJAU}({MERAH}exit{HIJAU}){MERAH}
   """)
    masuk = input(f"{KUNING}?.{PUTIH} Choose :{HIJAU} ")
    if masuk == '1' or masuk == '01':
      cookie = input(f"\n{HIJAU}?.{PUTIH} Cookie :{KUNING} ")
      if 'c_user=' in str(cookie):
        self.__satu__(cookie)
      else:
        masuk = input(f'''{HIJAU}JANGAN KOSONG GOBLOK!!!
{HIJAU}TEKAN {MERAH}ENTER!!''');os.system('python Convert.py');print()
    elif masuk == '2' or masuk == '02':
      cookie = input(f"\n{HIJAU}?.{PUTIH} Cookie :{KUNING} ")
      if 'c_user=' in str(cookie):
        self.__dua__(cookie)
      else:
        masuk = input(f'''{HIJAU}JANGAN KOSONG GOBLOK!!!
{HIJAU}TEKAN {MERAH}ENTER!!''');os.system('python Convert.py');print()
    elif masuk == '3' or masuk == '03':
      cookie = input(f"\n{HIJAU}?.{PUTIH} Cookie :{KUNING} ")
      if 'c_user=' in str(cookie):
        self.__tiga__(cookie)
      else:
        masuk = input(f'''{HIJAU}JANGAN KOSONG GOBLOK!!!
{HIJAU}TEKAN {MERAH}ENTER!!''');os.system('python Convert.py');print()
    elif masuk == '4' or masuk == '04':
      print(f"{KUNING}?.{HIJAU} Anda akan diarahkan ke youtube...");time.sleep(2);os.system('xdg-open https://youtube.com/channel/UCTuJ142jrkZxS_QnkttTMNQ');os.system('python Convert.py')
    elif masuk == '5' or masuk == '05':
      exit('SELAMAT TINGGAL SAYANG')
    else:
      masuk = input(f'''{HIJAU}JANGAN KOSONG GOBLOK!!!
{HIJAU}TEKAN {MERAH}ENTER!!''');os.system('python Convert.py');print()
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
          masuk = input(f"""{MERAH}!.{HIJAU} Token tidak ditemukan
{HIJAU}TEKAN {MERAH}ENTER!!""");os.system('python Convert.py');print()
        else:
          for token in find:
            print(f"\n{KUNING}?.{PUTIH} Your token :{HIJAU} {token}")
    except Exception as e:
      exit(f"{MERAH}!.{MERAH} {e}")
  def __tiga__(self,cookie):
    try:
      with requests.Session() as r:
        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36',
            'Cookie': cookie
        }
        response = r.get('https://web.facebook.com/adsmanager?_rdc=1&_rdr', headers = headers)
        find = re.findall('(EAAA)\w+', str(response.text))
        if len(find) == 0:
          masuk = input(f"""{MERAH}!.{HIJAU} Token tidak ditemukan
{HIJAU}TEKAN {MERAH}ENTER!!""");os.system('python Convert.py')
        else:
          for token in find:
            print(f"\n{KUNING}?.{PUTIH} Your token :{HIJAU} {token}")
    except Exception as e:
      exit(f"{MERAH}!.{MERAH} {e}")
  def __dua__(self,cookie):
    try:
      with requests.Session() as r:
        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36',
            'Cookie': cookie
        }
        respon = r.get('https://web.facebook.com/adsmanager?_rdc=1&_rdr', headers = headers)
        find = re.findall('act=(.*?)&nav_source', respon.text)
        if len(find) == 0:
          masuk = input(f"""{MERAH}!.{HIJAU} Token tidak ditemukan
{HIJAU}TEKAN {MERAH}ENTER!!""");os.system('python Convert.py');print()
        else:
          for y in find:
            response = r.get(f'https://web.facebook.com/adsmanager/manage/campaigns?act={y}&nav_source=no_referrer', headers = headers)
            token = re.search('(EAAB\w+)', response.text).group(1)
            print(f"\n{KUNING}?.{PUTIH} Your token :{HIJAU} {token}")
    except Exception as e:
      exit(f"{MERAH}!.{MERAH} {e}")

if __name__=='__main__':
  os.system('git pull');convert()
