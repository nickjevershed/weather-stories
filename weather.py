# Get long term data from the BoM for multiple Sydney locations into single dataframe
# Add forecasted data
# Export for reportermate

import reportermate
import requests
import pandas as pd
from io import BytesIO
from zipfile import ZipFile
import os
import scraperwiki

WILLY_KEY = os.environ['WILLY_KEY']

locations = [
{"name":"Sydney CBD", "bomID":"066062","willyID":"4950"},
{"name":"Parramatta", "bomID":"066124","willyID":""}
]

for i, location in enumerate(locations):
	url = "http://www.bom.gov.au/jsp/ncc/cdio/weatherData/av?p_display_type=dailyZippedDataFile&p_stn_num={bomID}&p_c=-872895264&p_nccObsCode=122&p_startYear=2018".format(bomID=locations['bomID'])
	print i
	print "getting", url
	
	# Fetching the URL with requests
	
	r = requests.get(url, allow_redirects=False)
	print r.status_code

	if r.status_code != 200:
		print "can't get", locations['bomID']

	if r.status_code == 200:

		strFile = BytesIO()
		strFile.write(r.content)

		with open('IDCJAC0010_{bomID}_1800_Data.zip'.format(bomID=locations['bomID']), 'wb') as f:
			f.write(r.content)

		input_zip = ZipFile('{bomID}.zip'.format(bomID=bomID), 'r')
		ex_file = input_zip.read('IDCJAC0010_{bomID}_1800_Data.csv'.format(bomID=locations['bomID']))

		with open('IDCJAC0010_{bomID}_1800_Data.csv'.format(bomID=locations['bomID']), 'wb') as f:
			f.write(ex_file)

		df = pd.read_csv('IDCJAC0010_{bomID}_1800_Data.csv'.format(bomID=locations['bomID']))
		
# https://api.willyweather.com.au/v2/{WILLY_KEY}/locations/{willyID}/weather.json?forecasts=weather&days=5
