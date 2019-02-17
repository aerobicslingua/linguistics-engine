export FLASK_APP=$(CURDIR)/server.py

prepare:
	pip3 install -U -r requirements.txt 
	python3 -m spacy download en
testPoS:
	python3 PoS.py ./partial.vtt
run:
	python3 -m flask run --port 7000

