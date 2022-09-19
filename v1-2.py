from telethon.sync import TelegramClient
from telethon.tl.functions.messages import GetDialogsRequest
from telethon.tl.types import InputPeerEmpty, InputPeerChannel, InputPeerUser, PeerUser
from telethon.errors.rpcerrorlist import PeerFloodError, UserPrivacyRestrictedError, ChatWriteForbiddenError, UserAlreadyParticipantError
from telethon.tl.functions.channels import InviteToChannelRequest
from telethon.tl.functions.channels import GetFullChannelRequest, JoinChannelRequest
from telethon import types, utils, errors
from telethon.errors.rpcerrorlist import FloodWaitError
import configparser
import sys
import csv
from csv import reader
import traceback
from message import Message
import time
import random
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)
from colorama import init, Fore
init()
n = Fore.RESET
lg = Fore.LIGHTGREEN_EX
r = Fore.RED
w = Fore.WHITE
cy = Fore.CYAN
ye = Fore.YELLOW
colors = [lg, r, w, cy, ye]
def legend_devpost():
    import random
    Legend = ["",
              "███████╗██╗   ██╗ █████╗ ████████╗███╗   ███╗███████╗██████╗ ██╗   ██╗ █████╗",
              "██╔════╝██║   ██║██╔══██╗╚══██╔══╝████╗ ████║██╔════╝██╔══██╗╚██╗ ██╔╝██╔══██╗",
              "█████╗  ██║   ██║███████║   ██║   ██╔████╔██║█████╗  ██║  ██║ ╚████╔╝ ███████║",
              "██╔══╝  ██║   ██║██╔══██║   ██║   ██║╚██╔╝██║██╔══╝  ██║  ██║  ╚██╔╝  ██╔══██║",
              "██║     ╚██████╔╝██║  ██║   ██║   ██║ ╚═╝ ██║███████╗██████╔╝   ██║   ██║  ██║",
              "╚═╝      ╚═════╝ ╚═╝  ╚═╝   ╚═╝   ╚═╝     ╚═╝╚══════╝╚═════╝    ╚═╝   ╚═╝  ╚═╝"]

    for dev in Legend:
        print(f'{random.choice(colors)}{dev}{n}')
    print(f'=========================Telegram İletişim : t.me/fuatadmin_tr{n}')
    print(f'=========================Developper : t.me/HasanSencer{n}')
legend_devpost()

with open('memory.csv', 'r') as hash_obj:
    csv_reader = reader(hash_obj)
    list_of_rows = list(csv_reader)  
    row_number = 1
    col_number = 1
    Number = list_of_rows[row_number - 1][col_number - 1]
    
Legend = int(Number)
global nextLegend
nextLegend = Legend+1

with open('numaralar.csv', 'r') as read_obj:
    csv_reader = reader(read_obj)
    list_of_rows = list(csv_reader)    
    row_number = Legend
    col_number = 1
    value = list_of_rows[row_number - 1][col_number - 1]

po = 0
po += 1
with open('api.csv', 'r') as api_obj_id:
    csv_reader = csv.reader(api_obj_id)
    list_of_rows = list(csv_reader)
    row_number = int(po)
    col_number = 1
    deltaop = list_of_rows[row_number - 1][col_number - 1]
with open('api.csv', 'r') as hash_obj:
    csv_reader = csv.reader(hash_obj)
    list_of_rows = list(csv_reader)
    row_number = int(po)
    col_number = 2
    deltaxd = list_of_rows[row_number - 1][col_number - 1]
api_id = int(deltaop)
api_hash = str(deltaxd) 

pphone = value

config = configparser.ConfigParser()
config.read("ayarlar.ini")
to_group = config['Redstone']['BizimGrup']
messagessss = Message
legendfile = config['Redstone']['Message_file']

SLEEP_TIME_2 = 100
def autos():
    Legend_dev_message = messagessss
    channel_username = to_group
    phone = utils.parse_phone(pphone)
    client = TelegramClient(f"sessions/{phone}", api_id, api_hash)
    
    client.connect()
    if not client.is_user_authorized():
        print(Style.BRIGHT + Fore.RED + 'bir şeyler ters gitti...')
        client.send_code_request(phone)
        client.sign_in(phone, input    (Style.BRIGHT + Fore.GREEN + 'Kodu Girin: '))
    

    user = client.get_me()
    if not user.last_name:
        LegendName = user.first_name
    else:
        LegendName = user.first_name +' '+user.last_name
    input_file = 'data.csv'
    users = []
    with open(input_file, encoding='UTF-8') as f:
        rows = csv.reader(f, delimiter=",", lineterminator="\n")
        next(rows, None)
        for row in rows:
            user = {}
            user['srno'] = row[0]
            user['username'] = row[1]
            user['id'] = int(row[2])
            #user['access_hash'] = int(row[3])
            user['name'] = row[3]
            users.append(user)

    with open('memory.csv', 'r') as hash_obj:
        csv_reader = reader(hash_obj)
        list_of_rows = list(csv_reader)  
        row_number = 1
        col_number = 2
        numnext = list_of_rows[row_number - 1][col_number - 1]
    
    startfrom = int(numnext)
    nextstart = startfrom+50
    
    with open('memory.csv', 'r') as hash_obj:
        csv_reader = reader(hash_obj)
        list_of_rows = list(csv_reader)  
        row_number = 1
        col_number = 3
        numend = list_of_rows[row_number - 1][col_number - 1]
    
    endto = int(numend)
    nextend = endto+50
        
    with open("memory.csv","w",encoding='UTF-8') as df:
        writer = csv.writer(df, delimiter=",", lineterminator="\n")
        writer.writerow([nextLegend,nextstart,nextend])

    rex = 0
    for user in users:
        if (int(startfrom) <= int(user['srno'])) and (int(user['srno']) <= int(endto)):
            try:
                rex += 1
                status = 'Redstone'
                receiver = client.get_input_entity(user['username'])
                if user['username'] == "":
                    print("username yok, diğerine geçiyorum...")
                    continue

                if not legendfile:
                    client.send_message(receiver, f"Merhaba {user['name']}\n {Legend_dev_message}")
                else:
                    client.send_file(receiver, legendfile)
                    client.send_message(receiver, f"Merhaba {user['name']}\n {Legend_dev_message}")
                status = Style.BRIGHT + Fore.GREEN + 'Başarılı!'


                time.sleep(random.randrange(3, 6))

            except UserPrivacyRestrictedError:
                status = 'Gizlilik Ayarları Bu Kullanıcıya İzin Vermiyor.'


            except UserAlreadyParticipantError:
                status = 'Bu Üye Zaten Grupta!'


            except PeerFloodError as g:
                status = 'Hesap Spamda!'
            except FloodWaitError as t:
                stime = t.seconds
                print(f" {stime} saniye bekle...")
                time.sleep(stime)
            except errors.RPCError as e:
                status = e.__class__.__name__

            except:
                traceback.print_exc()
                print("Beklenmedik Hata!")
                continue
            print(Style.BRIGHT + Fore.GREEN +f" {LegendName} {Style.BRIGHT+Fore.RESET} > Gönderdi! {Style. RESET_ALL} {Style.BRIGHT+Fore.CYAN}>> {user['name']} >> {status} >> {rex}")
        elif int(user['srno']) > int(endto):
            print(Style.BRIGHT + Fore.GREEN + "\nMesaj Gönderimi Tamamlandı!\n")
            print(Style.BRIGHT + Fore.YELLOW + 'Çıkış Yapmak İçin Entere Basınız.')
            stat = input()
            if stat == 1 :
                autos()
            else:
                quit()
             
autos()