import requests
from bs4 import BeautifulSoup
from operator import itemgetter

url = 'https://www.ebay.com/sch/i.html?_from=R40&_nkw=base+set+charizard&LH_BIN=1&_sop=12' #can replace "base+set+charizard" for whatever you want to search, add "&_pgn=" with a number after "=" to navigate through pages, planning on implementing an incrementer
request = requests.get(url)
print(request) #output will be <Response[200]> if request is successful
soup = BeautifulSoup(request.text, 'lxml')
ebay_s = soup.find_all('div', class_='s-item__info clearfix')[2:] #start from 3rd element since the first 2 are under a hidden element
ebay_data = []
for item in ebay_s:
    title = item.find('div', class_='s-item__title').text.strip()
    if "charizard" in title.lower() and 'base set' in title.lower() and '1999' in title.lower(): #specific keywords to optimize results for whatever you're searching for
        price = float(item.find('div', class_='s-item__detail s-item__detail--primary').text.strip().replace(',','').strip('$'))
        quality = item.find('div', class_='s-item__subtitle')
        if quality is not None:
            quality = quality.text.strip()
        else:
            quality = 'N/A'
        shipping = item.find('span', class_='s-item__shipping s-item__logisticsCost').text.strip()
        url =  item.find('a', class_='s-item__link').get('href')
        data_tuple = (title, price, quality, shipping, url)
        ebay_data.append(data_tuple)
ebay_data = sorted(ebay_data, key=itemgetter(1)) #sort by price
for item in ebay_data:
    print("Name:", item[0])
    print("Price:","$" + '{:,.2f}'.format(item[1]))
    print("Quality:", item[2])
    print("Shipping:", item[3])
    print("URL:", item[4])
    print("-" * 50)

