# Deploy linguistics-engine 

### Download zip package from [releases](https://github.com/aerobicslingua/linguistics-engine/releases)
```
wget https://github.com/aerobicslingua/linguistics-engine/releases/download/0.1.0/linguistics-engine-x86-0.1.0.zip
unzip linguistics-engine-x86-0.1.0.zip
```

### Config and start
```
cd linguistics-engine-imageAPI-x86
make config NAME=le
make start NAME=le
```
You can visit the `127.0.0.1:7000/` to test.

