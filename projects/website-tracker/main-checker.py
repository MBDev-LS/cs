
import time
import json

import requester_and_hasher

def add_site(site_list_dict: dict) -> dict:
	site_dict = {
			"domain_name": None,
			"home_path": None,
			"https": True,
			"hash_history": [
				{
					"unix_time": None,
					"hash": None
				}
			]
		}
	
	site_dict["domain_name"] = input('Enter site domain name: ')
	site_dict["home_path"] = input('Enter the path of the home page, include leading \'/\' (Press enter for \'/\'): ')
	site_dict["home_path"] = '/' if site_dict["home_path"] == '' else site_dict["home_path"]

	site_dict["https"] = input('Does this site include support for HTTPS (y/n):')

	while site_dict["https"].lower() not in ['y', 'n']:
		print('Error: Please enter \'y\' or \'n\'')
		site_dict["https"] = input('Does this site include support for HTTPS (y/n):')
	
	site_dict["https"] = True if site_dict["https"].lower() == 'y' else False

	site_list_dict['site_list'].append(site_dict)

def monitor_sites(site_list_dict: dict, cycle_delay: int) -> dict:
	while True:
		for site in site_list_dict["sites_list"]:
			baseLink = f'{"https" if site["https"] is True else "http"}://{site["domain_name"]}{site["home_path"]}'
			domain_name = site["domain_name"]
			domain_name.replace(".", "\.")
			linkMatcher = r"(https{0,1}:\/\/(w{3}\d*\.)* " + domain_name + r" ){0,1}\/([a-zA-Z0-9\/\.a-z A-Z-_~!$&'()*+,;=:@]|%[a-zA-Z0-9]{2})*"
			newHash = requester_and_hasher.getStandardWebsiteHash(baseLink, linkMatcher, baseLink)
			hashTime = time.time()
			site["hash_history"].append({
				"unix_time": hashTime,
				"hash": newHash
			})
			hashList = site["hash_history"]
			if len(set([historicHash["hash"] for historicHash in hashList])) > 1:
				print(f'At {hashList[-1]["unix_time"]} {site["domain_name"]} has changed, new hash is {hashList[-1]["hash"]}')
			else:
				print(f'At {hashList[-1]["unix_time"]} {site["domain_name"]} has remains unchanged, hash is still {hashList[-1]["hash"]}')
		
		time.sleep(cycle_delay)

with open('projects/website-tracker/websiteStore.json', 'rt') as f:
	siteListDict = json.loads(f.read())

monitor_sites(siteListDict, 10)
