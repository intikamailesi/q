import os

import csv

import time





rexaccount = int(input('Kaç Hesapta Rehbere Ekleme İşlemi Yapmak İstiyorsun? : '))



with open('../memory.csv', 'w', encoding='UTF-8') as file:

    writer = csv.writer(file, delimiter=",", lineterminator="\n")

    writer.writerow([1,1,60])



for loop in range(rexaccount):

    os.startfile("addcon.py")

    time.sleep(2)



time.sleep(5)

os.remove("../memory.csv")

