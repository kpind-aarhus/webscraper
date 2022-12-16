import requests
from pathlib import Path
import csv

with open("vejvisere.csv") as i:
	reader = csv.DictReader(i)
	for line in reader:
		id = line["uniqueID"]
		res = requests.get(f'https://storage.googleapis.com/openaws-webonly/{id}_c.pdf')

		with open(Path('download', f'{id}_c.pdf'), "wb") as f:
			f.write(res.content)
			print(f'{id}_c.pdf'+' downloaded')