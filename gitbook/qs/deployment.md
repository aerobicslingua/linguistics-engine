# Deploy linguistics-engine 

### Download zip package from [releases](https://github.com/aerobicslingua/linguistics-engine/releases)
```
wget https://github.com/aerobicslingua/linguistics-engine/releases/download/0.1.3/linguistics-engine-x86-0.1.3.zip
unzip linguistics-engine-x86-0.1.3.zip
```

### Config and start
```
cd linguistics-engine-imageAPI-x86
make config NAME=le DE_URL=[dictionary_api_url]
make start NAME=le
```
* `DE_URL` is formed as `ip:port`, representing ip address and port where dictionary api is installed, e.g, `192.168.21.62:3000`.
* You can visit the `127.0.0.1:7000/` to test the linguistics api.

