import requests
import logging
from config import settings

logging.basicConfig(filename=settings.log_path, filemode='a', format='%(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logging.info('Running updater')

record_name = settings.record_name

headers = {
    'X-Auth-Email': settings.email,
    'X-Auth-Key': settings.api_key,
    'Content-Type': 'application/json',
}

# Get zone id
url = f'https://api.cloudflare.com/client/v4/zones?name={settings.zone_name}'
response = requests.get(url, headers=headers)
zone_id = response.json()['result'][0]['id']
logging.info(f"Gathered zone_id: {zone_id}")

# Get record id
url = f'https://api.cloudflare.com/client/v4/zones/{zone_id}/dns_records?name={record_name}'
response = requests.get(url, headers=headers)
record_id = response.json()['result'][0]['id']
logging.info(f"Gathered record_id: {record_id}")

# Get current Public IP
ip = requests.get('https://api.ipify.org').text
logging.info(f"Public IP is: {ip}")

# Update record
url = f'https://api.cloudflare.com/client/v4/zones/{zone_id}/dns_records/{record_id}'
response = requests.put(url, json={
    'type': 'A',
    'name': record_name,
    'content': ip,
    'ttl': 1,
    'proxied': settings.proxied,
}, headers=headers)
logging.info(f"Updating record")

if response.status_code == 200:
    logging.info("Updated record")
else:
    logging.error(f"Failed updating record. Error: {response.text}")