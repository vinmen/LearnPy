#! /usr/bin/env python3

import urllib.request
import json

def main():
	dataurl = "http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_month.geojson"
	response = urllib.request.urlopen(dataurl)

	if response.getcode() == 200:
		data = response.read()		
		encoding = response.info().get_content_charset('utf-8')
		jsondata = json.loads(data.decode(encoding))
		f = open("/home/menon/Codes/py/learnPy/test.json", "w")
		f.write(str(jsondata))
		
		if "title" in jsondata["metadata"]:
			print(jsondata["metadata"]["title"])
		else:
			print("error")

if __name__ == '__main__':
	main()