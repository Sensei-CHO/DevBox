# DDNS Updater

DDNS Updater is a DNS record updater for cloudflare.

This application is made to be Plug-N-Play.

## Features

- Logging
- Configuration file

## Setup

Install python3:

```bash
apt install python3 python3-pip
```

Install requirements:

```bash
python3 -m pip install -r requirements.txt
```

Populate `.env` file:

```env
api_key=a1b2c3                        # Global API Key
email=user@example.com                # Your Email
zone_name=example.com                 # Name of your zone (example.com)
record_name=record.example.com        # Name of your record (record.example.com)
proxied=true                          # If your record is proxied or not (true/false)
log_path=/var/log/ddns_updater.log    # Path and name of log file (/home/use/app/app.log)
```

Configure crontab:

```bash
crontab -e

*/5 * * * * cd /path/to/app && python3 /path/to/app/app.py
```

## Todo

- Add support for multiple `zones` and `records`
- Make it production ready
- Add webhook support
- Better log management (time, size limit)