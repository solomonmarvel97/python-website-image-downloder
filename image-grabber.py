from bs4 import BeautifulSoup as bs
import os
import requests

# grab images from url
url = 'https://www.pexels.com/search/girls/'

# crawl page
website_page = requests.get(url)
soup = bs(website_page.text, 'html.parser')

# locate all elements with image tag
image_tag = soup.findAll('img')

# create directory for model images
if not os.path.exists('models'):
	os.makedirs('models')

# move to new directory
os.chdir('models')

count = 0

# writing images
for i in image_tag:
	try:
		url = i['src']

		source = requests.get(url)

		if source.status_code == 200:

			with open('model - ' + str(x) + '.jpg', 'wb') as df:
				
				df.write(requests.get(url).content)
				
				df.close()
				
				count += 1
	except:
		pass