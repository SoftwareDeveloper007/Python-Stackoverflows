#!python3
#coding:utf8
import unicodecsv as csv

with open('iTunes_titles.csv', 'rb') as csvfile:
    fieldnames = ['Title', 'URL']
    reader = csv.DictReader(csvfile, fieldnames=fieldnames, quoting=csv.QUOTE_ALL, encoding='utf-8-sig')
    for row in reader:
        for key, val in row.items():
            print(key, val)
