import urllib2
import json

def main():
	dataurl = "http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_month.geojson"
	webdata = urllib2.urlopen(dataurl)

	if webdata.getcode() == 200:
		data = webdata.read()
		jsondata = json.loads(data)

		if "title" in jsondata["metadata"]:
			print(jsondata["metadata"]["title"])

	else:
		print("error")		


if __name__ == '__main__':
	main()