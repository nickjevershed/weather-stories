import reportermate
import requests
import pandas as pd
from io import BytesIO
from zipfile import ZipFile

locations = ['066062']

for i, no in enumerate(locations):
	url = "http://www.bom.gov.au/jsp/ncc/cdio/weatherData/av?p_display_type=dailyZippedDataFile&p_stn_num={no}&p_c=-872895264&p_nccObsCode=122&p_startYear=2018".format(no=no)
	print i
	print "getting", url
	# Fetching the URL with requests
	
	r = requests.get(url, allow_redirects=False)
	print r.status_code

	if r.status_code != 200:
		print "can't get", sa2

	if r.status_code == 200:

		strFile = BytesIO()
		strFile.write(r.content)

		with open('IDCJAC0010_{no}_1800_Data.zip'.format(no=no), 'wb') as f:
			f.write(r.content)

		input_zip = ZipFile('{no}.zip'.format(no=no), 'r')
		ex_file = input_zip.read('IDCJAC0010_{no}_1800_Data.csv'.format(no=no))
		# print(ex_file)

		with open('IDCJAC0010_{no}_1800_Data.csv'.format(no=no), 'wb') as f:
			f.write(ex_file)

		df = pd.read_csv('IDCJAC0010_{no}_1800_Data.csv'.format(no=no))
		print df
