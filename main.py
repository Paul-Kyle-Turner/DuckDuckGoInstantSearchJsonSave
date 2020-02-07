import requests
import argparse
import json

if __name__ == '__main__':
    DDG_URL = 'http://api.duckduckgo.com/?q=x&format=json'
    parser = argparse.ArgumentParser()
    parser.add_argument('query', help='Search query')
    args = parser.parse_args()
    json_data = json.loads(requests.get(DDG_URL.replace('x', args.query)).text)
    with open('duckduckgo.json', 'w+') as outfile:
        json.dump(json_data, outfile, indent=4)
