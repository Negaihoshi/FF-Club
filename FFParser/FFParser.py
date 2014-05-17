#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import urllib.request
import json
from bs4 import BeautifulSoup
import requests
import re

def BSPaser(req):

	list = []
	list2 = []

	soup = BeautifulSoup(req)
	webtext = soup.get_text().strip().split()

	print(soup.head.title)
	#print(webtext)
	#class="tableizer-table"

	table = soup.find_all(style="text-align: center;")
	#print(table)

	datastruct = {
		"id": "",
		"社團": ""
	}
	id = 0

	jsonFile = open("data.json","w+",encoding="utf-8")
	jsonFile.write("[\n")

	for x in range(5,len(table),5):
		id+=1
		datastruct['社團'] = re.match('^.+>(.+)<', str(table[x])).groups()[0]
		datastruct['id'] = id
		#print(datastruct['id'],datastruct['社團'])
		toJson = json.dumps(datastruct, ensure_ascii=False, indent=2)
		jsonFile.write(toJson)
		if datastruct['id'] != 744: jsonFile.write(",")

	jsonFile.write("\n]")
	jsonFile.close()



def WebRequest(url):

  req = requests.get(url)

  print(req.url)
  req.encoding = 'utf8'
  #print(req.headers)
  #print(req.text)
  BSPaser(req.text)

if __name__ == "__main__":
	WebRequest('http://www.f-2.com.tw/index.php?q=ff/44836')


