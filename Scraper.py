import requests
from bs4 import BeautifulSoup
item_dict = {'Elysian Spirit Shield':'12817','Blood Shard':'12817'}

def get_pricedata(_id):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:79.0) Gecko/20100101 Firefox/79.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Referer': 'https://secure.runescape.com/m=itemdb_oldschool/results',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',
        'Cache-Control': 'max-age=0',
    }
    
    params = (
        ('obj', f'{_id}'),
    )
    
    response = requests.get('https://secure.runescape.com/m=itemdb_oldschool/Blood+shard/viewitem', headers=headers, params=params,)
    soup = BeautifulSoup(response.content,'html.parser')
    price = str(soup('h3'))
    price = price[price.find('"'):price.find('">')].replace('"','')   
    name = str(soup('title')).replace('[<title>','').replace('</title>]','').replace(' - Grand Exchange - Old School RuneScape','')
    
    return price,name
get_pricedata('12817')