
import requests
import bs4

peopleLinkList = []

from config import DOMAIN

def removeAllFromList(lst: list, obj) -> list:
    while obj in lst:
        lst.remove(obj)
    
    return lst

for i in range(1, 5):
    listLink = f'http://{DOMAIN}/people/?p={i}&char=ShowAll'

    soup = bs4.BeautifulSoup(requests.get(listLink).text, 'html.parser')

    parents = soup.find_all('td', class_='oDataGridCell')

    children = [parent.findChildren('a', recursive=False) for parent in parents]
    children = [child[0] for child in removeAllFromList(children, [])]

    children2 = [childp.findChildren('span', recursive=False) for childp in children]
    children2 = [child[0] for child in removeAllFromList(children2, [])]
    childrensLinks = [child.getText() for child in children2]

    peopleLinkList += childrensLinks

print(peopleLinkList)
print(len(peopleLinkList))