#!python3
#coding:utf8

import requests
import unicodecsv as csv

with open('output.csv', 'wb') as csvfile:
    # csvfile.write(u'\ufeff'.encode('utf8'))
    fieldnames = ['Title']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames, quoting=csv.QUOTE_ALL, encoding='utf-8-sig')
    writer.writeheader()
    data = {'Title': '" ... ну и денек! "'}
    writer.writerow(data)

with open('output.csv', 'rb') as csvfile:
    fieldnames = ['Title']
    reader = csv.DictReader(csvfile, fieldnames=fieldnames, quoting=csv.QUOTE_ALL, encoding='utf-8-sig')
    for row in reader:
        print(row)


# # coding: utf-8
# import csv
# D = {'name':u'马克','pinyin':u'mǎkè'}
# f = open('out.csv','wb')
# f.write(u'\ufeff'.encode('utf8')) # BOM (optional...Excel needs it to open UTF-8 file properly)
# w = csv.DictWriter(f,sorted(D.keys()))
# w.writeheader()
# w.writerow({k:v.encode('utf8') for k,v in D.items()})
# f.close()


