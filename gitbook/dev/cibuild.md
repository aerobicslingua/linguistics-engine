# How to build with CI ?

### Basic workflow
* `travis CI` is used for intergration build
* `.travis.yml` is written to build docker image and deployment controler by calling `Makefile`

### The release usage
```
git tag [semver]
git push origin [semver]
```
where `[semver]` represents semantic version.

* The docker image called `aerobicslingua/linguistics-engine-x86:[semver]` is generated on [docker hub](https://cloud.docker.com/u/aerobicslingua/repository/docker/aerobicslingua/linguistics-engine-x86).
* The deployment controller is generated in [gitbub release](https://github.com/aerobicslingua/linguistics-engine/releases).
