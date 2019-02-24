# Install prerequisites 

### Install `make`
```bash
sudo apt install build-essential -y
```

### Install Docker CE 18.06
* Follow the [reference](https://docs.docker.com/install/linux/docker-ce/ubuntu/) to install.
* Add current user to docker group after installation.
```bash
sudo usermod -aG docker $USER
```
* `docker version` to test.

### Install `docker-compose 1.22.0`  
* Follow the [reference](https://docs.docker.com/compose/install/) to install.
* `docker-compose` to test.
