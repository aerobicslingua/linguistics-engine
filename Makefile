GITBOOK = $(CURDIR)/gitbook
DOCS = $(CURDIR)/docs
IMAGE_ENV = $(CURDIR)/image
DF = $(IMAGE_ENV)/Dockerfile
DEPLOYMENT = $(CURDIR)/deployment
OWNER = aerobicslingua
REPO = linguistics-engine
SRC = $(IMAGE_ENV)/src
VERSION = test
ARCH = x86

.PHONY: create-devenv start-devenv clean-devenv
export FLASK_APP=$(SRC)/server.py
create-devenv:
	pip3 install -U -r $(SRC)/requirements.txt 
	python3 -m spacy download en
start-devenv:
	python3 -m flask run --port 7000
clean-devenv:
	pip3 uninstall -r $(SRC)/requirements.txt

.PHONY: mk-book clean-book
mk-book: $(GITBOOK)
	gitbook build $(GITBOOK) $(DOCS)

clean-book:
	rm -rf $(DOCS)/*

.PHONY: mk-image clean-image
mk-image:
	docker run --rm --privileged multiarch/qemu-user-static:register --reset
	docker build -t $(OWNER)/$(REPO)-$(ARCH):$(VERSION) -f $(DF)-$(ARCH) $(IMAGE_ENV) 

clean-image:
	docker rmi $(OWNER)/$(REPO)-$(ARCH):$(VERSION)


.PHONY: mk-deployment clean-deployment

DEPLOYMENT_x86=$(DEPLOYMENT)/imageAPI-x86

mk-deployment-x86: $(DEPLOYMENT_x86)
	mkdir $(REPO)-imageAPI-x86
	cp $(DEPLOYMENT_x86)/docker-compose.yml $(DEPLOYMENT_x86)/temp.env $(DEPLOYMENT_x86)/Makefile $(REPO)-imageAPI-x86/
	sed -i s+VERSION=test.*+VERSION=$(VERSION)+g $(REPO)-imageAPI-x86/temp.env
	zip -r $(REPO)-x86-$(VERSION).zip $(REPO)-imageAPI-x86
	rm -rf $(REPO)-imageAPI-x86

mk-deployment: mk-deployment-x86

clean-deployment: $(REPO)-*-$(VERSION).zip
	rm $(REPO)-*-$(VERSION).zip


.PHONY: pushtohub
pushtohub:
	docker tag $(OWNER)/$(REPO)-$(ARCH):$(VERSION) $(OWNER)/$(REPO)-$(ARCH):$(TAG)
	docker login -u $(USER) -p $(PASS)
	docker push $(OWNER)/$(REPO)-$(ARCH):$(TAG)
