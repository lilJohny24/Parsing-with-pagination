import requests
from bs4 import BeautifulSoup
base = 'https://parsinger.ru/html/'
def get_link(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            sale_buttons = soup.find_all(class_='sale_button')
            href_value = [base + link.find('a')['href'] for link in sale_buttons]
            return href_value
    except Exception as e:
        print(f"Error: {e}")
        return []


new_listik = []
base_url = 'https://parsinger.ru/html/index3_page_{}.html'

def get_article(b_links):
    try:
        new_response = requests.get(b_links)
        if new_response.status_code == 200:
            new_soup = BeautifulSoup(new_response.content, 'html.parser')
            article = new_soup.find_all('p', class_='article')
            for art in article:
                new_art = int(art.get_text()[9:])
                new_listik.append(new_art)
    except Exception as x:
        print(f"Error: {x}")

for page in range(1, 5):
    url = base_url.format(page)
    for i in get_link(url):
        b_links = str(i)
        get_article(b_links)
        
sum_new_art = sum(new_listik)
print(sum_new_art)
                
                
            
         
        

        

