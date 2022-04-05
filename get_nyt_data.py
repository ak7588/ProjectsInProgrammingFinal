import pandas as pd
import numpy as np
import requests
from datetime import datetime
import json
import time

api_key = 'g23gy8sq5KG0i4Tb5TnVMESGx9rEqMgl'

url = 'https://api.nytimes.com/svc/search/v2/articlesearch.json'
all_articles = []

# current_time = datetime.now().strftime('%Y%m%d')

# params = {
# 		'api-key': api_key,
# 		'q': 'vaccine',
# 		'begin_date': '20201213',
# 		'end_date':	current_time,
# 		'fq': 'glocations:("United States") AND body:("covid", "vaccine")'
# 	}


# response = requests.get(url, params)
# response = response.json()['response']

# num_articles = response['meta']['hits']


# for i in range(num_articles // 10):
# 	try:
# 		params['page'] = i
# 		print(params)
# 		articles = requests.get(url, params).json()['response']['docs']
# 		all_articles.extend(articles)
# 		time.sleep(6)
# 	except:
# 		continue

# with open("response.json", "w") as f:
#     f.write(json.dumps(all_articles))

with open("response.json", "r") as f:
	response = json.load(f)
	articles = []

	for article in response:
		try:
			article_data = {
				'abstract': article['abstract'],
				'url': article['web_url'],
				'snipper': article['snippet'],
				'lead_par': article['lead_paragraph'],
				'pub_date': article['pub_date'],
				'type_of_material': article['type_of_material']
			}
			articles.append(article_data)

		except:
			continue

	df = pd.DataFrame(articles)
	df.to_csv("nyt_articles.csv", index=False);
