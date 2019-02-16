prepare:
	pip3 install -U spacy
	pip3 install webvtt-py
	pip3 install flask
	pip3 install -U flask-cors
	python3 -m spacy download en
run:
	python3 PoS.py ./partial.vtt


