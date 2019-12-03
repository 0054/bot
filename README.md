# bot

### usage
```
git clone https://github.com/0054/bot.git
cd bot
virtualenv .venv
source .venv/bin/activate
pip install -r bot/requirements.txt
```

#### run locally
make env.sh

```
cat env.sh
#!/usr/bin/env bash

export BOT_TOKEN=
export SOCKS5_PROXY=
export SOCKS5_PROXY_PORT=
export SOCKS5_USER=
export SOCKS5_PASSWORD=
```
```
source env.sh
python3 bot/bot.py
```
