# Deploy linguistics-engine 

### Download zip package from [releases](https://github.com/aerobicslingua/linguistics-engine/releases)
```
wget https://github.com/aerobicslingua/linguistics-engine/releases/download/0.1.1/linguistics-engine-x86-0.1.1.zip
unzip linguistics-engine-x86-0.1.1.zip
```

### Config and start
```
cd linguistics-engine-imageAPI-x86
make config NAME=le IP='192.168.21.62'
make start NAME=le
```
* `IP` represents ip address where dictionary api is installed
* You can visit the `127.0.0.1:7000/` to test the linguistics api.

