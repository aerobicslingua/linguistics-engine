# How to build locally

### Build docker image
```
cd linguistics-engine/
make mk-image
```
`aerobicslingua/linguistics-engine-x86:test` is created.

### Test image
```
cd linguistics-engine/deployment
make config NAME=le DE_URL=[dictionary_api_url]
make start NAME=le
```
where `[dictionary_api_url]` is formed as `ip:port`, is the ip and port of `dictionary-engine`. By default, it is `0.0.0.0:3000`.

The container should be started and the http service is listening at port `7000`.
* `docker ps -a` to make sure the service is up.
* Visit it to make sure it works.

### Build deployment package
```
cd linguistics-engine/
make mk-deployment 
```
`linguistics-engine-x86-test.zip` is generated.
