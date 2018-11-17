from bs4 import BeautifulSoup
from urllib import request, error


try:
    with request.urlopen('http://akipress.org/') as resp:
        data = resp.read()
        soup = BeautifulSoup(data, 'html.parser')
        items = soup.find_all('a', attrs={'class': 'newslink'})
        for item in items:
            if 'turmush' in item.get('href'):
                with request.urlopen(item.get('href')) as resp2:
                    data2 = resp2.read()
                    soup2 = BeautifulSoup(data2, 'html.parser')
                    title = soup2.find('h1', attrs={'class': 'newsheadline_title'})
                    text = soup2.find('div', attrs={'class': 'text'})
                    with open('file.txt', 'a') as file:
                        file.write(title.get_text())
                        file.write(text.get_text())
except error.HTTPError as e:
    print(e)
