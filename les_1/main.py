import requests
import json
from pprint import pprint

token = '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'
main_url = 'https://github.com/'
api_url = 'https://api.github.com/'
user = 'adm-lev'
param = 'tab=repositories'

request = requests.get(api_url + 'user/repos', auth=(user, token))

obj = json.loads(request.text)

for repo in obj:
    pprint(repo['name'])


