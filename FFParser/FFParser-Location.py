#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import urllib.request
import json
from bs4 import BeautifulSoup
import requests
import re

def BSPaser(req,day):

	list = []

	soup = BeautifulSoup(req)
	webtext = soup.get_text().strip().split()

	print(soup.head.title)
	#print(webtext)
	#class="tableizer-table"

	table = soup.find_all(style="text-align: center;")
	#print(table)


	id = 0
	FileName = "FF_Day"+str(day)+".json"
	jsonFile = open(FileName,"w+",encoding="utf-8")
	groups = open("groupsName.json","w+",encoding="utf-8")

	hintFile = []
	groups.write("[")
	for x in range(3,len(table),3):
		datastruct = {
			"id": "",
			"Name": "",
			"Location": ""
		}
		id+=1
		datastruct['id'] = id
		data = re.match('^.+>(.+)<', str(table[x])).groups()
		data2 = re.match('^.+>(.+)<', str(table[x+1])).groups()

		temp=str(data2)
		temp=temp.strip('\',)')
		temp=temp.strip('\'(')
		temp2=str(data)
		temp2=temp2.strip('\',)')
		temp2=temp2.strip('\'(')
		datastruct['Location'] = temp2
		datastruct['Name'] = temp

		hintFile.append(temp)
		#print(temp)
		#datastruct['社團'] = re.match('^.+>(.+)<', str(table[x])).groups()
		#print(datastruct['id'],datastruct['社團'])

		list.append(datastruct)

	toJson = json.dumps(list, ensure_ascii=False, indent=2)
	jsonFile.write(toJson)
	jsonFile.close()
	hintFile = ','.join([str(i) for i in hintFile])

	groups.write(hintFile)
	groups.write("]")
	groups.close()



def WebRequest(url, day):

  req = requests.get(url)

  print(req.url)
  req.encoding = 'utf8'
  #print(req.headers)
  #print(req.text)
  BSPaser(req.text, day)

if __name__ == "__main__":
	#Day 1
	WebRequest('http://www.f-2.com.tw/index.php?q=ff/49229',1)
	#Day 2
	WebRequest('http://www.f-2.com.tw/index.php?q=ff/49230',2)
