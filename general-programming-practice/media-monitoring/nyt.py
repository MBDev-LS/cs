
from pynytimes import NYTAPI
import config

nyt = NYTAPI(config.NYT_KEY, parse_dates=True)

print(nyt.latest_articles(section='breaking'))

def checkNytWorldWire():
	nytLatestWorld = nyt.latest_articles(section='world')
	nytLatestAll = nyt.latest_articles()

