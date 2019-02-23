# How to set development environment ?

### Clone the project
```
git clone https://github.com/aerobicslingua/linguistics-engine.git
```

### Install dependencies
The source code is under `image/src`, and written in `python3` with `flask` framework.
```
cd linguistics-engine
make create-devenv
```
It will install the dependencies packages in system.

### Start and stop service
```
cd linguistics-engine
make start-devenv
```

* It starts http server listening at `127.0.0.1:7000`. Visit it through browser to test whether it is active.
* You can modify the code under `image/src`, the server will be restarted automatically once the code is changed.
* You can type `ctrl-c` to stop the service.


### Clean the development environment
```
cd linguistics-engine
make clean-devenv
```
