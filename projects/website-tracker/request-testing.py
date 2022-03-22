
import requests
from bs4 import BeautifulSoup
import re
import hashlib

siteUrl = 'https://www.chrisbryant.org.uk/'
siteUrl = 'https://louisstevens.com'

linkMatcher = r"(https{0,1}:\/\/(w{3}\d*\.)*louisstevens\.com){0,1}\/([a-zA-Z0-9\/\.a-z A-Z-_~!$&'()*+,;=:@]|%[a-zA-Z0-9]{2})*"

def generateWebsiteHashList(baseLink, linkMatcher, pageUrl, hashList=None):
	hashList = [] if hashList is None else hashList

	try:
		requestObject = requests.get(pageUrl)
	except:
		requestObject = requests.get(baseLink + pageUrl)


	siteSourceHashObject = hashlib.md5(bytes(requestObject.text, encoding='utf-8'))
	if siteSourceHashObject.hexdigest() in hashList:
		return hashList
	
	hashList.append(siteSourceHashObject.hexdigest())

	siteSourceCodeText = requestObject.text
	sourceCodeSoup = BeautifulSoup(siteSourceCodeText, 'html.parser')
	linkList = sourceCodeSoup.findAll(['a', 'link'])

	for link in linkList:
		if re.match(linkMatcher, link.get('href')) is not None:
			hashList = generateWebsiteHashList(baseLink, linkMatcher, link.get('href'), hashList)
	
	return hashList

def getStandardWebsiteHash(baseLink, linkMatcher, pageUrl):
	hashList = generateWebsiteHashList(baseLink, linkMatcher, pageUrl)
	hashList.sort()
	hashString = ''.join(hashList)

	websiteHashObject = hashlib.md5(bytes(hashString, encoding='utf-8'))

	return websiteHashObject.hexdigest()


resultsList = []
for i in range(50):
	resultsList.append(getStandardWebsiteHash(siteUrl, linkMatcher, siteUrl))

worked = True if len(set(resultsList)) == 1 else False

print(f'Success: {worked}')
