FLASK_APP=$(CURDIR)/server.py
prepare:
	pip3 install -U spacy
	pip3 install webvtt-py
	pip3 install flask
	pip3 install -U flask-cors
	python3 -m spacy download en
testPoS:
	python3 PoS.py ./partial.vtt
run:
	python3 -m flask run --port 7000

