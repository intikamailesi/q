from logging import exception
from telethon.sync import TelegramClient
from telethon.tl.functions.messages import GetDialogsRequest
from telethon.tl.types import InputPeerEmpty, InputPeerChannel, InputPeerUser, PeerUser
from telethon.errors.rpcerrorlist import PeerFloodError, UserPrivacyRestrictedError, ChatWriteForbiddenError, UserAlreadyParticipantError
from telethon.tl.functions.channels import InviteToChannelRequest
from telethon.tl.functions.channels import GetFullChannelRequest, JoinChannelRequest
from telethon import types, utils, errors
import configparser
from telethon.errors.rpcerrorlist import FloodWaitError, UserDeactivatedBanError, PeerFloodError, UserPrivacyRestrictedError, UserNotMutualContactError, UserChannelsTooMuchError, ChannelInvalidError, UsernameNotOccupiedError, UserBannedInChannelError, ChatWriteForbiddenError
import sys
import csv
from csv import reader
import traceback
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
    numdel = list_of_rows[row_number - 1][col_number - 1]
    
delta = int(numdel)
global nextdelta
nextdelta = delta+1



with open('numaralar.csv', 'r') as read_obj:
    csv_reader = reader(read_obj)
    list_of_rows = list(csv_reader)    
    row_number = delta
    col_number = 1
    value = list_of_rows[row_number - 1][col_number - 1]
    
with open('api.csv', 'r') as api_obj_id:
    csv_reader = reader(api_obj_id)
    list_of_rows = list(csv_reader)
    row_number = delta
    col_number = 1
    deltaop = list_of_rows[row_number - 1][col_number - 1]
    
with open('api.csv', 'r') as hash_obj:
    csv_reader = reader(hash_obj)
    list_of_rows = list(csv_reader)  
    row_number = delta
    col_number = 2
    deltaxd = list_of_rows[row_number - 1][col_number - 1]
    
api_id = int(deltaop)
api_hash = str(deltaxd)
pphone = value




config = configparser.ConfigParser()
config.read("ayarlar.ini")
to_group = config['Redstone']['BizimGrup']

SLEEP_TIME_2 = 100
def autos():
    
    channel_username = to_group
    phone = utils.parse_phone(pphone)
    client = TelegramClient(f"sessions/{phone}", api_id, api_hash)
    
    client.connect()
    if not client.is_user_authorized():
        print(Style.BRIGHT + Fore.RED + 'bir şeyler ters gitti..')
        client.send_code_request(phone)
        client.sign_in(phone, input    ('Kodu Gir: '))
    
    
    user = client.get_me()
    if not user.last_name:
        LegendName = user.first_name
    else:
        LegendName = user.first_name +' '+user.last_name
    LegendPhone = user.phone
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
        writer.writerow([nextdelta,nextstart,nextend])

    for user in users:
        if (int(startfrom) <= int(user['srno'])) and (int(user['srno']) <= int(endto)):
            try:
                status = 'Redstone'
                if user['username'] == "":
                    print("username yok, diğerine geçiyorum...")
                    continue
                    
                client(InviteToChannelRequest(channel_username,[user['username']]))
                status = Style.BRIGHT + Fore.GREEN + 'Başarılı!'
                
                
                print(Style.BRIGHT + Fore.YELLOW + "Lütfen Bekle...")
                time.sleep(random.randrange(7,15))
                
            except UserPrivacyRestrictedError:
                status = Style.BRIGHT + Fore.RED + 'Gizlilik Ayarları Bu Kullanıcıya İzin Vermiyor.'
                time.sleep(random.randrange(3,5))
            except UserAlreadyParticipantError:
                print(Style.BRIGHT + Fore.YELLOW + 'Bu üye zaten grupta!')
                            
            except PeerFloodError as g:
                status = 'Hesap Spamda!'
                print(Style.BRIGHT + Fore.YELLOW + 'Hesabı Lütfen Dinlendir...')
                time.sleep(random.randrange(100000,1000000))
            except FloodWaitError as fw:
                status = 'Hesap Spamda!'
                print(Style.BRIGHT + Fore.YELLOW + 'Hesabı Lütfen Dinlendir...')
                time.sleep(random.randrange(100000,1000000))
            except ChatWriteForbiddenError as cwfe:
                client(JoinChannelRequest(channel_username))
                time.sleep(5)
                continue
            except UserChannelsTooMuchError:
                status = (Style.BRIGHT + Fore.RED + 'Kullanıcı Çok Fazla Gruba Üye!')

            except UserNotMutualContactError:
                status = (Style.BRIGHT + Fore.RED + 'Karşıdaki Kullanıcı İle İletişim Kurulmuyor!')
            except UserBannedInChannelError:
                print(Style.BRIGHT + Fore.RED + f"Bu Numara {LegendPhone} Sınırsız Spam Yemiş!")
                time.sleep(60000)   
            except errors.RPCError as e:
                status = e.__class__.__name__
            
            except Exception as d:
            	status = d
            	
            except exception as v:
                traceback.print_exc()
                print("Beklenmeyen Hata!")
                continue
            channel_connect = client.get_entity(channel_username)
            channel_full_info = client(GetFullChannelRequest(channel=channel_connect))
            countt = int(channel_full_info.full_chat.participants_count)

            print(Style.BRIGHT + Fore.GREEN +f" {LegendName} {Style.BRIGHT+Fore.RESET} > Grup Üyesi {(countt)}{Style. RESET_ALL} {Style.BRIGHT+Fore.CYAN}>> {user['name']} >> {status}")
        elif int(user['srno']) > int(endto):
            print(Style.BRIGHT + Fore.GREEN + "\nEkleme Başarıyla Tamamlandı!\n")
            print(Style.BRIGHT + Fore.YELLOW + 'Çıkış Yapmak İçin Entere Bas.')
            stat = input()
            if stat == 1 :
                autos()
            else:
                quit()
             
autos()